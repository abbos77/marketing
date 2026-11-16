# Запуск из корня репозитория: python3 tools/make-uz.py
# Генерирует uz/index.html из index.html: перевод + пути + мета.
import re, sys
src = open('index.html', encoding='utf-8').read()
s = src
BASE = 'https://abbos77.github.io/marketing/'

def R(a, b, count=None):
    global s
    n = s.count(a)
    if n == 0:
        print('MISSING:', a[:90]); sys.exit(1)
    if count is not None and n != count:
        print(f'COUNT {n}!={count}:', a[:90]); sys.exit(1)
    s = s.replace(a, b)

# ---------- head ----------
R('<html lang="ru">', '<html lang="uz">')
R('<title>Забанили? Разблокировка и аудит рекламы Meta Ads — Аббос</title>',
  '<title>Akkaunt blokdami? Instagram va Facebook reklama akkauntini blokdan chiqarish — Abbos</title>')
R('content="Разберусь, за что заблокировали рекламный кабинет, страницу или профиль, и помогу вернуть рекламу в работу. Бесплатная диагностика и бесплатный аудит рекламы."',
  'content="Instagram yoki Facebookdagi reklama akkaunti, sahifa yoki profilingiz bloklandimi? Sababini topib, blokdan chiqarishga yordam beraman. Tekshiruv va reklama auditi bepul, toʻlov natijadan keyin."')
R(f'<link rel="canonical" href="{BASE}">', f'<link rel="canonical" href="{BASE}uz/">')
R('<meta property="og:locale" content="ru_RU">\n<meta property="og:locale:alternate" content="uz_UZ">', '<meta property="og:locale" content="uz_UZ">\n<meta property="og:locale:alternate" content="ru_RU">')
R(f'<meta property="og:url" content="{BASE}">', f'<meta property="og:url" content="{BASE}uz/">')
R('Забанили? Разберусь, за что, и помогу вернуть рекламу в работу', 'Akkaunt blokdami? Sababini topib, blokdan chiqarishga yordam beraman', 2)
R('content="Разблокировка рекламных кабинетов, страниц и профилей, бесплатная диагностика и аудит рекламы Meta Ads. Без паролей, цена до старта."',
  'content="Instagram va Facebookda bloklangan reklama akkaunti, sahifa va profillarni tiklashga yordam. Tekshiruv va audit bepul, parol soʻralmaydi, toʻlov natijadan keyin."')
R('content="Разблокировка, бесплатная диагностика и аудит рекламы Meta Ads. Без паролей, цена до старта."',
  'content="Bloklangan akkauntni tiklashga yordam, bepul tekshiruv va reklama auditi. Parol soʻralmaydi, toʻlov natijadan keyin."')
R('assets/img/og-ru.jpg', 'assets/img/og-uz.jpg')
R('content="Аббос — Meta Ads: разблокировка и бесплатный аудит рекламы"', 'content="Abbos — Meta Ads: blokdan chiqarish va reklamaning bepul auditi"')
R('"url": "' + BASE + '",', '"url": "' + BASE + 'uz/",')
R('"description": "Разблокировка рекламных кабинетов, страниц и профилей, бесплатная диагностика и аудит рекламы Meta Ads, арбитраж трафика (white-hat).",',
  '"description": "Instagram va Facebookda bloklangan reklama akkaunti, sahifa va profillarni tiklashga yordam, bepul tekshiruv va reklama auditi, trafik arbitraji (white-hat).",')
R('"addressLocality": "Ташкент"', '"addressLocality": "Toshkent"')

HREF = f'''<link rel="alternate" hreflang="ru" href="{BASE}">
<link rel="alternate" hreflang="uz" href="{BASE}uz/">
<link rel="alternate" hreflang="x-default" href="{BASE}">'''


# ---------- header ----------
R('aria-label="Abbos — на главную"', 'aria-label="Abbos — bosh sahifaga"')
R('<nav class="nav" aria-label="Разделы">', '<nav class="nav" aria-label="Boʻlimlar">')
R('<a href="#services">Услуги</a>', '<a href="#services">Xizmatlar</a>')
R('<a href="#arbitrage">Арбитраж</a>', '<a href="#arbitrage">Arbitraj</a>')
R('<a href="#price">Цены</a>', '<a href="#price">Narxlar</a>')
R('<a href="#contact">Контакты</a>', '<a href="#contact">Aloqa</a>')
R('''<div class="lang" aria-label="Язык">
        <a href="./" hreflang="ru" aria-current="page">RU</a>
        <a href="uz/" hreflang="uz" lang="uz">UZ</a>''', '''<div class="lang" aria-label="Til">
        <a href="../" hreflang="ru" lang="ru">RU</a>
        <a href="./" hreflang="uz" aria-current="page">UZ</a>''')

