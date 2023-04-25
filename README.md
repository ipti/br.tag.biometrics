# TAG - Fingerprint Recognition
## Libraries used
Adafruit_fingerprint<br>
Flask<br>
Flask SocketIO<br>
Flask CORS<br>
Time<br>
Serial<br>
Tkinter<br>

## Message codes and information in JSON format
|     Event     |   ID   |          Info         |
| ------------- | ---|------------------------ |
|NOFINGER | 100 | Sem o dedo no leitor |
|WAITINGIMAGE | 101 | Aguardando imagem... |
|MODELING | 102 | Modelagem... |
|MODELED | 103 | Modelado |
|SEARCHING | 104 | Procurando... |
|PUTFINGER | 105 | Coloque o dedo no sensor... |
|PUTFINGERAGAIN | 106 | Coloque o mesmo dedo novamente... |
|PICTURETAKEN | 107 | Imagem tirada |
|WAITINGFINGER | 108 | . |
|REMOVEFINGER | 113 | Remover dedo |
|CARRER | 114 | Criado |
|SAVING | 115 | Salvando... |
|SAVED | 116 | Salvo |
|STORED | 117 | Armazenado |
|STOREOK | 200 | Impressão cadastrada com sucesso |
|DELETEOK | 201 | Impressão deletada com sucesso |
|FINGERDETECTED | 202 | Impressão detectada |
|EMPTYLIBRARY | 203 | Biblioteca esvaziada com sucesso |
|PASSVERIFY | 204 | Aprovação bem sucedida |
|MODULEOK | 205 | Módulo OK |
|OK | 206 | OK |
|STOREFAIL | 500 | Ocorreu um erro ao cadastrar |
|DELETEFAIL | 501 | Ocorreu um erro ao deletar |
|FINGERNODETECTED | 502 | Impressão não encontrada |
|EMPTYLIBRARYFAIL | 503 | Falha ao esvaziar a biblioteca |
|PACKETRECIEVEERR | 504 | Erro de recebimento de pacote |
|IMAGEFAIL | 505 | Falha na imagem |
|IMAGEMESS | 506 | Imagem confusa |
|FEATUREFAIL | 507 | Falha de recurso |
|NOMATCH | 508 | Sem correspondência |
|NOTFOUND | 509 | Não encontrado |
|ENROLLMISMATCH | 510 | Impressões não correspondem |
|BADLOCATION | 511 | Erro de local de armazenamento |
|DBRANGEFAIL | 512 | Falha de alcance no banco de dados |
|UPLOADFEATUREFAIL | 513 | Falha no recurso de upload |
|PACKETRESPONSEFAIL | 514 | Falha de resposta do pacote |
|UPLOADFAIL | 515 | Falha no envio |
|DBCLEARFAIL | 516 | Falha na limpeza do banco de dados |
|PASSFAIL | 517 | Falha na aprovação |
|INVALIDIMAGE | 518 | Imagem invalida |
|FLASHERR | 519 | Erro de armazenamento flash |
|INVALIDREG | 520 | Registro invalido |
|ADDRCODE | 521 | ADDR Code |
|IMAGEFAIL | 522 | Erro de imagem |
|OTHERERROR | 523 | Outro erro |
|CONFUSINGIMAGE | 524 | Imagem muito confusa |
|NOTIDENTIFTRESOURCES | 525 | Não foi possível identificar recursos |
|BADSTORAGELOCATION | 526 | Local de armazenamento incorreto |
|FLASHSTORAGEERROR | 527 | Erro de armazenamento flash |
|SAVINGERROR | 528 | Ocorreu um erro ao salvar |
|FINGERSNOTMATCH | 529 | As impressões não correspondem |

Obs.:the JSON format is with event, id, info attributes. With the exception of FINGERDETECTED which contains the finger_id and the confidence