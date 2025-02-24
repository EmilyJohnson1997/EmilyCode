import requests

# 示例 API（这里用 https://jsonplaceholder.typicode.com 作为模拟接口）
url = "https://jsonplaceholder.typicode.com/posts"

# 请求头
headers = {
    "Content-Type": "application/json",
    "User-Agent": "Python-Requests"
}

# 发送 GET 请求
response = requests.get(url, headers=headers)

# 解析返回的 JSON 数据
if response.status_code == 200:
    data = response.json()
    print("接口返回的数据:", data[:3])  # 只打印前三条数据
else:
    print("请求失败，状态码:", response.status_code)
