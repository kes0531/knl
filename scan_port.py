import socket
import sys
import threading
from tqdm import tqdm

maxConnection = 10000          
connection_lock = threading.BoundedSemaphore(value=maxConnection) 
# ip_regex = re.compile("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$")
# url_regex = re.compile("([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?")
access_port = []
total_access_port = {}

def scan_port(address, port_num) :
    global access_port
    try:
        response_data = None
        scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        scan.settimeout(5)
        scan.connect((address, port_num))
        scan.send("Port Scanning..\n".encode())
        response_data = scan.recv(1024)
        if response_data:
            access_port.append(str(port_num))
        scan.close()
    except KeyboardInterrupt:
        sys.exit()
    except:
        pass
    finally :
        connection_lock.release()
    
def scan_info(input_address):
    while True :
        try : 
                ip_address = socket.gethostbyname(input_address)
                for num in tqdm(range(1,65536)): # 포트 범위 65535까지 검색
                    connection_lock.acquire()
                    t = threading.Thread(target=scan_port, args=(ip_address, num))
                    t.start()
                total_access_port['port_num'] = access_port
                break
        except KeyboardInterrupt:
            sys.exit()
    return total_access_port
