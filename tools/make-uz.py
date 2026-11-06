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
  '<title>Bloklandimi? Meta Ads reklamasini blokdan chiqarish va bepul audit — Abbos</title>')
R('content="Разберусь, за что заблокировали рекламный кабинет, страницу или профиль, и помогу вернуть рекламу в работу. Бесплатная диагностика и бесплатный аудит рекламы."',
  'content="Reklama kabineti, sahifa yoki profil nega bloklanganini aniqlayman va reklamani qayta ishga tushirishga yordam beraman. Bepul diagnostika va reklamaning bepul auditi."')
R(f'<link rel="canonical" href="{BASE}">', f'<link rel="canonical" href="{BASE}uz/">')
R('<meta property="og:locale" content="ru_RU">\n<meta property="og:locale:alternate" content="uz_UZ">', '<meta property="og:locale" content="uz_UZ">\n<meta property="og:locale:alternate" content="ru_RU">')
R(f'<meta property="og:url" content="{BASE}">', f'<meta property="og:url" content="{BASE}uz/">')
R('Забанили? Разберусь, за что, и помогу вернуть рекламу в работу', 'Bloklandimi? Sababini aniqlab, reklamani qayta ishga tushirishga yordam beraman', 2)
R('content="Разблокировка рекламных кабинетов, страниц и профилей, бесплатная диагностика и аудит рекламы Meta Ads. Без паролей, цена до старта."',
  'content="Reklama kabinetlari, sahifa va profillarni blokdan chiqarish, Meta Ads reklamasining bepul diagnostikasi va auditi. Parolsiz, narx oldindan."')
R('content="Разблокировка, бесплатная диагностика и аудит рекламы Meta Ads. Без паролей, цена до старта."',
  'content="Blokdan chiqarish, Meta Ads reklamasining bepul diagnostikasi va auditi. Parolsiz, narx oldindan."')
R('assets/img/og-ru.jpg', 'assets/img/og-uz.jpg')
R('content="Аббос — Meta Ads: разблокировка и бесплатный аудит рекламы"', 'content="Abbos — Meta Ads: blokdan chiqarish va reklamaning bepul auditi"')
R('"url": "' + BASE + '",', '"url": "' + BASE + 'uz/",')
R('"description": "Разблокировка рекламных кабинетов, страниц и профилей, бесплатная диагностика и аудит рекламы Meta Ads, арбитраж трафика (white-hat).",',
  '"description": "Reklama kabinetlari, sahifa va profillarni blokdan chiqarish, Meta Ads reklamasining bepul diagnostikasi va auditi, trafik arbitraji (white-hat).",')
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
R('<a href="#contact">Контакты</a>', '<a href="#contact">Kontaktlar</a>')
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
R('<li class="pill">Аудит</li>', '<li class="pill">Audit</li>')
R('id="hero-title">Забанили<span>?</span>', 'id="hero-title">Bloklandimi<span>?</span>')
R('<p class="hero__sub">Разберусь, за что, и помогу <em>вернуть рекламу в работу.</em></p>',
  '<p class="hero__sub">Sababini aniqlab, <em>reklamani qayta ishga tushirishga</em> yordam beraman.</p>')
R('<p class="hero__lead">Я Аббос. 2,5 года работал в Meta Pro Team — команде, которая помогает рекламодателям. Знаю, как устроены правила, проверки и апелляции изнутри. Теперь помогаю бизнесу и арбитражникам — спокойно, по делу и без пустых обещаний.</p>',
  '<p class="hero__lead">Men Abbosman. 2,5 yil reklama beruvchilarga yordam beradigan Meta Pro Team jamoasida ishladim. Qoidalar, tekshiruvlar va apellyatsiyalar ichkaridan qanday ishlashini bilaman. Endi biznes va arbitrajchilarga yordam beraman — xotirjam, aniq va quruq vaʼdalarsiz.</p>')
