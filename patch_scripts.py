#!/usr/bin/env python3
#!/usr/bin/env python3
"""
patch_scripts.py
Chạy script này MỘT LẦN sau khi bạn sao chép các file backend vào thư mục scripts/.
Nó sẽ tự động thêm import db_config vào đầu mỗi file để đọc cấu hình từ Docker env vars.

Cách dùng:
  python patch_scripts.py
"""
import re, os, sys

SCRIPTS_DIR = os.path.join(os.path.dirname(__file__), "backend", "scripts")

PATCH_HEADER = """# ── PATCHED by patch_scripts.py ──────────────────────
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from db_config import PG_CONFIG, NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD, GROQ_API_KEY
# ──────────────────────────────────────────────────────
"""

# Map: file -> các biến cần replace
REPLACEMENTS = {
    "bootstrap_schema_postgres.py": [
        (r'DB_CONFIG\s*=\s*\{[^}]+\}', 'DB_CONFIG = PG_CONFIG'),
        (r'"host"\s*:\s*"localhost"', '"host": os.environ.get("PG_HOST","localhost")'),
    ],
    "etl_to_postgresql.py": [
        (r'DB_CONFIG\s*=\s*\{[^}]+\}', 'DB_CONFIG = PG_CONFIG'),
    ],
    "postgres_to_neo4j.py": [
        (r'PG_CONFIG\s*=\s*\{[^}]+\}', 'PG_CONFIG = PG_CONFIG'),
        (r'NEO4J_URI\s*=\s*["\']bolt://localhost["\']', 'NEO4J_URI = NEO4J_URI'),
        (r'NEO4J_USER\s*=\s*["\']neo4j["\']', 'NEO4J_USER = NEO4J_USER'),
        (r'NEO4J_PASSWORD\s*=\s*["\'][\w]+["\']', 'NEO4J_PASSWORD = NEO4J_PASSWORD'),
    ],
    "load_rules.py": [
        (r'NEO4J_URI\s*=\s*["\']bolt://localhost["\']', 'NEO4J_URI = NEO4J_URI'),
        (r'USER\s*=\s*["\']neo4j["\']', 'USER = NEO4J_USER'),
        (r'PASSWORD\s*=\s*["\'][\w]+["\']', 'PASSWORD = NEO4J_PASSWORD'),
    ],
    "cat_api_rule_based_neo4j.py": [
        (r'GROQ_API_KEY\s*=\s*[^ \n]+', 'GROQ_API_KEY = GROQ_API_KEY'),
        (r'PG_CONFIG\s*=\s*\{[^}]+\}', 'PG_CONFIG = PG_CONFIG'),
        (r'NEO4J_URI\s*=\s*["\']bolt://localhost["\']', 'NEO4J_URI = NEO4J_URI'),
        (r'NEO4J_USER\s*=\s*["\']neo4j["\']', 'NEO4J_USER = NEO4J_USER'),
        (r'NEO4J_PASSWORD\s*=\s*["\'][\w]+["\']', 'NEO4J_PASSWORD = NEO4J_PASSWORD'),
    ],
}



def patch_file(filepath, replacements):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    if "PATCHED by patch_scripts.py" in content:
        print(f"  SKIP (already patched): {os.path.basename(filepath)}")
        return
    content = PATCH_HEADER + content
    for pattern, replacement in replacements:
        content = re.sub(pattern, replacement, content, count=1)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  OK: {os.path.basename(filepath)}")

if __name__ == "__main__":
    print("Patching backend scripts for Docker environment...")
    for fname, reps in REPLACEMENTS.items():
        fpath = os.path.join(SCRIPTS_DIR, fname)
        if os.path.exists(fpath):
            patch_file(fpath, reps)
        else:
            print(f"  NOT FOUND (copy vào scripts/ trước): {fname}")
    print("Done! Rebuild Docker image: docker-compose build init api")






