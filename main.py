from news_fetcher import fetch_news

from database import (
    init_db,
    is_duplicate,
    save_news
)

from ai_processor import process_news

from telegram_bot import send_message




def main():

    init_db()


    news = fetch_news()


    fresh_news = []


    for item in news:


        if not is_duplicate(item["link"]):

            fresh_news.append(item)

            save_news(
                item["link"]
            )


    if len(fresh_news) == 0:


        send_message(
            "امروز خبر جدیدی پیدا نشد."
        )


        return



    result = process_news(
        fresh_news
    )



    send_message(
        result
    )



if __name__ == "__main__":

    main()
