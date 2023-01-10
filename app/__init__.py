from contextlib import suppress
import json
import os
from multiprocessing import active_children

import socketio as IO
from aiohttp import web
import asyncio
import janus

from app.fingerprint import FingerprintController
from app.models import SearchedMessage
from app import messages



socketio = IO.AsyncServer(async_mode='aiohttp', cors_allowed_origins='*', logger=True, async_handlers=True, engineio_logger=True)

fingerprint = []

if(os.name == 'nt'):
    fingerprint = FingerprintController("COM3");
else:
    print("initializing...")
    fingerprint = FingerprintController("/dev/ttyUSB0")

static_files = {
    '/': {'filename': './templates/consumer.html', 'content_type': 'text/plain'},
}

promises = []

requests = []

queue: janus.Queue = None 

@socketio.on("connect")
def connect(sid, environ):
    requests.append(sid)

async def kill_requests(sid):
    for r in requests:
        print(r)
        if r != sid:
            await socketio.disconnect(r)
    requests.append(sid)

def add_task(sid, action, params):
    task = asyncio.ensure_future(action(params))
    promises.append((sid, task))
    return task

async def kill_process(current_sid):
    pending = asyncio.all_tasks()
    for task in pending:
        task.cancel()
    

@socketio.on('IdStore')
async def store_finger(sid, IdStore):
    # socketio.emit('message', messages.STOREOK)
    req = fingerprint.enroll_finger(int(IdStore), socketio)
    promises.append(req)
    if await req:
        await socketio.emit('message', messages.STOREOK)
    else:
        await socketio.emit('message', messages.STOREFAIL)

@socketio.on('IdDelete')
async def delete_finger(sid, IdDelete):
    req = fingerprint.req.delete_model(int(IdDelete))
    promises.append(req)
    if req == fingerprint.adafruit_fingerprint.OK:
        socketio.emit('message', messages.DELETEOK)
    else:
        socketio.emit('message', messages.DELETEFAIL)


async def handle_search(sid):
    # await kill_requests(sid)

    print("HANDLE SEARCH")
    req = await fingerprint.get_fingerprint(socketio)
    if req:
        messages.FINGERDETECTED['id_finger'] = fingerprint.finger.finger_id
        messages.FINGERDETECTED['confidence'] = fingerprint.finger.confidence
        await socketio.emit('message', messages.FINGERDETECTED)
    else:
        await socketio.emit('message', messages.FINGERNODETECTED)

    
async def consumer():
    while True:
        try:
            val = await queue.async_q.get()
            # print(queue.async_q.get())
            await handle_search(val)
            # await queue.async_q.task_done()
            # await queue.async_q.join()
            # queue.close()
            # await queue.wait_closed()
            # await kill_process("")
            # await handle_search(val)
        except:
            pass





@socketio.on('message')
async def handle_message(sid, message):
    global queue
    print('request:', requests)
    if message == 'SearchSendMessage':
       # print("recebendo", sid, message) 
        # for t in requests:
        #     print("opa", t)
        #     if queue.async_q.empty() == False:
        #         print(await queue.async_q.get(t))
        await queue.async_q.put(sid)
        print("Adicionado")
    elif message == 'StoreSendMessage':
        store_finger()
    elif message == 'FakeSearch':
        print("LOG: fake search")                
        socketio.emit('message', json.dumps(SearchedMessage(30, 183).__dict__))
    elif message == 'DeleteSendMessage':
        delete_finger()
    elif message == 'ClearSendMessage':
        if fingerprint.req.empty_library() == fingerprint.adafruit_fingerprint.OK:
            socketio.emit('message', messages.EMPTYLIBRARY)
        else:
            socketio.emit('message', messages.EMPTYLIBRARYFAIL)



# x = threading.Thread(target=consumer)

# x.start()

app = web.Application()
socketio.attach(app)


async def init_app():
    global queue
    queue = janus.Queue()
    # fut = loop.run_in_executor(None, consumer, queue.sync_q)
    # await fut
    socketio.start_background_task(consumer)

    #await asyncio.gather(*asyncio.all_tasks() - {asyncio.current_task()})
    # active = active_children()
    # for child in active:
    #     child.terminate()
    # for child in active:
    #     child.join()
    # await queue.async_q.join()

    # queue.close()
    # await queue.wait_closed()
    return app
