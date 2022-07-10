import requests

directory_sheet = open("directory_sheet.txt",'r', encoding='utf-8')
allow_list = []
scan_result = {}

# 점검 URL http://testphp.vulnweb.com/

def directory_listing(url):
    try:
        while(True):
            directory_list = directory_sheet.readline()
            result = requests.get(str(url)+directory_list)
            if directory_list == '' : break
            if result.status_code == 200 :
                allow_list.append(str(url)+directory_list)
    except:
        pass
    
    if len(allow_list) == 0 :
        scan_result['dic_listing'] = "양호"
        scan_result['allow_list'] = "없음"
    elif len(allow_list) > 0 :
        scan_result['dic_listing'] = "취약"
        scan_result['allow_list'] = allow_list
    return scan_result