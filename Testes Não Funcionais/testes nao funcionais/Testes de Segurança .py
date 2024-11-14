import subprocess

comando = ["nmap", "-sS", "-p", "80,443", "seu_sistema.com"]
resultado = subprocess.run(comando, stdout=subprocess.PIPE)
print(resultado.stdout.decode())
