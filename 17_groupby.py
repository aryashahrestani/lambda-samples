# استفاده از groupby با لامبدا برای گروه‌بندی داده‌ها
# groupby: گروه‌بندی با لامبدا
# تابع groupby را از کتابخانه itertools وارد می‌کنیم
from itertools import groupby

# یک لیست از تاپل‌های حاوی درس و نمره تعریف می‌کنیم
data = [("math", 18), ("physics", 15), ("math", 20), ("art", 17), ("physics", 19)]

# مرتب‌سازی اول لازم است (groupby روی داده مرتب کار می‌کند)
# داده‌ها را بر اساس نام درس با لامبدا مرتب می‌کنیم
sorted_data = sorted(data, key=lambda x: x[0])

# روی داده‌های مرتب‌شده گروه‌بندی انجام می‌دهیم
for subject, group in groupby(sorted_data, key=lambda x: x[0]):
    # نمرات هر گروه را استخراج می‌کنیم
    scores = [item[1] for item in group]
    # نام درس و نمرات آن را چاپ می‌کنیم
    print(f"{subject}: {scores}")
# art: [17]
# math: [18, 20]
# physics: [15, 19]
