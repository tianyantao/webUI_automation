import requests
import re
from config.globalparam import *


def get_cookie():
    t = re.findall("user=tk=.*?(?=;)", str(requests.get(
        'http://my.'+domain+'/login/prelogin?sid=2&username='+username+'&password='+password).headers))[
        0]
    return t


def get_province():
    res = requests.get("http://my."+domain+"/Ajax/GetUser?type=1",
                       headers={'Content-Type':'application/x-www-form-urlencoded','cookie':get_cookie()}).content
    return re.findall("(?<=Province:').*?(?=')",res)[0]

def get_expireyear():
    res = requests.get("http://my."+domain+"/Ajax/GetUser?type=1",
                       headers={'Content-Type': 'application/x-www-form-urlencoded', 'cookie': get_cookie()}).content
    ex_year = re.findall("(?<=ExpireYear:').*?(?=')",res)[0]
    return ex_year


