import urllib
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "utf-8",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Cache-Control": "max-age=0"
} 


for link in range(0,51):
    try:
        url = 'https://www.pro-football-reference.com/years/'+str(1970+link)+'/games.htm'
        request = urllib.request.Request( url, None, headers )
        response = urllib.request.urlopen( request )
        with open('data/'+'page'+str(link+1)+'.html', 'w') as f:
            f.write(str(response.read()))
        time.sleep(10)
    except urllib.error.HTTPError as err:
        print(err)
        print("No page with start "+" found")