# ---------- hero ----------
R('Abbos / Meta Ads / Ташкент / 2026', 'Abbos / Meta Ads / Toshkent / 2026')
R('<ul class="pills" aria-label="Направления">', '<ul class="pills" aria-label="Yoʻnalishlar">')
R('<li class="pill pill--hot">Разблокировка</li>', '<li class="pill pill--hot">Blokdan chiqarish</li>')
R('<li class="pill">Арбитраж</li>', '<li class="pill">Arbitraj</li>')
R('<li class="pill">Аудит</li>', '<li class="pill">Bepul audit</li>')
R('id="hero-title">Забанили<span>?</span>', 'id="hero-title">Akkaunt<br>blokdami<span>?</span>')
R('<p class="hero__sub">Разберусь, за что, и помогу <em>вернуть рекламу в работу.</em></p>',
  '<p class="hero__sub">Instagram va Facebook reklamasini <em>blokdan chiqarishga yordam beraman.</em></p>')
R('<p class="hero__lead">Я Аббос. 2,5 года работал в Meta Pro Team — команде, которая помогает рекламодателям. Знаю, как устроены правила, проверки и апелляции изнутри. Теперь помогаю бизнесу и арбитражникам — спокойно, по делу и без пустых обещаний.</p>',
  '<p class="hero__lead">Men Abbosman. 2,5 yil Meta Pro Team jamoasida reklama beruvchilarga yordam berganman — akkauntlar nega bloklanishini va apellyatsiya qanday yozilishini ichkaridan bilaman. Biznes egalari va arbitrajchilarga bloklangan akkauntni tiklash, reklamani tekshirish va toʻgʻri sozlashda yordam beraman — quruq vaʼdalarsiz.</p>')
R('Бесплатная диагностика\n', 'Blokni bepul tekshirtirish\n', 2)
R('>Аудит рекламы — бесплатно</a>', '>Reklama auditi — bepul</a>')
R('Отвечаю в Telegram в течение 2 часов, с 13:00 до 23:00', 'Telegramda 2 soat ichida javob beraman (13:00–23:00)')
R('<span>Бесплатный созвон в <b>Zoom</b> или <b>Discord</b></span>', '<span><b>Zoom</b> yoki <b>Discord</b>da bepul onlayn suhbat</span>')
R('alt="Аббос — специалист по рекламе Meta Ads"', 'alt="Abbos — Meta Ads reklama mutaxassisi"')
R('<ul class="chips" aria-label="Условия">', '<ul class="chips" aria-label="Shartlar">')
R('            Без паролей\n', '            Parol soʻramayman\n')
R('            Диагностика бесплатно\n', '            Tekshiruv bepul\n')
R('            Цена до старта\n', '            Narx oldindan aytiladi\n')
R('<b>2,5 года</b>\n          <span>в Meta Pro Team</span>', '<b>2,5 yil</b>\n          <span>Meta Pro Team tajribasi</span>')

# ---------- ленты ----------
R('Instagram Boost <i>✦</i> Разблокировка <i>✦</i> Facebook Ads', 'Instagram Boost <i>✦</i> Blokdan chiqarish <i>✦</i> Facebook Ads')
R('Meta Ads <i>✦</i> Разблокировка <i>✦</i> Арбитраж <i>✦</i> Аудит <i>✦</i>', 'Meta Ads <i>✦</i> Blokdan chiqarish <i>✦</i> Arbitraj <i>✦</i> Audit <i>✦</i>')

# ---------- услуги ----------
R('<p class="eyebrow eyebrow--light">Услуги</p>', '<p class="eyebrow eyebrow--light">Xizmatlar</p>')
R('id="services-title">С чем <em>помогаю</em>', 'id="services-title">Qanday <em>yordam beraman</em>')
R('<span class="tag tag--ink">самое частое</span>', '<span class="tag tag--ink">eng koʻp murojaat</span>')
R('<h3 class="svc__title">Снятие ограничений</h3>', '<h3 class="svc__title">Blokdan chiqarish</h3>')
R('Заблокирован рекламный кабинет, страница, профиль или бизнес-портфолио? Найду реальную причину ограничения, подготовлю апелляцию, которую читают, и проведу до ответа поддержки.',
  'Reklama akkaunti, sahifa, profil yoki biznes-menejeringiz blokga tushdimi? Blokning asl sababini topaman, apellyatsiyani toʻgʻri yozib beraman va Meta qoʻllab-quvvatlash xizmati javob bergunga qadar jarayonni kuzatib boraman.')
