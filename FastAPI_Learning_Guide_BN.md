# FastAPI শেখার এবং Books Project তৈরির গাইড

স্বাগতম! এই গাইডে আমরা একদম শুরু থেকে FastAPI শিখবো এবং একটি "Books API" প্রজেক্ট তৈরি করবো।

## FastAPI কি এবং কেন শিখবেন?
**FastAPI** হলো Python দিয়ে API (Application Programming Interface) বানানোর জন্য একটি আধুনিক এবং অত্যন্ত দ্রুত ফ্রেমওয়ার্ক।

*   **দ্রুত (Fast):** এটি NodeJS এবং Go-এর মতোই দ্রুত।
*   **সহজ (Easy):** কোড লেখা খুব সহজ এবং কম সময়ে বেশি কাজ করা যায়।
*   **অটোমেটিক ডকুমেন্টেশন (Docs):** আপনি কোড লিখলেই এটি অটোমেটিক্যালি একটি সুন্দর ডকুমেন্টেশন পেজ বানিয়ে দেয় (Swagger UI)।
*   **টাইপ সেফটি (Type Safety):** Python Type Hints ব্যবহার করার কারণে ভুল হওয়ার সম্ভাবনা কমে যায়।

---

## ধাপ ১: পরিবেশ সেটআপ (Environment Setup)

কোনো কিছু শুরু করার আগে আমাদের কম্পিউটারে Python এবং প্রয়োজনীয় লাইব্রেরি ইন্সটল করতে হবে।

### ১.১ ফোল্ডার তৈরি এবং ওপেন করা
আপনি ইতিমধ্যেই `Books_Project` ফোল্ডারে আছেন। আমরা এখানেই সব কাজ করবো।

### ১.২ ভার্চুয়াল এনভায়রনমেন্ট (Virtual Environment) তৈরি
ভার্চুয়াল এনভায়রনমেন্ট হলো একটি আলাদা বক্সের মতো, যেখানে আমরা আমাদের প্রজেক্টের লাইব্রেরিগুলো রাখবো, যাতে অন্য প্রজেক্টের সাথে মিশে না যায়।

Terminal এ এই কমান্ডটি লিখুন:
```bash
python -m venv venv
```
এটি `venv` নামে একটি ফোল্ডার তৈরি করবে।

এখন এটি চালু (activate) করতে হবে:
*   **Windows:** `.\venv\Scripts\activate`

চালু হলে টার্মিনালের শুরুতে `(venv)` লেখা দেখবেন।

### ১.৩ প্রয়োজনীয় লাইব্রেরি ইন্সটল
আমাদের দুটি প্রধান লাইব্রেরি লাগবে:
1.  **fastapi:** মূল ফ্রেমওয়ার্ক।
2.  **uvicorn:** এটি হলো সার্ভার, যা আমাদের FastAPI কোড চালাবে।

একটি `requirements.txt` ফাইল তৈরি করুন এবং তাতে লিখুন:
```txt
fastapi
uvicorn
```

এরপর Terminal এ কমান্ড দিন:
```bash
pip install -r requirements.txt
```

---

## ধাপ ২: প্রথম কোড (Hello World)

এখন আমরা দেখবো আমাদের সেটআপ ঠিক আছে কিনা। `main.py` নামে একটি ফাইল তৈরি করুন এবং নিচের কোডটি লিখুন:

```python
from fastapi import FastAPI

# ১. অ্যাপ তৈরি করা
app = FastAPI()

# ২. পাথ অপারেশন (Path Operation) বা রুট (Route) তৈরি
# @app.get("/") মানে হলো, কেউ যদি আপনার ওয়েবসাইটের হোম পেজে (/) যায়,
# তাহলে নিচের ফাংশনটি কাজ করবে।
@app.get("/")
def read_root():
    return {"message": "স্বাগতম আমার FastAPI প্রজেক্টে!"}
```

### কোডটি চালানোর নিয়ম
Terminal এ লিখুন:
```bash
uvicorn main:app --reload
```
*   `main`: ফাইল এর নাম (`main.py`)
*   `app`: ফাইলের ভেতরের `FastAPI` ভেরিয়েবলটির নাম।
*   `--reload`: কোড চেঞ্জ করলে সার্ভার অটোমেটিক রিস্টার্ট হবে (ডেভেলপমেন্টের জন্য খুব সুবিধাজনক)।

