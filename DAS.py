import requests
url = 'http://172.17.50.43/creative'
r = requests.get(url)#
print(r.text)
#This will get the status code
print('Status code:\n ******')
print("\t*", r.status_code)
print('*****')
#This will only get the headers only
h = requests.head(url)
print('Header:n\******')
#To print line by line
for x in h.headers:
    print("\t",x,":", h.headers[x])
print('*******')
url2 = 'http://172.17.50.43/headers.php'
headers = {'User-Agent': 'Mobile'}
response = requests.get(url2,headers= headers)
html = response.text
print(response.text)