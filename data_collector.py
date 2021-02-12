from bs4 import BeautifulSoup
import requests
import re
import schedule,time


def main():
    my_header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/79.0.3945.88 Safari/537.36'}
    URL = 'https://minfin.com.ua/currency/crypto/'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all('span', class_='coin-price--num')
    pattern = '\d{2}\s\d{3}'
    a = re.findall(pattern,str(results))
    btc = a[0]
    f = open("BTC-USD.txt",'a')
    wrt = str(btc)+'\n'
    f.write(wrt)
    print(btc)


if __name__ == '__main__':
    main()
    schedule.every(1).day.at("10:30").do(main)
    while 1:
        schedule.run_pending()
        time.sleep(1)
