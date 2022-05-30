import socket
import re
import sys

port_regex = re.compile("([0-9]+){1,5}-([0-9]+){1,5}")
ip_regex = re.compile("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$")
url_regex = re.compile("([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?")

def scan(address) :
    access_port = []
    while True :
        try:
            port_range = input("포트 범위 설정 (ex:0-20000) 기본값은 0-65535 미입력 시 기본값으로 시작 \n입력 : ")
            port_number = port_regex.search(port_range.replace(" ",""))
            if port_range :
                port_min = int(port_number.group(1))
                port_max = int(port_number.group(2))+1
            elif port_range == "" :
                port_min = 0
                port_max = 65535
            else :
                print("\n\n잘못된 입력입니다. 다시 입력해주세요.")
                continue
        except KeyboardInterrupt:
            sys.exit()
        except :
            print("잘못된 입력입니다. 예시와 같은 양식으로 입력해주세요.\n\n")
            continue
        
        print("입력 범위 내 열린 포트 확인 중")
        for port in range(port_min,port_max):
            print(f'{port}', end='\r')
            try:
                scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                scan.connect((address, port))
                recieve = scan.recv(1024)
                if recieve:
                    access_port.append(port)
                scan.close()
            except:
                pass
        print("허용 포트 리스트\n",access_port)
        break
def scan_port():
    while True :
        input_address = input("IP 또는 URL 입력 : ")
        if url_regex.search(input_address.replace(" ","")) is not None and (ip_regex.search(input_address.replace(" ","")) is not None or ip_regex.search(input_address.replace(" ","")) is None):
            domain_address = re.sub("http(s)?:\/\/", '', input_address)
            result_address = domain_address.strip('/')
            ip_address = socket.gethostbyname(result_address)
            scan(ip_address)
            break
        else :
            print("잘못된 입력, 다시 입력해주세요.\n")
            continue