R('aria-label="Снятие ограничений — написать в Telegram"', 'aria-label="Blokdan chiqarish — Telegramga yozish"')
R('<span class="tag tag--urgent">срочно</span>', '<span class="tag tag--urgent">shoshilinch</span>')
R('<h3 class="svc__title">Взлом и фишинг</h3>', '<h3 class="svc__title">Buzilgan akkauntni tiklash</h3>')
R('Потеряли доступ, сменились админы, списали деньги с карты? Помогу восстановить доступ, убрать чужих, защитить аккаунт и научу отличать фишинговое «письмо от Meta» от настоящего.',
  'Akkauntingizga kira olmayapsizmi, begona admin paydo boʻldimi yoki kartadan pul yechildimi? Kirishni tiklashga, begonalarni chiqarib yuborishga va akkauntni himoyalashga yordam beraman. «Metadan kelgan» soxta xatlarni haqiqiysidan ajratishni ham oʻrgataman.')
R('aria-label="Взлом и фишинг — написать в Telegram"', 'aria-label="Buzilgan akkauntni tiklash — Telegramga yozish"')
R('<span class="tag tag--free">бесплатно</span>', '<span class="tag tag--free">bepul</span>')
R('<h3 class="svc__title">Аудит рекламы</h3>', '<h3 class="svc__title">Reklama auditi</h3>')
R('Посмотрю ваши кампании или бизнес-страницу и скажу, где теряются деньги и что может привести к бану. Без воды — конкретный список правок.',
  'Reklamangiz yoki biznes-sahifangizni koʻrib chiqaman: pul qayerda behuda ketayotganini va nima blokka olib kelishi mumkinligini aytaman. Umumiy gaplar emas — aniq tuzatishlar roʻyxati.')
R('aria-label="Получить аудит бесплатно"', 'aria-label="Auditni bepul olish"')
R('<h3 class="svc__title">Арбитраж трафика</h3>', '<h3 class="svc__title">Trafik arbitraji</h3>')
R('Запуск и масштабирование кампаний в Meta Ads под офферы. Связки, креативы, аудитории — и кабинеты, которые не улетают в бан на третий день.',
  'Offerlar uchun Meta Ads reklamasini ishga tushirish va kengaytirish. Bogʻlamalar, kreativlar, auditoriyalar — va uchinchi kuniyoq blokga tushmaydigan akkauntlar.')
R('aria-label="Арбитраж трафика — подробнее"', 'aria-label="Trafik arbitraji — batafsil"')

# ---------- доверие ----------
R('<p class="eyebrow eyebrow--dot">Почему мне доверяют</p>', '<p class="eyebrow eyebrow--dot">Nega menga ishonishadi</p>')
R('id="trust-title">Я видел, как это работает <em>с той стороны</em>', 'id="trust-title">Meta qanday ishlashini <em>ichkaridan bilaman</em>')
R('alt="Аббос в солнцезащитных очках с телефоном"', 'alt="Abbos quyosh koʻzoynagida, qoʻlida telefon"')
R('aria-label="Без паролей. Цена до старта. Диагностика бесплатно."', 'aria-label="Parol soʻramayman. Narx oldindan aytiladi. Tekshiruv bepul."', 2)
R('БЕЗ ПАРОЛЕЙ • ЦЕНА ДО СТАРТА • ДИАГНОСТИКА БЕСПЛАТНО •', 'PAROL SOʻRAMAYMAN • NARX OLDINDAN • TEKSHIRUV BEPUL •', 2)
R('<p>2,5 года я работал в Meta Pro Team<sup><a href="#trust-note" aria-label="Примечание 1">¹</a></sup> — разбирал проблемы рекламодателей, монетизацию и ограничения каждый день. Поэтому я не гадаю, почему вас заблокировали, а знаю, куда смотреть.</p>',
  '<p>2,5 yil Meta Pro Team<sup><a href="#trust-note" aria-label="1-izoh">¹</a></sup> jamoasida ishladim: har kuni reklama beruvchilarning muammolari, bloklar va monetizatsiya masalalarini hal qilardim. Shuning uchun akkauntingiz nega bloklanganini taxmin qilmayman — qayerdan qidirishni bilaman.</p>')
R('<p>Ещё 4 года я в UI/UX-дизайне — понимаю, как должны выглядеть креатив и страница, чтобы им верили и люди, и модерация.</p>',
  '<p>Bundan tashqari, 4 yildan beri UI/UX-dizayn bilan shugʻullanaman: reklama va sahifa qanday koʻrinsa, odamlar ham, Meta moderatsiyasi ham ishonishini bilaman.</p>')
