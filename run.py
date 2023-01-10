from contextlib import suppress
from app import web, init_app

if __name__ == '__main__':
    # app.cleanup_ctx.append(main)
    
    web.run_app(init_app(), host='0.0.0.0', port=5000)

    # asyncio.run(runn())