from itertools import product
import requests

words = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*'

def find_form(form_val):
    if form_val[0].find("name") == 1: form_val = form_val[1]
    else :
        cnt = 0
        while(True):
            if form_val[cnt].find("name") == 1 : 
                form_val = form_val[cnt+1]
                break
            else : cnt += 1
    return form_val


def brutefoce_attack():
    count = 0
    temp = None
    login_url = input("로그인 URL 입력 : ")
    id = input("\nID 입력 : ")
    print("\n로그인 실패 시 표시되는 문구를 입력해주십시오. (예) Login Fail, Password Incorrect, 로그인 실패")
    login_fail_text = input("\n입력 : ")

    temp_address = requests.post(login_url)
    name_id = temp_address.text.split('<input type="text"')
    name_id = name_id[1].split("\"")
    name_id = find_form(name_id)
    name_pw = temp_address.text.split('<input type="password"')
    name_pw = name_pw[1].split('\"')
    name_pw = find_form(name_pw)
    for password_length in range(6):
        for password in product(words, repeat=password_length):
            password =''.join(password)
            login_packet = {
                name_id : id,
                name_pw : password,
            }
            address = requests.post(login_url, data=login_packet)
            count += 1
            print(f"무차별 대입 허용 횟수 : {count}", end='\r')
            if count == 50 :
                print("\n무차별 대입 공격에 취약합니다.")
                inspection_value = "취약"
                break
            elif address.text.find(login_fail_text) == -1:
                if count <= 1 :
                    print("로그인 실패 문구를 잘못 입력했습니다.")
                    temp = 1
                elif count <= 3 and count > 1 :
                    print("\n무차별 대입 공격 미허용")
                    inspection_value = "양호"
                elif count > 5 and count < 10 :
                    print("\n무차별 대입 공격을 완전히 허용하지는 않으나, 시도 회수 제한이 필요합니다.")
                    inspection_value = "위험"
                break
        if count == 50 or temp == 1 :
            break
    return inspection_value