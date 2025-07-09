
import requests
import json
import datetime
import hashlib
from pymongo import MongoClient
from apscheduler.schedulers.blocking import BlockingScheduler

def get_brand(title):
    brands = ['Asus', 'Lenovo', 'HP', 'Dell', 'Acer', 'Apple', 'MSI', 'Microsoft']
    for brand in brands:
        if brand.lower() in title.lower():
            return brand
    return "Other"

def generate_hash(item):
    unique_string = item['title'] + str(item['price']) + item['link']
    return hashlib.md5(unique_string.encode('utf-8')).hexdigest()

def scrape_laptops():
    url = 'https://api.digikala.com/v1/search/?q=لپتاپ&page=1'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    data = response.json()

    client = MongoClient("mongodb://localhost:27017/")
    db = client["digikala"]
    collection = db["laptops"]

    new_count = 0
    for product in data['data']['products']:
        title = product['title_fa']
        brand = get_brand(title)
        price = product['default_variant']['price']['selling_price']
        link = 'https://www.digikala.com' + product['url']['uri']

        item = {
            "brand": brand,
            "title": title,
            "price": price,
            "link": link,
            "timestamp": datetime.datetime.now().isoformat()
        }

        item_hash = generate_hash(item)
        if not collection.find_one({"_id": item_hash}):
            item["_id"] = item_hash
            collection.insert_one(item)
            new_count += 1

    print(f"✅ {new_count} محصول جدید ذخیره شد. ({datetime.datetime.now().strftime('%H:%M:%S')})")

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(scrape_laptops, 'interval', minutes=5)
    print("🚀 اسکرپر در حال اجرا است. هر 5 دقیقه بروزرسانی می‌شود...")
    scrape_laptops()  # اولین اجرا بلافاصله
    scheduler.start()
