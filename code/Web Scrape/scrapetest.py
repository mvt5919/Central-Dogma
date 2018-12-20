from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

try:
	html = urlopen('http://pythonscraping.com/pages/page1.html')

except HTTPError as e:
	print(e)




