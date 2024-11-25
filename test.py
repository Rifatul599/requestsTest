import requests
r=requests.get('https://imgs.xkcd.com/comics/python.png')

with open('comic.png','wb') as f:
    f.write(r.content)

print(r.status_code)

print(r.ok)

print(r.headers)

payload={'page':2, 'count':25}

r=requests.get('https://httpbin.org/get', params=payload)
print(r.text)
print(r.url)

payload={'username':'Rifat', 'password':'Testing'}
r=requests.post('https://httpbin.org/post', data=payload)

print(r.text)
print(r.json())
r_dict=r.json()
print(r_dict['form'])

r=requests.get('https://httpbin.org/basic-auth/Rifat/Testing', auth=('Rifat' , 'Testing'))
print(r.text)
print(r)