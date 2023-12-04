#MENSAGENS DO BACK
STOREOK =   { 
                "event": "STOREOK",
                "id": 200,
                "info": "Impressao cadastrada com sucesso"
        }
STOREFAIL = {   
                "event": "STOREFAIL",
                "id": 500,
                "info": "Ocorreu um erro ao cadastrar"
        }
DELETEOK =  {
                "event": "DELETEOK",
                "id": 201,
                "info": "Impressao deletada com sucesso"
        }
DELETEFAIL = {
                "event": "DELETEFAIL",
                "id": 501,
                "info": "Ocorreu um erro ao deletar"
        }
FINGERDETECTED = {
                "event": "FINGERDETECTED",
                "id": 202,
                "id_finger": 0,
                "confidence": 0,
                "info": "Impressao detectada"
        }
FINGERNODETECTED = {
                "event": "FINGERNODETECTED",
                "id": 502,
                "info": "Impressao nao encontrada"
        }
EMPTYLIBRARY = {
                "event": "EMPTYLIBRARY",
                "id": 203,
                "info": "Biblioteca esvaziada com sucesso"
        }
EMPTYLIBRARYFAIL = {
                "event": "EMPTYLIBRARYFAIL",
                "id": 503,
                "info": "Falha ao esvaziar a biblioteca"
        }
INCREMENTCOUNTER = {
                "event": "INCREMENTCOUNTER",
                "id": 204,
                "info": "Contador incrementado"
        }

# MENSAGENS DA BIBLIOTECA
PACKETRECIEVEERR = {
                "event": "PACKETRECIEVEERR",
                "id": 504,
                "info": "Erro de recebimento de pacote"
        }
IMAGEFAIL = {
            "event": "IMAGEFAIL",
            "id": 505,
            "info": "Falha na imagem"
        }
IMAGEMESS = {
            "event": "IMAGEMESS",
            "id": 506,
            "info": "Imagem confusa"
        }
FEATUREFAIL = {
            "event": "FEATUREFAIL",
            "id": 507,
            "info": "Falha de recurso"
        }
NOMATCH = {
            "event": "NOMATCH",
            "id": 508,
            "info": "Sem correspondência"
        }
NOTFOUND = {
            "event": "NOTFOUND",
            "id": 509,
            "info": "Nao encontrado"
        }
ENROLLMISMATCH = {
            "event": "ENROLLMISMATCH",
            "id": 510,
            "info": "Impressoes nao correspondem"
        }
BADLOCATION = {
            "event": "BADLOCATION",
            "id": 511,
            "info": "Erro de local de armazenamento"
        }
DBRANGEFAIL = {
            "event": "DBRANGEFAIL",
            "id": 512,
            "info": "Falha de alcance no banco de dados"
        }
UPLOADFEATUREFAIL = {
            "event": "UPLOADFEATUREFAIL",
            "id": 513,
            "info": "Falha no recurso de upload"
        }
PACKETRESPONSEFAIL = {
            "event": "PACKETRESPONSEFAIL",
            "id": 514,
            "info": "Falha de resposta do pacote"
        }
UPLOADFAIL = {
            "event": "UPLOADFAIL",
            "id": 515,
            "info": "Falha no envio"
        }
DBCLEARFAIL = {
            "event": "DBCLEARFAIL",
            "id": 516,
            "info": "Falha na limpeza do banco de dados"
        }
PASSFAIL = {
            "event": "PASSFAIL",
            "id": 517,
            "info": "Falha na aprovacao"
        }
INVALIDIMAGE = {
            "event": "INVALIDIMAGE",
            "id": 518,
            "info": "Imagem invalida"
        }
FLASHERR = {
            "event": "FLASHERR",
            "id": 519,
            "info": "Erro de armazenamento flash"
        }
INVALIDREG = {
            "event": "INVALIDREG",
            "id": 520,
            "info": "Registro invalido"
        }
ADDRCODE = {
            "event": "ADDRCODE",
            "id": 521,
            "info": "ADDR Code"
        }
PASSVERIFY = {
            "event": "PASSVERIFY",
            "id": 204,
            "info": "Aprovacao bem sucedida"
        }
MODULEOK = {
            "event": "MODULEOK",
            "id": 205,
            "info": "Modulo OK"
        }
OK = {
            "event": "OK",
            "id": 206,
            "info": "OK"
}
# MENSAGENS DO LEITOR
NOFINGER =  {
            "event": "NOFINGER",
            "id": 100,
            "info": "Sem o dedo no leitor"
        }
WAITINGIMAGE = {
            "event": "WAITINGIMAGE",
            "id": 101,
            "info": "Aguardando imagem..."
        }
MODELING = {
            "event": "MODELING",
            "id": 102,
            "info": "Modelagem..."
        }
MODELED = {
            "event": "MODELED",
            "id": 103,
            "info": "Modelado"
        }
SEARCHING = {
            "event": "SEARCHING",
            "id": 104,
            "info": "Procurando..."
        }
PUTFINGER = {
            "event": "PUTFINGER",
            "id": 105,
            "info": "Coloque o dedo no sensor..."
        }
PUTFINGERAGAIN = {
            "event": "PUTFINGERAGAIN",
            "id": 106,
            "info": "Coloque o mesmo dedo novamente..."
        }
PICTURETAKEN = {
            "event": "PICTURETAKEN",
            "id": 107,
            "info": "Imagem tirada"
        }
WAITINGFINGER = {
            "event": "WAITINGFINGER",
            "id": 108,
            "info": "."
        }
IMAGEFAIL = {
            "event": "IMAGEFAIL",
            "id": 522,
            "info": "Erro de imagem"
        }
OTHERERROR = {
            "event": "OTHERERROR",
            "id": 523,
            "info": "Outro erro"
        }
CONFUSINGIMAGE = {
            "event": "CONFUSINGIMAGE",
            "id": 524,
            "info": "Imagem muito confusa"
        }
NOTIDENTIFTRESOURCES = {
            "event": "NOTIDENTIFTRESOURCES",
            "id": 525,
            "info": "Não foi possível identificar recursos"
        }
REMOVEFINGER = {
            "event": "REMOVEFINGER",
            "id": 113,
            "info": "Remover dedo"
        }
CARRER = {
            "event": "CARRER",
            "id": 114,
            "info": "Criado"
        }
SAVING = {
            "event": "SAVING",
            "id": 115,
            "info": "Salvando..."
        }
SAVED = {
            "event": "SAVED",
            "id": 116,
            "info": "Salvo"
        }
STORED = {
            "event": "STORED",
            "id": 117,
            "info": "Armazenado"
        }
BADSTORAGELOCATION = {
            "event": "BADSTORAGELOCATION",
            "id": 526,
            "info": "Local de armazenamento incorreto"
        }
FLASHSTORAGEERROR = {
            "event": "FLASHSTORAGEERROR",
            "id": 527,
            "info": "Erro de armazenamento flash"
        }
SAVINGERROR = {
            "event": "SAVINGERROR",
            "id": 528,
            "info": "Ocorreu um erro ao salvar"
        }
FINGERSNOTMATCH = {
            "event": "FINGERSNOTMATCH",
            "id": 529,
            "info": "As impressões não correspondem"
        }