এখন ব্রাউজারে গিয়ে `http://127.0.0.1:8000` লিংকে যান। আপনি ব্রাউজারে `{"message": "স্বাগতম আমার FastAPI প্রজেক্টে!"}` দেখতে পাবেন।

সবচেয়ে মজার বিষয় হলো অটোমেটিক ডকুমেন্টেশন। ব্রাউজারে `http://127.0.0.1:8000/docs` লিংকে যান। দেখবেন আপনার API এর জন্য একটি সুন্দর পেজ তৈরি হয়ে গেছে!

---

## ধাপ ৩: FastAPI এর লজিক এবং সিনট্যাক্স বোঝা

### ৩.১ Type Hints (টাইপ হিন্টস)
Python এ ভেরিয়েবলের টাইপ বলে দেওয়াটা FastAPI তে খুব গুরুত্বপূর্ণ। এটি Pydantic লাইব্রেরি ব্যবহার করে ডেটা ভ্যালিডেশন করে।

উদাহরণ:
```python
def get_full_name(first_name: str, last_name: str):
    return first_name + " " + last_name
```
এখানে `: str` বলে দিচ্ছে যে `first_name` অবশ্যই একটি স্ট্রিং (text) হতে হবে।

### ৩.২ Path Parameters (পাথ প্যারামিটার)
ধরুন আমরা একটি নির্দিষ্ট বইয়ের তথ্য চাই। তখন আমরা URL এর মাধ্যমে বইয়ের ID পাঠাতে পারি।

`main.py` তে এই কোডটি যোগ করুন:

```python
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
```
এখন যদি ব্রাউজারে `http://127.0.0.1:8000/items/5` এ যান, আপনি `{"item_id": 5}` পাবেন।
লক্ষণীয়: `item_id: int` দেওয়ার কারণে, কেউ যদি `http://127.0.0.1:8000/items/foo` দেয়, FastAPI অটোমেটিক এরর দেখাবে কারণ `foo` কোনো সংখ্যা (int) নয়।

---

## ধাপ ৪: Books Project শুরু করা

এখন আমরা আমাদের আসল প্রজেক্ট "Books API" এর কাঠামো তৈরি করবো।

আমাদের বইয়ের তথ্যের জন্য একটি মডেল লাগবে। এর জন্য আমরা **Pydantic Model** ব্যবহার করবো। এটি নিশ্চিত করে যে আমরা সঠিক ডেটা পাচ্ছি।

`main.py` আপডেট করুন:

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Pydantic Model - ডেটার কাঠামো বা স্কিমা
class Book(BaseModel):
    id: int
    title: str
    author: str
    category: str
    price: float

# মেমোরিতে কিছু ডামি বই রাখা (প্র্যাকটিসের জন্য, পরে আমরা ডাটাবেস ব্যবহার করবো)
books_db = [
    Book(id=1, title="Himu", author="Humayun Ahmed", category="Fiction", price=250.0),
    Book(id=2, title="Pather Panchali", author="Bibhutibhushan Bandyopadhyay", category="Novel", price=300.50),
]

# ১. সব বই দেখা (GET)
@app.get("/books", response_model=List[Book])
def get_all_books():
    return books_db

# ২. নতুন বই যোগ করা (POST)
@app.post("/books", response_model=Book)
def create_book(book: Book):
    books_db.append(book)
    return book

# ৩. নির্দিষ্ট বই খোঁজা (GET by ID)
@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in books_db:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="বইটি পাওয়া যায়নি")
```

### এটি কিভাবে টেস্ট করবেন?
1. `main.py` সেভ করুন।
2. সার্ভার চালু থাকা অবস্থায় `http://127.0.0.1:8000/docs` এ যান।
3. **POST /books**: Try it out এ ক্লিক করে একটি নতুন বইয়ের JSON দিন এবং execute করুন।
4. **GET /books**: execute করে দেখুন নতুন বইটি তালিকায় এসেছে কিনা।

---

## পরবর্তী ধাপ (Future Learning)
আপনি এখন বেসিক CRUD (Create, Read) অপারেশন শিখেছেন। পরবর্তীতে আমরা শিখবো:
*   কিভাবে ডাটা এডিট (PUT) এবং ডিলিট (DELETE) করতে হয়।
*   কিভাবে আসল ডাটাবেস (SQLAlchemy বা Tortoise ORM) ব্যবহার করতে হয়।

শুভ কোডিং! কোনো প্রশ্ন থাকলে আমাকে জানাতে পারেন।
