import streamlit as st
import pandas as pd
from datetime import datetime

# إعدادات الصفحة الاحترافية لنيو فيجن
st.set_page_config(
    page_title="نيو فيجن برو | التنسيق النظيف",
    page_icon="👑",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# حزمة التصميم الفاخرة المستقرة والمحاذاة العربية
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;900&display=swap');
    
    html, body, [data-testid="stSidebarUserContent"], .stApp {
        font-family: 'Tajawal', sans-serif !important;
        direction: rtl !important;
        text-align: right !important;
        background-color: #0d1117 !important;
    }
    
    h1, h2, h3, h4, h5, h6, p, label, .stMarkdown, p {
        text-align: right !important;
        direction: rtl !important;
        color: #f0f6fc !important;
    }
    
    /* تصميم البطاقات الزجاجية الفاخرة */
    div[data-testid="stVerticalBlock"] > div {
        background: rgba(22, 27, 34, 0.8) !important;
        border: 1px solid rgba(48, 54, 61, 0.8) !important;
        border-radius: 20px !important;
        padding: 22px !important;
        margin-bottom: 15px !important;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37) !important;
    }
    
    div[data-testid="stVerticalBlock"] div[data-testid="stVerticalBlock"] {
        background: transparent !important;
        border: none !important;
        padding: 0 !important;
        box-shadow: none !important;
    }
    
    input, textarea {
        direction: rtl !important;
        text-align: right !important;
        background-color: #161b22 !important;
        color: #c9d1d9 !important;
        border-radius: 14px !important;
        border: 1px solid #30363d !important;
        padding: 12px !important;
    }
    
    .stButton>button {
        width: 100% !important;
        border-radius: 16px !important;
        height: 3.5em !important;
        background: linear-gradient(135deg, #1f6feb 0%, #0d44a5 100%) !important;
        color: #ffffff !important;
        font-weight: 900 !important;
        font-size: 17px !important;
        box-shadow: 0 4px 20px rgba(31, 111, 235, 0.4) !important;
    }
    
    [data-testid="stDataEditor"] {
        border-radius: 16px !important;
        border: 1px solid #30363d !important;
        overflow: hidden !important;
    }
    
    header, footer, #MainMenu { visibility: hidden !important; }
    
    .kpi-container {
        display: flex;
        justify-content: space-between;
        gap: 8px;
        margin-bottom: 10px;
        direction: rtl;
    }
    .kpi-card {
        flex: 1;
        background: #161b22;
        border: 1px solid #30363d;
        border-radius: 14px;
        text-align: center;
        padding: 10px 2px;
    }
    .kpi-value {
        font-size: 20px;
        font-weight: 900;
        margin-top: 5px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div style='text-align: center; padding: 5px 0;'>
        <h1 style='color: #1f6feb; font-weight: 900; font-size: 26px; margin-bottom: 5px;'>👑 PLATINUM REPORT SYSTEM</h1>
        <p style='color: #8b949e; font-size: 14px;'>نسخة نقية وخالية تماماً من الأكواد والرموز الزائدة</p>
    </div>
""", unsafe_allow_html=True)

# 👤 إعدادات الهوية الشخصية
st.markdown("<h3 style='color: #1f6feb; font-size: 17px; font-weight: 700;'>👤 بيانات التقرير الأساسية</h3>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    my_name = st.text_input("اسمك الشخصي:", "مقيم")
    report_time = st.text_input("وقت إرسال التقرير:", "23:30h")
with col2:
    upline_name = st.text_input("اسم الأبلاين المباشر:", "حبيبة")
    today_date_input = st.text_input("التاريخ الحالي:", datetime.now().strftime("%d / %m / %Y"))

st.markdown("<br>", unsafe_allow_html=True)

# الحالات الثابتة المعزولة
statuses = [
    "لم يرد على الدعوة",
    "حضر الشرح (دخل اللايف)",
    "غائب (لم يرد على التذكير)",
    "اعتراض (رفض الدعوة)",
    "وعود بالتسجيل"
]

# 📥 صندوق لصق البيانات
st.markdown("<h3 style='color: #1f6feb; font-size: 17px; font-weight: 700;'>📥 1. نسخ ولصق القائمة المستهدفة</h3>", unsafe_allow_html=True)
raw_input = st.text_area(
    "ألصق الأرقام والأسماء هنا مباشرة:", 
    placeholder="ألصق قائمتك هنا...",
    height=140
)

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
    st.markdown("<h3 style='color: #1f6feb; font-size: 17px; font-weight: 700;'>🔄 2. التحكم السريع في الحالات اليومية</h3>", unsafe_allow_html=True)
    
    edited_df = st.data_editor(df, hide_index=True, use_container_width=True)
    
    total = len(edited_df)
    attended = len(edited_df[edited_df['الحالة'] == statuses[1]])
    absent = len(edited_df[edited_df['الحالة'] == statuses[2]])
    rejected = len(edited_df[edited_df['الحالة'] == statuses[3]])
    registered = len(edited_df[edited_df['الحالة'] == statuses[4]])
    no_reply = len(edited_df[edited_df['الحالة'] == statuses[0]])
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown(f"""
        <div class='kpi-container'>
            <div class='kpi-card' style='border-top: 3px solid #58a6ff;'><div style='color:#8b949e; font-size:11px;'>الواصلة</div><div class='kpi-value' style='color:#58a6ff;'>{total}</div></div>
            <div class='kpi-card' style='border-top: 3px solid #3fb950;'><div style='color:#8b949e; font-size:11px;'>الحاضرين</div><div class='kpi-value' style='color:#3fb950;'>{attended}</div></div>
            <div class='kpi-card' style='border-top: 3px solid #d29922;'><div style='color:#8b949e; font-size:11px;'>الغائبين</div><div class='kpi-value' style='color:#d29922;'>{absent}</div></div>
            <div class='kpi-card' style='border-top: 3px solid #f85149;'><div style='color:#8b949e; font-size:11px;'>الاعتراضات</div><div class='kpi-value' style='color:#f85149;'>{rejected}</div></div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #1f6feb; font-size: 17px; font-weight: 700;'>📊 3. معالجة وتوليد التقرير المنسق</h3>", unsafe_allow_html=True)
    
    if st.button("👑 اضغط هنا لتوليد تقرير الواتساب النهائي"):
        
        # تنسيق مخصص ونظيف للواتساب خالي تماماً من جداول Markdown ومن رموز <br>
        report_text = f"""👑 *تقرير العمل اليومي* 👑

📅 *التاريخ*: {today_date_input}
⏰ *توقيت الإرسال*: {report_time}
✨ *الاسم الشخصي*: *{my_name}*
👥 *من طرف الأبلاين*: *{upline_name}*

▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
📊 *أولاً: الملخص الإحصائي*
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
📥 *عدد العروض الواصلة*:  *{total}*
🟢 *عدد الدخول للشرح*:  *{attended}*
🟡 *عدد الغائبين عن الشرح*:  *{absent}*
🔴 *عدد الاعتراضات*:  *{rejected}*
📝 *عدد الوعود بالتسجيل*:  *{registered}*

▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
📱 *ثانياً: تفاصيل حالة الأرقام*
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬

✅ *دخلوا الشرح بنجاح (حضور) 🟢:*\n"""
        
        if attended > 0:
            for r in edited_df[edited_df['الحالة'] == statuses[1]].to_dict('records'):
                report_text += f"• `{r['الرقم']}` ({r['AName'] if 'AName' in r else r['الاسم']})\n"
        else:
            report_text += "_لا يوجد حالياً_\n"
        
        report_text += "\n⚪ *لم يردوا على الدعوة (عدم رد/مغلق):*\n"
        if no_reply > 0:
            for r in edited_df[edited_df['الحالة'] == statuses[0]].to_dict('records'):
                report_text += f"• `{r['الرقم']}`\n"
        else:
            report_text += "_لا يوجد حالياً_\n"
            
        report_text += "\n🟡 *تمت الدعوة ولم يردوا في التذكير:*\n"
        if absent > 0:
            for r in edited_df[edited_df['الحالة'] == statuses[2]].to_dict('records'):
                report_text += f"• `{r['الرقم']}`\n"
        else:
            report_text += "_لا يوجد حالياً_\n"
            
        report_text += "\n✖️ *الاعتراضات (رفضوا الدعوة) 🔴:*\n"
        if rejected > 0:
            for r in edited_df[edited_df['الحالة'] == statuses[3]].to_dict('records'):
                report_text += f"• `{r['الرقم']}`\n"
        else:
            report_text += "_لا يوجد حالياً_\n"
            
        report_text += "\n✨ *الوعود بالتسجيل (الاستمارات) 📝:*\n"
        if registered > 0:
            for r in edited_df[edited_df['الحالة'] == statuses[4]].to_dict('records'):
                report_text += f"• `{r['الرقم']}`\n"
        else:
            report_text += "_لا يوجد حالياً_"

        st.success("🎉 ممتاز! تم حذف الأكواد وستظهر لك القائمة نقية وجاهزة:")
        st.text_area("📋 حدد النص بالكامل من الصندوق وانسخه للواتساب مباشرة:", report_text, height=400)
