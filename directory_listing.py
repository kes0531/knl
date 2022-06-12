import requests

d_list = ['/icons/','/images/','/pr/','/adm/','/admin/','/files/','/download/','/files/attach/images', '%3f.jsp']
allow_list = []
scan_result = {}

# 점검 URL http://testphp.vulnweb.com/

def directory_listing(url):
    for i in range(len(d_list)) :
        result = requests.get(str(url)+d_list[i])
        if result.status_code == 200 :
            allow_list.append(str(url)+d_list[i])
    
    if len(allow_list) == 0 :
        scan_result['dic_listing'] = "양호"
        scan_result['allow_list'] = "없음"
    elif len(allow_list) > 0 :
        scan_result['dic_listing'] = "취약"
        scan_result['allow_list'] = allow_list

    return scan_result
