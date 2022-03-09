import requests
from Utilities.configurations import *
from Utilities.resources import ApiResources
from pythonBasics.payLoad import loginPayload



def before_all(context):
    context.kumuenv = context.config.userdata.get("env")
    context.link = kumuenvi(context.kumuenv)

    context.otp_secret = context.config.userdata.get("otp_secret")

    context.num = context.config.userdata.get("env")
    context.cp_num = kumuacn(context.num)




def before_feature(context, feature):
    context.headers = {'Accept': '*/*', 'Device-Id': '49582553B73D4CFCB15CBA653C6C8461',
                       'Device-Type': 'ios',
                       'Version-Code': '1224',
                       'Content-Type': 'application/json'
                       }
    context.body = {"cellphone": context.cp_num,"country_code": "+63"}

    context.url = context.link + ApiResources.sendOTP
    context.sms_response = requests.post(context.url, json=context.body,
                                         headers=context.headers)

    print(context.sms_response.json())
    context.sms_json = context.sms_response.json()
    context.sms = context.sms_json['message']
    print(context.sms)
    assert context.sms == 'A verify code has been sent to your email'

    # Retrieve OTP Code
    url2 = context.link + ApiResources.getOTP
    headers = {"otp-secret-key": context.otp_secret}
    context.sms_response = requests.get(url2,
                                        params={'cellphone': context.cp_num, 'country_code': '63', 'rate_limit': '2'},
                                        headers=headers)

    print(context.sms_response.json())
    otp_json = context.sms_response.json()
    otp = otp_json['data'][0]['verification_code']
    print(otp)
    # User login to account
    url3 = context.link + ApiResources.login
    headers = {'Device-Type': 'ios', 'Device-Id': 'f3b365ac2e06a5a2', 'Version-Code': '1224',
               'Version-Code': '1237',
               'Content-Type': 'application/json'}
    login = requests.post(url3, json={"country_code": "+63",
                                      "cellphone": context.cp_num,
                                      "verification_code": otp}, headers=headers)

    print(login.json())
    token_json = login.json()
    context.token = token_json['data']['token']
    context.guid = token_json['data']['guid']
    print("token:" + context.token)
    print("guid:" + context.guid)
