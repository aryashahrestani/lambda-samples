# استفاده از توابع any و all با لامبدا
# any و all با لامبدا
# یک لیست از اعداد تعریف می‌کنیم
nums = [1, 2, 3, 4, 5]

# بررسی می‌کنیم آیا حداقل یک عدد زوج در لیست وجود دارد
has_even = any(map(lambda x: x % 2 == 0, nums))
# بررسی می‌کنیم آیا همه اعداد مثبت هستند
all_positive = all(map(lambda x: x > 0, nums))

# نتیجه بررسی وجود عدد زوج را چاپ می‌کنیم
print(has_even)       # True (حداقل یک زوج)
# نتیجه بررسی مثبت بودن همه اعداد را چاپ می‌کنیم
print(all_positive)   # True (همه مثبت)

# بررسی وضعیت کاربران
# یک لیست از دیکشنری‌های وضعیت کاربران تعریف می‌کنیم
users = [{"active": True}, {"active": False}, {"active": True}]
# بررسی می‌کنیم آیا همه کاربران فعال هستند
all_active = all(map(lambda u: u["active"], users))
# بررسی می‌کنیم آیا حداقل یک کاربر فعال وجود دارد
any_active = any(map(lambda u: u["active"], users))
# نتیجه بررسی فعال بودن همه کاربران را چاپ می‌کنیم
print(all_active)  # False
# نتیجه بررسی وجود حداقل یک کاربر فعال را چاپ می‌کنیم
print(any_active)  # True
