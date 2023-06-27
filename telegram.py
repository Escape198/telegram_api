

def send_telegram_message(text: str) -> dict:
    token = "XXXXXXXXXX:XXXXXXX_XXXXXXXXXXXXXXXXXXXXXXXXXXX"
    chat_id = "-XXXXXXXXX"
    url_req = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}"
    results = requests.get(url_req)
    return results.json()


def main(request):
    if request.method == 'POST':
        try:
            pass
        except Exception as _ex:
            send_telegram_message(u'\U0001F525' + u'\U0001F525' + u'\U0001F525' + f'''
                Error occurred \n
                Error text: {_ex} \n
                Request: {request.POST}
            ''')
