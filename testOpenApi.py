__author__ = "zhaichuang"

import sqlite3,requests,json,re,time


def cmp(src_data,dst_data):
    if isinstance(src_data, dict):
        """若为dict格式"""
        for key in dst_data:
            if key not in src_data:
                print("src不存在这个key:%s"%key)
        for key in src_data:
            if key in dst_data:
                global thiskey
                thiskey = key
                """递归"""
                cmp(src_data[key], dst_data[key])
            else:
                dict[key] = ["dst不存在这个key"]
    elif isinstance(src_data, list):
        """若为list格式"""
        if len(src_data) != len(dst_data):
            print("list len: '{}' != '{}'".format(len(src_data), len(dst_data)))

        for src_list, dst_list in zip(src_data, dst_data):
            print(src_data,dst_data)
            """递归"""
            cmp(src_list, dst_list)
    else:
        if str(src_data) != str(dst_data):
            print("%s:%s != %s:%s"%(thiskey,src_data,thiskey,dst_data))


conn = sqlite3.connect("./db.sqlite3")
cu = conn.cursor()
def access_token():
    token_url ="https://testapi.weishao.com.cn"
    access_token_api = cu.execute("select * FROM apitest_apiinfo WHERE id =2").fetchone()
    token_name = access_token_api[1]
    token_path = access_token_api[13]
    token_method = access_token_api[12]
    token_request = access_token_api[3]
    token_response = access_token_api[4]
    token_request = json.loads(token_request)
    # token_request["app_key"]="14383894cd370976"
    # token_request["app_secret"]="40cbaac53cbe2e40d47fa13c054f4a24"
    token_request["app_key"]="c2a5f03cf652b821"
    token_request["app_secret"]="e78dae941ebc64a42abc9299584d9d2b"
    res = requests.post(token_url+token_path,data=token_request,verify=False)
    token = res.json()["access_token"]
    refresh_token = res.json()["refresh_token"]
    token_response = json.loads(token_response)
    if len(res.json()) == len(token_response):
        if res.json().keys() == token_response.keys():
            print("access_token 测试通过")
        print("两次结果不同的地方:")
        print(cmp(token_response,res.json()))
    #print(res.elapsed.microseconds/1000000)
    return {"token":token,"refresh_token":refresh_token}

def gettoken_refresapi():
    token_url ="https://testapi.weishao.com.cn"
    refresh_token_api = cu.execute("select * FROM apitest_apiinfo WHERE id =3").fetchone()
    refresh_name = refresh_token_api[1]
    refresh_path = refresh_token_api[13]
    refresh_method = refresh_token_api[12]
    refresh_request = refresh_token_api[3]
    refresh_response = refresh_token_api[4]
    refresh_response = json.loads(refresh_response)
    refresh_request = json.loads(refresh_request)
    #更新appkey appsecret refresh_token
    refresh_request["app_key"]="c2a5f03cf652b821"
    refresh_request["app_secret"]="e78dae941ebc64a42abc9299584d9d2b"
    refresh_request["refresh_token"]=access_token()["refresh_token"]
    #发送请求并返回结果
    res = requests.post(token_url+refresh_path,data=refresh_request,verify=False)
    result = res.json()
    token = result["access_token"]
    if len(result) == len(refresh_response):
        if result.keys() == refresh_response.keys():
            print("refresh_api测试通过")
            print("两次结果不同的地方:")
            print(cmp(refresh_response,result))
    return token


def runAll(token,url):
    success =[]
    failed = []
    apis = cu.execute("select * FROM apitest_apiinfo WHERE id>3").fetchall()
    for api in apis:
        name = api[1]
        path = api[13]
        method = api[12]
        request = api[3]
        response = api[4]
        #将response结果转为json
        try:
            response = json.loads(response)
        except Exception as e:
            print("response json.loads出错:",e)

        #替换token
        if "access_token" in path:
            path = re.sub(r"[a-zA-Z0-9]{32}",token,path)
        if "access_token" in request:
            request = re.sub(r"[a-zA-Z0-9]{32}",token,request)
        url2 = url+path
        #发送请求:
        if method == 1:
            res = requests.get(url2,params=request,verify=False)
        if method == 2:
            request = json.loads(request)
            headers = {"Content-Type":"application/json"}
            res = requests.post(url2,json=request,headers=headers,verify=False)

        print("[接口名称]:%s"%name)
        print("[接口URL]:%s"%url2)
        print("[接口请求]:%s"%request)
        print("[预期返回]:%s"%response)
        print("[实际返回]:%s"%res.json())


        # cu.execute("UPDATE apitest_apiinfo SET aresponse = '%s' WHERE aname='%s' "%(res.text,name))
        # conn.commit()
        if response == res.json():
            print("接口:%s PASS  接口返回内容全部相同"%name)
            success.append("1")
        elif response.keys() == res.json().keys():
            print("接口:%s Failed  接口返回key相同,值不同"%name)
            failed.append("1")
            print("接口返回不同点:",cmp(response,res.json()))
        else:
            pass
            # print("接口:%s Failed"%name)
            # failed.append("0")
            # print(type(response))
            # print("接口返回不同点:",cmp(res.json(),response))
        print()
    return {"success":len(success),"failed":len(failed)}
if __name__ == '__main__':
    token = gettoken_refresapi()
    url180 = "https://172.16.56.180/openapitest/openapiv2"
    urltestapi = "https://testapi.weishao.com.cn/api/v2"
    resutl = runAll(token,url180)
    print("成功:%s 失败:%s"%(resutl["success"],resutl["failed"]))