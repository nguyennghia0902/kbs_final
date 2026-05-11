"""
db_config.py – Cấu hình kết nối được inject qua environment variable (Docker)
Import module này thay cho hardcode trong từng script.
"""
import os

PG_CONFIG = dict(
    host=os.environ.get("PG_HOST", "localhost"),
    port=int(os.environ.get("PG_PORT", 5432)),
    dbname=os.environ.get("PG_DB", "kbs_adaptive_exam"),
    user=os.environ.get("PG_USER", "kbs_user"),
    password=os.environ.get("PG_PASSWORD", "kbs_password"),
)

NEO4J_URI      = os.environ.get("NEO4J_URI",      "bolt://localhost:7687")
NEO4J_USER     = os.environ.get("NEO4J_USER",     "neo4j")
NEO4J_PASSWORD = os.environ.get("NEO4J_PASSWORD", "12345678")

GROQ_API_KEY   = os.environ.get("GROQ_API_KEY", "")

EXCEL_FILE     = os.environ.get("EXCEL_FILE", "/app/data/questions_week3_fixed_complete.xlsx")
RULES_CSV      = os.environ.get("RULES_CSV",   "/app/rules.csv")