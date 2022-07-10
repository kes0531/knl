import requests
from tqdm import tqdm

# 점검 URL http://testphp.vulnweb.com/

def directory_listing(url):
    directory_sheet = open("directory_sheet.txt",'r', encoding='utf-8')
    directory_index = directory_sheet.read().split('\n')
    allow_list = []
    scan_result = {}
    try:
        for i in tqdm(range(len(directory_index))) :
            result = requests.get(str(url)+directory_index[i])
            if result.status_code == 200 :
                allow_list.append(str(url)+directory_index[i])
    except:
        pass
    
    if len(allow_list) == 0 :
        scan_result['dic_listing'] = "양호"
        scan_result['allow_list'] = "없음"
    elif len(allow_list) > 0 :
        scan_result['dic_listing'] = "취약"
        scan_result['allow_list'] = allow_list
    return scan_result