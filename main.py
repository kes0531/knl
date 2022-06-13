import sys, os, re
import webbrowser
from bruteforce import *
from scan_method import *
from scan_port import *
from directory_listing import *

url_regex = re.compile("([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?")
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

def report_maker(input_val, bf_val, dic_val, ms_val, ps_val) :
    this_path = os.getcwd()
    template = open('template.html', 'r', encoding='UTF-8')
    report_template = template.read()
    if bf_val == 0 :
        report_template = report_template.replace("{scan_url}", str(input_val))
        report_template = report_template.replace("{server_info}", str(ms_val['server_info']))
        report_template = report_template.replace("{bf_result}", "무차별 대입 공격 점검 미실시")
        report_template = report_template.replace("{ms_result}", str(ms_val['method']))
        report_template = report_template.replace("{ps_result}", str(ps_val['port_num']))
        report_template = report_template.replace("{dic_result}", str(dic_val['dic_listing']))
        report_template = report_template.replace("{allow_list}", str(dic_val['allow_list']))
    else :
        report_template = report_template.replace("{scan_url}", str(input_val))
        report_template = report_template.replace("{server_info}", str(ms_val['server_info']))
        report_template = report_template.replace("{bf_result}", str(bf_val))
        report_template = report_template.replace("{ms_result}", str(ms_val['method']))
        report_template = report_template.replace("{ps_result}", str(ps_val['port_num']))
        report_template = report_template.replace("{dic_result}", str(dic_val['dic_listing']))
        report_template = report_template.replace("{allow_list}", str(dic_val['allow_list']))
    report_output = open('inspection_report.html', 'w')
    report_output.write(report_template)
    template.close()
    webbrowser.get(chrome_path).open(this_path+'/inspection_report.html')

def address_regex(in_data):
    domain_address = re.sub("http(s)?:\/\/", '', in_data)
    temp = re.sub("\/.+", '', domain_address)
    result_address = temp.strip('/')
    return result_address



if __name__ == "__main__":
    print("\n웹_취약점_점검_도구 ver.1\n                         by.NaChangWon\n")
    print("보안 초심자 및 비전공자를 대상으로 웹 취약점 관련 정보를 쉽게 제공하고자 제작되었습니다.")
    print("악위적인 행위로 사용 시 법에 저촉될 수 있습니다.\n")
    print("테스트 사이트 : http://suninatas.com/, 자체 제작 사이트\n")
    bf_val = None
    dic_val = None
    ms_val = None
    ps_val = None
    print("로그인 무차별 대입 공격에 대한 점검을 포함하시려면 아래 입력에 숫자 1 을 입력해주십시오. \n")
    while(True):
        try:
            input_val = input("점검하실 URL 또는 옵션을 입력해주십시오. \n입력 : ")
            if input_val == '1' :
                input_val = input("점검하실 URL을 입력해주십시오. \n입력 : ")
                bf_val = brutefoce_attack(input_val)
                dic_val = directory_listing(input_val)
                result_address = address_regex(input_val)
                ms_val = scan_method("http://"+result_address)
                ps_val = scan_info(result_address)
            elif bf_val == None :
                bf_val = 0
                dic_val = directory_listing(input_val)
                result_address = address_regex(input_val)
                ms_val = scan_method("http://"+result_address)
                ps_val = scan_info(result_address)
            report_maker(input_val ,bf_val, dic_val, ms_val, ps_val)
            print("\n점검 완료")
            break
        except KeyboardInterrupt:
            sys.exit()
        except:
            os.system('cls')    
            print("\n!! 잘못된 입력입니다. 처음부터 다시 입력해주십시오 !!\n")
            continue
