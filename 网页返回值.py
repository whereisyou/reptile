import requests


r = requests.get('http://ww2.sinaimg.cn/bmiddle/005IXZdnjw1ermv25ktjfj30ae0ewdhm.jpg')
with open('a.jpg','wb') as f:
	f.write(r.content)