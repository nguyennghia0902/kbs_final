FROM python:3.11-slim
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends curl && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY streamlit_app.py  /app/streamlit_app.py
COPY st_home.py        /app/st_home.py
COPY st_gentest_app.py /app/st_gentest_app.py
EXPOSE 8501
HEALTHCHECK --interval=15s --timeout=5s --retries=5 CMD curl -f http://localhost:8501/_stcore/health || exit 1
CMD ["streamlit", "run", "streamlit_app.py", "--server.address=0.0.0.0", "--server.port=8501", "--server.headless=true", "--browser.gatherUsageStats=false"]