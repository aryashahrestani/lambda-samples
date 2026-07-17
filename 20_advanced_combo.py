# ترکیب پیشرفته: sort + filter + map + reduce روی داده واقعی
# تابع reduce را از کتابخانه functools وارد می‌کنیم
from functools import reduce

# یک لیست از سفارش‌های فروشگاهی با آیتم‌ها و کاربران تعریف می‌کنیم
orders = [
    {"id": 1, "items": [{"price": 10}, {"price": 20}], "user": "ali"},
    {"id": 2, "items": [{"price": 100}], "user": "sara"},
    {"id": 3, "items": [{"price": 5}, {"price": 5}, {"price": 5}], "user": "reza"},
    {"id": 4, "items": [], "user": "mina"},
]

# سفارش‌های غیرخالی با مجموع قیمت > 15، مرتب شده نزولی
# داده‌ها را مرتب می‌کنیم: فیلتر سفارش‌های غیرخالی و مرتب‌سازی نزولی بر اساس مجموع قیمت
result = sorted(
    # سفارش‌هایی که آیتم دارند را فیلتر می‌کنیم
    filter(lambda o: len(o["items"]) > 0, orders),                         # فیلتر خالی
    # مجموع قیمت آیتم‌های هر سفارش را با reduce محاسبه می‌کنیم
    key=lambda o: reduce(lambda s, i: s + i["price"], o["items"], 0),     # کلید = مجموع قیمت
    # مرتب‌سازی به صورت نزولی
    reverse=True
)

# روی نتیجه مرتب‌شده حلقه می‌زنیم
for order in result:
    # مجموع قیمت آیتم‌های هر سفارش را با reduce محاسبه می‌کنیم
    total = reduce(lambda s, i: s + i["price"], order["items"], 0)
    # نام کاربر و مجموع سفارش را چاپ می‌کنیم
    print(f"User {order['user']}: total=${total}")
# sara: $100
# ali: $30
# reza: $15
