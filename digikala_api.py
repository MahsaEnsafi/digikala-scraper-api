from fastapi import FastAPI
from pymongo import MongoClient
from fastapi.responses import JSONResponse
from typing import Optional

app = FastAPI()

# اتصال به MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["digikala"]
collection = db["laptops"]

@app.get("/laptops")
def get_laptops(brand: Optional[str] = None):
    query = {}
    if brand:
        query["brand"] = brand
    data = list(collection.find(query, {"_id": 0}))  # حذف فیلد _id از خروجی
    return JSONResponse(content=data)

@app.get("/")
def root():
    return {"message": "API دیجی‌کالا فعال است. از /laptops استفاده کنید."}