R('2,5</span> <small>года</small></b><span>в Meta Pro Team</span>', '2,5</span> <small>yil</small></b><span>Meta Pro Team tajribasi</span>')
R('<span data-count="4">4</span> <small>года</small></b><span>в дизайне и UX</span>', '<span data-count="4">4</span> <small>yil</small></b><span>dizayn va UX sohasida</span>')
R('<span>паролей, которые я прошу у клиентов</span>', '<span>marta mijozdan parol soʻraganman</span>')
R('¹ В составе компании-подрядчика Meta. Сейчас работаю независимо и с Meta не связан.', '¹ Meta pudratchi kompaniyasi tarkibida. Hozir mustaqil ishlayman va Meta bilan bogʻliq emasman.')
R('<p class="geo__label">Работаю с бизнесом из</p>', '<p class="geo__label">Qaysi davlatlar bilan ishlayman</p>')
R('>Узбекистан</li>', '>Oʻzbekiston</li>')
R('>Кыргызстан</li>', '>Qirgʻiziston</li>')
R('>Таджикистан</li>', '>Tojikiston</li>')
R('>Азербайджан</li>', '>Ozarbayjon</li>')
R('<p class="geo__more">и удалённо — откуда угодно.</p>', '<p class="geo__more">va masofadan — istalgan davlat bilan.</p>')

# ---------- арбитраж ----------
R('id="arb-title" data-reveal><span>Сливаете</span> <span>бюджет?</span>', 'id="arb-title" data-reveal><span>Byudjet</span> <span>kuyyaptimi?</span>')
R('Арбитраж в Meta Ads — это не «залил и молись».', 'Meta Ads tizimida arbitraj — «reklamani qoʻyib, omadga ishonish» emas.')
R('Большинство кабинетов умирает не из-за плохого оффера, а из-за ошибок, которые видно с первого взгляда: креатив нарушает правила, домен уже в чёрном списке, прогрев сделан наспех. Я помогу собрать связку, которая живёт дольше и окупается.',
  'Koʻp akkauntlar yomon offer sababli emas, bir qarashda koʻrinadigan xatolar sababli blokga tushadi: kreativ qoidalarga zid, domen qora roʻyxatda, akkaunt shoshilib «qizdirilgan». Uzoq ishlaydigan va xarajatini qoplaydigan bogʻlama yigʻishga yordam beraman.')
R('<h3 class="arb__list-title" data-reveal>Что входит</h3>', '<h3 class="arb__list-title" data-reveal>Nimalar kiradi</h3>')
R('>Разбор оффера и подбор подходов</li>', '>Offer tahlili va yondashuvlarni tanlash</li>')
R('>Креативы и тексты, которые проходят модерацию</li>', '>Moderatsiyadan oʻtadigan kreativlar va matnlar</li>')
R('>Структура кампаний и тесты</li>', '>Kampaniyalar tuzilmasi va testlar</li>')
R('>Масштабирование без внезапных банов</li>', '>Kutilmagan bloklarsiz kengaytirish</li>')
R('>Консультации для соло-арбитражников и команд</li>', '>Yakka arbitrajchilar va jamoalar uchun maslahat</li>')
R('<span>Без клоакинга, фарма и «обхода модерации». Работаю в рамках правил — поэтому кабинеты живут.</span>',
  '<span>Kloaking, ferma akkauntlar va «moderatsiyani aylanib oʻtish» yoʻq. Qoidalar doirasida ishlayman — shuning uchun akkauntlar uzoq yashaydi.</span>')

# ---------- созвон ----------
R('<!-- 5a. СОЗВОН (Zoom / Discord) — согласовано, бесплатно -->', '<!-- 5a. QOʻNGʻIROQ (Zoom / Discord) -->')
R('<p class="eyebrow eyebrow--light">Созвон</p>', '<p class="eyebrow eyebrow--light">Onlayn suhbat</p>')
R('id="call-title">Удобнее голосом? <em>Созвонимся</em>', 'id="call-title">Gaplashish qulaymi? <em>Onlayn uchrashamiz</em>')
R('<p class="call__text">Бесплатно, в Zoom или Discord — как вам удобнее. Покажете кабинет через демонстрацию экрана, и разберём ситуацию вместе, в реальном времени. Пароли не нужны.</p>',
  '<p class="call__text">Bepul, Zoom yoki Discordda — sizga qaysi biri qulay boʻlsa. Ekraningizni koʻrsatasiz, muammoni birga, jonli tarzda koʻrib chiqamiz. Parol kerak emas.</p>')
R('<ul class="call__chips" aria-label="Детали созвона">', '<ul class="call__chips" aria-label="Suhbat tafsilotlari">')
R('</svg>Бесплатно</li>', '</svg>Bepul</li>')
R('</svg>Демонстрация экрана</li>', '</svg>Ekranni koʻrsatish</li>')
R('            Договориться о созвоне\n', '            Suhbat vaqtini kelishish\n')
R('</span>Аббос</span>', '</span>Abbos</span>')
R('<b>Вы</b>', '<b>Siz</b>')
R('</svg>Демонстрация экрана</span>', '</svg>Ekran namoyishi</span>')

