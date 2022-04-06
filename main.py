from bs4 import BeautifulSoup
import lxml
import requests
import smtplib

MY_EMAIL = "x@gmail.com"
PASSWORD = "xx"

url2 = 'https://www.amazon.com/dp/B01LYP2A8Q/ref=sspa_dk_detail_0?pd_rd_i=B01LYP2A8Q&pd_rd_w=TZHwu&pf_rd_p=57cbdc41-b' \
       '731-4e3d-aca7-49078b13a07b&pd_rd_wg=xQLx2&pf_rd_r=X799MZ2QRS8WPQC5N381&pd_rd_r=de3087ef-11f9-4251-8197-bfc42f' \
       'f2c93d&s=sporting-goods&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyRTk5MkowTjJOWjJHJmVuY3J5cHRlZElkPUEwNDY0MjkwMUtXMldQ' \
       'OTUyUDc2SCZlbmNyeXB0ZWRBZElkPUEwMDI1NjM1MjBYS1FHT0JDUzNTQiZ3aWRnZXROYW1lPXNwX2RldGFpbF90aGVtYXRpYyZhY3Rpb249Y' \
       '2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU&th=1'

accept_language = 'es-419,es;q=0.9'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Sa' \
             'fari/537.36'
url = 'https://www.amazon.com/dp/B07W55DDFB/ref=redir_mobile_desktop?_encoding=UTF8&returnFromLogin=1'

headers = {
    'Accept-Language': accept_language,
    'User-Agent': user_agent
}
response = requests.get(url=url2, headers=headers)

soup = BeautifulSoup(response.content, 'lxml')

price = soup.find(name='span', class_='a-offscreen').getText()
price_ = float(price.strip('US$'))
print(price_)

if price_ <= 30.00:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs='baalbornozl@unal.edu.co',
            msg=f'Subject: Protector más barato. \n\n El protector que estabas buscando ahora está costando '
                f'{price_}'.encode('utf8')
        )



