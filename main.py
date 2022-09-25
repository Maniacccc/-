from datetime import date, datetime
import math
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage, WeChatTemplate
import requests
import os
import random

today = datetime.now()
start_date = os.environ['START_DATE']
city = os.environ['CITY']
birthday = os.environ['BIRTHDAY']

app_id = os.environ["APP_ID"]
app_secret = os.environ["APP_SECRET"]

user_id = os.environ["USER_ID"]
template_id = os.environ["TEMPLATE_ID"]


def get_weather():
  url = "http://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city=" + city
  res = requests.get(url).json()
  weather = res['data']['list'][0]
  return weather['weather'], math.floor(weather['low']),math.floor(weather['high'])

def get_today():
  return datetime.strftime(today, "%Y年%m月%d日 星期%w")

def get_week():
   week_list = ["星期一","星期二","星期三","星期四","星期五","星期六","星期日"]
   return week_list[today.weekday()]

def get_count():
  delta = today - datetime.strptime(start_date, "%Y-%m-%d")
  return delta.days

def get_birthday():
  next = datetime.strptime(str(date.today().year) + "-" + birthday, "%Y-%m-%d")
  if next < datetime.now():
    next = next.replace(year=next.year + 1)
  return (next - today).days

def get_words():
  words = requests.get("https://api.shadiao.pro/chp")
  if words.status_code != 200:
    return get_words()
  return words.json()['data']['text']

def get_random_color():
  return "#%06x" % random.randint(0, 0xFFFFFF)
def get_random_color1():
  return "#%06x" % random.randint(0, 0xFFFFFF)
def get_random_color2():
  return "#%06x" % random.randint(0, 0xFFFFFF)
def get_random_color3():
  return "#%06x" % random.randint(0, 0xFFFFFF)
def get_random_color4():
  return "#%06x" % random.randint(0, 0xFFFFFF)
def get_random_color5():
  return "#%06x" % random.randint(0, 0xFFFFFF)

client = WeChatClient(app_id, app_secret)

wm = WeChatMessage(client)
wea, low,high = get_weather()
data = {"weather":{"value":wea,"color":get_random_color1()},"temperature":{"value":high+"℃~"+low+℃+,"color":get_random_color2()},"today":{"value":get_today()+" "+get_week(),"color":get_random_color4()},"love_days":{"value":get_count(),"color":get_random_color5()},"words":{"value":get_words(), "color":get_random_color()}}
res = wm.send_template(user_id, template_id, data)
print(res)
