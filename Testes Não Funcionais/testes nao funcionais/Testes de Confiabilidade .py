import datetime

def verificar_disponibilidade(url):
    response = requests.get(url)
    return response.status_code == 200

inicio = datetime.datetime.now()
tempo_monitoração = datetime.timedelta(hours=1)
while datetime.datetime.now() - inicio < tempo_monitoração:
    if verificar_disponibilidade(url):
        print("Sistema disponível")
    else:
        print("Sistema indisponível")
    time.sleep(60) 
