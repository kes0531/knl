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
            else : print("응답코드",res_head.status_code," HEAD 미사용")
            if res_get.status_code == 200 : method.append('GET')
            else : print("응답코드 ",res_head.status_code," GET 미사용")
            if res_post.status_code == 200 : method.append('POST')
            else : print("응답코드 ",res_head.status_code," POST 미사용")
            if res_put.status_code == 200 : method.append('PUT')
            else : print("응답코드 ",res_head.status_code," PUT 미사용")
            if res_delete.status_code == 200 : method.append('DELETE')
            else : print("응답코드 ",res_head.status_code," DELETE 미사용")
            total_info['method'] = method
        return total_info
    else :
        print("사이트 헤더 정보를 읽어올 수 없음\n")