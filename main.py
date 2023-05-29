import requests
from bs4 import BeautifulSoup
import smtplib

target_price = 45000

EMAIL = YOUR_EMAIL
PASS = YOUR_PASS
URL = "https://www.hepsiburada.com/iphone-13-pro-max-128-gb-p-HBCV00000ODIWT"

def send_mail(name):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASS)
        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg=f"Subject: Indirimmm!Sectiginiz {name} urunu indirimde!\n\n"
                                                                 f"\nAsagidaki linke tiklayarak urune ulasabilirsiniz.\n"
                                                                 f"{URL}")
    print("gonderildi")

header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "Accept-Language":"tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Encoding":"gzip, deflate, br"

}
response = requests.get(url=URL, headers=header)

soup = BeautifulSoup(response.text, "lxml")
price_str = soup.find("span", class_="price")
price_str = price_str.find("span").get_text()
print(price_str)
price = ""

for number in price_str:
    try:
        if int(number) or number == "0":
            price = price + number

    except ValueError:
        pass

price = int(price)

name = soup.find("h1", id="product-name")
name = name.getText().split("        ")[1].split("\r")[0]

if target_price >= price:
     send_mail(name)
