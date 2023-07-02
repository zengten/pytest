import requests

url = 'http://kdtx-test.itheima.net/api/login'
login_data = {
    "username": "admin",
    "password": "HM_2023_test",
    "code": "2",
    "uuid": "8575f18fceb940e48a474fdeba9b5f65"
}
login_header = {
    "Content-Type": "application/json"
}
login_resp = requests.post(url, json=login_data, headers=login_header)
print(login_resp.status_code)
print(login_resp.json())
