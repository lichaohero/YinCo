from django.db import models
import hashlib
import json

from django.http import JsonResponse
from django.shortcuts import render
import time
from django.conf import settings
from user.models import UserProfile



# Create your models here.
def tokens(request):
    #登录
    if request.method != 'POST':
        result = {'code': 10200 , 'error': 'Please use POST'}
        return JsonResponse(result)
    json_str = request.body
    json_obj = json.loads(json_str)
    username = json_obj['username']
    password = json_obj['password']

    users = UserProfile.objects.filter(username=username)
    if not users:
        result = {'code': 10201, 'error':'username or password is wrong !!'}
        return JsonResponse(result)

    user = users[0]
    m = hashlib.md5()
    m.update(password.encode())
    if m.hexdigest() != user.password:
        result = {'code': 10202, 'error': 'username or password is wrong !!'}
        return JsonResponse(result)
    #发门票
    token = make_token(username)
    result = {'code':200, 'username':username,'data':{'token':token.decode()},'carts_count':0}
    return JsonResponse(result)



def make_token(username, expire=3600*24):
    import jwt
    now = time.time()
    key = settings.SHOP_TOKEN_KEY
    payload = {'username':username, 'exp':int(now+expire)}
    return jwt.encode(payload, key, algorithm='HS256')