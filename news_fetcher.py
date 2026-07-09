import feedparser


RSS_FEEDS = [

    # Hacker News
    "https://hnrss.org/frontpage",

    # HackerNoon
    "https://hackernoon.com/feed",

    # Hashnode
    "https://hashnode.com/n/feed",

    # Tech sources
    "https://techcrunch.com/feed/",
    "https://www.theverge.com/rss/index.xml",
    "https://feeds.arstechnica.com/arstechnica/index",

    # Technology education/news
    "https://web.ue-germany.com/feed"

]


def fetch_news():

    news = []


    for url in RSS_FEEDS:

        try:

            feed = feedparser.parse(url)


            for item in feed.entries[:15]:


                news.append({

                    "title": item.get(
                        "title",
                        ""
                    ),

                    "link": item.get(
                        "link",
                        ""
                    ),

                    "description":
                    item.get(
                        "summary",
                        ""
                    )

                })


        except Exception as e:

            print(
                "RSS ERROR:",
                url,
                e
            )


    return news