R('Бесплатная диагностика\n', 'Bepul diagnostika\n', 2)
R('>Аудит рекламы — бесплатно</a>', '>Reklama auditi — bepul</a>')
R('Отвечаю в Telegram в течение 2 часов, с 13:00 до 23:00', 'Telegramda 2 soat ichida javob beraman, 13:00 dan 23:00 gacha')
R('<span>Бесплатный созвон в <b>Zoom</b> или <b>Discord</b></span>', '<span><b>Zoom</b> yoki <b>Discord</b> orqali bepul qoʻngʻiroq</span>')
R('alt="Аббос — специалист по рекламе Meta Ads"', 'alt="Abbos — Meta Ads reklama mutaxassisi"')
R('<ul class="chips" aria-label="Условия">', '<ul class="chips" aria-label="Shartlar">')
R('            Без паролей\n', '            Parolsiz\n')
R('            Диагностика бесплатно\n', '            Diagnostika bepul\n')
R('            Цена до старта\n', '            Narx oldindan\n')
R('<b>2,5 года</b>\n          <span>в Meta Pro Team</span>', '<b>2,5 yil</b>\n          <span>Meta Pro Team jamoasida</span>')

# ---------- ленты ----------
R('Instagram Boost <i>✦</i> Разблокировка <i>✦</i> Facebook Ads', 'Instagram Boost <i>✦</i> Blokdan chiqarish <i>✦</i> Facebook Ads')
R('Meta Ads <i>✦</i> Разблокировка <i>✦</i> Арбитраж <i>✦</i> Аудит <i>✦</i>', 'Meta Ads <i>✦</i> Blokdan chiqarish <i>✦</i> Arbitraj <i>✦</i> Audit <i>✦</i>')

# ---------- услуги ----------
R('<p class="eyebrow eyebrow--light">Услуги</p>', '<p class="eyebrow eyebrow--light">Xizmatlar</p>')
R('id="services-title">С чем <em>помогаю</em>', 'id="services-title">Nimada <em>yordam beraman</em>')
R('<span class="tag tag--ink">самое частое</span>', '<span class="tag tag--ink">eng koʻp uchraydi</span>')
R('<h3 class="svc__title">Снятие ограничений</h3>', '<h3 class="svc__title">Cheklovlarni olib tashlash</h3>')
R('Заблокирован рекламный кабинет, страница, профиль или бизнес-портфолио? Найду реальную причину ограничения, подготовлю апелляцию, которую читают, и проведу до ответа поддержки.',
  'Reklama kabineti, sahifa, profil yoki biznes-portfolio bloklandimi? Cheklovning haqiqiy sababini topaman, oʻqiladigan apellyatsiya tayyorlayman va qoʻllab-quvvatlash javob berguncha birga boraman.')
R('aria-label="Снятие ограничений — написать в Telegram"', 'aria-label="Cheklovlarni olib tashlash — Telegramga yozish"')
R('<span class="tag tag--urgent">срочно</span>', '<span class="tag tag--urgent">shoshilinch</span>')
R('<h3 class="svc__title">Взлом и фишинг</h3>', '<h3 class="svc__title">Buzib kirish va fishing</h3>')
R('Потеряли доступ, сменились админы, списали деньги с карты? Помогу восстановить доступ, убрать чужих, защитить аккаунт и научу отличать фишинговое «письмо от Meta» от настоящего.',
  'Kirish yoʻqoldimi, adminlar almashdimi, kartadan pul yechildimi? Kirishni tiklash, begonalarni olib tashlash va akkauntni himoyalashda yordam beraman, soxta «Meta xati»ni haqiqiysidan ajratishni oʻrgataman.')
R('aria-label="Взлом и фишинг — написать в Telegram"', 'aria-label="Buzib kirish va fishing — Telegramga yozish"')
R('<span class="tag tag--free">бесплатно</span>', '<span class="tag tag--free">bepul</span>')
R('<h3 class="svc__title">Аудит рекламы</h3>', '<h3 class="svc__title">Reklama auditi</h3>')
R('Посмотрю ваши кампании или бизнес-страницу и скажу, где теряются деньги и что может привести к бану. Без воды — конкретный список правок.',
  'Kampaniyalaringiz yoki biznes-sahifangizni koʻrib chiqaman va pul qayerda yoʻqolayotganini, nima banga olib kelishi mumkinligini aytaman. Ortiqcha gaplarsiz — aniq tuzatishlar roʻyxati.')
