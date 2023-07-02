import requests

url = 'http://kdtx-test.itheima.net/api/captchaImage'

resp = requests.get(url)
print(resp.status_code)
print(resp.json())
