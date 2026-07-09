from google import genai

from config import GEMINI_API_KEY



client = genai.Client(
    api_key=GEMINI_API_KEY
)



def process_news(news):


    articles = ""


    for i, item in enumerate(news):

        articles += f"""

خبر شماره {i+1}

عنوان:
{item['title']}

توضیح:
{item['description']}

لینک:
{item['link']}

---------------------

"""


    prompt = f"""

نقش تو:
یک سردبیر حرفه‌ای اخبار تکنولوژی هستی.


وظیفه:

از بین تمام خبرهای زیر اخبار مهم واقعی را انتخاب کن.

هیچ محدودیت عددی برای تعداد خبرها نداریم.
هر تعداد خبری که ارزش خواندن دارد بیاور.


موضوعات مهم:

- هوش مصنوعی
- برنامه نویسی
- امنیت سایبری
- بلاک چین
- استارتاپ‌ها
- سخت افزار
- تحقیقات علمی


خروجی باید کاملا فارسی باشد.


قوانین بسیار مهم:

1.
متن را برای نمایش در تلگرام آماده کن.


2.
فارسی را راست به چپ بنویس.


3.
بین بخش‌ها فاصله مناسب قرار بده.


4.
ترجمه تحت‌اللفظی نکن.
معنی خبر را منتقل کن.


5.
برای هر خبر:


عنوان فارسی:


ترجمه و توضیح:


خلاصه:


چرا مهم است:


منبع:


---------------------


از علامت‌های عجیب استفاده نکن.


اخبار:

{articles}

"""


    response = client.models.generate_content(

        model="gemini-2.5-flash",

        contents=prompt

    )


    return response.text