R('aria-label="Получить аудит бесплатно"', 'aria-label="Auditni bepul olish"')
R('<h3 class="svc__title">Арбитраж трафика</h3>', '<h3 class="svc__title">Trafik arbitraji</h3>')
R('Запуск и масштабирование кампаний в Meta Ads под офферы. Связки, креативы, аудитории — и кабинеты, которые не улетают в бан на третий день.',
  'Meta Ads tizimida offerlar uchun kampaniyalarni ishga tushirish va masshtablash. Bogʻlamalar, kreativlar, auditoriyalar — va uchinchi kuni banga uchmaydigan kabinetlar.')
R('aria-label="Арбитраж трафика — подробнее"', 'aria-label="Trafik arbitraji — batafsil"')

# ---------- доверие ----------
R('<p class="eyebrow eyebrow--dot">Почему мне доверяют</p>', '<p class="eyebrow eyebrow--dot">Nega menga ishonishadi</p>')
R('id="trust-title">Я видел, как это работает <em>с той стороны</em>', 'id="trust-title">Bu tizimni <em>ichkaridan koʻrganman</em>')
R('alt="Аббос в солнцезащитных очках с телефоном"', 'alt="Abbos quyosh koʻzoynagida, qoʻlida telefon"')
R('aria-label="Без паролей. Цена до старта. Диагностика бесплатно."', 'aria-label="Parolsiz. Narx oldindan. Diagnostika bepul."', 2)
R('БЕЗ ПАРОЛЕЙ • ЦЕНА ДО СТАРТА • ДИАГНОСТИКА БЕСПЛАТНО •', 'PAROLSIZ • NARX OLDINDAN • DIAGNOSTIKA BEPUL •', 2)
R('<p>2,5 года я работал в Meta Pro Team<sup><a href="#trust-note" aria-label="Примечание 1">¹</a></sup> — разбирал проблемы рекламодателей, монетизацию и ограничения каждый день. Поэтому я не гадаю, почему вас заблокировали, а знаю, куда смотреть.</p>',
  '<p>2,5 yil Meta Pro Team<sup><a href="#trust-note" aria-label="1-izoh">¹</a></sup> jamoasida ishladim — har kuni reklama beruvchilarning muammolari, monetizatsiya va cheklovlar bilan shugʻullandim. Shuning uchun sizni nega bloklashganini taxmin qilmayman — qayerga qarashni bilaman.</p>')
R('<p>Ещё 4 года я в UI/UX-дизайне — понимаю, как должны выглядеть креатив и страница, чтобы им верили и люди, и модерация.</p>',
  '<p>Yana 4 yildan beri UI/UX-dizayndaman — odamlar ham, moderatsiya ham ishonishi uchun kreativ va sahifa qanday koʻrinishi kerakligini tushunaman.</p>')
R('2,5</span> <small>года</small></b><span>в Meta Pro Team</span>', '2,5</span> <small>yil</small></b><span>Meta Pro Team jamoasida</span>')
R('<span data-count="4">4</span> <small>года</small></b><span>в дизайне и UX</span>', '<span data-count="4">4</span> <small>yil</small></b><span>dizayn va UX sohasida</span>')
R('<span>паролей, которые я прошу у клиентов</span>', '<span>mijozlardan soʻraydigan parollarim</span>')
R('¹ В составе компании-подрядчика Meta. Сейчас работаю независимо и с Meta не связан.', '¹ Meta pudratchi kompaniyasi tarkibida. Hozir mustaqil ishlayman va Meta bilan bogʻliq emasman.')
R('<p class="geo__label">Работаю с бизнесом из</p>', '<p class="geo__label">Bu davlatlardagi biznes bilan ishlayman</p>')
R('>Узбекистан</li>', '>Oʻzbekiston</li>')
R('>Кыргызстан</li>', '>Qirgʻiziston</li>')
R('>Таджикистан</li>', '>Tojikiston</li>')
R('>Азербайджан</li>', '>Ozarbayjon</li>')
R('<p class="geo__more">и удалённо — откуда угодно.</p>', '<p class="geo__more">va masofadan — istalgan joydan.</p>')

