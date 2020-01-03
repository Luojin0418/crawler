from urllib.parse import urlencode
import requests
from pyquery import PyQuery as pq
import json

base_url='https://www.zhihu.com/api/v4/topics/19550228/feeds/essence?include=data%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Danswer%29%5D.target.content%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Danswer%29%5D.target.is_normal%2Ccomment_count%2Cvoteup_count%2Ccontent%2Crelevant_info%2Cexcerpt.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Darticle%29%5D.target.content%2Cvoteup_count%2Ccomment_count%2Cvoting%2Cauthor.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dtopic_sticky_module%29%5D.target.data%5B%3F%28target.type%3Dpeople%29%5D.target.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.annotation_detail%2Ccontent%2Chermes_label%2Cis_labeled%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%3F%28target.type%3Danswer%29%5D.target.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Darticle%29%5D.target.annotation_detail%2Ccontent%2Chermes_label%2Cis_labeled%2Cauthor.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics%3Bdata%5B%3F%28target.type%3Dquestion%29%5D.target.annotation_detail%2Ccomment_count%3B&limit=10'
headers={
    'Referer':'https://www.zhihu.com/',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    'x-requested-with':'fetch',
#     'cookies':'_zap=6fc39499-01e8-455e-82de-af9993c7861d; d_c0="ABCuS2Z-chCPTv6XOD7nLiR1Okf5HnjQowc=|1575341452"; _xsrf=6ZUKXHOMaSTPHAeOA4bWg8si1wbf8xMd; capsion_ticket="2|1:0|10:1575517595|14:capsion_ticket|44:NWQ0MDk0ZjhjNTk0NDUyMTliNzMxNmU2ZTU4ZGYzMGU=|28de0879844359ab4472f4e1070d0e4374584c66d04a1c88671fd61ea2fddf4f"; z_c0="2|1:0|10:1575517620|4:z_c0|92:Mi4xSXhpY0JRQUFBQUFBRUs1TFpuNXlFQ1lBQUFCZ0FsVk50TXZWWGdEWTEzbkxockhoYU5uNHhweExVNVdlSFNRcFpB|d00eaefb37480d0270dd5101e4b419632f75e53acc437492ebf31cb509a54079"; q_c1=d1384048bf5743b08ee59ded18298d87|1575602618000|1575602618000; tst=r; KLBRSID=fb3eda1aa35a9ed9f88f346a7a3ebe83|1577935001|1577930949'
}

def get_Page(offset):
    params={'offset':offset}
    url = base_url+urlencode(params)
    try:
        response=requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(response.status_code)
    except requests.ConnectionError as e:
        print('Error', e.args)

def parse_page(finjson):
    if finjson:
        items = finjson.get('data')
        for item in items:
            item = item.get('target')
            zhihu = {}
            zhihu['id'] = item.get('id')
#             print(type(item.get('question')))
            zhihu['question'] = item.get('title')
            zhihu['url'] = item.get('url')
            zhihu['content'] = pq(item.get('content')).text().strip()
            zhihu['comment_count'] = item.get('comment_count')
            yield zhihu

for offset in range(25, 85, 10):
    finjson = get_Page(offset)
#     print(json)
    results = parse_page(finjson)
#     print(results)
#     print(number)
    for result in results:
#         print(type(result))
        js = json.dumps(result, indent=2, ensure_ascii=False)
        with open('Ajax.txt', 'a', encoding='utf-8') as f:
            f.write(js)