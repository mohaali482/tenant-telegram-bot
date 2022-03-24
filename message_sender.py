import requests
from plugins.settings import API

def send_message (chat_id, message):
    url_req = "https://api.telegram.org/bot" + API + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + message 
    results = requests.get(url_req)