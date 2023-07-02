# pytest
### 搭建自动化测试环境

```shell
# 安装requests
pip install requests
# 查看安装情况
pip show requests
```

### 项目结构目录

```

```

### requests使用

requests方法模板

`requests.请求方法(url, param=None, data=None, json=None, headers=None, proxies=cur_proxy)`

方法说明：

- 常见请求方法：get，post，put，delete
- url：请求的url地址
- params：请求查询参数
- data：请求体为form表单时设置参数
- json：请求体为json时设置参数
- headers：请求头设置参数
- proxies：发送请求时，是否设置代理

```python
# 不使用代理
cur_proxy = {
    'http': None,
    'https': None
}
```

requests请求返回response说明：

response.status_code：返回状态码

response.json()：json格式的响应内容

response.text：文本格式的响应内容

response.url：请求url

response.encoding：查看响应头部的字符编码

response.headers：头信息

response.cookies：cookies信息