# ---------- арбитраж ----------
R('id="arb-title" data-reveal><span>Сливаете</span> <span>бюджет?</span>', 'id="arb-title" data-reveal><span>Byudjet</span> <span>kuyyaptimi?</span>')
R('Арбитраж в Meta Ads — это не «залил и молись».', 'Meta Ads tizimida arbitraj — bu «qoʻydim-u, omadga topshirdim» emas.')
R('Большинство кабинетов умирает не из-за плохого оффера, а из-за ошибок, которые видно с первого взгляда: креатив нарушает правила, домен уже в чёрном списке, прогрев сделан наспех. Я помогу собрать связку, которая живёт дольше и окупается.',
  'Aksariyat kabinetlar yomon offer tufayli emas, birinchi qarashdayoq koʻrinadigan xatolar tufayli «oʻladi»: kreativ qoidalarni buzadi, domen allaqachon qora roʻyxatda, «qizdirish» shoshma-shosharlik bilan qilingan. Uzoqroq yashaydigan va oʻzini oqlaydigan bogʻlamani yigʻishga yordam beraman.')
R('<h3 class="arb__list-title" data-reveal>Что входит</h3>', '<h3 class="arb__list-title" data-reveal>Nimalar kiradi</h3>')
R('>Разбор оффера и подбор подходов</li>', '>Offer tahlili va yondashuvlarni tanlash</li>')
R('>Креативы и тексты, которые проходят модерацию</li>', '>Moderatsiyadan oʻtadigan kreativlar va matnlar</li>')
R('>Структура кампаний и тесты</li>', '>Kampaniyalar tuzilmasi va testlar</li>')
R('>Масштабирование без внезапных банов</li>', '>Kutilmagan banlarsiz masshtablash</li>')
R('>Консультации для соло-арбитражников и команд</li>', '>Yakka arbitrajchilar va jamoalar uchun konsultatsiyalar</li>')
R('<span>Без клоакинга, фарма и «обхода модерации». Работаю в рамках правил — поэтому кабинеты живут.</span>',
  '<span>Kloaking, ferma va «moderatsiyani chetlab oʻtish»siz. Qoidalar doirasida ishlayman — shuning uchun kabinetlar yashaydi.</span>')

# ---------- созвон ----------
R('<!-- 5a. СОЗВОН (Zoom / Discord) — согласовано, бесплатно -->', '<!-- 5a. QOʻNGʻIROQ (Zoom / Discord) -->')
R('<p class="eyebrow eyebrow--light">Созвон</p>', '<p class="eyebrow eyebrow--light">Qoʻngʻiroq</p>')
R('id="call-title">Удобнее голосом? <em>Созвонимся</em>', 'id="call-title">Ovozda qulayroqmi? <em>Gaplashib olamiz</em>')
R('<p class="call__text">Бесплатно, в Zoom или Discord — как вам удобнее. Покажете кабинет через демонстрацию экрана, и разберём ситуацию вместе, в реальном времени. Пароли не нужны.</p>',
  '<p class="call__text">Bepul, Zoom yoki Discord orqali — qaysi biri qulay boʻlsa. Kabinetni ekran namoyishi orqali koʻrsatasiz va vaziyatni birga, real vaqtda tahlil qilamiz. Parollar kerak emas.</p>')
R('<ul class="call__chips" aria-label="Детали созвона">', '<ul class="call__chips" aria-label="Qoʻngʻiroq tafsilotlari">')
R('</svg>Бесплатно</li>', '</svg>Bepul</li>')
R('</svg>Демонстрация экрана</li>', '</svg>Ekran namoyishi</li>')
R('            Договориться о созвоне\n', '            Qoʻngʻiroqni kelishib olish\n')
R('</span>Аббос</span>', '</span>Abbos</span>')
R('<b>Вы</b>', '<b>Siz</b>')
R('</svg>Демонстрация экрана</span>', '</svg>Ekran namoyishi</span>')

# ---------- как я работаю ----------
R('<p class="eyebrow eyebrow--dot">Как я работаю</p>', '<p class="eyebrow eyebrow--dot">Qanday ishlayman</p>')
R('id="how-title">Четыре шага, <em>без сюрпризов</em>', 'id="how-title">Toʻrt qadam, <em>syurprizlarsiz</em>')
for n in ['01','02','03','04']:
    R(f'<span class="step__num">Шаг {n}</span>', f'<span class="step__num">{n}-qadam</span>')
