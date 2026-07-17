# استفاده از لامبدا به عنوان مقدار بازگشتی از یک تابع
# لامبدا به عنوان تابع بازگشتی (return function)
# تابعی تعریف می‌کنیم که یک ضریب می‌گیرد و یک تابع لامبدا برمی‌گرداند
def make_multiplier(n):
    # یک لامبدا برمی‌گردانیم که ورودی را در n ضرب می‌کند
    return lambda x: x * n

# تابعی برای دو برابر کردن اعداد می‌سازیم
double = make_multiplier(2)
# تابعی برای سه برابر کردن اعداد می‌سازیم
triple = make_multiplier(3)

# تابع double را با مقدار ۱۰ صدا می‌زنیم و نتیجه را چاپ می‌کنیم
print(double(10))  # 20
# تابع triple را با مقدار ۱۰ صدا می‌زنیم و نتیجه را چاپ می‌کنیم
print(triple(10))  # 30

# مثال: سازنده لاگر با prefix مختلف
# تابعی تعریف می‌کنیم که یک پیشوند می‌گیرد و یک لاگر برمی‌گرداند
def make_logger(prefix):
    # یک لامبدا برمی‌گردانیم که پیام را با پیشوند قالب‌بندی می‌کند
    return lambda msg: f"[{prefix}] {msg}"

# یک لاگر با پیشوند INFO می‌سازیم
info = make_logger("INFO")
# یک لاگر با پیشوند ERROR می‌سازیم
error = make_logger("ERROR")
# لاگر info را با پیام مشخص صدا می‌زنیم و چاپ می‌کنیم
print(info("Server started"))   # [INFO] Server started
# لاگر error را با پیام مشخص صدا می‌زنیم و چاپ می‌کنیم
print(error("Disk full"))       # [ERROR] Disk full
