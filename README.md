# StudyMate Resilient Vercel Serverless API Engine

Production-ready, high-availability serverless API replicating the StudyMate API suite (`/api/video/<id>`, `/api/lesson/<id>`, `/api/classroom/<id>`, `/api/batches`).

Designed to deploy to **Vercel** with zero-configuration, providing **zero-downtime failover** through direct authenticated Khan Global Studies (KGS) student sessions.

---

## 🚀 Features

- **Exact Contract Matching:** Outputs JSON matching `study-mate.in/api/video/{video_id}`:
  ```json
  {
    "hd_video_url": "https://www.youtube.com/embed/...",
    "video_url": "https://kgs-v2.akamaized.net/...",
    "pdfs": [
      {
        "title": "Lecture PDF",
        "url": "https://kgs-v2.akamaized.net/...pdf"
      }
    ]
  }
  ```
- **Live KGS Session Auth:** Automatically authenticates with KGS credentials and generates fresh Bearer tokens for live student access.
- **Multi-Tier Failover:**
  1. *Direct KGS API* (Active live session)
  2. *StudyMate Live Proxy*
  3. *In-Memory & Bundled Offline Fallbacks*
- **Full CORS Support:** Ready for web apps, Flutter/React Native, or Telegram bots.

---

## 📁 Project Structure

```
studymate-api-vercel/
├── api/
│   └── index.py             # Serverless Flask application entrypoint
├── data/
│   └── batches_fallback.json # Pre-bundled 1089 batch dataset
├── vercel.json              # Vercel serverless rewrite rules
├── requirements.txt         # Minimal Python dependencies for Vercel
├── run.py                   # Local development server
├── test_api.py              # Automated test suite
├── .env                     # Local environment variables
└── README.md
```

---

## 🛠️ Deploy to Vercel (1-Click)

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/dk9624561-cpu/dhiraj-api)

1. Click the button above or open [Vercel Dashboard](https://vercel.com).
2. Click **"Add New Project"** ➔ Import `dk9624561-cpu/dhiraj-api`.
3. (Optional) Set Environment Variables:
   - `KGS_PHONE` = `7544898925`
   - `KGS_PASSWORD` = `75448989`
   - `KGS_TOKEN` = `147419804|EOm8dRWhsJkHRS4Oatok5NBYIRwug62TpTx2DOIS14fefc33`
4. Click **Deploy**.


---

## 📡 API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | Web dashboard & interactive testing interface |
| `GET` | `/health` | Health & monitoring status |
| `GET` | `/api/video/<video_id>` | Stream & PDF links for a lecture |
| `GET` | `/api/lesson/<topic_id>` | Videos & notes list for a topic |
| `GET` | `/api/classroom/<course_id>`| Classroom topics for a batch |
| `GET` | `/api/batches` | List of 1089+ KGS course batches |

---

## 💻 Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run automated tests
python test_api.py

# Start local server
python run.py
```
Server runs at `http://localhost:5000`.