R('<h3 class="step__title">Пишете в Telegram</h3>', '<h3 class="step__title">Telegramga yozasiz</h3>')
R('Коротко: что случилось и скриншот ограничения или ссылка на рекламу.', 'Qisqacha: nima boʻldi va cheklov skrinshoti yoki reklamaga havola.')
R('<h3 class="step__title">Бесплатная диагностика</h3>', '<h3 class="step__title">Bepul diagnostika</h3>')
R('За 15–30 минут говорю, есть ли шансы и что нужно сделать.', '15–30 daqiqada imkoniyat bor-yoʻqligini va nima qilish kerakligini aytaman.')
R('<h3 class="step__title">Фиксируем цену</h3>', '<h3 class="step__title">Narxni kelishamiz</h3>')
R('Вы знаете сумму до начала работы. Без доплат по ходу.', 'Ish boshlanishidan oldin summani bilasiz. Jarayonda qoʻshimcha toʻlovlarsiz.')
R('<h3 class="step__title">Работаю и держу в курсе</h3>', '<h3 class="step__title">Ishlayman va xabardor qilib turaman</h3>')
R('Вы видите каждый шаг, а не ждёте в тишине.', 'Har bir qadamni koʻrib turasiz, jimjitlikda kutib oʻtirmaysiz.')

# ---------- сколько ----------
R('<p class="eyebrow eyebrow--ink">Цены</p>', '<p class="eyebrow eyebrow--ink">Narxlar</p>')
letters_ru = ''.join(f'<span class="l" style="--i:{i}">{c}</span>' for i,c in enumerate('Сколько')) + '<span class="l l--q" style="--i:7">?</span>'
letters_uz = ''.join(f'<span class="l" style="--i:{i}">{c}</span>' for i,c in enumerate('Qancha')) + '<span class="l l--q" style="--i:6">?</span>'
R(f'<span class="sr-only">Сколько?</span><span aria-hidden="true">{letters_ru}</span>', f'<span class="sr-only">Qancha?</span><span aria-hidden="true">{letters_uz}</span>')
R('Честно: зависит от случая. Поэтому цену я называю после диагностики, а не до.', 'Rostini aytsam: holatga bogʻliq. Shuning uchun narxni diagnostikadan keyin aytaman, oldin emas.')
R('<b class="ptag__title">Диагностика — <mark>бесплатно</mark>.</b>', '<b class="ptag__title">Diagnostika — <mark>bepul</mark>.</b>')
R('<span class="ptag__text">Сначала смотрю, потом говорю цену.</span>', '<span class="ptag__text">Avval koʻraman, keyin narxni aytaman.</span>')
R('<b class="ptag__title">Аудит — <mark>бесплатно</mark>.</b>', '<b class="ptag__title">Audit — <mark>bepul</mark>.</b>')
R('<span class="ptag__text">Всегда.</span>', '<span class="ptag__text">Har doim.</span>')
R('<b class="ptag__title">Цена фиксируется до старта.</b>', '<b class="ptag__title">Narx ish boshlanishidan oldin belgilanadi.</b>')
R('<span class="ptag__text">Никаких «а ещё нужно доплатить».</span>', '<span class="ptag__text">Hech qanday «yana toʻlash kerak» boʻlmaydi.</span>')
R('<b class="ptag__title">Нет шансов — скажу прямо.</b>', '<b class="ptag__title">Imkoniyat yoʻq — toʻgʻrisini aytaman.</b>')
R('<span class="ptag__text">И не возьму денег за безнадёжный случай.</span>', '<span class="ptag__text">Umidsiz holat uchun pul olmayman.</span>')
R('<b class="ptag__title">Оплата после <mark>результата</mark>.</b>', '<b class="ptag__title">Toʻlov — <mark>natijadan</mark> keyin.</b>')
R('<span class="ptag__text">Платите, когда доступ восстановлен или ограничение снято.</span>', '<span class="ptag__text">Kirish tiklanganda yoki cheklov olib tashlanganda toʻlaysiz.</span>')
R('Арбитраж, ведение рекламы и доп. услуги — стоимость после короткого созвона.', 'Arbitraj, reklamani yuritish va qoʻshimcha xizmatlar — narxi qisqa qoʻngʻiroqdan keyin.')

