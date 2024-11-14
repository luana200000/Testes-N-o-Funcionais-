import time
import requests
from concurrent.futures import ThreadPoolExecutor

url = "http://seu_sistema.com"

def simular_usuario(id):
    response = requests.get(url)
    return response.status_code

num_usuarios = 10000
with ThreadPoolExecutor(max_workers=100) as executor:
    future_to_user = {executor.submit(simular_usuario, i): i for i in range(num_usuarios)}
    for future in future_to_user:
        status_code = future.result()
        if status_code != 200:
            print(f"Erro no usuário {future_to_user[future]}: Status code {status_code}")
