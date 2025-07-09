
# 🛍️ Digikala Laptop Scraper + API

این پروژه شامل یک اسکریپر (Web Scraper) برای دریافت قیمت و مشخصات لپ‌تاپ‌های سایت دیجی‌کالا است که اطلاعات را هر ۵ دقیقه به صورت خودکار در MongoDB ذخیره می‌کند و از طریق FastAPI در قالب API قابل دسترسی می‌باشد.

---

## 🧰 ابزارها و تکنولوژی‌ها

- Python
- MongoDB
- FastAPI
- APScheduler
- requests
- pymongo

---

## 🔁 امکانات پروژه

- دریافت اطلاعات لحظه‌ای از سایت دیجی‌کالا (عنوان، قیمت، لینک، برند)
- جلوگیری از ذخیره اطلاعات تکراری با استفاده از هش (hash)
- اجرای خودکار هر ۵ دقیقه با استفاده از APScheduler
- ساخت API با قابلیت فیلتر بر اساس برند برای استفاده در سایت یا اپلیکیشن

---

## 🚀 نحوه اجرا

### 1. نصب کتابخانه‌ها

```bash
pip install -r requirements.txt
```

### 2. اجرای اسکریپر (زمان‌بندی شده):

```bash
python digikala_scraper_apscheduler.py
```

### 3. اجرای API با FastAPI:

```bash
uvicorn digikala_api:app --reload
```

---

## 🌐 دسترسی به API

- نمایش تمام لپ‌تاپ‌ها:
  ```
  http://localhost:8000/laptops
  ```

- فیلتر بر اساس برند خاص (مثلاً Asus):
  ```
  http://localhost:8000/laptops?brand=Asus
  ```

---

## 📁 ساختار پروژه

| فایل | توضیح |
|------|-------|
| `digikala_scraper_apscheduler.py` | اسکریپر با زمان‌بندی |
| `digikala_api.py` | فایل API با FastAPI |
| `requirements.txt` | لیست پکیج‌های موردنیاز |
| `README.md` | مستندات پروژه (همین فایل) |

---

