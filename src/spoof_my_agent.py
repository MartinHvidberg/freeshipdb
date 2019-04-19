import urllib3

user_agent = {'user-agent': 'Non of your business...'}
http = urllib3.PoolManager(10, headers=user_agent)
r1 = http.urlopen('GET', 'http://httpbin.org/headers')

print(r1.data)