# ---------- как я работаю ----------
R('<p class="eyebrow eyebrow--dot">Как я работаю</p>', '<p class="eyebrow eyebrow--dot">Qanday ishlayman</p>')
R('id="how-title">Четыре шага, <em>без сюрпризов</em>', 'id="how-title">Ish tartibi: <em>4 oddiy qadam</em>')
for n in ['01','02','03','04']:
    R(f'<span class="step__num">Шаг {n}</span>', f'<span class="step__num">{n}-qadam</span>')
R('<h3 class="step__title">Пишете в Telegram</h3>', '<h3 class="step__title">Telegramga yozasiz</h3>')
R('Коротко: что случилось и скриншот ограничения или ссылка на рекламу.', 'Nima boʻlganini qisqacha yozing va blok skrinshotini yoki reklama havolasini yuboring.')
R('<h3 class="step__title">Бесплатная диагностика</h3>', '<h3 class="step__title">Bepul tekshiruv</h3>')
R('За 15–30 минут говорю, есть ли шансы и что нужно сделать.', '15–30 daqiqada akkauntni tiklash imkoni bor-yoʻqligini va nima qilish kerakligini aytaman.')
R('<h3 class="step__title">Фиксируем цену</h3>', '<h3 class="step__title">Narxni kelishamiz</h3>')
R('Вы знаете сумму до начала работы. Без доплат по ходу.', 'Narxni ish boshlanmasdan oldin bilasiz. Keyin qoʻshimcha toʻlov soʻralmaydi.')
R('<h3 class="step__title">Работаю и держу в курсе</h3>', '<h3 class="step__title">Ishlayman va xabar berib turaman</h3>')
R('Вы видите каждый шаг, а не ждёте в тишине.', 'Har bir qadamdan xabardor boʻlasiz — javobsiz kutib qolmaysiz.')

# ---------- сколько ----------
R('<p class="eyebrow eyebrow--ink">Цены</p>', '<p class="eyebrow eyebrow--ink">Xizmat narxi</p>')
letters_ru = ''.join(f'<span class="l" style="--i:{i}">{c}</span>' for i,c in enumerate('Сколько')) + '<span class="l l--q" style="--i:7">?</span>'
letters_uz = ''.join(f'<span class="l" style="--i:{i}">{c}</span>' for i,c in enumerate('Qancha')) + '<span class="l l--q" style="--i:6">?</span>'
R(f'<span class="sr-only">Сколько?</span><span aria-hidden="true">{letters_ru}</span>', f'<span class="sr-only">Qancha?</span><span aria-hidden="true">{letters_uz}</span>')
R('Честно: зависит от случая. Поэтому цену я называю после диагностики, а не до.', 'Ochigʻi, har bir holat har xil. Shuning uchun narxni akkauntni tekshirib koʻrgandan keyin aytaman.')
R('<b class="ptag__title">Диагностика — <mark>бесплатно</mark>.</b>', '<b class="ptag__title">Blokni tekshirish — <mark>bepul</mark>.</b>')
R('<span class="ptag__text">Сначала смотрю, потом говорю цену.</span>', '<span class="ptag__text">Avval koʻraman, keyin narxni aytaman.</span>')
R('<b class="ptag__title">Аудит — <mark>бесплатно</mark>.</b>', '<b class="ptag__title">Reklama auditi — <mark>bepul</mark>.</b>')
R('<span class="ptag__text">Всегда.</span>', '<span class="ptag__text">Har doim.</span>')
R('<b class="ptag__title">Цена фиксируется до старта.</b>', '<b class="ptag__title">Narx oldindan kelishiladi.</b>')
R('<span class="ptag__text">Никаких «а ещё нужно доплатить».</span>', '<span class="ptag__text">«Yana qoʻshimcha toʻlash kerak» degan gap boʻlmaydi.</span>')
R('<b class="ptag__title">Нет шансов — скажу прямо.</b>', '<b class="ptag__title">Imkon boʻlmasa — ochiq aytaman.</b>')
R('<span class="ptag__text">И не возьму денег за безнадёжный случай.</span>', '<span class="ptag__text">Tiklab boʻlmaydigan holat uchun pul olmayman.</span>')
R('<b class="ptag__title">Оплата после <mark>результата</mark>.</b>', '<b class="ptag__title">Toʻlov — <mark>natijadan</mark> keyin.</b>')
R('<span class="ptag__text">Платите, когда доступ восстановлен или ограничение снято.</span>', '<span class="ptag__text">Akkaunt tiklangach yoki blok olib tashlangach toʻlaysiz.</span>')
R('Арбитраж, ведение рекламы и доп. услуги — стоимость после короткого созвона.', 'Arbitraj, reklama yuritish va qoʻshimcha xizmatlar narxi — qisqa suhbatdan keyin.')

