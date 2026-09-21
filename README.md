<h1 align="center">
  <picture>
    <source media="(max-width: 700px)" srcset="assets/banner-compact.png">
    <img src="assets/banner.png" width="100%"
       alt="Plate: engraved portrait of Amos Mwangi beside the line Backend and Platform Engineer, Nairobi UTC+3, with a health-check terminal readout and the figures 12.6M records served, 3,820 contributions in 2026, 60 percent latency cut after a Go rewrite.">
  </picture>
</h1>

I build the part of a product that has to be right: the API, the data model, the queue, and the deploy path that puts them in front of users. Mostly **Python** and **Go**, on **PostgreSQL**, under real load. Remote, from Nairobi.

## What I am doing now

- Backend work on data-heavy platforms: ingestion pipelines, query paths that stay fast as tables grow past eight figures, and the migrations that get there without downtime.
- Moving hot paths off Python and into Go services where the latency budget is tight.
- Running my own small production systems end to end, including point-of-sale and marketplace software in daily use by Kenyan businesses.

## Selected work

| System | What it does | The hard part | Stack |
|---|---|---|---|
| [**Arizona Sunshine Portal**](https://github.com/Cooperation-org/Az-Sunshine) | Public portal over Arizona campaign finance filings | 12.6M records kept queryable and correct through repeated bulk ingests | Django, PostgreSQL, React |
| **GoVerde Errands Marketplace** | Two-sided errands marketplace with live chat and escrow | WebSocket sessions, escrow state machine, role-based access across three user types | FastAPI, PostgreSQL, TypeScript |
| **Tensor Marketplace** | Digital goods marketplace with paid download delivery | Stripe webhooks reconciled against signed, expiring file URLs | Django REST Framework, Next.js |
| [**Classy Carry POS**](https://github.com/Emos21/classycarry-erp) | Point of sale and stock control for a leather goods retailer | M-Pesa STK push, offline-tolerant SQLite, staff role gating | PHP 8, SQLite, M-Pesa Daraja |
| **Amber Quill** | Age-restricted liquor storefront | Two payment processors, age gate, per-region delivery rules | React, Node.js |

Tools I wrote to think about systems rather than to ship features: [**chronos**](https://github.com/Emos21/chronos), boolean algebra over cron schedules, in Dart. [**subnetics**](https://github.com/Emos21/subnetics), a CIDR buddy allocator with a live fragmentation treemap. [**MpesaGuard**](https://github.com/Emos21/MpesaGuard), mobile money transaction screening.

## Stack

![Python](https://img.shields.io/badge/Python-12110F?style=flat-square&logo=python&logoColor=F5F2EA) ![Go](https://img.shields.io/badge/Go-12110F?style=flat-square&logo=go&logoColor=F5F2EA) ![Django](https://img.shields.io/badge/Django-12110F?style=flat-square&logo=django&logoColor=F5F2EA) ![FastAPI](https://img.shields.io/badge/FastAPI-12110F?style=flat-square&logo=fastapi&logoColor=F5F2EA) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-12110F?style=flat-square&logo=postgresql&logoColor=F5F2EA) ![Docker](https://img.shields.io/badge/Docker-12110F?style=flat-square&logo=docker&logoColor=F5F2EA)

| Layer | What I reach for |
|---|---|
| **Languages** | Python, Go, TypeScript, SQL, Dart |
| **Backend** | Django, Django REST Framework, FastAPI, Celery, REST and GraphQL |
| **Data** | PostgreSQL, Redis, MongoDB, SQLite |
| **Infrastructure** | Docker, Linux, Nginx, GitHub Actions, VPS and cPanel deploys |
| **Frontend, when I own the whole thing** | React, Next.js, Vue, Tailwind |

## By the numbers

- **12.6M** records in one Django and PostgreSQL deployment, still serving reads in milliseconds.
- **60%** of request latency removed by moving the hottest endpoints to Go.
- **3,820** contributions so far in 2026, 3,142 of them in private repositories.
- **21** public repositories across Python, Go, Dart, PHP and TypeScript.

## How I work

- Tests before "done". A feature without a failing-then-passing test is a rumour.
- Migrations are reversible, deploys are boring, and logs say what happened.
- I would rather delete a service than add one.

## Contact

- **Email:** emosmwangi@gmail.com
- **Portfolio:** [amosmwangi.com](https://amosmwangi.com)
- **LinkedIn:** [amos-mwangi-backend-developer](https://www.linkedin.com/in/amos-mwangi-backend-developer)

Open to remote backend and platform engineering roles. Nairobi, UTC+3, which overlaps a full European day and a US morning.

<details>
<summary>Fig. 2: the same photograph, drawn in 60 columns of text</summary>

```

                            ...
                      .=*#%@@@@@@@%*-..
                   -#@@@@@@@@@@@@@@@@@@*-
                :*@@@@@@@@@@@@@@@@@@@@@@@@*.
              -#@@@@@%%%%%#####%%%%@@@@@@@@@*:
             *@@@%################%%%%%%%@@@@@*
            *@@@##%%%%####*******#####%%##%@@@@*
           +@@@##%%##**+++++++++++****###%##%@@@=
          +@@@%##%#*+=--:---====----==+*##%%#%@@@.
         .@@@%####**+=----------::::--=+*##%%#@@@#
         +@@%#####**++====-----:--===++**##%%#%@@@.
         %@%#######**++=--::::::---=+++**######%%@-
        .%%#***#%#**+++=--:..:::::-==+**##%%#*##%@+
        :@%#***#+=---==----:::.::----==--=+*#***#@*
        :@%#+*+++***###*+=-----==--=+******++++*#@+
         *@#***+#@#+##==********##*+--%%#*%#*++*@@:
      .+*+@###**+**==+=+*##*++++*#%#+=++=+#####*@*-+:
      =@###*##**++==+****+++*++*****##+++++*###*##%@#
      -@*=**#**+++++++=--+**+==+***+=+****++*##**+#@:
       *%*#+***+===---:-====-...=++======++*******%=
        *@@*****=-:::::==-+++--=**-=+=-:-=+*****@%-
         *%%****+=-:::--=+*##*+#%##*+=---=++***#%:
         :#%##***++=--+#%%%#####%%@@%#*++++***##=
          ..+#*****++%@@#*=--====+*#%@@%*****#=
             +#******#%@#*+++++++**#%@%%*####+
              +#*****==***+=-----=+**#***###=
               ******#+==++++++++*++++#####*
               +#######+=--------===+*@####*
               =%%@@@@@%+==-----===*#@@@@%%#.
               =%#%@@@@@@%**#**#%%%@@@@@@%%#%+
              -%####%@@@@@@@@@@@@@@@@@@@%%%%@@+
              %@%##**%@@@@@@@@@@@@@@@@@@%##%@@@-
             -@@@%*+++++*######%%%%%###**#%@@@@@:
            +@@@@@@%*=-==========++++=++#@@@@@@@%.
          .=@@@@@@@@@%*=---------=====*%@@@@@@@@@%-.
     .:=*%@@@@@@@@@@@@@@%*=-:::----+#@@@@@@@@@@@@@@@%*-.
.:=*%@@@@@@@@@@@@@@@@@@@@@@%*=--=*%@@@@@@@@@@@@@@@@@@@@@%+-.
```

Rendered from the source photograph by [`scripts/ascii.py`](scripts/ascii.py). The plate at the top of the page is Floyd-Steinberg dithering from [`scripts/portrait.py`](scripts/portrait.py), set in [`scripts/banner.html`](scripts/banner.html) and shot with headless Chrome. Rebuild both with `scripts/build.sh`.
</details>
