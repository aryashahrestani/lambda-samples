# مرتب‌سازی نزولی با reverse
# لیستی از اعداد تعریف می‌کنیم
numbers = [4, 2, 9, 1, 5]
# اعداد را به صورت نزولی مرتب می‌کنیم
desc = sorted(numbers, key=lambda x: x, reverse=True)
# نتیجه را چاپ می‌کنیم
print(desc)  # [9, 5, 4, 2, 1]

# مرتب‌سازی بر اساس طول رشته
# لیستی از رشته‌ها تعریف می‌کنیم
words = ["hi", "python", "java", "c"]
# رشته‌ها را بر اساس طولشان مرتب می‌کنیم
by_len = sorted(words, key=lambda w: len(w))
# نتیجه را چاپ می‌کنیم
print(by_len)  # ['c', 'hi', 'java', 'python']
