import requests

from config import BOT_TOKEN, CHAT_ID



def send_message(message):


    url = (

        f"https://api.telegram.org/"

        f"bot{BOT_TOKEN}/sendMessage"

    )


    data = {


        "chat_id": CHAT_ID,


        "text": message,


        "parse_mode": "HTML",


        "disable_web_page_preview": True

    }


    response = requests.post(

        url,

        data=data

    )


    if response.status_code != 200:

        print(response.text)
