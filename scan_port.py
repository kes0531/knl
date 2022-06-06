import socket
import re, sys
import threading
from tqdm import tqdm

print_lock = threading.Semaphore(value=1) 
maxConnection = 10000          
connection_lock = threading.BoundedSemaphore(value=maxConnection) 
port_regex = re.compile("([0-9]+){1,5}-([0-9]+){1,5}")
ip_regex = re.compile("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$")
url_regex = re.compile("([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?")
access_port = []

def scan_port(address, port_num) :
    global access_port
    try:
        response_data = None
        scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        scan.connect((address, port_num))
        response_data = scan.recv(1024)
        if response_data:
            access_port.append(port_num)
        scan.close()
    except KeyboardInterrupt:
        sys.exit()
    except:
        pass
    finally:
        if response_data == 'error':
            connection_lock.release()
            return
    connection_lock.release()
    return access_port
    
def scan_info():
    while True :
        try : 
            input_address = input("IP 또는 URL 입력 : ")
            if url_regex.search(input_address.replace(" ","")) is not None and (ip_regex.search(input_address.replace(" ","")) is not None or ip_regex.search(input_address.replace(" ","")) is None):
                domain_address = re.sub("http(s)?:\/\/", '', input_address)
                result_address = domain_address.strip('/')
                ip_address = socket.gethostbyname(result_address)
                for num in tqdm(range(1,65536)): # 포트 범위 65535까지 검색
                    connection_lock.acquire()
                    t = threading.Thread(target=scan_port, args=(ip_address, num))
                    t.start()
            break
        except KeyboardInterrupt:
            sys.exit()
        except :
            print("잘못된 입력입니다. 다시 입력해주세요.\n")
            continue

if __name__ == "__main__":
    scan_info()
    print("\n",access_port)