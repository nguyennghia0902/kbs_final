# 🎓 KBS Adaptive Exam System

Hệ thống sinh đề thi trắc nghiệm & chấm điểm tự động theo năng lực (CAT).

## 👥 Thông tin nhóm thực hiện

Dự án là sản phẩm đồ án của **Học viên cao học K36**, Ngành **Khoa học Máy tính** - **Trường Đại học Sư phạm TP.HCM**.

### Thành viên
- **Nguyễn Thị Mỹ Hạnh** – `KHMT836007`
- **Bùi Nguyên Nghĩa** – `KHMT836021`
- **Nguyễn Đức Thành** – `KHMT836031`

### Giảng viên hướng dẫn
- **PGS. TS. Nguyễn Đình Hiển**

## Stack
| Thành phần | Công nghệ |
|---|---|
| UI | Streamlit (`localhost:8501`) |
| API | FastAPI + Uvicorn (`localhost:8000`) |
| Graph DB | Neo4j (`localhost:7474`) |
| DBeaver | PostgreSQL (`localhost:5432`) |
| LLM Feedback | Groq API (llama-3.1-8b-instant) |

---

## 🚀 Setup nhanh (3 bước)

### Bước 1 – Lấy Groq API Key (miễn phí)
1. Truy cập **https://console.groq.com/keys**
2. Đăng nhập (Google/GitHub) → click **Create API Key**
3. Copy key dạng `gsk_xxxx...`
4. Điền vào file `.env`:
   ```
   GROQ_API_KEY=gsk_xxxx...
   ```
   > ⚠️ **KHÔNG** commit file `.env` lên git (đã có `.gitignore`)

### Bước 2 – Chạy toàn bộ hệ thống
```bash
docker-compose up -d
```
Đợi khoảng **60-90 giây** để init container hoàn tất, sau đó mở:
- **Streamlit UI**: http://localhost:8501
- **API Docs**: http://localhost:8000/docs
- **Neo4j Browser**: http://localhost:7474

---

## 📁 Cấu trúc thư mục
```
kbs_project/
├── docker-compose.yml
├── .env                          ← Điền GROQ_API_KEY vào đây
├── .env.example                  ← Template
├── data/
│   └── questions_week3_fixed_complete.xlsx  
├── backend/
│   ├── requirements.txt
│   ├── Dockerfile.init
│   ├── Dockerfile.api
│   └── scripts/
│       ├── run_init.py           ← Tự động chạy khi start
│       ├── db_config.py          ← Cấu hình DB từ env vars
│       ├── bootstrap_schema_postgres.py
│       ├── Script-seed-data.sql
│       ├── etl_to_postgresql.py
│       ├── postgres_to_neo4j.py
│       ├── load_rules.py
│       ├── rules.csv
│       └── cat_api_rule_based_neo4j.py  ← API chính
└── streamlit_app/
    ├── Dockerfile
    ├── requirements.txt
    ├── streamlit_app.py
    ├── st_home.py
    └── st_gentest_app.py
```

---

## ⚙️ Các script đã được patch
Các file backend (`bootstrap_schema_postgres.py`, `etl_to_postgresql.py`,
`postgres_to_neo4j.py`, `load_rules.py`, `cat_api_rule_based_neo4j.py`) cần
được **patch 2 thay đổi nhỏ** để đọc host từ environment variable Docker:

```python
# Thêm dòng này vào đầu mỗi file
from db_config import PG_CONFIG, NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD, GROQ_API_KEY

# Sau đó thay thế block config cứng:
# TRƯỚC:
DB_CONFIG = {"host": "localhost", ...}
# SAU:
DB_CONFIG = PG_CONFIG
```
> File `db_config.py` tự động đọc từ env vars, khi chạy local dùng `localhost`,
> khi chạy trong Docker dùng tên service (`postgres`, `neo4j`).

---

## 🔑 Lấy API Key LLM (Groq) an toàn

| Cách | Mô tả |
|---|---|
| **Groq Console** (khuyên dùng) | https://console.groq.com/keys – Free tier rộng rãi, không cần thẻ |
| **Biến môi trường** | Lưu vào `.env`, không hardcode trong code |
| **Docker secret** | Dùng `docker secret` cho production |

> Model mặc định: `llama-3.1-8b-instant` (nhanh, miễn phí). Có thể đổi sang
> `llama-3.3-70b-versatile` trong `cat_api_rule_based_neo4j.py` để chính xác hơn.

---

## 🛑 Dừng hệ thống
```bash
docker-compose down          # Dừng, giữ data
docker-compose down -v       # Dừng + xóa data (reset hoàn toàn)
```
