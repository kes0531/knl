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

def add_bf(): # 무차별 대입 점검 시에만 ID 입력 및 패스워드 실패 문구 입력 창이 뜨기 위한 함수
    if bf_option.get() == 1 :
        bf_id.grid(row=5, column=0, columnspan=2)
        input_id.grid(row=6, column=0, columnspan=2)
        bf_pw.grid(row=7, column=0, columnspan=2)
        input_pw_msg.grid(row=8, column=0, columnspan=2)
    elif bf_option.get() == 0 :
        bf_id.grid_forget()
        input_id.grid_forget()
        bf_pw.grid_forget()
        input_pw_msg.grid_forget()


def run_event():
    input_val = input_url.get()
    dic_val = None
    ms_val = None
    ps_val = None
    if bf_option.get() == 1 :
        bf_val = brutefoce_attack(input_val, str(input_id.get()), str(input_pw_msg.get())) # 무차별 대입 점검 시에만 표시되는 텍스트 박스에 입력된 값을 가져옴
        progress_bar(25)
        dic_val = directory_listing(re.match(r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b.', input_val).group(0)) # 로그인 URL에선 점검 불가, 도메인만 추출하기 위해 추가
        progress_bar(50)
        result_address = address_regex(input_val)
        ms_val = scan_method("http://"+result_address)
        progress_bar(75)
        ps_val = scan_info(result_address)
        progress_bar(100)
    elif bf_option.get() == 0 :
        bf_val = 0
        dic_val = directory_listing(input_val)
        progress_bar(33)
        result_address = address_regex(input_val)
        ms_val = scan_method("http://"+result_address)
        progress_bar(66)
        ps_val = scan_info(result_address)
        progress_bar(100)
    report_maker(input_val ,bf_val, dic_val, ms_val, ps_val)



if __name__ == "__main__":
    tk = Tk()
    tk.title("웹 취약점 점검 도구")
    input_guide = Label(tk, text="웹 취약점 관련 정보를 쉽게 제공하고자 제작되었습니다.\n악용 시 법에 저촉될 수 있습니다.\n\n무차별 대입 공격 점검을 희망한다면\n로그인 페이지 URL을 입력해주세요. \n\nURL 입력하고 실행 시 점검이 시작됩니다.")
    input_guide.grid(row=0, column=0, columnspan=2)
    
    input_url = Entry(tk, width=40) # URL 입력 텍스트 바
    input_url.grid(row=1, column=0)

    run_button = Button(tk, text="실행",command=run_event) # 실행 버튼
    run_button.grid(row=1, column=1)

    options_guide = Label(tk, text="무차별 대입 공격 점검 여부")
    options_guide.grid(row=2, column=0, columnspan=2)

    bf_option = IntVar()
    check_bf_option = Checkbutton(tk, text="점검 시 체크", variable=bf_option, command=add_bf)
    check_bf_option.grid(row=3, column=0, columnspan=2)

    # 무차별 공격 점검시에만 표시될 입력 폼들
    bf_id = Label(tk, text="ID")
    bf_id.grid(row=5, column=0, columnspan=2)
    input_id = Entry(tk)
    input_id.grid(row=6, column=0, columnspan=2)
    bf_pw = Label(tk, text="아래에 로그인 실패 시 문구를 입력\n(예) Login Fail, Password Incorrect, 로그인 실패")
    bf_pw.grid(row=7, column=0, columnspan=2)
    input_pw_msg = Entry(tk, width=30)
    input_pw_msg.grid(row=8, column=0, columnspan=2)
    # 점검하지 않을 시에는 보이지 않기 위해 미리 숨겨둠
    bf_id.grid_forget()
    input_id.grid_forget()
    bf_pw.grid_forget()
    input_pw_msg.grid_forget()

    cur_pb = DoubleVar()
    stats_pb = Progressbar(tk, maximum=100, length=320, variable=cur_pb)
    stats_pb.grid(row=9, column=0, columnspan=2)

    tk.mainloop()
   
