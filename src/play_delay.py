import urllib3
import time

str_url = r"https://www.balticshipping.com/vessel/imo/9060730"

http = urllib3.PoolManager()
r = http.request('GET', str_url, preload_content=False)
for chunk in r.stream(32):
    time.sleep(0.01)
    print(chunk)
r.release_conn()