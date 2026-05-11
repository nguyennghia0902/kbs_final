# ✅ Checklist thiết lập dự án

## Lần đầu setup (chỉ làm 1 lần)

- [ ] **1. Clone / tạo thư mục dự án** theo cấu trúc trong README.md
- [ ] **2. Lấy Groq API Key**
  - Truy cập https://console.groq.com/keys
  - Đăng ký miễn phí (dùng Google/GitHub)
  - Tạo key → copy vào `.env`
- [ ] **3. Điền `.env`**
  ```
  GROQ_API_KEY=gsk_xxxxxxxx
  ```
- [ ] **4. Sao chép các file backend** vào `backend/scripts/`:
  - `bootstrap_schema_postgres.py`
  - `Script-seed-data.sql`
  - `etl_to_postgresql.py`
  - `postgres_to_neo4j.py`
  - `load_rules.py`
  - `rules.csv`
  - `cat_api_rule_based_neo4j.py`
- [ ] **5. Đặt file Excel** vào `data/questions_week3_fixed_complete.xlsx`
- [ ] **6. Patch scripts** (bước tự động):
  ```bash
  python patch_scripts.py
  ```
- [ ] **7. Build & chạy Docker**:
  ```bash
  docker-compose up -d --build
  ```
- [ ] **8. Mở Streamlit**: http://localhost:8501 🎉

## Mỗi lần chạy lại (sau lần đầu)
```bash
docker-compose up -d
# Mở http://localhost:8501
```