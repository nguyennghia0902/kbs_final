<div align="center">

# 🎓 KBS - Adaptive Competency Testing System (ACTS)


**HỆ THỐNG KIỂM TRA TRẮC NGHIỆM THÍCH ỨNG THEO NĂNG LỰC**

**Môn Python và Cấu trúc dữ liệu và giải thuật**

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111-green?logo=fastapi)](https://fastapi.tiangolo.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.35-red?logo=streamlit)](https://streamlit.io)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue?logo=postgresql)](https://postgresql.org)
[![Neo4j](https://img.shields.io/badge/Neo4j-5.x-green?logo=neo4j)](https://neo4j.com)
[![Docker](https://img.shields.io/badge/Docker-Compose-blue?logo=docker)](https://docker.com)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

</div>

---


Dự án là sản phẩm đồ án của **nhóm học viên cao học K36**, Ngành **Khoa học Máy tính** — **Trường Đại học Sư phạm TP.HCM**

| Họ và tên | MSHV | Vai trò |
|---|---|---|
| **Nguyễn Thị Mỹ Hạnh** | KHMT836007 | Thành viên |
| **Bùi Nguyên Nghĩa** | KHMT836021 | Thành viên |
| **Nguyễn Đức Thành** | KHMT836031 | Thành viên |

> 🎓 **Giảng viên hướng dẫn**: PGS.TS. Nguyễn Đình Hiển

---

## 1. Tổng quan hệ thống

Hệ thống triển khai mô hình **Computerized Adaptive Testing (CAT)** nhằm sinh đề thi thích nghi theo năng lực người học. Thay vì một bài kiểm tra cố định, hệ thống liên tục ước lượng năng lực học viên (θ – theta) qua từng câu trả lời và chọn câu hỏi tiếp theo phù hợp nhất.

### Kiến trúc Hybrid Database

```
┌─────────────────────────────────────────────────────────┐
│                    Streamlit UI (:8501)                  │
└─────────────────────┬───────────────────────────────────┘
                      │ HTTP REST
┌─────────────────────▼───────────────────────────────────┐
│                FastAPI + Uvicorn (:8000)                 │
│  ┌─────────────┐  ┌──────────────┐  ┌───────────────┐  │
│  │  CAT Engine │  │ Rule Engine  │  │  LLM Feedback │  │
│  │    (IRT)    │  │ (Neo4j Rules)│  │  (Groq API)   │  │
│  └──────┬──────┘  └──────┬───────┘  └───────────────┘  │
└─────────┼────────────────┼─────────────────────────────-┘
          │                │
┌─────────▼──────┐  ┌──────▼──────────────────────────────┐
│  PostgreSQL    │  │              Neo4j                   │
│  (:5432)       │  │  (:7474 Browser / :7687 Bolt)        │
│                │  │                                      │
│  - questions   │  │  (Subject)──[:HAS]──(Topic)          │
│  - students    │  │  (Question)──[:RELATED_TO]──(Topic)  │
│  - attempts    │  │  (Student)──[:MASTERY]──(Topic)      │
│  - answers     │  │  (Rule)──[:APPLIES_TO]──(Topic)      │
│  - ...         │  │  ...                                 │
└────────────────┘  └──────────────────────────────────────┘
```

Hệ thống kết hợp 3 phương pháp:

- **IRT (Item Response Theory)**: ước lượng năng lực θ qua mô hình logistic 1-3 tham số
- **Rule-based Reasoning**: cập nhật năng lực theo luật suy luận lưu trong Neo4j
- **Knowledge Graph**: biểu diễn quan hệ tri thức giữa Topic, Question, Student

### Stack công nghệ

| Thành phần | Công nghệ | Cổng |
|---|---|---|
| UI | Streamlit | `localhost:8501` |
| API | FastAPI + Uvicorn | `localhost:8000` |
| Graph DB | Neo4j | `localhost:7474` (Browser) / `7687` (Bolt) |
| Relational DB | PostgreSQL | `localhost:5432` |
| LLM Feedback | Groq API (`llama-3.1-8b-instant`) | — |
| Container | Docker + Docker Compose | — |

---

## 2. Tính năng chính

- ✅ **Sinh đề thích nghi (CAT)**: câu hỏi được chọn dựa trên năng lực θ hiện tại của học viên
- ✅ **Chấm điểm tự động**: kết quả và phản hồi chi tiết sau mỗi bài thi
- ✅ **Phản hồi LLM**: giải thích đáp án bằng ngôn ngữ tự nhiên qua Groq API
- ✅ **Knowledge Graph**: trực quan hóa mối quan hệ tri thức trên Neo4j Browser
- ✅ **Rule Engine**: các luật suy luận cập nhật mastery score tự động
- ✅ **Quản lý sinh viên**: tra cứu, theo dõi lịch sử thi và tiến trình năng lực
- ✅ **One-command deploy**: toàn bộ hệ thống khởi động bằng một lệnh Docker

---

## 3. Yêu cầu hệ thống

### Phần mềm bắt buộc

| Phần mềm | Phiên bản | Ghi chú |
|---|---|---|
| **Docker Desktop** | 24.x+ | Bao gồm Docker Compose v2 |
| **Git** | Bất kỳ | Để clone repository |

> ⚠️ **Không cần** cài Python, PostgreSQL, hay Neo4j riêng — tất cả chạy trong container.



### Cổng sử dụng

| Dịch vụ | Cổng |
|---|---|
| Streamlit UI | `8501` |
| FastAPI | `8000` |
| PostgreSQL | `5432` |
| Neo4j Browser | `7474` |
| Neo4j Bolt | `7687` |

> Đảm bảo các cổng trên chưa bị chiếm dụng trước khi chạy.

---

## 4. Cài đặt và chạy

### Bước 1 — Lấy Groq API Key (miễn phí, không cần thẻ)

1. Truy cập **https://console.groq.com/keys**
2. Đăng nhập bằng Google hoặc GitHub
3. Click **"Create API Key"** → copy key dạng `gsk_xxxx...`

### Bước 2 — Clone và cấu hình

```bash
git clone https://github.com/nguyennghia0902/kbs_final
cd kbs_final
```

Tạo hoặc mở file `.env` và điền API key:

```env
GROQ_API_KEY=gsk_xxxx...
```

> ⚠️ File `.env` đã có trong `.gitignore` — **KHÔNG** commit lên git.

#

### Bước 3 — Khởi động hệ thống (1 lệnh duy nhất)

```bash
docker-compose up -d --build
```

Đợi **60–90 giây** để `init` container hoàn tất pipeline khởi tạo, sau đó mở:

| Dịch vụ | URL |
|---|---|
| 🎓 Streamlit UI | http://localhost:8501 |
| 📖 API Docs (Swagger) | http://localhost:8000/docs |
| 🔵 Neo4j Browser | http://localhost:7474 |

### Theo dõi quá trình khởi tạo

```bash
docker logs -f kbs_init
```

Khi thấy dòng sau là hệ thống đã sẵn sàng:

```
ALL INIT STEPS COMPLETED SUCCESSFULLY ✅
```

---

## 5. Cấu trúc thư mục

```
kbs_project/
├── docker-compose.yml              ← Orchestrate toàn bộ services
├── .env                            ← Điền GROQ_API_KEY vào đây
├── .env.example                   
├── README.md
│
├── data/
│   └── questions_week3_fixed_complete.xlsx   ← Dữ liệu câu hỏi
│
├── backend/
│   ├── requirements.txt            ← Thư viện Python backend
│   ├── Dockerfile.init             ← Container khởi tạo DB (chạy 1 lần)
│   ├── Dockerfile.api              ← Container FastAPI
│   └── scripts/
│       ├── run_init.py             ← Orchestrator: tự động chạy toàn bộ pipeline
│       ├── db_config.py            ← Đọc config từ Docker env vars
│       ├── bootstrap_schema_postgres.py   ← Tạo schema PostgreSQL
│       ├── Script-seed-data.sql    ← Dữ liệu mẫu ban đầu
│       ├── etl_to_postgresql.py    ← Import Excel → PostgreSQL
│       ├── postgres_to_neo4j.py    ← Đồng bộ PostgreSQL → Neo4j
│       ├── load_rules.py           ← Load 15 rules vào Neo4j
│       ├── rules.csv               ← Định nghĩa luật suy luận
│       └── cat_api_rule_based_neo4j.py   ← FastAPI application chính
│
└── streamlit_app/
    ├── Dockerfile
    ├── requirements.txt            ← Thư viện Python frontend
    ├── streamlit_app.py            ← Entry point
    ├── st_home.py                  ← Trang chủ
    └── st_gentest_app.py           ← Giao diện thi CAT
```

---

## 6. Pipeline khởi tạo tự động

Khi `docker-compose up`, container `init` tự động chạy theo thứ tự:

```
postgres (healthy?) ──┐
                      ├──► init container
neo4j   (healthy?) ──┘         │
                               ▼
                    1. Bootstrap PostgreSQL schema
                    2. ETL: Excel → PostgreSQL
                    3. Seed data SQL (students, blueprints...)
                    4. Sync PostgreSQL → Neo4j
                    5. Load 15 rules → Neo4j
                               │
                               ▼
                    api container (FastAPI)
                               │
                               ▼
                    streamlit container (UI)
```

> Container `init` có `restart: "no"` — chỉ chạy **một lần duy nhất**. Các lần `docker-compose up` tiếp theo bỏ qua bước này.

---


## 7. Quản lý hệ thống

```bash
# Dừng, giữ nguyên data
docker-compose down

# Dừng và xóa toàn bộ data (reset hoàn toàn)
docker-compose down -v

# Khởi động lại từ đầu (sau khi reset)
docker-compose up -d --build

# Xem logs từng service
docker logs -f kbs_init
docker logs -f kbs_api
docker logs -f kbs_streamlit
docker logs -f kbs_postgres
docker logs -f kbs_neo4j

# Kiểm tra data sau khi init
docker exec kbs_postgres psql -U kbs_user -d kbs_adaptive_exam -c "SELECT COUNT(*) FROM students;"
docker exec kbs_postgres psql -U kbs_user -d kbs_adaptive_exam -c "SELECT COUNT(*) FROM questions;"
```

---

## 8. Cấu hình LLM

| Tùy chọn | Mô tả |
|---|---|
| **Groq Console** (khuyên dùng) | [https://console.groq.com/keys](https://console.groq.com/keys) – Free tier, không cần thẻ |
| **Lưu trữ** | File `.env` — không hardcode trong source code |
| **Production** | Dùng `docker secret` hoặc secret manager |

Model mặc định: `llama-3.1-8b-instant` (nhanh, miễn phí). Đổi sang model mạnh hơn trong `cat_api_rule_based_neo4j.py`:

```python
# Nhanh, miễn phí (mặc định)
model = "llama-3.1-8b-instant"

# Chính xác hơn (vẫn miễn phí, rate limit thấp hơn)
model = "llama-3.3-70b-versatile"
```

---

## 9. Troubleshooting

| Lỗi | Nguyên nhân | Giải pháp |
|---|---|---|
| `Connection refused localhost:5432` | Script dùng `localhost` trong Docker | Thêm `from db_config import PG_CONFIG` |
| `students: 0 rows` | Seed SQL chưa chạy đúng | Dùng `step_seed()` split từng statement |
| `IsADirectoryError: Is a directory: /` | `seed_candidates` là string thay vì list | Đặt path trong `[...]` |
| `foreign key constraint` | Seed chạy trước ETL | Đổi thứ tự: ETL → Seed |
| `service_healthy` timeout | Container chưa kịp ready | Tăng `healthcheck interval` hoặc dùng `service_started` cho Streamlit |
| Neo4j `connection refused` | Neo4j chậm khởi động | `wait_neo4j()` retry tự động, đợi thêm |

---

## 10. Giấy phép

Dự án được phát triển cho mục đích học thuật — Đồ án mon học cao học Khoa học Máy tính, Trường Đại học Sư phạm TP.HCM.

---

<div align="center">

Made with ❤️ by **KBS Team 3 — K36KHMT.NC HCMUE**

</div>
