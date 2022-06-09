import requests

def scan_method(scan_url):
    method = ''
    res_option = requests.options(scan_url)
    res_head = requests.head(scan_url)
    res_get = requests.get(scan_url)
    res_post = requests.post(scan_url)
    res_put = requests.put(scan_url)
    res_delete = requests.delete(scan_url)

    # print("\n사용중인 method\n")
    if res_option.status_code == 200 :
        try :  
            if res_option.headers['allow'] :
                print(res_option.headers['allow'],"사용")
                if res_option.headers['server'] :
                    print("Server info:",res_option.headers['server'])
                else : pass
        except :
            # print("웹사이트 Server 정보\n",res_option.headers['server'])
            if res_head.status_code == 200 : method += ' ' + 'HEAD'
            else : print("응답코드",res_head.status_code," HEAD 미사용")
            if res_get.status_code == 200 : method += ' ' + 'GET'
            else : print("응답코드 ",res_head.status_code," GET 미사용")
            if res_post.status_code == 200 : method += ' ' + 'POST'
            else : print("응답코드 ",res_head.status_code," POST 미사용")
            if res_put.status_code == 200 : method += ' ' + 'PUT'
            else : print("응답코드 ",res_head.status_code," PUT 미사용")
            if res_delete.status_code == 200 : method += ' ' + 'DELETE'
            else : print("응답코드 ",res_head.status_code," DELETE 미사용")
        return method
    else :
        print("사이트 헤더 정보를 읽어올 수 없음\n")