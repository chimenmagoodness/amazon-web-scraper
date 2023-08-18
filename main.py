from bs4 import BeautifulSoup
import smtplib
import requests
import time
import lxml
from datetime import datetime

crawl_time = "09:30:00"
today = datetime.now()
today_time = today.time()
main_time = today_time.strftime("%H:%M:%S")

while True:
    if main_time == crawl_time:
        request_page = requests.Session()
        request_page.auth = ('user', 'pass')
        request_page.headers.update({'x-test': 'true'})
        HEADERS = ({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                    'Accept-Language': 'en-US, en;q=0.5'

        })
        url = "https://www.amazon.com/dp/B0BTQ61Z6D/" #https://www.amazon.com/dp/B0CB745VMN/"
        request_page = requests.get(url, headers=HEADERS)
        response = request_page
        soup = BeautifulSoup(response.content, "lxml")
        product_name = ""
        product_price = ""
        try:
            product_title = soup.find("span", attrs={"id": 'productTitle'})
            product_name = product_title.get_text().strip()
            price = soup.find("span", attrs={"class": 'a-offscreen'})
            product_price = price.get_text()
            with open("product-info.txt", "w+") as file:
                file.write(f"{int(product_price.replace('$', '').replace(',', '').replace('.', ''))}")
                file_info = file.read()

            if int(file_info) > int(product_price.replace('$', '').replace(',', '').replace('.', '')):
                saved = int(file_info) - int(product_price.replace('$', '').replace(',', '').replace('.', ''))
                # now getting the bot to send the product and price through an email.
                print("connecting to the host sever.../.../.../")
                mail_box = smtplib.SMTP("smtp.gmail.com", 587)
                print('connected.')
                mail_box.starttls()
                print("starting security protocol.../.../.../")
                info = f'The Product "{product_name}" current price is now {product_price}. you can now click the link below to buy\n{url}. if you buy no you have saved ${saved}'
                print("loging  in now..../.../../../")
                mail_box.login(user='1spassabite@gmail.com', password="60587102")
                print("login Success. sending email immediately..././././..../")
                mail_box.sendmail(from_addr="1stpassabite@gmail.com", to_addrs="switnexxtra@gmail.com", msg=info)
                print("Success. Success. Success. mail sent successfully\nCongratulations.")
                mail_box.quit()

        except:
            print("there was an error debug and try again.")

    else:
        print("Not time to Crawl yet")
    time.sleep(60)
# print(f"Product: {product_name}\nPrice: {product_price}")

# print(f"Product: {product_name}\nPrice: {product_price}")

# now getting the bot to send the product and price through an email.
# try:
#     print("connecting to the host sever.../.../.../")
#     mail_box = smtplib.SMTP("smtp.gmail.com", 587)
#     print('connected.')
#     mail_box.starttls()
#     print("starting security protocol.../.../.../")
#     info = f'The Product "{product_name}" current price is now {product_price}. you can now click the link below to buy\n{url}'
#     print("loging  in now..../.../../../")
#     mail_box.login(user='1spassabite@gmail.com', password="60587102")
#     print("login Success. sending email immediately..././././..../")
#     mail_box.sendmail(from_addr="1stpassabite@gmail.com", to_addrs="switnexxtra@gmail.com", msg=info)
#     print("Success. Success. Success. mail sent successfully\nCongratulations.")
#     mail_box.quit()
# except:
#     print("there was an error debug and try again.")