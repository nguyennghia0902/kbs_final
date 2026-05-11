#!/usr/bin/env python3
import os, sys, time, logging, psycopg2

logging.basicConfig(level=logging.INFO, format="%(asctime)s [INIT] %(message)s")
log = logging.getLogger("init")

PG_HOST     = os.environ.get("PG_HOST",     "postgres")
PG_PORT     = int(os.environ.get("PG_PORT", "5432"))
PG_DB       = os.environ.get("PG_DB",       "kbs_adaptive_exam")
PG_USER     = os.environ.get("PG_USER",     "kbs_user")
PG_PASSWORD = os.environ.get("PG_PASSWORD", "kbs_password")
NEO4J_URI   = os.environ.get("NEO4J_URI",   "bolt://neo4j:7687")
NEO4J_USER  = os.environ.get("NEO4J_USER",  "neo4j")
NEO4J_PASS  = os.environ.get("NEO4J_PASSWORD", "12345678")
EXCEL_FILE  = os.environ.get("EXCEL_FILE",  "/app/data/questions_week3_fixed_complete.xlsx")
RULES_CSV   = os.environ.get("RULES_CSV",   "/app/rules.csv")

PG_CONFIG = dict(host=PG_HOST, port=PG_PORT, dbname=PG_DB, user=PG_USER, password=PG_PASSWORD)

def patch_pg(module):
    """Tìm bất kỳ dict nào có key 'host' và 'dbname', patch thành giá trị từ env."""
    for attr in dir(module):
        val = getattr(module, attr)
        if isinstance(val, dict) and "host" in val and "dbname" in val:
            val.update(PG_CONFIG)
            log.info(f"  patched {module.__name__}.{attr}.host → {PG_HOST}")

def patch_neo4j(module):
    for attr in ["NEO4J_URI", "NEO4J_URL"]:
        if hasattr(module, attr):
            setattr(module, attr, NEO4J_URI)
    for attr in ["NEO4J_USER", "USER"]:
        if hasattr(module, attr) and getattr(module, attr) in ("neo4j",):
            setattr(module, attr, NEO4J_USER)
    for attr in ["NEO4J_PASSWORD", "PASSWORD"]:
        if hasattr(module, attr):
            setattr(module, attr, NEO4J_PASS)

def patch_excel(module):
    for attr in dir(module):
        val = getattr(module, attr)
        if isinstance(val, str) and val.endswith(".xlsx"):
            setattr(module, attr, EXCEL_FILE)

def wait_postgres(max_retries=30, delay=3):
    log.info("Waiting for PostgreSQL...")
    for i in range(max_retries):
        try:
            conn = psycopg2.connect(**PG_CONFIG)
            conn.close()
            log.info("PostgreSQL ready.")
            return
        except Exception:
            log.info(f"  PG not ready ({i+1}/{max_retries}), retry in {delay}s...")
            time.sleep(delay)
    raise RuntimeError("PostgreSQL did not become ready in time.")

def wait_neo4j(max_retries=40, delay=5):
    log.info("Waiting for Neo4j...")
    from neo4j import GraphDatabase
    for i in range(max_retries):
        try:
            drv = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASS))
            with drv.session() as s:
                s.run("RETURN 1")
            drv.close()
            log.info("Neo4j ready.")
            return
        except Exception:
            log.info(f"  Neo4j not ready ({i+1}/{max_retries}), retry in {delay}s...")
            time.sleep(delay)
    raise RuntimeError("Neo4j did not become ready in time.")

def run_step(name, fn):
    log.info(f">>> {name}")
    try:
        fn()
        log.info(f"OK: {name}")
    except Exception as e:
        log.error(f"FAILED: {name}: {e}")
        raise

def step_bootstrap():
    import bootstrap_schema_postgres as m
    patch_pg(m)
    m.main()

def step_seed():
    seed_candidates = [
        "/app/Script-seed-data.sql",
        os.path.join(os.path.dirname(__file__), "Script-seed-data.sql"),
    ]
    seed_file = next((p for p in seed_candidates if os.path.exists(p)), None)
    if not seed_file:
        log.warning("Seed file not found, skipping")
        return

    with open(seed_file, "r", encoding="utf-8") as f:
        raw = f.read()

    statements = []
    for stmt in raw.split(";"):
        lines = [l for l in stmt.splitlines() if not l.strip().startswith("--")]
        clean = " ".join(lines).strip()
        if clean:
            statements.append(clean)

    conn = psycopg2.connect(**PG_CONFIG)
    conn.autocommit = True
    ok, skipped = 0, 0
    try:
        with conn.cursor() as cur:
            for i, stmt in enumerate(statements):
                try:
                    cur.execute(stmt)
                    ok += 1
                except Exception as e:
                    skipped += 1
                    log.warning(f"Seed stmt[{i}] skipped: {e}")
    finally:
        conn.close()
    log.info(f"Seed done: {ok} OK, {skipped} skipped")

    conn2 = psycopg2.connect(**PG_CONFIG)
    try:
        with conn2.cursor() as cur:
            cur.execute("SELECT COUNT(*) FROM students")
            log.info(f"students count = {cur.fetchone()[0]}")
    finally:
        conn2.close()


def step_etl():
    import etl_to_postgresql as m
    patch_pg(m)
    patch_excel(m)
    m.main()

def step_neo4j_sync():
    import postgres_to_neo4j as m
    patch_pg(m)
    patch_neo4j(m)
    from neo4j import GraphDatabase
    m.get_pg_connection = lambda: __import__("psycopg2").connect(
        cursor_factory=__import__("psycopg2.extras", fromlist=["RealDictCursor"]).RealDictCursor,
        **PG_CONFIG
    )
    m.get_neo_driver = lambda: GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASS))
    m.main()

def step_load_rules():
    import load_rules as m
    patch_neo4j(m)
    from neo4j import GraphDatabase
    m.driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASS))
    m.load_rules(RULES_CSV, reset=True)

if __name__ == "__main__":
    wait_postgres()
    wait_neo4j()

    steps = [
        ("Bootstrap PostgreSQL schema", step_bootstrap),
        ("ETL Excel → PostgreSQL",      step_etl),       # ← đổi lên trước seed
        ("Seed data SQL",               step_seed),       # ← xuống sau ETL
        ("Sync PostgreSQL → Neo4j",     step_neo4j_sync),
        ("Load rules → Neo4j",          step_load_rules),
    ]

    for name, fn in steps:
        run_step(name, fn)

    log.info("ALL INIT STEPS COMPLETED SUCCESSFULLY ✅")