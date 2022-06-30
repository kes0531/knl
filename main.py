from tkinter import *
from tkinter.ttk import Progressbar
import os, re
import webbrowser
from bruteforce import *
from scan_method import *
from scan_port import *
from directory_listing import *

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

def progress_bar(stats_val):
    cur_pb.set(stats_val)
    stats_pb.update()

def run_event():
    input_val = input_url.get()
    bf_val = None
    dic_val = None
    ms_val = None
    ps_val = None
    # try:
        # if input_val == '1' :
        #     bf_val = brutefoce_attack(input_val)
        #     dic_val = directory_listing(input_val)
        #     result_address = address_regex(input_val)
        #     ms_val = scan_method("http://"+result_address)
        #     ps_val = scan_info(result_address)
    if bf_val == None :
        bf_val = 0
        dic_val = directory_listing(input_val)
        progress_bar(33)
        result_address = address_regex(input_val)
        ms_val = scan_method("http://"+result_address)
        progress_bar(66)
        ps_val = scan_info(result_address)
        progress_bar(100)
    report_maker(input_val ,bf_val, dic_val, ms_val, ps_val)
    # except:
    #     os.system('cls')    
    #     print("\n!! 잘못된 입력입니다. 처음부터 다시 입력해주십시오 !!\n")
    #     continue



if __name__ == "__main__":
    tk = Tk()
    tk.title("웹 취약점 점검 도구")
    input_guide = Label(tk, text="웹 취약점 관련 정보를 쉽게 제공하고자 제작되었습니다.\n악용 시 법에 저촉될 수 있습니다.\n \nURL 입력하고 실행 시 점검이 시작됩니다.")
    input_guide.grid(row=0, column=0, columnspan=2)
    
    input_url = Entry(tk, width=40) # URL 입력 텍스트 바
    input_url.grid(row=1, column=0)

    button = Button(tk, text="실행",command=run_event) # 실행 버튼
    button.grid(row=1, column=1)

    # options_guide = Label(tk, text="무차별 대입 공격 점검")
    # options_guide.grid(row=2, column=0, columnspan=2)

    # bf_options = IntVar()
    # option_1 = Radiobutton(tk, text="실행", value=1, variable=bf_options, command=bf_option)
    # option_1.grid(row=3, column=0, columnspan=2)
    # option_2 = Radiobutton(tk, text="미실행", value=0, variable=bf_options, command=bf_option)
    # option_2.grid(row=4, column=0, columnspan=2)

    cur_pb = DoubleVar()
    stats_pb = Progressbar(tk, maximum=100, length=320, variable=cur_pb)
    stats_pb.grid(row=6, column=0, columnspan=2)

    tk.mainloop()
   
