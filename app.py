import streamlit as st
import pandas as pd
from datetime import datetime

# إعدادات الصفحة لتناسب الهاتف
st.set_page_config(page_title="مساعد نيو فيجن", page_icon="👑", layout="centered")

# تنسيق مخصص للهواتف (CSS) لتكبير الأزرار وتسهيل القراءة
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #FF4B4B;
        color: white;
        font-weight: bold;
    }
    textarea {
        direction: rtl;
    }
    input {
        direction: rtl;
    }
    </style>
""", unsafe_allow_html=True)

st.title("👑 نظام إدارة التقارير اليومية")
st.write("صُمم خصيصاً لتسهيل متابعة وتوليد تقارير العروض اليومية.")

# إدخال البيانات الأساسية
with st.expander("👤 البيانات الأساسية (اضغط للتعديل)", expanded=True):
    my_name = st.text_input("اسمك الشخصي:", "مسوق نيو فيجن")
    upline_name = st.text_input("اسم الأبلاين:", "")
    report_time = st.text_input("وقت التقرير:", "23:30h")

# الحالات المتاحة للفرز
statuses = [
    "لم يرد على الدعوة ⚪",
    "حضر الشرح (دخل اللايف) 🟢",
    "غائب (وافق ولم يرد على التذكير) 🟡",
    "اعتراض (رفض الدعوة) 🔴",
    "وعود بالتسجيل (ملأ الاستمارة) 📝"
]

st.subheader("📥 1. أدخل القائمة اليومية")
raw_input = st.text_area(
    "أصق الأسماء والأرقام هنا مباشرة من الواتساب:", 
    placeholder="مثال:\nNono__be — +213556377360\nKhelifa Kader — +213669882986",
    height=150
)

if raw_input:
    lines = [line.strip() for line in raw_input.split('\n') if line.strip()]
    data = []
    
    # تنظيف وتفكيك النص المدخل
    for line in lines:
        # إزالة الترقيم التلقائي إن وجد (مثل: 1. أو 2-)
        clean_line = line
        if '.' in line[:3]: clean_line = line.split('.', 1)[1].strip()
        elif '-' in line[:3]: clean_line = line.split('-', 1)[1].strip()
        
        if "—" in clean_line:
            name, phone = clean_line.split("—", 1)
            data.append({"الاسم": name.strip(), "الرقم": phone.strip(), "الحالة": statuses[0]})
        elif " - " in clean_line:
            name, phone = clean_line.split(" - ", 1)
            data.append({"الاسم": name.strip(), "الرقم": phone.strip(), "الحالة": statuses[0]})
        else:
            data.append({"الاسم": "مستهدف جديد", "الرقم": clean_line.strip(), "الحالة": statuses[0]})
    
    df = pd.DataFrame(data)
    
    st.subheader("🔄 2. حدد حالة كل رقم")
    st.caption("اضغط على خانة 'الحالة' بجانب كل رقم لتغيير وضع المستهدف الحالي:")
    
    # جدول تفاعلي ذكي وسريع على الهاتف
    edited_df = st.data_editor(df, hide_index=True, use_container_width=True)
    
    st.subheader("📊 3. استخراج التقرير النهائي")
    if st.button("👑 توليد التقرير المنسق لنسخه للواتساب"):
        today_date = datetime.now().strftime("%d / %m / %Y")
        
        # الحسابات الإحصائية
        total = len(edited_df)
        attended = len(edited_df[edited_df['الحالة'] == statuses[1]])
        absent = len(edited_df[edited_df['الحالة'] == statuses[2]])
        rejected = len(edited_df[edited_df['الحالة'] == statuses[3]])
        registered = len(edited_df[edited_df['الحالة'] == statuses[4]])
        no_reply = len(edited_df[edited_df['الحالة'] == statuses[0]])
        
        # صياغة النص النهائي للتقرير ليتوافق مع الجداول والرموز المطلوبة
        report_text = f"""👑 *تقرير اليوم* 👑  
📅 *الخميس*: {today_date}  
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
        
        # إضافة الأرقام حسب فئاتها
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

        st.success("🎉 تم توليد التقرير بنجاح! انسخه بالكامل من الصندوق أدناه:")
        st.text_area("📋 التقرير الجاهز للنسخ:", report_text, height=350)
