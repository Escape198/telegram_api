

def send_telegram_message(text):
    token = "XXXXXXXXXX:XXXXXXX_XXXXXXXXXXXXXXXXXXXXXXXXXXX"
    chat_id = "-XXXXXXXXX"
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    results = requests.get(url_req)
    return results.json()
