import requests
import json
from Utilities.configurations import getconfig
from Utilities.resources import ApiResources


headers = {'Accept': '*/*', 'Device-Id': '49582553B73D4CFCB15CBA653C6C8461',
           'Device-Type': 'ios',
           'Version-Code': '1224',
           'Content-Type': 'application/json'
           }
url = getconfig()['API']['PROD'] + ApiResources.sendOTP
sms_response = requests.post(url, json={"cellphone": "0000889901", "country_code": "+63"}, headers=headers)

print(sms_response.text)
sms_json = json.loads(sms_response.text)
sms = sms_json['message']
print(sms)
assert sms == 'A verify code has been sent to your email'

# Retrieve OTP Code
url2 = getconfig()['API']['PROD'] + ApiResources.getOTP
headers = {"otp-secret-key": "782a6798b2f0ce9a01be38af39ef34bd"}
sms_response = requests.get(url2, params={'cellphone': '0000889901', 'country_code': '63', 'rate_limit': '2'},
                            headers=headers)

print(sms_response.text)
otp_json = json.loads(sms_response.text)
otp = otp_json['data'][0]['verification_code']
print(otp)
# User login to account
url3 = getconfig()['API']['PROD'] + ApiResources.login
headers = {'Device-Type': 'ios', 'Device-Id': 'f3b365ac2e06a5a2', 'Version-Code': '1224',
           'Version-Code': '1237',
           'Content-Type': 'application/json'}
login = requests.post(url3, json={"country_code": "+63",
                                  "cellphone": "0000889901",
                                  "verification_code": otp}, headers=headers)

print(login.text)
token_json = json.loads(login.text)
token = token_json['data']['token']
guid = token_json['data']['guid']
print("token:" + token)
print("guid:" + guid)

# User uploads photo

url4 = getconfig()['API']['PROD'] + ApiResources.upload
headers = {
    'X-kumu-UserId': guid,
    'X-kumu-Token': token,
    'Device-Type': 'ios',
    'Device-Id': 'D90E03B9B2B64F7A9502BF2A4C41FE79',
    'Version-Code': '1224'

}
payload = {'type': 'feed'}
file = [('image_file[]',('KumuTest.jpeg',open('/Users/juliusc/Downloads/KumuTest.jpeg','rb'),'image/jpeg'))]

upload_response = requests.post(url4, headers=headers, files=file, data=payload)
print(upload_response.json())
getImage = upload_response.json()['data'][0]['image']
getImageSmall = upload_response.json()['data'][0]['image_small']

# PUBLISH PHOTO
headers = {
    'X-kumu-Token': token,
    'Device-Id': 'D90E03B9B2B64F7A9502BF2A4C41FE79',
    'Device-Type': 'ios',
    'Version-Code': '842',
    'X-kumu-UserId': guid,
    'Content-Type': 'application/json'
}
image = {'content':'helloworld1234','image_url':getImage, 'cover_image':getImageSmall}
url5 = getconfig()['API']['PROD'] + ApiResources.publish
publish_response = requests.post(url5, headers=headers, json=image, )
print(publish_response.text)
