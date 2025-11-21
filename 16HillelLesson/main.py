import time
import sqlite3
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def get_data_by_selenium(url: str) -> str:
    """Звертається до сервера за URL та повертає HTML сайту"""
    options = Options()
    options.add_argument("--headless")  # запуск без відкриття вікна браузера
    options.add_argument("--disable-gpu")

    # webdriver_manager автоматично завантажує потрібний ChromeDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)
    time.sleep(3)  # можна замінити на WebDriverWait для надійності
    data = driver.page_source
    driver.quit()
    return data

def parse_data(data: str) -> list:
    """Функція парсингу даних з HTML документа"""
    rez = []
    if data:
        soup = BeautifulSoup(data, 'html.parser')
        li_list = soup.find_all('li', attrs={'class': 'catalog-grid__cell'})
        for li in li_list:
            a = li.find('a', attrs={'class': 'goods-tile__heading'})
            href = a['href']
            title = a.text.strip()

            old = li.find('div', attrs={'class': 'goods-tile__price--old'})
            price = li.find('div', attrs={'class': 'goods-tile__price'})

            old_price = None
            if old:
                old_text = ''.join(c for c in old.text if c.isdigit())
                if old_text:
                    old_price = int(old_text)

            price = int(''.join(c for c in price.text if c.isdigit()))
            rez.append((title, href, price, old_price))
    return rez

def create_table() -> bool:
    """Створює таблицю video_cards, якщо її ще немає"""
    sqlite_connection = sqlite3.connect('cards.db')
    sqlite_create_table_query = '''
        CREATE TABLE IF NOT EXISTS video_cards (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            url TEXT NOT NULL,
            price INTEGER NOT NULL,
            old_price INTEGER
        );
    '''
    cursor = sqlite_connection.cursor()
    cursor.execute(sqlite_create_table_query)
    sqlite_connection.commit()
    sqlite_connection.close()
    return True

def save_to_db(rows) -> None:
    """Підключається до бази даних та записує дані у таблицю video_cards"""
    if create_table():
        sqlite_connection = sqlite3.connect('cards.db')
        cursor = sqlite_connection.cursor()
        cursor.executemany(
            "INSERT INTO video_cards(title, url, price, old_price) VALUES (?,?,?,?)",
            rows
        )
        sqlite_connection.commit()
        sqlite_connection.close()

def main() -> None:
    """Головна функція"""
    url = 'https://hard.rozetka.com.ua/videocards/c80087/'
    data = get_data_by_selenium(url)
    rows = parse_data(data)
    save_to_db(rows)
    print(f"Збережено {len(rows)} записів у базу даних.")

if __name__ == '__main__':
    main()