# ---------- аудит ----------
R('<p class="eyebrow eyebrow--light">Аудит</p>', '<p class="eyebrow eyebrow--light">Audit</p>')
R('id="audit-title">Бесплатный аудит <em>рекламы или страницы</em>', 'id="audit-title">Reklama yoki sahifangizni <em>bepul tekshirib beraman</em>')
R('Пришлите ссылку — я посмотрю кампании, креативы, настройки Pixel и саму страницу. В течение дня получите разбор: что мешает продажам, что может привести к бану и что исправить в первую очередь.',
  'Havola yuboring — reklama kampaniyalari, kreativlar, Pixel sozlamalari va sahifangizni koʻrib chiqaman. Bir kun ichida xulosa olasiz: sotuvga nima xalaqit beryapti, nima blokka olib kelishi mumkin va avval nimani tuzatish kerak.')
R('<ul class="checks" data-reveal aria-label="Что проверяю">', '<ul class="checks" data-reveal aria-label="Nimalarni tekshiraman">')
R('</span>Структура кампаний и аудитории</li>', '</span>Kampaniyalar tuzilishi va auditoriyalar</li>')
R('</span>Креативы и тексты на соответствие правилам</li>', '</span>Kreativ va matnlar qoidalarga mosmi</li>')
R('</span>Meta Pixel и события</li>', '</span>Meta Pixel va hodisalar</li>')
R('</span>Бизнес-страница и профиль</li>', '</span>Biznes-sahifa va profil</li>')
R('</span>Риски блокировки</li>', '</span>Blokga tushish xavfi</li>')
R('<!-- Web3Forms: ключ публичный по дизайну сервиса -->', '<!-- Web3Forms: kalit xizmat dizayniga koʻra ochiq -->')
R('value="Заявка на бесплатный аудит — сайт Abbos"', 'value="Bepul audit uchun ariza — Abbos sayti (UZ)"')
R('value="Сайт Abbos · Meta Ads"', 'value="Abbos sayti · Meta Ads (UZ)"')
R('<label for="f-name">Имя</label>', '<label for="f-name">Ismingiz</label>')
R('<label for="f-contact">Telegram или телефон</label>', '<label for="f-contact">Telegram yoki telefon raqamingiz</label>')
R('<label for="f-link">Ссылка на страницу или аккаунт</label>', '<label for="f-link">Sahifa yoki akkaunt havolasi</label>')
R('<legend>Что нужно</legend>', '<legend>Sizga nima kerak?</legend>')
for ru, uz, chk in [('Снятие ограничений','Blokdan chiqarish',''),('Взлом','Buzilgan akkaunt',''),('Аудит','Audit',' checked'),('Арбитраж','Arbitraj',''),
                    ('Сайт','Sayt',''),('Ведение страниц','Sahifa yuritish',''),('Качество лидов','Sifatli lidlar',''),('Другое','Boshqa','')]:
    R(f'<input type="radio" name="need" value="{ru}"{chk}><span>{ru}</span>', f'<input type="radio" name="need" value="{uz}"{chk}><span>{uz}</span>')
R('<label for="f-msg">Комментарий (необязательно)</label>', '<label for="f-msg">Izoh (ixtiyoriy)</label>')
R('<span class="aform__btn-text">Получить аудит бесплатно</span>', '<span class="aform__btn-text">Bepul audit olish</span>')
R('Я не прошу пароли и коды подтверждения. Никогда.', 'Parol va tasdiqlash kodlarini soʻramayman. Hech qachon.')
R('<p>Заявка у меня. Напишу вам в Telegram в ближайшее время.</p>', '<p>Arizangiz qabul qilindi. Tez orada Telegramda yozaman.</p>')
R('<p>Что-то пошло не так. Напишите мне напрямую в Telegram —</p>', '<p>Xatolik yuz berdi. Menga toʻgʻridan-toʻgʻri Telegramda yozing —</p>')

