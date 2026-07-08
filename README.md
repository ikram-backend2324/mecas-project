# NUBEL — Belarus qabul tizimi

Nukus davlat texnika universiteti uchun mustaqil qabul portali (HEMIS'dan
alohida). Abituriyentlar onlayn ariza topshiradi, tizim har biriga
takrorlanmaydigan **kod** va **QR-chek** beradi. Adminlar talabani kod orqali
qidiradi. Butun talaba interfeysi **o'zbek tilida**.

2+2 dastur: dastlabki 2 yil Qoraqalpog'istonda, keyingi 2 yil Belarusda.

## Texnologiyalar
Django 5 · PostgreSQL (`dj_database_url`) · Jazzmin admin · WhiteNoise ·
Gunicorn · qrcode/Pillow

## Lokal ishga tushirish
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createadmin          # admin / admin123 + boshlang'ich ma'lumot
python manage.py runserver
```
`DATABASE_URL` berilmasa avtomatik sqlite ishlatiladi (lokal test uchun).
Prod'da PostgreSQL — kod o'zgarmaydi.

## Render — build & start
**Build command:**
```
pip install -r requirements.txt && python manage.py migrate && python manage.py createadmin && python manage.py collectstatic --noinput
```
**Start command:**
```
gunicorn nubel_project.wsgi:application
```

## Muhit o'zgaruvchilari (Render)
| Kalit | Izoh |
|---|---|
| `DATABASE_URL` | PostgreSQL ulanish (Render avtomatik beradi) |
| `SECRET_KEY` | Maxfiy kalit |
| `DEBUG` | Prod'da `False` |
| `ALLOWED_HOSTS` | masalan `mysite.onrender.com` |
| `CSRF_TRUSTED_ORIGINS` | `https://mysite.onrender.com` |

## Standart admin
`admin / admin123` — `createadmin` buyrug'i yaratadi (mavjud bo'lsa o'tkazadi).
**Prod'da parolni o'zgartiring.**

## Foydalanuvchilar
- **Talaba**: username + parol + telefon bilan ro'yxatdan o'tadi, kiradi,
  profilini tahrirlaydi (rasm yuklaydi), ariza topshiradi, chek oladi.
- **Admin**: Jazzmin panel, kod bo'yicha qidiruv, holatni o'zgartirish.

Sessiya asosidagi autentifikatsiya (token yo'q), ruxsatlar `@login_required`
va `is_staff` orqali.

## Telefon tasdiqlash (hozircha o'chirilgan)
Ro'yxatdan o'tish SMS'siz ishlaydi. Keyinchalik yoqish uchun:
`accounts/sms.py` tayyor — `SMS_BACKEND=console|eskiz` va
`PHONE_VERIFICATION_REQUIRED=True` o'rnatilsa OTP oqimi ishga tushadi.
Kod o'zgartirishsiz.

## URL'lar
| URL | Sahifa |
|---|---|
| `/` | Bosh sahifa |
| `/royxatdan-otish/` | Ro'yxatdan o'tish |
| `/kirish/` · `/chiqish/` | Kirish · Chiqish |
| `/profil/` · `/profil/tahrirlash/` | Profil · tahrirlash |
| `/ariza/topshirish/` | Ariza yaratish |
| `/chek/<kod>/` | QR-chek (chop etish) |
| `/tekshirish/<kod>/` | Ommaviy tekshiruv (QR shu yerga yo'naltiradi) |
| `/admin/` | Jazzmin admin |

## Til (UZ / RU)
Interfeys ikki tilda: **O'zbekcha** va **Русский**. Yuqori o'ng burchakdagi
**UZ / RU** tugmasi orqali almashtiriladi. Tanlangan til sessiyada saqlanadi.
Tarjimalar `nubel_project/translations.py` faylida — gettext/`.mo` ishlatilmaydi,
shuning uchun build vaqtida hech narsa kompilyatsiya qilinmaydi
(`compilemessages` kerak emas).

## Python versiyasi
`.python-version` fayli **3.12.9** ni belgilaydi. Bu muhim: Render standart
holda Python 3.14 ishlatsa, Django/Jazzmin admin panelida
`'super' object has no attribute 'dicts'` xatosi chiqadi. 3.12 buni hal qiladi.
