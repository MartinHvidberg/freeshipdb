import urllib2

url = '7116808'

response = urllib2.urlopen(url)
webContent = response.read()

f = open('7116808.html', 'w')
f.write(webContent)
f.close


---

# query the website and return the html to the variable 'page'
page = urllib.request.urlopen(urlpage)
# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')