"""Lightweight two-language (uz/ru) translation layer.

No gettext / .mo files are used — so there is nothing to compile at build
time. The active language is stored in the session ("lang") and looked up
here by short, stable keys.
"""

DEFAULT_LANG = "uz"
LANGS = ("uz", "ru")

TRANSLATIONS = {
    # ---- top bar / header / nav ----
    "topbar.phone": {"uz": "Ishonch telefoni", "ru": "Телефон доверия"},
    "topbar.tagline": {
        "uz": "Nukus davlat texnika universiteti · Belarus qo'shma dasturi",
        "ru": "Нукусский государственный технический университет · Совместная программа с Беларусью",
    },
    "brand.title": {"uz": "NUBEL Qabul tizimi", "ru": "Система приёма NUBEL"},
    "brand.subtitle": {
        "uz": "Belarus universitetlariga hujjat topshirish portali",
        "ru": "Портал подачи документов в университеты Беларуси",
    },
    "nav.home": {"uz": "Bosh sahifa", "ru": "Главная"},
    "nav.apply": {"uz": "Ariza topshirish", "ru": "Подать заявку"},
    "nav.profile": {"uz": "Mening profilim", "ru": "Мой профиль"},
    "nav.admin": {"uz": "Admin panel", "ru": "Админ-панель"},
    "nav.logout": {"uz": "Chiqish", "ru": "Выход"},
    "nav.login": {"uz": "Kirish", "ru": "Вход"},
    "nav.register": {"uz": "Ro'yxatdan o'tish", "ru": "Регистрация"},
    "footer.univ": {
        "uz": "Nukus davlat texnika universiteti",
        "ru": "Нукусский государственный технический университет",
    },
    "footer.tag": {
        "uz": "NUBEL — Belarus qo'shma ta'lim dasturi",
        "ru": "NUBEL — совместная образовательная программа с Беларусью",
    },

    # ---- home ----
    "home.badge": {"uz": "2+2 qo'shma ta'lim dasturi",
                   "ru": "Совместная образовательная программа 2+2"},
    "home.hero_title": {
        "uz": "Belarus universitetlariga hujjat topshirish portali",
        "ru": "Портал подачи документов в университеты Беларуси",
    },
    "home.hero_text": {
        "uz": "Dastlabki 2 yil Qoraqalpog'istonda, keyingi 2 yil Belarusda "
              "o'qing. Arizangizni onlayn topshiring, noyob kod va QR-chek oling.",
        "ru": "Первые 2 года обучение в Каракалпакстане, следующие 2 года — в "
              "Беларуси. Подайте заявку онлайн и получите уникальный код и QR-квитанцию.",
    },
    "home.features_title": {"uz": "Dastur imkoniyatlari",
                            "ru": "Возможности программы"},
    "home.features_sub": {
        "uz": "Mustaqil qabul tizimi orqali barcha jarayonni onlayn boshqaring",
        "ru": "Управляйте всем процессом онлайн через независимую систему приёма",
    },
    "home.f1_t": {"uz": "Onlayn ariza", "ru": "Онлайн-заявка"},
    "home.f1_d": {
        "uz": "Shaxsiy ma'lumotlar va hujjatlarni bir marta yuklab, arizani topshiring.",
        "ru": "Загрузите личные данные и документы один раз и подайте заявку.",
    },
    "home.f2_t": {"uz": "Noyob kod", "ru": "Уникальный код"},
    "home.f2_d": {
        "uz": "Har bir abituriyentga takrorlanmaydigan ariza kodi beriladi.",
        "ru": "Каждому абитуриенту присваивается неповторимый код заявки.",
    },
    "home.f3_t": {"uz": "QR-chek", "ru": "QR-квитанция"},
    "home.f3_d": {
        "uz": "Chekni chop etib, universitetga oflayn ko'rsatishingiz mumkin.",
        "ru": "Распечатайте квитанцию и предъявите её в университете офлайн.",
    },
    "home.f4_t": {"uz": "Tez qidiruv", "ru": "Быстрый поиск"},
    "home.f4_d": {
        "uz": "Adminlar sizni kod orqali bir zumda topadi.",
        "ru": "Администраторы найдут вас по коду за секунды.",
    },
    "home.how_title": {"uz": "Qanday ishlaydi?", "ru": "Как это работает?"},
    "home.how_sub": {"uz": "To'rt oddiy qadam", "ru": "Четыре простых шага"},
    "home.s1_t": {"uz": "Ro'yxatdan o'ting", "ru": "Зарегистрируйтесь"},
    "home.s1_d": {
        "uz": "Foydalanuvchi nomi, parol va telefon raqamingiz bilan hisob yarating.",
        "ru": "Создайте аккаунт с именем пользователя, паролем и номером телефона.",
    },
    "home.s2_t": {"uz": "Arizani to'ldiring", "ru": "Заполните заявку"},
    "home.s2_d": {
        "uz": "Shaxsiy ma'lumotlar va kerakli hujjatlarni yuklang.",
        "ru": "Загрузите личные данные и необходимые документы.",
    },
    "home.s3_t": {"uz": "Kod va chek oling", "ru": "Получите код и квитанцию"},
    "home.s3_d": {
        "uz": "Tizim sizga noyob kod va QR-chek beradi.",
        "ru": "Система выдаст вам уникальный код и QR-квитанцию.",
    },
    "home.s4_t": {"uz": "Universitetga keling", "ru": "Придите в университет"},
    "home.s4_d": {
        "uz": "Chekni chop etib, oflayn tekshiruvdan o'ting.",
        "ru": "Распечатайте квитанцию и пройдите офлайн-проверку.",
    },

    # ---- auth ----
    "reg.title": {"uz": "Ro'yxatdan o'tish", "ru": "Регистрация"},
    "reg.sub": {"uz": "Hisob yarating va arizangizni topshiring.",
                "ru": "Создайте аккаунт и подайте заявку."},
    "reg.submit": {"uz": "Ro'yxatdan o'tish", "ru": "Зарегистрироваться"},
    "reg.have": {"uz": "Hisobingiz bormi?", "ru": "Уже есть аккаунт?"},
    "login.title": {"uz": "Tizimga kirish", "ru": "Вход в систему"},
    "login.sub": {"uz": "Foydalanuvchi nomi va parolingizni kiriting.",
                  "ru": "Введите имя пользователя и пароль."},
    "login.submit": {"uz": "Kirish", "ru": "Войти"},
    "login.no": {"uz": "Hisobingiz yo'qmi?", "ru": "Нет аккаунта?"},

    # ---- profile ----
    "prof.edit": {"uz": "Profilni tahrirlash", "ru": "Редактировать профиль"},
    "prof.myapp": {"uz": "Mening arizam", "ru": "Моя заявка"},
    "prof.viewcheck": {"uz": "Chekni ko'rish", "ru": "Посмотреть квитанцию"},
    "prof.noapp": {"uz": "Siz hali ariza topshirmagansiz.",
                   "ru": "Вы ещё не подали заявку."},
    "prof.save": {"uz": "Saqlash", "ru": "Сохранить"},
    "prof.cancel": {"uz": "Bekor qilish", "ru": "Отмена"},
    "prof.photo": {"uz": "Profil rasmi", "ru": "Фото профиля"},

    # ---- shared field labels ----
    "f.first": {"uz": "Ism", "ru": "Имя"},
    "f.last": {"uz": "Familiya", "ru": "Фамилия"},
    "f.middle": {"uz": "Otasining ismi", "ru": "Отчество"},
    "f.email": {"uz": "Email", "ru": "Email"},
    "f.phone": {"uz": "Telefon raqami", "ru": "Номер телефона"},
    "f.phone_short": {"uz": "Telefon", "ru": "Телефон"},
    "f.dob": {"uz": "Tug'ilgan sana", "ru": "Дата рождения"},
    "f.passport_no": {"uz": "Passport raqami", "ru": "Номер паспорта"},
    "f.programme": {"uz": "Yo'nalish", "ru": "Направление"},
    "f.faculty": {"uz": "Fakultet", "ru": "Факультет"},
    "f.status": {"uz": "Holati", "ru": "Статус"},
    "f.code": {"uz": "Ariza kodi", "ru": "Код заявки"},
    "f.date": {"uz": "Topshirilgan sana", "ru": "Дата подачи"},
    "f.fio": {"uz": "F.I.Sh.", "ru": "Ф.И.О."},

    # ---- application create ----
    "cr.title": {"uz": "Ariza yaratish", "ru": "Создание заявки"},
    "cr.programme": {"uz": "Yo'nalish (dastur)", "ru": "Направление (программа)"},
    "cr.docs": {"uz": "Hujjatlar", "ru": "Документы"},
    "cr.passport": {"uz": "Passport", "ru": "Паспорт"},
    "cr.transcript": {"uz": "Diplom ilovasi", "ru": "Приложение к диплому"},
    "cr.transcript_note": {"uz": "(magistratura uchun)",
                           "ru": "(для магистратуры)"},
    "cr.cert": {"uz": "Attestat yoki diplom nusxasi",
                "ru": "Копия аттестата или диплома"},
    "cr.photo": {"uz": "Foto (3x4)", "ru": "Фото (3x4)"},
    "cr.extra": {"uz": "Sertifikat", "ru": "Сертификат"},
    "cr.extra_note": {"uz": "(mavjud bo'lsa)", "ru": "(при наличии)"},
    "cr.save": {"uz": "Saqlash", "ru": "Сохранить"},
    "select.placeholder": {"uz": "--Tanlang--", "ru": "--Выберите--"},

    # ---- receipt ----
    "rc.title": {"uz": "NUBEL — Ariza cheki", "ru": "NUBEL — Квитанция заявки"},
    "rc.note": {
        "uz": "Ushbu chekni chop eting va universitetga kelganingizda "
              "ko'rsating. Adminlar sizni {code} kodi orqali topadi.",
        "ru": "Распечатайте эту квитанцию и предъявите её в университете. "
              "Администраторы найдут вас по коду {code}.",
    },
    "rc.print": {"uz": "Chop etish", "ru": "Печать"},
    "rc.back": {"uz": "Profilga qaytish", "ru": "Вернуться в профиль"},

    # ---- verify ----
    "vf.title": {"uz": "Ariza tekshiruvi", "ru": "Проверка заявки"},
    "vf.valid": {
        "uz": "Ushbu ariza tizimda ro'yxatdan o'tgan va haqiqiy.",
        "ru": "Эта заявка зарегистрирована в системе и является действительной.",
    },

    # ---- flash messages ----
    "msg.registered": {
        "uz": "Ro'yxatdan muvaffaqiyatli o'tdingiz. Xush kelibsiz!",
        "ru": "Вы успешно зарегистрировались. Добро пожаловать!",
    },
    "msg.logged_in": {"uz": "Tizimga muvaffaqiyatli kirdingiz.",
                      "ru": "Вы успешно вошли в систему."},
    "msg.logged_out": {"uz": "Tizimdan chiqdingiz.",
                       "ru": "Вы вышли из системы."},
    "msg.profile_updated": {"uz": "Profil ma'lumotlari yangilandi.",
                            "ru": "Данные профиля обновлены."},
    "msg.have_app": {"uz": "Sizda allaqachon ariza mavjud.",
                     "ru": "У вас уже есть заявка."},
    "msg.app_created": {
        "uz": "Arizangiz qabul qilindi! Kodingizni saqlab qo'ying.",
        "ru": "Ваша заявка принята! Сохраните ваш код.",
    },
}

STATUS_LABELS = {
    "kutilmoqda": {"uz": "Kutilmoqda", "ru": "На рассмотрении"},
    "qabul_qilindi": {"uz": "Qabul qilindi", "ru": "Принято"},
    "rad_etildi": {"uz": "Rad etildi", "ru": "Отклонено"},
}


def normalize(lang):
    return "ru" if (lang or "").startswith("ru") else "uz"


def tr(key, lang=DEFAULT_LANG, **fmt):
    lang = normalize(lang)
    entry = TRANSLATIONS.get(key)
    if not entry:
        return key
    text = entry.get(lang) or entry.get(DEFAULT_LANG) or key
    return text.format(**fmt) if fmt else text


def status_label(value, lang=DEFAULT_LANG):
    lang = normalize(lang)
    entry = STATUS_LABELS.get(value)
    return entry.get(lang, value) if entry else value