# ---------- под ключ ----------
R('<p class="eyebrow eyebrow--dot">[ 09 ] / Под ключ</p>', '<p class="eyebrow eyebrow--dot">[ 09 ] / Toʻliq xizmat</p>')
R('id="turnkey-title" data-reveal>Под <span>ключ</span>', 'id="turnkey-title" data-reveal>Toʻliq <span>xizmat</span>')
R('Реклама работает, только когда ей есть куда вести. Поэтому могу взять на себя всё: от сайта до заявок.', 'Reklama mijozni toʻgʻri joyga olib borsagina ishlaydi. Shuning uchun hammasini oʻzim qilib bera olaman: saytdan tortib arizalargacha.')
R('<h3 class="tk__title">Сайты и лендинги</h3>', '<h3 class="tk__title">Sayt va lendinglar</h3>')
R('Продающие одностраничники и сайты-визитки под рекламу Meta: быстрые на телефоне, с формой заявки и уже настроенным Pixel. Я 4 года в UI/UX — дизайн и вёрстку делаю сам.',
  'Meta reklamasi uchun sotuvchi lending va vizitka-saytlar: telefonda tez ochiladi, ariza formasi va Pixel sozlangan boʻladi. 4 yildan beri UI/UX bilan shugʻullanaman — dizayn va vyorstkani oʻzim qilaman.')
R('>Посмотреть портфолио <svg', '>Portfolioni koʻrish <svg')
R('<h3 class="tk__title">Ведение Instagram и Facebook</h3>', '<h3 class="tk__title">Instagram va Facebook sahifasini yuritish</h3>')
R('Оформление профиля, контент-план, визуал постов и сторис, ответы на типовые вопросы. Страница, которая продаёт сама — и которую не стыдно показывать в рекламе.',
  'Profilni bezash, kontent-reja, post va storislar dizayni, koʻp beriladigan savollarga javoblar. Oʻzi sotadigan va reklamada koʻrsatsa uyalmaydigan sahifa.')
R('<h3 class="tk__title">Качество лидов</h3>', '<h3 class="tk__title">Sifatli lidlar</h3>')
R('Много заявок, а продаж нет? Настрою формы и кампании под вашу нишу: уточняющие вопросы, отсев случайных людей, оптимизация на тех, кто реально покупает. Знаю специфику учебных центров, мебели, стройматериалов и малого бизнеса.',
  'Ariza koʻp, sotuv esa yoʻqmi? Forma va reklamani sohangizga moslab sozlayman: aniqlashtiruvchi savollar, tasodifiy odamlarni saralash, haqiqiy xaridorlarga optimallashtirish. Oʻquv markazlari, mebel, qurilish mollari va kichik biznes sohalarini yaxshi bilaman.')
R('Меньше «просто спросить» — больше тех, кто готов платить.', '«Shunchaki soʻrab koʻrdim» kamroq — sotib olishga tayyor mijozlar koʻproq.')
R('<p class="tk-more__label" data-reveal>Ещё</p>', '<p class="tk-more__label" data-reveal>Yana</p>')
R('</svg>Бизнес-портфолио (Business Manager)</li>', '</svg>Biznes-menejer (Business Manager) sozlash</li>')
R('</svg>Ведение таргета</li>', '</svg>Target reklama yuritish</li>')
R('</svg>Каталог товаров</li>', '</svg>Mahsulotlar katalogi</li>')
R('</svg>Проверка креативов до запуска</li>', '</svg>Kreativlarni ishga tushirishdan oldin tekshirish</li>')
R('</svg>Консультации по правилам рекламы</li>', '</svg>Reklama qoidalari boʻyicha maslahat</li>')

