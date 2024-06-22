# simple_http_client.py
import requests

def get_website_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return None

if __name__ == "__main__":
    url = 'https://www.example.com'
    content = get_website_content(url)
    if content:
        print("Website Content:")
        print(content[:500])  # Print first 500 characters
    else:
        print("Failed to retrieve the website content")
