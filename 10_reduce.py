# reduce: کاهش لیست به یک مقدار
# تابع reduce را از ماژول functools وارد می‌کنیم
from functools import reduce

# لیستی از اعداد تعریف می‌کنیم
nums = [1, 2, 3, 4]
# با استفاده از reduce و لامبدا، حاصلضرب تمام اعداد را محاسبه می‌کنیم
product = reduce(lambda a, b: a * b, nums)
# نتیجه را چاپ می‌کنیم
print(product)  # 24 (1*2*3*4)

# پیدا کردن بزرگترین عدد
# با استفاده از reduce، بزرگترین عدد لیست را پیدا می‌کنیم
maximum = reduce(lambda a, b: a if a > b else b, nums)
# نتیجه را چاپ می‌کنیم
print(maximum)  # 4
