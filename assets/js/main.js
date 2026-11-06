/* Abbos — Meta Ads. Анимации и мелкая логика. Vanilla JS, без зависимостей. */
(() => {
  const root = document.documentElement;
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const finePointer = matchMedia('(hover: hover) and (pointer: fine)').matches;

  /* ==========================================================
     НАСТРОЙКИ — контакты и пиксель меняются ТОЛЬКО здесь.
     Все ссылки с data-link="…" на странице подставятся автоматически.
     ========================================================== */
  const CONFIG = {
    telegram:  'https://t.me/bossja999',      // новый юзернейм: 'https://t.me/НОВЫЙ'
    phone:     '+998943717923',               // для ссылки tel:
    phoneLabel:'+998 94 371-79-23',           // как номер показан на сайте
    instagram: '',                            // 'https://instagram.com/…'
    facebook:  '',                            // 'https://facebook.com/…'
    pixelId:   '798392145862804',             // Meta Pixel
  };

  const handle = url => '@' + url.replace(/[?#].*$/, '').split('/').filter(Boolean).pop();
  const labelFor = (key, v) =>
    key === 'phone' ? (CONFIG.phoneLabel || v) :
    key === 'facebook' ? v.replace(/^https?:\/\/(www\.|m\.)?/, '').replace(/\/$/, '') :
    handle(v);
  document.querySelectorAll('[data-link]').forEach(a => {
    const key = a.dataset.link, v = CONFIG[key];
    if (!v) return;
    a.href = key === 'phone' ? 'tel:' + v.replace(/[^+\d]/g, '') : v;
    const lab = a.querySelector('[data-link-label]');
    if (lab) lab.textContent = labelFor(key, v);
  });
  /* Instagram / Facebook появятся, как только в CONFIG будет ссылка */
  document.querySelectorAll('[data-optional]').forEach(el => { if (!CONFIG[el.dataset.optional]) el.hidden = true; });

  /* ---------- Meta Pixel: PageView, Contact (клик), Lead (заявка) ---------- */
  if (CONFIG.pixelId) {
    !function (f, b, e, v, n, t, s) {
      if (f.fbq) return; n = f.fbq = function () { n.callMethod ? n.callMethod.apply(n, arguments) : n.queue.push(arguments); };
      if (!f._fbq) f._fbq = n; n.push = n; n.loaded = !0; n.version = '2.0'; n.queue = [];
      t = b.createElement(e); t.async = !0; t.src = v; s = b.getElementsByTagName(e)[0]; s.parentNode.insertBefore(t, s);
    }(window, document, 'script', 'https://connect.facebook.net/en_US/fbevents.js');
    fbq('init', CONFIG.pixelId);
    fbq('track', 'PageView');
  }
  const track = ev => { if (window.fbq) window.fbq('track', ev); };
  document.addEventListener('click', e => { if (e.target.closest('[data-event="Contact"]')) track('Contact'); });

  /* ---------- форма аудита → Web3Forms ---------- */
  const form = document.getElementById('audit-form');
  if (form) {
    const status = form.querySelector('[data-form-status]');
    const btn = form.querySelector('[type="submit"]');
    form.querySelectorAll('.field input, .field textarea').forEach(el =>
      el.addEventListener('input', () => el.closest('.field').classList.remove('is-error')));

    form.addEventListener('submit', async e => {
      e.preventDefault();
      let firstBad = null;
      form.querySelectorAll('[required]').forEach(el => {
        const bad = !el.value.trim();
        el.closest('.field').classList.toggle('is-error', bad);
        el.setAttribute('aria-invalid', bad ? 'true' : 'false');
        if (bad && !firstBad) firstBad = el;
      });
      if (firstBad) { firstBad.focus(); status.textContent = 'Заполните отмеченные поля.'; return; }
      if (form.botcheck && form.botcheck.checked) return;

      form.classList.remove('is-failed');
      form.classList.add('is-sending'); btn.disabled = true;
      try {
        const res = await fetch(form.action, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
          body: JSON.stringify(Object.fromEntries(new FormData(form))),
        });
        const json = await res.json().catch(() => ({}));
        if (!res.ok || !json.success) throw new Error(json.message || res.status);
        form.classList.add('is-done');
        status.textContent = 'Заявка у меня. Напишу вам в Telegram в ближайшее время.';
        track('Lead');
      } catch (err) {
        form.classList.add('is-failed');
        status.textContent = 'Что-то пошло не так. Напишите мне напрямую в Telegram.';
      } finally {
        form.classList.remove('is-sending'); btn.disabled = false;
      }
    });
  }

  /* ---------- шапка: стекло после прокрутки ---------- */
  const head = document.querySelector('.site-head');
  const onScrollHead = () => head && head.classList.toggle('is-scrolled', scrollY > 24);
  onScrollHead();
  addEventListener('scroll', onScrollHead, { passive: true });

  /* ---------- появление при прокрутке ---------- */
  const revealEls = document.querySelectorAll('[data-reveal]');
  if (reduce || !('IntersectionObserver' in window)) {
    revealEls.forEach(el => el.classList.add('is-in'));
  } else {
    const io = new IntersectionObserver(entries => {
      entries.forEach(e => {
        if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -12% 0px' });
    revealEls.forEach(el => io.observe(el));
  }

  /* SMIL-анимации (воронка): играют только на экране; при reduced motion — стоп-кадр */
  document.querySelectorAll('svg[data-smil]').forEach(svg => {
    if (!svg.pauseAnimations) return;
    if (reduce) { svg.setCurrentTime(1.6); svg.pauseAnimations(); return; }
    svg.pauseAnimations();
    new IntersectionObserver(([e]) => e.isIntersecting ? svg.unpauseAnimations() : svg.pauseAnimations()).observe(svg);
  });

  if (reduce) {
    document.querySelectorAll('[data-progress]').forEach(el => el.style.setProperty('--prog', '1'));
    document.querySelectorAll('.step').forEach(el => el.classList.add('is-lit'));
    return;
  }

  /* ---------- hero: параллакс от мыши и прокрутки ---------- */
  const hero = document.querySelector('.hero-zone');
  const target = { x: 0, y: 0, mx: -999, my: -999 };
  const cur = { x: 0, y: 0, mx: -999, my: -999 };
  let heroVisible = true;

  if (hero) {
    new IntersectionObserver(([e]) => { heroVisible = e.isIntersecting; }).observe(hero);
    if (finePointer) {
      hero.addEventListener('pointermove', e => {
        const r = hero.getBoundingClientRect();
        target.x = ((e.clientX - r.left) / r.width - 0.5) * 2;
        target.y = ((e.clientY - r.top) / r.height - 0.5) * 2;
        target.mx = e.clientX - r.left;
        target.my = e.clientY - r.top;
        if (cur.mx < -900) { cur.mx = target.mx; cur.my = target.my; }
      });
      hero.addEventListener('pointerleave', () => { target.x = 0; target.y = 0; });
    }
  }

  /* ---------- бегущие полосы: постоянный ход + ускорение и смена направления от скролла ---------- */
  const tracks = [...document.querySelectorAll('.band__track')].map(el => ({
    el, x: 0, w: 0, speed: parseFloat(el.dataset.speed || '1'),
  }));
  const measure = () => tracks.forEach(t => { t.w = t.el.scrollWidth / 2; });
  measure();
  addEventListener('resize', measure);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(measure);

  let lastY = scrollY, vel = 0, dir = 1, last = performance.now();

  /* таймлайн «Как я работаю»: --prog 0…1 и подсветка шагов */
  const progs = [...document.querySelectorAll('[data-progress]')].map(el => {
    const list = el.querySelector('.steps__list');
    return { el, list, steps: [...el.querySelectorAll('.step')], visible: false, offset: 0, span: 1 };
  });
  const measureProg = () => progs.forEach(pr => {
    const lr = pr.list.getBoundingClientRect(), er = pr.el.getBoundingClientRect();
    pr.offset = lr.top - er.top;              // начало списка внутри секции
    pr.span = Math.max(1, lr.height * 0.9);   // путь заполнения
  });
  measureProg(); addEventListener('resize', measureProg);
  const prIO = new IntersectionObserver(entries => entries.forEach(e => {
    const pr = progs.find(x => x.el === e.target); if (pr) pr.visible = e.isIntersecting;
  }));
  progs.forEach(pr => prIO.observe(pr.el));

  /* секции с параллаксом от прокрутки (--sy) */
  const scrolly = [...document.querySelectorAll('[data-scrolly]')].map(el => ({ el, visible: false }));
  const syIO = new IntersectionObserver(entries => entries.forEach(e => {
    const s = scrolly.find(x => x.el === e.target); if (s) s.visible = e.isIntersecting;
  }));
  scrolly.forEach(s => syIO.observe(s.el));

  /* печать-сюзане: медленно крутится, от прокрутки — быстрее */
  const spinners = [...document.querySelectorAll('[data-spin] .seal__ring')];
  let spin = 0;

  function frame(now) {
    const dt = Math.min(64, now - last) / 1000; last = now;
    const y = scrollY, dy = y - lastY; lastY = y;
    if (dy !== 0) dir = dy > 0 ? 1 : -1;
    vel += ((dt ? Math.abs(dy) / dt : 0) - vel) * 0.12;          // сглаженная скорость, px/s
    const boost = Math.min(vel * 0.35, 900);

    for (const t of tracks) {
      if (!t.w) continue;
      t.x -= t.speed * dir * (70 + boost) * dt;
      t.x = ((t.x % t.w) + t.w) % t.w - t.w;                        // держим в (−w, 0]
      t.el.style.transform = `translate3d(${t.x.toFixed(2)}px,0,0)`;
    }

    for (const pr of progs) {
      if (!pr.visible) continue;
      const r = pr.el.getBoundingClientRect();
      const p = Math.max(0, Math.min(1, (innerHeight * 0.62 - (r.top + pr.offset)) / (pr.span || 1)));
      pr.el.style.setProperty('--prog', p.toFixed(4));
      pr.steps.forEach((st, i) => st.classList.toggle('is-lit', p >= (i + 0.35) / pr.steps.length));
    }

    for (const sec of scrolly) {
      if (!sec.visible) continue;
      const r = sec.el.getBoundingClientRect();
      const sy = ((r.top + r.height / 2) - innerHeight / 2) / innerHeight;
      sec.el.style.setProperty('--sy', Math.max(-1, Math.min(1, sy)).toFixed(4));
    }

    if (spinners.length) {
      spin = (spin + dir * (16 + Math.min(vel * 0.3, 720)) * dt) % 360;
      for (const el of spinners) el.style.transform = `rotate(${spin.toFixed(2)}deg)`;
    }

    if (hero && heroVisible) {
      cur.x += (target.x - cur.x) * 0.075;
      cur.y += (target.y - cur.y) * 0.075;
      cur.mx += (target.mx - cur.mx) * 0.12;
      cur.my += (target.my - cur.my) * 0.12;
      const sp = Math.max(0, Math.min(1, y / (hero.offsetHeight || 1)));
      const s = hero.style;
      s.setProperty('--px', cur.x.toFixed(4));
      s.setProperty('--py', cur.y.toFixed(4));
      s.setProperty('--sp', sp.toFixed(4));
      s.setProperty('--mx', cur.mx.toFixed(1));
      s.setProperty('--my', cur.my.toFixed(1));
    }
    requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);

  /* ---------- счётчики фактов ---------- */
  const fmt = (v, d) => v.toFixed(d).replace('.', ',');
  const countIO = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (!e.isIntersecting) return;
      countIO.unobserve(e.target);
      const el = e.target, to = parseFloat(el.dataset.count), from = parseFloat(el.dataset.from || '0');
      const d = parseInt(el.dataset.decimals || '0', 10), dur = 1500, t0 = performance.now();
      const tick = now => {
        const k = Math.min(1, (now - t0) / dur), ease = 1 - Math.pow(1 - k, 3);
        el.textContent = fmt(from + (to - from) * ease, d);
        if (k < 1) requestAnimationFrame(tick);
      };
      el.textContent = fmt(from, d);
      requestAnimationFrame(tick);
    });
  }, { threshold: 0.6 });
  document.querySelectorAll('[data-count]').forEach(el => countIO.observe(el));

  /* ---------- таймер «идущего» созвона ---------- */
  document.querySelectorAll('[data-timer]').forEach(el => {
    let sec = 0, id = null;
    new IntersectionObserver(([e]) => {
      if (e.isIntersecting && !id) {
        id = setInterval(() => {
          sec++;
          el.textContent = String(Math.floor(sec / 60)).padStart(2, '0') + ':' + String(sec % 60).padStart(2, '0');
        }, 1000);
      } else if (!e.isIntersecting && id) { clearInterval(id); id = null; }
    }).observe(el);
  });

  if (!finePointer) return;

  /* ---------- карточки: 3D-наклон за курсором ---------- */
  document.querySelectorAll('[data-tilt]').forEach(card => {
    card.addEventListener('pointermove', e => {
      const r = card.getBoundingClientRect();
      const px = (e.clientX - r.left) / r.width, py = (e.clientY - r.top) / r.height;
      card.classList.add('is-tilting');
      card.style.setProperty('--rx', ((0.5 - py) * 9).toFixed(2) + 'deg');
      card.style.setProperty('--ry', ((px - 0.5) * 11).toFixed(2) + 'deg');
      card.style.setProperty('--gx', (px * 100).toFixed(1) + '%');
      card.style.setProperty('--gy', (py * 100).toFixed(1) + '%');
    });
    card.addEventListener('pointerleave', () => {
      card.classList.remove('is-tilting');
      card.style.setProperty('--rx', '0deg');
      card.style.setProperty('--ry', '0deg');
    });
  });

  /* ---------- «магнитная» кнопка ---------- */
  document.querySelectorAll('[data-magnet]').forEach(btn => {
    btn.addEventListener('pointermove', e => {
      const r = btn.getBoundingClientRect();
      const dx = e.clientX - (r.left + r.width / 2), dy = e.clientY - (r.top + r.height / 2);
      btn.style.transform = `translate(${(dx * 0.22).toFixed(1)}px, ${(dy * 0.35).toFixed(1)}px)`;
    });
    btn.addEventListener('pointerleave', () => { btn.style.transform = ''; });
  });
})();