# ---------- аудит ----------
R('<p class="eyebrow eyebrow--light">Аудит</p>', '<p class="eyebrow eyebrow--light">Audit</p>')
R('id="audit-title">Бесплатный аудит <em>рекламы или страницы</em>', 'id="audit-title">Reklama yoki sahifaning <em>bepul auditi</em>')
R('Пришлите ссылку — я посмотрю кампании, креативы, настройки Pixel и саму страницу. В течение дня получите разбор: что мешает продажам, что может привести к бану и что исправить в первую очередь.',
  'Havolani yuboring — kampaniyalar, kreativlar, Pixel sozlamalari va sahifaning oʻzini koʻrib chiqaman. Bir kun ichida tahlil olasiz: sotuvga nima xalaqit beryapti, nima banga olib kelishi mumkin va birinchi navbatda nimani tuzatish kerak.')
R('<ul class="checks" data-reveal aria-label="Что проверяю">', '<ul class="checks" data-reveal aria-label="Nimalarni tekshiraman">')
R('</span>Структура кампаний и аудитории</li>', '</span>Kampaniyalar tuzilmasi va auditoriyalar</li>')
R('</span>Креативы и тексты на соответствие правилам</li>', '</span>Kreativlar va matnlarning qoidalarga mosligi</li>')
R('</span>Meta Pixel и события</li>', '</span>Meta Pixel va hodisalar</li>')
R('</span>Бизнес-страница и профиль</li>', '</span>Biznes-sahifa va profil</li>')
R('</span>Риски блокировки</li>', '</span>Bloklanish xavflari</li>')
R('<!-- Web3Forms: ключ публичный по дизайну сервиса -->', '<!-- Web3Forms: kalit xizmat dizayniga koʻra ochiq -->')
R('value="Заявка на бесплатный аудит — сайт Abbos"', 'value="Bepul audit uchun ariza — Abbos sayti (UZ)"')
R('value="Сайт Abbos · Meta Ads"', 'value="Abbos sayti · Meta Ads (UZ)"')
R('<label for="f-name">Имя</label>', '<label for="f-name">Ismingiz</label>')
R('<label for="f-contact">Telegram или телефон</label>', '<label for="f-contact">Telegram yoki telefon</label>')
R('<label for="f-link">Ссылка на страницу или аккаунт</label>', '<label for="f-link">Sahifa yoki akkauntga havola</label>')
R('<legend>Что нужно</legend>', '<legend>Nima kerak</legend>')
for ru, uz, chk in [('Снятие ограничений','Cheklovlarni olib tashlash',''),('Взлом','Buzib kirish',''),('Аудит','Audit',' checked'),('Арбитраж','Arbitraj',''),
                    ('Сайт','Sayt',''),('Ведение страниц','Sahifalarni yuritish',''),('Качество лидов','Lidlar sifati',''),('Другое','Boshqa','')]:
    R(f'<input type="radio" name="need" value="{ru}"{chk}><span>{ru}</span>', f'<input type="radio" name="need" value="{uz}"{chk}><span>{uz}</span>')
R('<label for="f-msg">Комментарий (необязательно)</label>', '<label for="f-msg">Izoh (ixtiyoriy)</label>')
R('<span class="aform__btn-text">Получить аудит бесплатно</span>', '<span class="aform__btn-text">Auditni bepul olish</span>')
R('Я не прошу пароли и коды подтверждения. Никогда.', 'Parollar va tasdiqlash kodlarini soʻramayman. Hech qachon.')
R('<p>Заявка у меня. Напишу вам в Telegram в ближайшее время.</p>', '<p>Ariza menda. Tez orada sizga Telegram orqali yozaman.</p>')
R('<p>Что-то пошло не так. Напишите мне напрямую в Telegram —</p>', '<p>Nimadir xato ketdi. Menga toʻgʻridan-toʻgʻri Telegramga yozing —</p>')

