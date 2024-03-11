import platform
import sys
import subprocess
sistemaop = sys.platform
sistema = platform.system()
version = platform.win32_ver()
hostname = platform.node()
procesador = platform.processor()
print("Estamos en {}".format(sistema), " en version: {}".format(version))
print ("Tipo SO: {}".format(sistemaop))
print ("El hostname de la maquina es: {}".format(hostname))
print ("Y la marca del procesador es: {}".format(procesador))
if sistema == 'Windows':
    local = subprocess.getoutput("""for /f "tokens=2 delims=[]" %a in ('ping -n 1 -4 "%computername%"') do @echo %a""")
else:
    local = subprocess.getoutput("ifconfig | grep 'inet ' | grep -Fv 127.0.0.1 | awk '{print $2}'")
print(local)
#Practica del siguiente script muestre ademans el hostname y el nombre del procesador de nuestro equipo.