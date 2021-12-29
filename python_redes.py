import socket
import sys
import time
print """
_ _ ____ _
| | (_) ___ _ __ ___ | _ \(_)___ ___ _____ _____ _ __
| | | |/ _ \| '_ \/ __| | | | | / __|/ __/ _ \ \ / / _ \ '__|
| |___| | (_) | | | \__ \ | |_| | \__ \ (_| (_) \ V / __/ |
|_____|_|\___/|_| |_|___/___|____/|_|___/\___\___/ \_/ \___|_|
|_____|
--[code by : 33Divace - LDEHC - (LionsDefender Ethical Hacking Community)
"""
def usage():
print 'Usage: Lions_Discover.py [target-host]'
print 'Examples:'
print 'Usage: Lions_Discover.py 192.168.0.4'
sys.exit(0)
if not len(sys.argv[1:]):
usage()
sys.exit(0)
time.sleep(1)
print '[*]Connection to target[*]'
time.sleep(1)
print '[*]Finding opened port and services running in the target[*]\n'
time.sleep(1)
for port in range(1,65535):
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) |criado o socket TCP,
if s.connect_ex((sys.argv[1],port)) ==0: | caso ele se conectar no [primeiro argumento] na porta x , significa que a porta esta aberta
version = s.recv(1024) |Aqui ele vai receber a comunicação , e vai pegar o banner dessa comunicação e exibir a versão já esseguir
print '[OPEN-PORT]',port,'Version==>',version | e ai ele vai imprimir a porta e a versão
foi uma cena básica mesmo , que qualquer um com conhecimento básico de python consegue, mais que faz diferença entre os profissionais, para não ficar dependendo muito dessas ferramentas 