# ---------- под ключ ----------
R('<p class="eyebrow eyebrow--dot">[ 09 ] / Под ключ</p>', '<p class="eyebrow eyebrow--dot">[ 09 ] / Tayyor yechim</p>')
R('id="turnkey-title" data-reveal>Под <span>ключ</span>', 'id="turnkey-title" data-reveal>Tayyor <span>yechim</span>')
R('Реклама работает, только когда ей есть куда вести. Поэтому могу взять на себя всё: от сайта до заявок.', 'Reklama faqat olib boradigan joyi boʻlsagina ishlaydi. Shuning uchun hammasini oʻz zimmamga olishim mumkin: saytdan arizalargacha.')
R('<h3 class="tk__title">Сайты и лендинги</h3>', '<h3 class="tk__title">Saytlar va lendinglar</h3>')
R('Продающие одностраничники и сайты-визитки под рекламу Meta: быстрые на телефоне, с формой заявки и уже настроенным Pixel. Я 4 года в UI/UX — дизайн и вёрстку делаю сам.',
  'Meta reklamasi uchun sotadigan bir sahifali saytlar va vizitka-saytlar: telefonda tez, ariza formasi va sozlangan Pixel bilan. 4 yildan beri UI/UX bilan shugʻullanaman — dizayn va vyorstkani oʻzim qilaman.')
R('>Посмотреть портфолио <svg', '>Portfolioni koʻrish <svg')
R('<h3 class="tk__title">Ведение Instagram и Facebook</h3>', '<h3 class="tk__title">Instagram va Facebookni yuritish</h3>')
R('Оформление профиля, контент-план, визуал постов и сторис, ответы на типовые вопросы. Страница, которая продаёт сама — и которую не стыдно показывать в рекламе.',
  'Profilni bezash, kontent-reja, postlar va storislar vizuali, odatiy savollarga javoblar. Oʻzi sotadigan — va reklamada koʻrsatishdan uyalmaydigan sahifa.')
R('<h3 class="tk__title">Качество лидов</h3>', '<h3 class="tk__title">Lidlar sifati</h3>')
R('Много заявок, а продаж нет? Настрою формы и кампании под вашу нишу: уточняющие вопросы, отсев случайных людей, оптимизация на тех, кто реально покупает. Знаю специфику учебных центров, мебели, стройматериалов и малого бизнеса.',
  'Arizalar koʻp, sotuv yoʻqmi? Formalar va kampaniyalarni nishangizga moslab sozlayman: aniqlashtiruvchi savollar, tasodifiy odamlarni saralash, haqiqatan sotib oladiganlarga optimallashtirish. Oʻquv markazlari, mebel, qurilish materiallari va kichik biznes xususiyatlarini bilaman.')
R('Меньше «просто спросить» — больше тех, кто готов платить.', '«Shunchaki soʻrash» kamroq — toʻlashga tayyorlar koʻproq.')
R('<p class="tk-more__label" data-reveal>Ещё</p>', '<p class="tk-more__label" data-reveal>Yana</p>')
R('</svg>Бизнес-портфолио (Business Manager)</li>', '</svg>Biznes-portfolio (Business Manager)</li>')
R('</svg>Ведение таргета</li>', '</svg>Targetni yuritish</li>')
R('</svg>Каталог товаров</li>', '</svg>Mahsulotlar katalogi</li>')
R('</svg>Проверка креативов до запуска</li>', '</svg>Kreativlarni ishga tushirishdan oldin tekshirish</li>')
R('</svg>Консультации по правилам рекламы</li>', '</svg>Reklama qoidalari boʻyicha konsultatsiyalar</li>')

