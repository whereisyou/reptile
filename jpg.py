import requests


r = requests.get('http://www.360buy.com')
try:
	r.raise_for_status()
	r.encoding = r.apparent_encoding
	print(r)
except:
	print('产生异常')