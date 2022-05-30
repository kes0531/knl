from bruteforce import *
from injection import *
from scan_method import *
from scan_port import *
import sys
import os

if __name__ == "__main__":
    print("\nWeb-vulnerability-scan-tool ver.0.1 - KNL\n")
    while(True):
        try:
            print("사용할 기능 선택 \n")
            print("1. bruteforce  2. 웹 서비스 메소드 점검  3. Port Scan 4. Injection(구현예정) 5. XSS(구현예정)")
            selec_modul = int(input("입력 : "))
            if selec_modul == 1 : 
                brutefoce_attack()
            elif selec_modul == 2 : 
                scan_method()
            elif selec_modul == 3 : 
                 scan_port()
            else :
                os.system('cls')
                print("\n아직 구현되지 않았습니다. 다른 기능을 이용해주세요.")
            
            answer = input("\n\n프로그램을 종료 하시겠습니까? [Y/N] \n입력 : ")
            if answer == 'Y' or answer == 'y' : break
            elif answer == 'N' or answer == 'n' : 
                os.system('cls')
                continue
        except KeyboardInterrupt:
            sys.exit()
        except:
            os.system('cls')    
            print("\n!! 잘못된 입력입니다. 처음부터 다시 입력해주십시오 !!\n")
            continue