# ---------- FAQ ----------
R('<p class="eyebrow eyebrow--light">Вопросы</p>', '<p class="eyebrow eyebrow--light">Savollar</p>')
for ru, uz in [
 ('Вы гарантируете разблокировку?', 'Blokdan chiqarishni kafolatlaysizmi?'),
 ('Нет, и никто честный не гарантирует — решение принимает Meta. Я гарантирую, что найду реальную причину, правильно оформлю апелляцию и скажу прямо, если шансов нет.',
  'Yoʻq, va hech bir halol mutaxassis kafolat bermaydi — qarorni Meta qabul qiladi. Men haqiqiy sababni topishni, apellyatsiyani toʻgʻri rasmiylashtirishni va imkoniyat boʻlmasa, toʻgʻrisini aytishni kafolatlayman.'),
 ('Вы работаете в Meta?', 'Siz Metada ishlaysizmi?'),
 ('Нет. Я 2,5 года работал в Meta Pro Team в составе компании-подрядчика. Сейчас я независимый специалист.',
  'Yoʻq. Men 2,5 yil pudratchi kompaniya tarkibida Meta Pro Team jamoasida ishladim. Hozir mustaqil mutaxassisman.'),
 ('Нужен ли вам мой пароль?', 'Sizga parolim kerakmi?'),
 ('Нет. Если нужен доступ — вы добавляете меня в бизнес-портфолио с ограниченной ролью и в любой момент можете убрать. Пароли и коды 2FA не прошу никогда.',
  'Yoʻq. Agar kirish kerak boʻlsa — meni biznes-portfolioga cheklangan rol bilan qoʻshasiz va istalgan vaqtda olib tashlashingiz mumkin. Parollar va 2FA kodlarini hech qachon soʻramayman.'),
 ('Сколько времени занимает разблокировка?', 'Blokdan chiqarish qancha vaqt oladi?'),
 ('От нескольких дней до нескольких недель — зависит от типа ограничения и скорости ответа поддержки. Точнее скажу после диагностики.',
  'Bir necha kundan bir necha haftagacha — cheklov turi va qoʻllab-quvvatlash xizmatining javob tezligiga bogʻliq. Aniqrogʻini diagnostikadan keyin aytaman.'),
 ('Аудит правда бесплатный? В чём подвох?', 'Audit rostdan bepulmi? Qayerda tuzoq bor?'),
 ('Подвоха нет. Аудит — способ показать, как я работаю. Если захотите внедрить правки со мной — договоримся отдельно. Не захотите — разбор останется у вас.',
  'Hech qanday tuzoq yoʻq. Audit — qanday ishlashimni koʻrsatish usuli. Tuzatishlarni men bilan kiritmoqchi boʻlsangiz — alohida kelishamiz. Xohlamasangiz — tahlil sizda qoladi.'),
 ('Работаете только с Узбекистаном?', 'Faqat Oʻzbekiston bilan ishlaysizmi?'),
 ('Нет, работаю удалённо с клиентами из любой страны. Языки: русский, узбекский, английский.', 'Yoʻq, istalgan davlatdagi mijozlar bilan masofadan ishlayman. Tillar: rus, oʻzbek, ingliz.'),
 ('Помогаете с арбитражем по «серым» схемам?', '«Kulrang» sxemalar boʻyicha arbitrajda yordam berasizmi?'),
 ('Нет. Клоакинг и обход модерации — быстрый путь в бан. Я помогаю строить связки, которые живут.', 'Yoʻq. Kloaking va moderatsiyani chetlab oʻtish — banga eng tez yoʻl. Men uzoq yashaydigan bogʻlamalar qurishga yordam beraman.'),
]:
    R(ru, uz)
R('            Написать в Telegram\n', '            Telegramga yozish\n')
R('>Написать в Telegram</a>', '>Telegramga yozish</a>')
R('<span>Написать в Telegram</span>', '<span>Telegramga yozish</span>')

# ---------- контакты ----------
R('<span class="contact__word contact__word--back">Пишите</span>', '<span class="contact__word contact__word--back">Yozing</span>')
R('<span class="contact__word contact__word--front">Пишите</span>', '<span class="contact__word contact__word--front">Yozing</span>')
R('<h2 class="sr-only" id="contact-title">Пишите</h2>', '<h2 class="sr-only" id="contact-title">Yozing</h2>')
R('Опишите ситуацию в двух словах — отвечу и скажу, чем могу помочь.', 'Vaziyatni ikki ogʻiz soʻz bilan yozing — javob beraman va qanday yordam bera olishimni aytaman.')
R('<small>Телефон</small>', '<small>Telefon</small>')

R('src="assets/img/site-preview.webp" width="600" height="3419"', 'src="assets/img/site-preview-uz.webp" width="600" height="3431"')

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
