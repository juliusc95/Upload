import configparser


def getconfig():
    config = configparser.ConfigParser()
    config.read('Utilities/properties.ini')
    return config


def kumuenvi(envbehave):
    if envbehave == 'prod':
        url = getconfig()['API']['PROD']
    elif envbehave == 'stg':
        url = getconfig()['API']['STG']
    else:
        url = getconfig()['API']['DEV']
    return url


def kumuacn(acn_behave):
    if acn_behave == 'prod':
        cp_num = '0000889901'
    elif acn_behave == 'stg':
        cp_num = '0000889901'
    else:
        cp_num = '0000567098'
    return cp_num
