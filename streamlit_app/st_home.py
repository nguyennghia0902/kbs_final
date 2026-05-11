import streamlit as st

st.set_page_config(
    page_title="Trang chủ",
    page_icon="🎓",
    layout="wide"
)

# ── CSS tùy chỉnh ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* Hero banner */
.hero-banner {
    background: linear-gradient(135deg, #01696f 0%, #0c4e54 60%, #0f3638 100%);
    border-radius: 14px;
    padding: 2.5rem 2rem 2rem 2rem;
    color: #ffffff;
    margin-bottom: 1.5rem;
}
.hero-banner h1 {
    font-size: 1.9rem;
    font-weight: 800;
    letter-spacing: -0.5px;
    margin-bottom: 0.35rem;
    color: #ffffff;
}
.hero-banner .subtitle {
    font-size: 1.05rem;
    opacity: 0.85;
    margin-bottom: 0.15rem;
}
.hero-banner .course-tag {
    display: inline-block;
    background: rgba(255,255,255,0.18);
    border: 1px solid rgba(255,255,255,0.35);
    border-radius: 999px;
    padding: 2px 14px;
    font-size: 0.82rem;
    margin-top: 0.6rem;
    letter-spacing: 0.3px;
}

/* Section card */
.info-card {
    background: var(--background-color, #f9f8f5);
    border: 1px solid rgba(0,0,0,0.08);
    border-radius: 10px;
    padding: 1.2rem 1.4rem;
    margin-bottom: 1rem;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}
.info-card h4 {
    font-size: 1rem;
    font-weight: 700;
    color: #01696f;
    margin-bottom: 0.5rem;
}

/* Tech badge */
.tech-badge {
    display: inline-block;
    background: #cedcd8;
    color: #0c4e54;
    border-radius: 6px;
    padding: 3px 10px;
    font-size: 0.78rem;
    font-weight: 600;
    margin: 2px 3px 2px 0;
}

/* Feature item */
.feature-item {
    padding: 0.55rem 0;
    border-bottom: 1px solid rgba(0,0,0,0.06);
    font-size: 0.92rem;
}
.feature-item:last-child { border-bottom: none; }
.feature-dot {
    display: inline-block;
    width: 8px; height: 8px;
    background: #01696f;
    border-radius: 50%;
    margin-right: 8px;
    vertical-align: middle;
}

/* Architecture layers */
.arch-layer {
    border-radius: 8px;
    padding: 0.55rem 1rem;
    margin-bottom: 0.45rem;
    font-size: 0.88rem;
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 10px;
}
.layer-client  { background: #dbeafe; color: #1e3a5f; }
.layer-api     { background: #dcfce7; color: #14532d; }
.layer-ai      { background: #ffedd5; color: #7c2d12; }
.layer-data    { background: #f1f5f9; color: #1e293b; }
</style>
""", unsafe_allow_html=True)

# ── HERO ────────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-banner">
    <h1>🎓 Adaptive Competency Testing System</h1>
    <div class="subtitle">HỆ THỐNG KIỂM TRA TRẮC NGHIỆM THÍCH ỨNG THEO NĂNG LỰC (ACTS)</div>
    <div class="subtitle" style="opacity:0.7; font-size:0.9rem;">
        Tích hợp CAT · IRT 1PL · Knowledge Graph · Rule Engine · LLM
    </div>
    <span class="course-tag">📚 CÁC HỆ CƠ SỞ TRI THỨC (KBS) · 2025–2026</span>
    <span class="course-tag">Trắc nghiệm Python</span>
    <span class="course-tag">Trắc nghiệm Cấu trúc dữ liệu và giải thuật</span>
</div>
""", unsafe_allow_html=True)

# ── LAYOUT CHÍNH: 2 cột lớn ─────────────────────────────────────────────────────
col_left, col_right = st.columns([2, 1], gap="large")

# ============================================================
# CỘT TRÁI
# ============================================================
with col_left:

    # --- Nhóm thực hiện ---
    st.markdown("""
    <div class="info-card">
        <h6>👥 Nhóm thực hiện</h6>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
| MSHV | Họ và tên | Email học viên |
|:---|:---|:---|
| KHMT836007 | Nguyễn Thị Mỹ Hạnh | hanhntm.KHMT036@pg.hcmue.edu.vn |
| KHMT836021 | Bùi Nguyên Nghĩa | nghiabn.KHMT036@pg.hcmue.edu.vn |
| KHMT836031 | Nguyễn Đức Thành | thanhnd.KHMT036@pg.hcmue.edu.vn |
    """)

    st.caption("🏛️ Học viên Cao học Khóa 36 · Ngành Khoa học Máy tính · Trường ĐH Sư phạm TP.HCM")


    # --- Giảng viên hướng dẫn ---
    st.markdown("""
    <div class="info-card">
        <h6>🎓 Giảng viên hướng dẫn</h6>
                PGS.TS. NGUYỄN ĐÌNH HIỂN
    </div>
    """, unsafe_allow_html=True)


    # --- Tổng quan dự án ---
    st.markdown("""
    <div class="info-card">
        <h4>📋 Tổng quan dự án</h4>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
ACTS là hệ thống kiểm tra trắc nghiệm thích ứng theo năng lực, được thiết kế
để **cá nhân hóa lộ trình đánh giá** cho từng người học dựa trên phản hồi
thực tế trong quá trình làm bài.

Thay vì bài kiểm tra cố định, mỗi câu hỏi tiếp theo được hệ thống **tự động
lựa chọn** tối ưu nhờ sự kết hợp của bốn thành phần AI đồng thời hoạt động:
năng lực $\\theta$ được cập nhật liên tục sau mỗi câu trả lời thông qua mô
hình **IRT 1PL**; **Rule Engine** điều hướng lộ trình chọn câu theo trạng thái
thông thạo topic; **Knowledge Graph (Neo4j)** lưu trữ và truy vấn mạng lưới
tri thức; và **LLM (Llama-3.1-8B / Groq)** sinh phản hồi cá nhân hóa tức thì
sau mỗi câu hỏi.
    """)

# ============================================================
# CỘT PHẢI
# ============================================================
with col_right:

    # --- Kiến trúc hệ thống ---
    st.markdown("""
    <div class="info-card">
        <h4>🏗️ Kiến trúc hệ thống (4 tầng)</h4>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
<div class="arch-layer layer-client">
    <span>🖥️</span>
    <span>Tầng Giao diện — <b>Streamlit</b> (Frontend Web App)</span>
</div>
<div class="arch-layer layer-api">
    <span>⚙️</span>
    <span>Tầng Nghiệp vụ — <b>FastAPI</b> · CAT Engine · Rule Engine · LLM Orchestrator</span>
</div>
<div class="arch-layer layer-ai">
    <span>🤖</span>
    <span>Tầng AI — <b>IRT 1PL</b> · <b>Rule Engine</b> · <b>Knowledge Graph</b> · <b>LLM Groq</b></span>
</div>
<div class="arch-layer layer-data">
    <span>🗄️</span>
    <span>Tầng Dữ liệu — <b>PostgreSQL</b> (giao dịch) · <b>Neo4j</b> (đồ thị tri thức)</span>
</div>
    """, unsafe_allow_html=True)

    st.divider()

    # --- Các kỹ thuật AI ---
    st.markdown("""
    <div class="info-card">
        <h4>🧠 Kỹ thuật tri thức được áp dụng</h4>
    </div>
    """, unsafe_allow_html=True)

    ai_items = [
        ("📐", "IRT 1PL (Item Response Theory)", "Mô hình xác suất ước lượng năng lực θ của người học sau mỗi câu trả lời (MLE)."),
        ("📜", "Rule-based Engine (Forward Chaining)", "Hệ luật IF–THEN điều hướng chọn câu hỏi: yếu topic X → tăng tần suất; θ hội tụ → kết thúc thi."),
        ("🕸️", "Knowledge Graph (Neo4j + Cypher)", "Biểu diễn cấu trúc tri thức: Subject → Topic → Question. Lưu mastery của từng sinh viên theo topic."),
        ("🤖", "LLM – Llama-3.1-8B (Groq API)", "Sinh phản hồi cá nhân hóa tức thì: giải thích đúng/sai, gợi ý ôn tập theo ngữ cảnh câu hỏi."),
        ("🔗", "Sync Service (PostgreSQL ↔ Neo4j)", "Đồng bộ hóa dữ liệu hai chiều giữa cơ sở dữ liệu quan hệ và đồ thị tri thức."),
    ]
    for icon, title, desc in ai_items:
        with st.expander(f"{icon} {title}"):
            st.caption(desc)

    st.divider()

    # --- Công nghệ ---
    st.markdown("""
    <div class="info-card">
        <h4>🛠️ Công nghệ sử dụng</h4>
    </div>
    """, unsafe_allow_html=True)

    tech_groups = {
        "Backend": ["FastAPI", "Python 3.11+", "SQLAlchemy", "Pydantic"],
        "Database": ["PostgreSQL", "Neo4j", "psycopg2", "neo4j-driver"],
        "AI / Algorithm": ["IRT 1PL (NumPy)", "Rule Engine", "Llama-3.1-8B", "Groq API"],
        "Frontend": ["Streamlit", "Pandas", "st.session_state"],
    }
    for group, techs in tech_groups.items():
        badges = "".join(f'<span class="tech-badge">{t}</span>' for t in techs)
        st.markdown(
            f"**{group}** &nbsp; {badges}",
            unsafe_allow_html=True
        )
        st.write("")

# ── TÍNH NĂNG ĐÃ THỰC HIỆN ────────────────────────────────────────────────────
st.divider()
st.markdown("### ⚡ Tính năng đã thực hiện")

f1, f2, f3 = st.columns(3)

with f1:
    st.markdown("""
    <div class="info-card">
    <h4>🔄 CAT Engine (Thích ứng)</h4>
    <div class="feature-item"><span class="feature-dot"></span>Khởi tạo phiên thi theo sinh viên + môn học</div>
    <div class="feature-item"><span class="feature-dot"></span>Chọn câu hỏi tối ưu theo θ hiện tại</div>
    <div class="feature-item"><span class="feature-dot"></span>Cập nhật θ real-time sau mỗi câu (MLE)</div>
    <div class="feature-item"><span class="feature-dot"></span>Tự dừng khi θ hội tụ hoặc đủ số câu</div>
    <div class="feature-item"><span class="feature-dot"></span>Tổng hợp báo cáo kết quả cuối phiên</div>
    </div>
    """, unsafe_allow_html=True)

with f2:
    st.markdown("""
    <div class="info-card">
    <h4>🕸️ Knowledge Graph & Rule</h4>
    <div class="feature-item"><span class="feature-dot"></span>Lưu đồ thị Subject → Topic → Question</div>
    <div class="feature-item"><span class="feature-dot"></span>Cập nhật mastery từng topic sau mỗi câu</div>
    <div class="feature-item"><span class="feature-dot"></span>Rule Engine Forward Chaining kích hoạt luật</div>
    <div class="feature-item"><span class="feature-dot"></span>Hiển thị mastery delta & số luật kích hoạt</div>
    <div class="feature-item"><span class="feature-dot"></span>Biểu đồ cột mastery theo topic trong kết quả</div>
    </div>
    """, unsafe_allow_html=True)

with f3:
    st.markdown("""
    <div class="info-card">
    <h4>🤖 LLM & Giao diện</h4>
    <div class="feature-item"><span class="feature-dot"></span>Sinh feedback cá nhân hóa sau mỗi câu</div>
    <div class="feature-item"><span class="feature-dot"></span>Giải thích đúng/sai kèm gợi ý ôn tập</div>
    <div class="feature-item"><span class="feature-dot"></span>Syntax highlighting cho câu hỏi code Python</div>
    <div class="feature-item"><span class="feature-dot"></span>Sidebar theo dõi tiến độ & trạng thái API</div>
    <div class="feature-item"><span class="feature-dot"></span>3-phase State Machine: Cấu hình → Thi → Kết quả</div>
    </div>
    """, unsafe_allow_html=True)

# ── FOOTER ─────────────────────────────────────────────────────────────────────
st.divider()
st.caption(
    "🎓 ACTS · Đồ án KBS · Học kỳ 2 · 2025–2026 · "
    "Khoa Công nghệ Thông tin · Trường Đại học Sư phạm TP. Hồ Chí Minh"
)
