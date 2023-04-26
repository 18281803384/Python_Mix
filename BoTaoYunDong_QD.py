import requests

cookies = {
    'QZ_SID': '9E31F5B926481E2ACD7E1833D8F65538',
    'sensorsdata2015jssdkcross': '%7B%22%24device_id%22%3A%2218793ad252a747-0a0825a51e454-744c1251-329160-18793ad252b12f7%22%7D',
    'sa_jssdk_2015_m_topsports_com_cn': '%7B%22distinct_id%22%3A%228a7a099f7c272839017ca634ab6f605d%22%2C%22first_id%22%3A%228a7a099f7c272839017ca634ab6f605d%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg3OTNhZDI1MmE3NDctMGEwODI1YTUxZTQ1NC03NDRjMTI1MS0zMjkxNjAtMTg3OTNhZDI1MmIxMmY3IiwiJGlkZW50aXR5X2xvZ2luX2lkIjoiOGE3YTA5OWY3YzI3MjgzOTAxN2NhNjM0YWI2ZjYwNWQiLCIkaWRlbnRpdHlfYW5vbnltb3VzX2lkIjoiOGE3YTA5OWY3YzI3MjgzOTAxN2NhNjM0YWI2ZjYwNWQifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%228a7a099f7c272839017ca634ab6f605d%22%7D%7D',
    'AppVersion': '3.0.3',
    'DeviceName': 'iPhone14,5',
    'OS': 'iOS15.5',
    'Device': '60324821583ce4226b38b8278e8c137b45e27f1c57148fc65c6bca04ec5bafee',
    'LoginToken': '9282e811-172a-4c9b-9920-3dc78a6d353c',
    'Source': 'ios',
    'memberId': '8a7a099f7c272839017ca634ab6f605d',
    'utm': 'AppStore',
    'acw_tc': '3ccdc14816819722168206291e416687e4cbba944a4159e336e384585b9610',
    'Hm_lvt_4a2fabef213b64697fb9ab3a6e6b3fcd': '1681809844',
    'Hm_lvt_0a5ea3a2650218d6fbebdb7ff9b9acd4': '1681809854',
}

headers = {
    'Host': 'm.topsports.com.cn',
    'brandCode': 'TS',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Content-Type': 'application/json',
    'Origin': 'https://m.topsports.com.cn',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 TopsportsApp/3.0.3 OS/iOS15.5 DeviceName/iPhone14,5',
    'Connection': 'keep-alive',
    'Referer': 'https://m.topsports.com.cn/m/dailycenter?brandCode=TS',
}

json_data = {
    'activityId': '0ae7d533258944bdae0aa23ce55925ec',
    'brandCode': 'TS',
}

response = requests.post('https://m.topsports.com.cn/h5/act/signIn/doSign', cookies=cookies, headers=headers, json=json_data)

print(response.text)
print(response.status_code)