# ---------- FAQ ----------
R('<p class="eyebrow eyebrow--light">Вопросы</p>', '<p class="eyebrow eyebrow--light">Savol-javob</p>')
for ru, uz in [
 ('Вы гарантируете разблокировку?', 'Blokdan chiqarishga kafolat berasizmi?'),
 ('Нет, и никто честный не гарантирует — решение принимает Meta. Я гарантирую, что найду реальную причину, правильно оформлю апелляцию и скажу прямо, если шансов нет.',
  'Yoʻq. Halol mutaxassis kafolat bermaydi, chunki qarorni Meta qabul qiladi. Men blokning asl sababini topishga, apellyatsiyani toʻgʻri yozishga va imkon boʻlmasa, buni ochiq aytishga kafolat beraman.'),
 ('Вы работаете в Meta?', 'Siz Metada ishlaysizmi?'),
 ('Нет. Я 2,5 года работал в Meta Pro Team в составе компании-подрядчика. Сейчас я независимый специалист.',
  'Yoʻq. 2,5 yil Meta pudratchi kompaniyasi tarkibida Meta Pro Team jamoasida ishlaganman. Hozir mustaqil mutaxassisman.'),
 ('Нужен ли вам мой пароль?', 'Parolimni berishim kerakmi?'),
 ('Нет. Если нужен доступ — вы добавляете меня в бизнес-портфолио с ограниченной ролью и в любой момент можете убрать. Пароли и коды 2FA не прошу никогда.',
  'Yoʻq. Kirish kerak boʻlsa, meni biznes-menejerga cheklangan rol bilan qoʻshasiz va istalgan payt oʻchirib qoʻya olasiz. Parol va 2FA kodlarini hech qachon soʻramayman.'),
 ('Сколько времени занимает разблокировка?', 'Blokdan chiqarish qancha vaqt oladi?'),
 ('От нескольких дней до нескольких недель — зависит от типа ограничения и скорости ответа поддержки. Точнее скажу после диагностики.',
  'Bir necha kundan bir necha haftagacha: blok turiga va Meta qoʻllab-quvvatlash xizmati qanchalik tez javob berishiga bogʻliq. Aniqroq muddatni tekshiruvdan keyin aytaman.'),
 ('Аудит правда бесплатный? В чём подвох?', 'Audit rostdan ham bepulmi? Sharti bormi?'),
 ('Подвоха нет. Аудит — способ показать, как я работаю. Если захотите внедрить правки со мной — договоримся отдельно. Не захотите — разбор останется у вас.',
  'Hech qanday sharti yoʻq. Audit — qanday ishlashimni koʻrsatish usuli. Tuzatishlarni men bilan qilmoqchi boʻlsangiz, alohida kelishamiz. Xohlamasangiz — xulosa oʻzingizda qoladi.'),
 ('Работаете только с Узбекистаном?', 'Faqat Oʻzbekiston bilan ishlaysizmi?'),
 ('Нет, работаю удалённо с клиентами из любой страны. Языки: русский, узбекский, английский.', 'Yoʻq, istalgan davlatdagi mijozlar bilan masofadan ishlayman. Oʻzbek, rus va ingliz tillarida.'),
 ('Помогаете с арбитражем по «серым» схемам?', '«Kulrang» sxemalar bilan arbitrajga yordam berasizmi?'),
 ('Нет. Клоакинг и обход модерации — быстрый путь в бан. Я помогаю строить связки, которые живут.', 'Yoʻq. Kloaking va moderatsiyani aylanib oʻtish — blokga eng qisqa yoʻl. Men uzoq ishlaydigan bogʻlamalar qurishga yordam beraman.'),
]:
    R(ru, uz)
R('            Написать в Telegram\n', '            Telegramga yozish\n')
R('>Написать в Telegram</a>', '>Telegramga yozish</a>')
R('<span>Написать в Telegram</span>', '<span>Telegramga yozish</span>')

# ---------- контакты ----------
R('<span class="contact__word contact__word--back">Пишите</span>', '<span class="contact__word contact__word--back">Yozing</span>')
R('<span class="contact__word contact__word--front">Пишите</span>', '<span class="contact__word contact__word--front">Yozing</span>')
R('<h2 class="sr-only" id="contact-title">Пишите</h2>', '<h2 class="sr-only" id="contact-title">Yozing</h2>')
R('Опишите ситуацию в двух словах — отвечу и скажу, чем могу помочь.', 'Muammoingizni ikki ogʻiz soʻz bilan yozing — javob berib, qanday yordam bera olishimni aytaman.')
R('<small>Телефон</small>', '<small>Telefon</small>')

R('src="assets/img/site-preview.webp" width="600" height="3419"', 'src="assets/img/site-preview-uz.webp" width="600" height="3555"')

# ---------- footer ----------
R('aria-label="Abbos — наверх"', 'aria-label="Abbos — yuqoriga"')
R('</svg>Наверх</a>', '</svg>Yuqoriga</a>')
R('© 2026 Abbos — Meta Ads специалист · Ташкент · ', '© 2026 Abbos — Meta Ads mutaxassisi · Toshkent · ')
R(' · Портфолио: <a href="https://abbos77.github.io/"', ' · Portfolio: <a href="https://abbos77.github.io/"')
R('Независимый специалист. Не связан с Meta Platforms, Inc. Facebook и Instagram — товарные знаки Meta Platforms, Inc.',
  'Mustaqil mutaxassis. Meta Platforms, Inc. bilan bogʻliq emas. Facebook va Instagram — Meta Platforms, Inc. kompaniyasining tovar belgilari.')

# ---------- HTML-комментарии на русском — убираем ----------
s = re.sub(r'<!--(?![^>]*Web3Forms: kalit)[^>]*[А-Яа-яЁё][^>]*-->', '', s)

# ---------- пути к ассетам ----------
s = s.replace('href="assets/', 'href="../assets/').replace('src="assets/', 'src="../assets/')
s = s.replace('"' + BASE + 'assets/', '"' + BASE + 'assets/')  # абсолютные не трогаем

open('uz/index.html', 'w', encoding='utf-8').write(s)
left = sorted(set(re.findall(r'[^\s<>"]*[А-Яа-яЁё][^\s<>"]*', s)))
print('cyrillic left:', left[:40], len(left))
