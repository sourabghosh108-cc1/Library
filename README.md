# Cyan Communications (Django on Vercel)

Xm **Mail** (`/mail/`) and Xm **Network** (`/network/`) in one Django project, deployed using [Vercel’s official Django support](https://vercel.com/docs/frameworks/full-stack/django).

## Project layout

| File / folder | Purpose |
|---------------|---------|
| `manage.py` | Django CLI; Vercel detects this for auto-config |
| `cyancom/wsgi.py` | WSGI entry (`application`) |
| `cyancom/settings.py` | `STATIC_ROOT`, hosts, database |
| `requirements.txt` | Python dependencies |
| `pyproject.toml` | `[tool.vercel]` entrypoint + build script |
| `build.py` | Runs `migrate` during Vercel build |
| `vercel.json` | Optional function limits (minimal config) |

Vercel **automatically** runs `collectstatic` when `STATIC_ROOT` is set. You do **not** need a separate static-build step or legacy `@vercel/static-build`.

## Deploy to Vercel (from GitHub)

1. Push this repo to GitHub ([Library](https://github.com/sourabghosh108-cc1/Library)).
2. Open [vercel.com/new](https://vercel.com/new) → **Import** the repository.
3. **Root directory:** leave as `.` (repository root).
4. **Framework preset:** Vercel should detect **Django** (`manage.py` + `requirements.txt`).
5. **Build command:** `python build.py` (or leave empty; `pyproject.toml` also defines it).
6. **Install command:** default (`pip install -r requirements.txt`).
7. Add environment variables (recommended):

   | Name | Value |
   |------|--------|
   | `DJANGO_SECRET_KEY` | long random string |
   | `DEBUG` | `False` |

8. Click **Deploy**.

After deploy:

- `/` — home (Mail + Network links)
- `/mail/` — email app
- `/network/` — social app
- `/static/` — CSS/JS (CDN)

## Local development

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Optional (matches production tooling):

```bash
npm i -g vercel
vercel dev
```

Requires Vercel CLI **50.38.0+**.

## Database on Vercel

- **Default on Vercel:** SQLite in `/tmp` (resets when the function cold-starts). Fine for demos; not for real users/data.
- **Production:** add Postgres (Neon, Supabase, Vercel Postgres), set `DATABASE_URL` in Vercel env vars. The project already reads `DATABASE_URL` in `cyancom/settings.py`.

Install driver when using Postgres (already in `requirements.txt`):

```bash
pip install psycopg2-binary
```

## Troubleshooting

| Issue | Fix |
|-------|-----|
| 404 on all routes | Ensure repo root contains `manage.py` and `cyancom/wsgi.py` |
| Static files 404 | Confirm `STATIC_ROOT = BASE_DIR / "staticfiles"` and redeploy (Vercel runs `collectstatic`) |
| CSRF / login fails on Vercel | Set `DJANGO_SECRET_KEY`; redeploy so `VERCEL_URL` is in `CSRF_TRUSTED_ORIGINS` |
| Old `builds` / `routes` in `vercel.json` | Remove them; use modern Django detection (this repo is already updated) |

## Docs

- [Deploy a Django app on Vercel](https://vercel.com/docs/frameworks/full-stack/django)
- [Python runtime](https://vercel.com/docs/functions/runtimes/python)
