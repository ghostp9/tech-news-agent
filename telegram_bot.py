import requests

from config import BOT_TOKEN, CHAT_ID



def send_message(message):

    url = (
        f"https://api.telegram.org/"
        f"bot{BOT_TOKEN}/sendMessage"
    )


    max_length = 4000


    parts = [
        message[i:i + max_length]
        for i in range(0, len(message), max_length)
    ]


    for part in parts:

        data = {

            "chat_id": CHAT_ID,

            "text": part,

            "disable_web_page_preview": True

        }


        response = requests.post(
            url,
            data=data
        )


        if response.status_code != 200:

            raise Exception(
                response.text
            )
