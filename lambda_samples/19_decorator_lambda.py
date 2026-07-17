# استفاده از لامبدا در decorator
# لامبدا در decorator
# تابعی تعریف می‌کنیم که تعداد تکرار را می‌گیرد
def repeat(n):
    # یک لامبدا برمی‌گرداند که تابع اصلی را می‌گیرد و یک تابع جدید با تکرار می‌سازد
    return lambda func: lambda *args, **kwargs: [func(*args, **kwargs) for _ in range(n)]

# دکوریتور repeat را با تعداد ۳ روی تابع say_hello اعمال می‌کنیم
@repeat(3)
# یک تابع ساده برای سلام تعریف می‌کنیم
def say_hello(name):
    # یک پیام خوشامدگویی برمی‌گردانیم
    return f"Hello {name}"

# تابع say_hello را با نام Ali صدا می‌زنیم و نتیجه را چاپ می‌کنیم
print(say_hello("Ali"))
# ['Hello Ali', 'Hello Ali', 'Hello Ali']
