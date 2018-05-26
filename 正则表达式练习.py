import re


with open(r"C:/Users/城/Desktop/网页.txt", "r") as f:
    k = f.read()
    po = re.sub(r"<[^>]*>","",k)
print(po)


key = r"chuxiuhong@hit.edu.cn"
p1 = re.search(r"@.*t\.",key)
print(p1.group())
