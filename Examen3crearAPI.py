import platform
import sys
import subprocess
import json
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/system_info', methods=['GET'])
def get_system_info():
    sistemaop = sys.platform
    sistema = platform.system()
    version = platform.win32_ver() if sistema == 'Windows' else platform.mac_ver() if sistema == 'Darwin' else platform.uname().version
    local = subprocess.getoutput("""for /f "tokens=2 delims=[]" %a in ('ping -n 1 -4 "%computername%"') do @echo %a """) if sistema == 'Windows' else subprocess.getoutput("ifconfig | grep 'inet' | grep -Fv 127.0.0.1 | awk '{print $2}'")
    hostname = platform.node()
    cpu = platform.processor()

    system_info = {'ip': local, 'so': sistema, 'version': version, 'hostname': hostname, 'cpu': cpu}
    
    return jsonify(system_info)

if __name__ == '__main__':
    app.run(debug=True)
