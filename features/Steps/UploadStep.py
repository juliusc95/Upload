import requests
import json
from behave import *
from Utilities.configurations import *
from Utilities.resources import *



@given('User is logged in given a photo')
def step_impl(context):
    context.payload = {'type': 'feed'}
    context.file = [('image_file[]',('KumuTest.jpeg',open('/Users/juliusc/Downloads/KumuTest.jpeg','rb'),'image/jpeg'))]


@when('User uploads photo')
def step_impl(context):
    context.url4 = context.link + ApiResources.upload
    headers = {
        'X-kumu-UserId': context.guid,
        'X-kumu-Token': context.token,
        'Device-Type': 'ios',
        'Device-Id': 'D90E03B9B2B64F7A9502BF2A4C41FE79',
        'Version-Code': '1224'
    }
    context.upload_response = requests.post(context.url4, headers=headers, files=context.file,
                                            data=context.payload)
    print(context.upload_response.json())
    context.getImage = context.upload_response.json()['data'][0]['image']
    context.getImageSmall = context.upload_response.json()['data'][0]['image_small']


@then('Photo is successfully uploaded')
def step_impl(context):
    headers = {
        'X-kumu-Token': context.token,
        'Device-Id': 'D90E03B9B2B64F7A9502BF2A4C41FE79',
        'Device-Type': 'ios',
        'Version-Code': '842',
        'X-kumu-UserId': context.guid,
        'Content-Type': 'application/json'
    }
    image = {'content': 'helloworld1234', 'image_url': context.getImage, 'cover_image': context.getImageSmall}
    url5 = context.link + ApiResources.publish
    publish_response = requests.post(url5, headers=headers, json=image, )
    print(publish_response.json())
    context.publish_json = publish_response.json()
    assert context.publish_json['message'] == "Publish successfully"
