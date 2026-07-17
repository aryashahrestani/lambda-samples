# استفاده از توابع min و max با پارامتر key و لامبدا
# min و max با key لامبدا
# یک لیست از دیکشنری‌های حاوی اطلاعات افراد تعریف می‌کنیم
people = [{"name": "Ali", "age": 25}, {"name": "Sara", "age": 30}, {"name": "Reza", "age": 20}]

# کوچکترین فرد را بر اساس سن با استفاده از لامبدا پیدا می‌کنیم
youngest = min(people, key=lambda p: p["age"])
# بزرگترین فرد را بر اساس سن با استفاده از لامبدا پیدا می‌کنیم
oldest = max(people, key=lambda p: p["age"])

# نتیجه کوچکترین سن را چاپ می‌کنیم
print(youngest)  # {'name': 'Reza', 'age': 20}
# نتیجه بزرگترین سن را چاپ می‌کنیم
print(oldest)    # {'name': 'Sara', 'age': 30}

# کوچکترین و بزرگترین بر اساس طول نام
# کوچکترین فرد را بر اساس طول نام با لامبدا پیدا می‌کنیم
shortest = min(people, key=lambda p: len(p["name"]))
# نتیجه کوتاه‌ترین نام را چاپ می‌کنیم
print(shortest)  # {'name': 'Ali', 'age': 25}
