import streamlit as st
import pandas as pd
from datetime import datetime

# 1. إعدادات الصفحة المتقدمة للمظهر الاحترافي
st.set_page_config(
    page_title="مساعد نيو فيجن الاحترافي",
    page_icon="👑",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. حزمة تصميم احترافية مخصصة للهواتف واللغة العربية (CSS Injection)
st.markdown("""
    <style>
    /* تحسين خطوط الواجهة والمحاذاة العربية */
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@4family=Tajawal:wght@500;700&display=swap');
    
    html, body, [data-testid="stSidebarUserContent"], .stApp {
        font-family: 'Tajawal', sans-serif;
        direction: rtl;
        text-align: right;
    }
    
    /* ضبط العناوين والمحاذاة جهة اليمين */
    h1, h2, h3, h4, h5, h6, p, label, .stMarkdown {
        text-align: right !important;
        direction: rtl !important;
    }
    
    /* تجميل البطاقات وصناديق الإدخال */
    div.stTextInput > div > div > input {
        direction: rtl !important;
        text-align: right !important;
        border-radius: 12px !important;
        border: 1px solid #3e424b !important;
        padding: 10px 15px !important;
    }
    
    div.stTextArea > div -> textarea {
        direction: rtl !important;
        text-align: right !important;
        border-radius: 12px !important;
        border: 1px solid #3e424b !important;
    }
    
    /* ترقية تصميم الأزرار لتصبح فخمة وتفاعلية */
    .stButton>button {
        width: 100%;
        border-radius: 14px !important;
        height: 3.2em !important;
        background: linear-gradient(135deg, #FF4B4B 0%, #CC1111 100%) !important;
        color: white !important;
        font-weight: bold !important;
        font-size: 16px !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(255, 75, 75, 0.3) !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(255, 75, 75, 0.5) !important;
    }
    
    /* إخفاء القوائم الجانبية المزعجة على شاشات الهاتف */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* تجميل حاوية البيانات وجدول الحالات */
    [data-testid="stDataEditor"] {
        direction: ltr !important; /* للحفاظ على تنسيق جدول الأرقام */
        border-radius: 12px !important;
        overflow: hidden;
    }
    </style>
""", unsafe_allow_html=True)

# ترويسة التطبيق الفخمة
st.markdown("<h1 style='text-align: center; color: #FF4B4B; margin-bottom: 5px;'>👑 لوحة تحكم التقارير الذكية</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888b94; font-size: 14px;'>النظام المطور لإدارة العروض والمتابعات اليومية بدقة واحترافية</p>", unsafe_allow_html=True)
st.markdown("---")

# صندوق البيانات الأساسية بتصميم مرتب
with st.container():
    st.markdown("<h4 style='color: #FF4B4B;'>👤 إعدادات الهوية الشخصية</h4>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        my_name = st.text_input("اسمك الكريم:", "مسوق نيو فيجن")
        report_time = st.text_input("توقيت الإرسال المعتاد:", "23:30h")
    with col2:
        upline_name = st.text_input("اسم الأبلاين المباشر:", "")
        today_date_input = st.text_input("التاريخ الحالي:", datetime.now().strftime("%d / %m / %Y"))

st.markdown("---")

# قسم الحالات الثابتة
statuses = [
    "لم يرد على الدعوة ⚪",
    "حضر الشرح (دخل اللايف) 🟢",
    "غائب (وافق ولم يرد على التذكير) 🟡",
    "اعتراض (رفض الدعوة) 🔴",
    "وعود بالتسجيل (ملأ الاستمارة) 📝"
]

# صندوق إدخال البيانات المطور
st.markdown("<h4 style='color: #FF4B4B;'>📥 1. نسخ ولصق القوائم اليومية</h4>", unsafe_allow_html=True)
raw_input = st.text_area(
    "ألصق الأرقام والأسماء هنا مباشرة من جهات الاتصال أو الواتساب:", 
    placeholder="مثال للتنسيق المدعوم تلقائياً:\n1. Nono__be — +213556377360\nKhelifa Kader — +213669882986",
    height=160
)

if raw_input:
    lines = [line.strip() for line in raw_input.split('\n') if line.strip()]
    data = []
    
    # خوارزمية ذكية لتنظيف وتفكيك النصوص الملتصقة
    for line in lines:
        clean_line = line
        # تنظيف الترقيم إن وجد
        if '.' in line[:4]: clean_line = line.split('.', 1)[1].strip()
        elif '-' in line[:4]: clean_line = line.split('-', 1)[1].strip()
        
        if "—" in clean_line:
            name, phone = clean_line.split("—", 1)
            data.append({"الاسم": name.strip(), "الرقم": phone.strip(), "الحالة": statuses[0]})
        elif " - " in clean_line:
            name, phone = clean_line.split(" - ", 1)
            data.append({"الاسم": name.strip(), "الرقم": phone.strip(), "الحالة": statuses[0]})
        else:
            data.append({"الاسم": "مستهدف", "الرقم": clean_line.strip(), "الحالة": statuses[0]})
    
    df = pd.DataFrame(data)
    
    st.markdown("---")
    st.markdown("<h4 style='color: #FF4B4B;'>🔄 2. فرز وتحديث الحالات بنقرة زر</h4>", unsafe_allow_html=True)
    st.caption("تصفح الجدول أدناه وقم بتغيير حالة كل شخص بناءً على تفاعله اليوم:")
    
    # عرض الجدول بشكل احترافي مع إخفاء الأعمدة غير الضرورية
    edited_df = st.data_editor(df, hide_index=True, use_container_width=True)
    
    st.markdown("---")
    st.markdown("<h4 style='color: #FF4B4B;'>📊 3. استخراج التقرير الفوري</h4>", unsafe_allow_html=True)
    
    if st.button("👑 توليد التقرير النهائي للواتساب"):
        # حساب الإحصائيات الدقيقة
        total = len(edited_df)
        attended = len(edited_df[edited_df['الحالة'] == statuses[1]])
        absent = len(edited_df[edited_df['الحالة'] == statuses[2]])
        rejected = len(edited_df[edited_df['الحالة'] == statuses[3]])
        registered = len(edited_df[edited_df['الحالة'] == statuses[4]])
        no_reply = len(edited_df[edited_df['الحالة'] == statuses[0]])
        
        # صياغة النص النهائي للتقرير ليتوافق تماماً مع صيغة الواتساب والجداول المطلوبة
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

        st.success("🎉 ممتاز! تم استخراج التقرير بجداول فخمة ومتوافقة مع نظام الأبلاين:")
        st.text_area("📋 اضغط مطولاً داخل الصندوق لنسخ التقرير بالكامل للأبلاين:", report_text, height=350)
