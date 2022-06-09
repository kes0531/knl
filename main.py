import sys, os, re
import webbrowser
from bruteforce import *
from scan_method import *
from scan_port import *

url_regex = re.compile("([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?")
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

def report_maker(bf_val, ms_val, ps_val) :
    this_path = os.getcwd()
    template = open('template.html', 'r', encoding='UTF-8')
    report_template = template.read()
    if bf_val == 0 :
        report_template = report_template.replace("{bf_result}", "무차별 대입 공격 점검 미실시")
        report_template = report_template.replace("{ms_result}", str(ms_val))
        report_template = report_template.replace("{ps_result}", str(ps_val))
    else :
        report_template = report_template.replace("{bf_result}", str(bf_val))
        report_template = report_template.replace("{ms_result}", str(ms_val))
        report_template = report_template.replace("{ps_result}", str(ps_val))
    report_output = open('inspection_report.html', 'w')
    report_output.write(report_template)
    template.close()
    webbrowser.get(chrome_path).open(this_path+'/inspection_report.html')


if __name__ == "__main__":
    print("\nWeb-vulnerability-scan-tool ver.1 - KNL\n")
    bf_val = None
    ms_val = None
    ps_val = None
    print("로그인 무차별 대입 공격에 대한 점검을 포함하시려면 아래 입력에 숫자 1 을 입력해주십시오. \n")
    while(True):
        try:
            input_val = input("점검하실 URL을 입력해주십시오. \n입력 : ")
            if input_val == '1' :
                bf_val = brutefoce_attack()
            elif bf_val == None :
                bf_val = 0
                # if url_regex.search(input_val.replace(" ","")) is None :
                #     print("URL 이 올바르지 않습니다. 다시 입력해주세요.")
                #     continue
                ms_val = scan_method(input_val)
                domain_address = re.sub("http(s)?:\/\/", '', input_val)
                result_address = domain_address.strip('/')
                ps_val = scan_info(result_address)
            report_maker(bf_val, ms_val, ps_val)
            print("\n점검 완료")
            break
        except KeyboardInterrupt:
            sys.exit()
        except:
            os.system('cls')    
            print("\n!! 잘못된 입력입니다. 처음부터 다시 입력해주십시오 !!\n")
            continue
