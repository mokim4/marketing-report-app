import streamlit as st
import pandas as pd
from datetime import datetime

# إعدادات الصفحة الاحترافية
st.set_page_config(
    page_title="نيو فيجن برو | Ultra-Premium",
    page_icon="👑",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# حزمة التصميم الفاخرة والهندسة البصرية الواجهة (Ultra-Premium CSS)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;900&display=swap');
    
    /* إعادة تعيين المظهر العام للتطبيق ليصبح فخماً وداكناً */
    html, body, [data-testid="stSidebarUserContent"], .stApp {
        font-family: 'Tajawal', sans-serif !important;
        direction: rtl !important;
        text-align: right !important;
        background-color: #0d1117 !important;
    }
    
    /* ضبط محاذاة العناوين والنصوص العربية */
    h1, h2, h3, h4, h5, h6, p, label, .stMarkdown, p {
        text-align: right !important;
        direction: rtl !important;
        color: #f0f6fc !important;
    }
    
    /* تصميم البطاقات الزجاجية الفاخرة (Glassmorphic Cards) */
    div[data-testid="stVerticalBlock"] > div {
        background: rgba(22, 27, 34, 0.8) !important;
        border: 1px solid rgba(48, 54, 61, 0.8) !important;
        border-radius: 20px !important;
        padding: 22px !important;
        margin-bottom: 15px !important;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37) !important;
    }
    
    /* إلغاء تأثير البطاقات المتداخلة للحفاظ على نظافة التصميم */
    div[data-testid="stVerticalBlock"] div[data-testid="stVerticalBlock"] {
        background: transparent !important;
        border: none !important;
        padding: 0 !important;
        box-shadow: none !important;
    }
    
    /* تجميل وترقية حقول الإدخال النصية */
    input, textarea {
        direction: rtl !important;
        text-align: right !important;
        background-color: #161b22 !important;
        color: #c9d1d9 !important;
        border-radius: 14px !important;
        border: 1px solid #30363d !important;
        padding: 12px !important;
        font-size: 15px !important;
        transition: all 0.3s ease-in-out !important;
    }
    
    input:focus, textarea:focus {
        border-color: #58a6ff !important;
        box-shadow: 0 0 0 3px rgba(88, 166, 255, 0.15) !important;
    }
    
    /* تصميم زر التوليد الخارق والمضيء (Glow Premium Button) */
    .stButton>button {
        width: 100% !important;
        border-radius: 16px !important;
        height: 3.5em !important;
        background: linear-gradient(135deg, #1f6feb 0%, #0d44a5 100%) !important;
        color: #ffffff !important;
        font-weight: 900 !important;
        font-size: 17px !important;
        letter-spacing: 0.5px;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        box-shadow: 0 4px 20px rgba(31, 111, 235, 0.4) !important;
        transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1) !important;
    }
    
    .stButton>button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 8px 25px rgba(31, 111, 235, 0.7) !important;
        background: linear-gradient(135deg, #388bfd 0%, #1f6feb 100%) !important;
    }
    
    /* تخصيص مظهر جدول البيانات التفاعلي ليكون منسقاً ونظيفاً */
    [data-testid="stDataEditor"] {
        border-radius: 16px !important;
        border: 1px solid #30363d !important;
        overflow: hidden !important;
    }
    
    /* إخفاء شريط أدوات المنصة للحصول على تجربة تطبيق مستقل بالكامل */
    header, footer, #MainMenu { visibility: hidden !important; }
    
    /* تصميم بطاقات الـ KPI الرقمية الفخمة */
    .kpi-container {
        display: flex;
        justify-content: space-between;
        gap: 10px;
        margin-bottom: 20px;
        direction: rtl;
    }
    .kpi-card {
        flex: 1;
        background: #161b22;
        border: 1px solid #30363d;
        border-radius: 14px;
        text-align: center;
        padding: 12px 5px;
    }
    .kpi-value {
        font-size: 22px;
        font-weight: 900;
        margin-top: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# ترويسة التطبيق الملكية الفخمة جداً
st.markdown("""
    <div style='text-align: center; padding: 10px 0;'>
        <h1 style='color: #1f6feb; font-weight: 900; font-size: 28px; margin-bottom: 8px;'>👑 PLATINUM REPORT SYSTEM</h1>
        <p style='color: #8b949e; font-size: 15px; font-weight: 500;'>النظام الذكي الفاخر لإدارة عروضك وتقاريرك المتقدمة</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 👤 قسم إعدادات الهوية الفاخر
st.markdown("<h3 style='color: #1f6feb; font-size: 18px; font-weight: 700;'>👤 إعدادات الملف الشخصي</h3>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    my_name = st.text_input("اسمك الشخصي:", "مسوق نيو فيجن")
    report_time = st.text_input("وقت إرسال التقرير اليومي:", "23:30h")
with col2:
    upline_name = st.text_input("اسم الأبلاين (Upline):", "")
    today_date_input = st.text_input("تاريخ اليوم الحالي:", datetime.now().strftime("%d / %m / %Y"))

st.markdown("<br>", unsafe_allow_html=True)

# 📥 قسم إدخال القوائم وتنظيفها تلقائياً
st.markdown("<h3 style='color: #1f6feb; font-size: 18px; font-weight: 700;'>📥 1. نسخ ولصق القائمة المستهدفة</h3>", unsafe_allow_html=True)
raw_input = st.text_area(
    "ألصق الأرقام والأسماء هنا مباشرة من الواتساب:", 
    placeholder="مثال:\n1. Nono__be — +213556377360\nKhelifa Kader — +213669882986",
    height=150
)

# الحالات الثابتة للفرز الذكي
statuses = [
    "لم يرد على الدعوة ⚪",
    "حضر الشرح (دخل اللايف) 🟢",
    "غائب (وافق ولم يرد على التذكير) 🟡",
    "اعتراض (رفض الدعوة) 🔴",
    "وعود بالتسجيل (ملأ الاستمارة) 📝"
]

if raw_input:
    lines = [line.strip() for line in raw_input.split('\n') if line.strip()]
    data = []
    
    for line in lines:
        clean_line = line
        if '.' in line[:4]: clean_line = line.split('.', 1)[1].strip()
        elif '-' in line[:4]: clean_line = line.split('-', 1)[1].strip()
        
        if "—" in clean_line:
            name, phone = clean_line.split("—", 1)
            data.append({"الاسم": name.strip(), "الرقم": phone.strip(), "الحالة": statuses[0]})
        elif " - " in clean_line:
            name, phone = clean_line.split(" - ", 1)
            data.append({"الاسم": name.strip(), "الرقم": phone.strip(), "الحالة": statuses[0]})
        else:
            data.append({"الاسم": "مستهدف جديد", "الرقم": clean_line.strip(), "الحالة": statuses[0]})
    
    df = pd.DataFrame(data)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #1f6feb; font-size: 18px; font-weight: 700;'>🔄 2. التحكم السريع في حالات الأعضاء</h3>", unsafe_allow_html=True)
    st.caption("اضغط مرتين على خانة الحالة لتعديل تفاعل الرقم فوراً:")
    
    # عرض الجدول التفاعلي
    edited_df = st.data_editor(df, hide_index=True, use_container_width=True)
    
    # حساب الإحصائيات الفورية
    total = len(edited_df)
    attended = len(edited_df[edited_df['الحالة'] == statuses[1]])
    absent = len(edited_df[edited_df['الحالة'] == statuses[2]])
    rejected = len(edited_df[edited_df['الحالة'] == statuses[3]])
    registered = len(edited_df[edited_df['الحالة'] == statuses[4]])
    no_reply = len(edited_df[edited_df['الحالة'] == statuses[0]])
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # عرض الـ KPIs بتصميم البطاقات المستقلة الفخمة جداً
    st.markdown(f"""
        <div class='kpi-container'>
            <div class='kpi-card' style='border-top: 3px solid #58a6ff;'><div style='color:#8b949e; font-size:12px;'>الواصلة</div><div class='kpi-value' style='color:#58a6ff;'>{total}</div></div>
            <div class='kpi-card' style='border-top: 3px solid #3fb950;'><div style='color:#8b949e; font-size:12px;'>الحاضرين</div><div class='kpi-value' style='color:#3fb950;'>{attended}</div></div>
            <div class='kpi-card' style='border-top: 3px solid #d29922;'><div style='color:#8b949e; font-size:12px;'>الغائبين</div><div class='kpi-value' style='color:#d29922;'>{absent}</div></div>
            <div class='kpi-card' style='border-top: 3px solid #f85149;'><div style='color:#8b949e; font-size:12px;'>الاعتراضات</div><div class='kpi-value' style='color:#f85149;'>{rejected}</div></div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #1f6feb; font-size: 18px; font-weight: 700;'>📊 3. معالجة وتصدير التقرير النهائي</h3>", unsafe_allow_html=True)
    
    if st.button("👑 اضغط هنا لتوليد تقرير الواتساب المنسق"):
        
        # بناء نص التقرير المطابق تماماً للجداول الفخمة المطلوبة للأبلاين
        report_text = f"""👑 *تقرير اليوم* 👑  
📅 *التاريخ*: {today_date_input}  
⏰ *الساعة* : {report_time}  
✨ *الاسم*: *{my_name}*  
👥 *من طرف الأبلاين*: *{upline_name}*  

---

### 📊 أولاً: الملخص الإحصائي

| المؤشر | العدد | الحالة |
| :--- | :---: | :--- |
| *عدد العروض الواصلة 📥* | *{total}* | إجمالي الأرقام المستهدفة |
| *عدد الدخول للشرح 🟢* | *{attended}* | التزم بالدعوة والتذكير وحضر |
| *عدد الغائبين 🟡* | *{absent}* | وافق على الدعوة وغاب عند التذكير |
| *عدد الإعتراضات 🔴* | *{rejected}* | رفضوا الدعوة من البداية |
| *عدد التسجيلات 📝* | *{registered}* | استمارات مسجلة |

---

### 📱 ثانياً: تفاصيل حالة الأرقام

| الوضع الحالي | قائمة الأرقام |
| :--- | :--- |
| *دخلوا الشرح بنجاح ✅* | """
        
        if attended > 0:
            for r in edited_df[edited_df['الحالة'] == statuses[1]].to_dict('records'):
                report_text += f"• `{r['الرقم']}` ({r['الاسم']})<br>"
        else: report_text += "_لا يوجد حالياً_<br>"
        
        report_text += " | \n| *لم يردوا على الدعوة (مغلق/عدم رد) ⚪* | "
        if no_reply > 0:
            for r in edited_df[edited_df['الحالة'] == statuses[0]].to_dict('records'):
                report_text += f"• `{r['الرقم']}`<br>"
        else: report_text += "_لا يوجد حالياً_<br>"
            
        report_text += " | \n| *تمت الدعوة ولم يردوا في التذكير 🟡* | "
        if absent > 0:
            for r in edited_df[edited_df['الحالة'] == statuses[2]].to_dict('records'):
                report_text += f"• `{r['الرقم']}`<br>"
        else: report_text += "_لا يوجد حالياً_<br>"
            
        report_text += " | \n| *الاعتراضات (رفضوا الدعوة) ✖️* | "
        if rejected > 0:
            for r in edited_df[edited_df['الحالة'] == statuses[3]].to_dict('records'):
                report_text += f"• `{r['الرقم']}` (رفض)<br>"
        else: report_text += "_لا يوجد حالياً_<br>"
            
        report_text += " | \n| *الوعود بالتسجيل (الاستمارات) ✨* | "
        if registered > 0:
            for r in edited_df[edited_df['الحالة'] == statuses[4]].to_dict('records'):
                report_text += f"• `{r['الرقم']}`<br>"
        else: report_text += "_لا يوجد حالياً_"
        
        report_text += " |"

        st.success("🎉 ممتاز! تم تشكيل التقرير الملكي بنجاح، انسخه الآن:")
        st.text_area("📋 اضغط بشكل مطول وانسخ النص بالكامل واذهب للواتساب:", report_text, height=350)
