import requests

def scan_method(scan_url):
    total_info = {}
    method = []
    res_option = requests.options(scan_url)
    res_head = requests.head(scan_url)
    res_get = requests.get(scan_url)
    res_post = requests.post(scan_url)
    res_put = requests.put(scan_url)
    res_delete = requests.delete(scan_url)

    if res_option.status_code == 200 :
        try :  
            if res_option.headers['allow'] :
                total_info['method'] = res_option.headers['allow']
                if res_option.headers['server'] :
                    total_info['server_info'] = res_option.headers['server']
                else : pass
        except :
            total_info['server_info'] = res_option.headers['server']
            if res_head.status_code == 200 : method.append('HEAD')
            if res_get.status_code == 200 : method.append('GET')
            if res_post.status_code == 200 : method.append('POST')
            if res_put.status_code == 200 : method.append('PUT')
            if res_delete.status_code == 200 : method.append('DELETE')
            total_info['method'] = method
    elif res_option.status_code != 200 and res_head.status_code != 200 :
        print("사이트 헤더 정보를 읽어올 수 없음\n")
    else :
        total_info['server_info'] = "서버 정보를 알 수 없음"
        if res_head.status_code == 200 : method.append('HEAD')
        if res_get.status_code == 200 : method.append('GET')
        if res_post.status_code == 200 : method.append('POST')
        if res_put.status_code == 200 : method.append('PUT')
        if res_delete.status_code == 200 : method.append('DELETE')
        total_info['method'] = method
    
    return total_info