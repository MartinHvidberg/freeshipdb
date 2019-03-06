import requests

r = requests.get('https://gisis.imo.org/Public/SHIPS/ShipDetails.aspx?IMONumber=9501916', auth=('bayoptic', '***'))
print(r.status_code)
#200
r.headers['content-type']
#'application/json; charset=utf8'
r.encoding
#'utf-8'
print(r.text)
#u'{"type":"User"...'
#r.json()
#{u'private_gists': 419, u'total_private_repos': 77, ...}