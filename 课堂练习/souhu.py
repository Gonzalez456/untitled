import requests
import re


def get_one():
    url = 'https://wenku.baidu.com/view/562720991b37f111f18583d049649b6648d7093a.html'
    headers = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1; 125LA; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022)'
    }
    request = requests.get(url, headers=headers)
    return request.text


def get_rs(html):
    pattern = re.compile(r'.*?(\u4E00-\u9FA5).*?', re.S)
    res = re.findall(pattern, html)
    return res


def get_save(text):
    text = str(text)
    with open(r'C:\Users\Administrator\Desktop\新建文本文档.txt', 'a', encoding='utf-8') as f:
        f.write(text)


def main():
    html = get_one()
    print(html)
    text = get_rs(html)
    print(text)
    get_save(text)



if __name__ == '__main__':
    main()
