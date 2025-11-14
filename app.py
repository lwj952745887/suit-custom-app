import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from datetime import datetime

st.set_page_config(page_title="西服定制登记系统", layout="wide")
st.title("👔 西服定制客户登记表")


def send_email(data_dict, image_count=0):
    try:
        sender = st.secrets["EMAIL_SENDER"]
        password = st.secrets["EMAIL_PASSWORD"]
        receiver = st.secrets["EMAIL_RECEIVER"]

        body = "🆕 新客户西服定制登记\n\n"
        for k, v in data_dict.items():
            if str(v).strip() != "":
                label = k.replace("(inch)", "（inch）")
                body += f"{label}：{v}\n"

        if image_count > 0:
            body += f"\n📷 客户图片：已上传 {image_count} 张\n"

        msg = MIMEText(body, 'plain', 'utf-8')
        msg['From'] = Header("西服登记系统", 'utf-8')
        msg['To'] = Header("管理员", 'utf-8')
        msg['Subject'] = Header(f"新客户登记 - {data_dict.get('姓名', '匿名')}", 'utf-8')

        server = smtplib.SMTP("smtp.163.com", 25)
        server.login(sender, password)
        server.sendmail(sender, [receiver], msg.as_string())
        server.quit()
        return True
    except Exception as e:
        st.warning(f"⚠️ 邮件发送失败: {str(e)}")
        return False


# ========== 表单 ==========
with st.form("suit_form"):
    # 1. 客户信息
    st.subheader("👤 客户信息")
    col1, col2, col3 = st.columns(3)
    name = col1.text_input("姓名 *", max_chars=20)
    phone = col2.text_input("手机号 *", max_chars=11)
    store = col3.text_input("所属门店", value="总部")

    # 2. 基础需求
    st.subheader("🧩 基础需求")
    process = st.selectbox(
        "工艺要求",
        [
            "精做粘合衬", "高定粘合衬", "半麻衬工艺", "全麻衬工艺", "手工半麻衬", "手工全麻衬",
            "半里布工艺", "无里布工艺", "半麻半里布", "半麻无里布", "全麻半里布", "全麻无里布",
            "特殊无里布/半里布", "需要沟通"
        ]
    )

    # 3. 上衣尺寸（inch）
    st.subheader("👕 上衣尺寸（单位：inch）")
    col1, col2, col3 = st.columns(3)
    chest = col1.number_input("胸围", min_value=28, max_value=60, value=37)
    waist_coat = col2.number_input("腰围", min_value=24, max_value=55, value=33)
    shoulder = col3.number_input("肩宽", min_value=12, max_value=24, value=18)
    sleeve = col1.number_input("袖长", min_value=20, max_value=32, value=24)
    cloth_length = col2.number_input("衣长", min_value=24, max_value=40, value=30)
    neck = col3.number_input("颈围", min_value=12, max_value=20, value=16)
    front_chest = col1.number_input("前胸", min_value=16, max_value=32, value=20)
    back = col2.number_input("后背", min_value=16, max_value=32, value=20)
    bust_point = col3.number_input("胸高", min_value=4, max_value=20, value=8)
    sleeve_width = col1.number_input("袖肥/臂围", min_value=8, max_value=24, value=12)
    bottom_hem_coat = col2.number_input("下摆", min_value=6, max_value=12, value=8)

    # 4. 上衣版型
    st.subheader("🎨 上衣版型")
    lapel_eye = st.selectbox("驳头凤眼款式", [
        "米兰眼", "机器凤眼", "撞色凤眼备注", "米兰眼未来之星", "米兰眼生命之旅", "米兰眼一心一意",
        "米兰眼无边无肯", "米兰眼方方圆圆", "米兰眼心心相印", "米兰眼事事如意", "米兰眼龙角型",
        "弧型米兰眼", "月牙型米兰眼", "机器真开眼", "无驳头凤眼", "真开米兰眼"
    ])
    lapel_style = st.selectbox("驳头领型", [
        "戗驳领", "平驳领", "细青果领", "中青果领", "大青果领", "内弧戗驳领", "内弧平驳领",
        "外弧戗驳领", "立领圆角", "立领方角", "中山装领圆角", "中山装领方角", "艾伦领",
        "戗驳领做黑色丁", "平驳领做黑色丁", "细青果领做黑色丁", "中青果领做黑色丁", "大青果领做黑色丁"
    ])
    front_closure = st.selectbox("门襟", [
        "单排1扣", "单排2扣", "单排3扣", "单排4扣", "单排5扣", "单排6扣",
        "双排2扣1", "双排4扣1", "双排6扣1", "双排4扣2", "双排6扣2", "双排8扣4", "双排10扣5", "双排8扣2"
    ])
    back_slit = st.selectbox("后叉", ["后中单开衩", "后侧双开衩", "后无衩"])
    hem_style = st.selectbox("下摆", ["下摆圆摆", "下摆直角", "下摆斜门襟直角"])
    lapel_width = st.selectbox("驳头宽度", [
        "5.5CM", "6CM", "6.5CM", "7CM", "8CM", "8.5CM", "9CM", "9.5CM", "10CM",
        "10.5CM", "11CM", "11.5CM", "12CM", "12.5CM", "13CM"
    ])
    handkerchief_pocket = st.selectbox("手巾袋形状", [
        "正常", "弧形袋", "船型袋", "刀型袋", "船型小圆角手巾袋", "贴胸袋", "色丁缎面手巾袋",
        "拼三分白缎手巾袋", "拼三分黑缎手巾袋", "拼三分本布手巾袋"
    ])
    side_pocket = st.selectbox("侧袋", [
        "平袋有袋盖", "斜袋有袋盖", "贴袋", "一字袋嵌线宽2cm", "双线袋", "斜双线袋",
        "双线袋色丁缎面", "平袋盖嵌线色丁缎面", "一字袋嵌线色丁缎面", "斜一字袋嵌线宽2cm", "月牙型双线袋"
    ])
    ticket_pocket = st.selectbox("小票袋款式", [
        "小平袋有盖", "小一字袋", "小双线袋", "小斜平袋有盖", "小斜双线袋", "小斜一字袋", "小贴袋", "无"
    ])
    cuff = st.selectbox("袖口", [
        "假衩假眼", "真袖衩真眼", "真袖衩斜扣眼", "假袖衩斜扣眼", "真袖衩2扣", "真袖衩3扣", "真袖衩4扣",
        "真袖衩5扣", "真袖衩6扣", "假袖叉2扣", "假袖叉3扣", "假袖衩4扣", "假袖衩5扣", "假袖衩6扣",
        "真斜袖衩真眼", "袖口撞色扣眼真衩真眼", "袖口撞色扣眼假衩", "翻遍马蹄袖"
    ])
    lining_note = st.text_input("里布备注")
    coat_button = st.text_input("纽扣（上衣）")

    # 5. 裤子尺寸（inch）
    st.subheader("👖 裤子尺寸（单位：inch）")
    col1, col2, col3 = st.columns(3)
    waist_pants = col1.number_input("裤腰围", min_value=24, max_value=50, value=32)
    hip = col2.number_input("臀围", min_value=30, max_value=50, value=38)
    thigh = col3.number_input("大腿围", min_value=20, max_value=35, value=24)
    inseam = col1.number_input("内长", min_value=24, max_value=36, value=30)
    outseam = col2.number_input("外长", min_value=34, max_value=46, value=40)
    knee = col3.number_input("膝围", min_value=14, max_value=24, value=18)
    bottom_pants = col1.number_input("脚口", min_value=12, max_value=22, value=16)

    # 6. 裤子版型
    st.subheader("🩳 裤子版型")
    waist_style = st.selectbox("裤腰头", [
        "常规宝剑头", "圆腰头", "方腰头", "那不勒斯圆腰头双扣", "那不勒斯方腰头双扣", "无搭嘴",
        "长搭嘴12cm", "那不勒斯窄腰 单扣 长搭嘴12cm", "宽腰双扣", "宽腰单扣", "弹力腰 暗松紧",
        "好莱坞腰头", "女士弯腰"
    ])
    front_pleat = st.selectbox("裤子前褶", ["单褶", "双褶", "无褶", "3褶"])
    back_pocket = st.selectbox("裤子后口袋", [
        "双线袋", "一字袋", "无口袋", "左一字袋", "右一字袋", "左双线袋", "右双线袋"
    ])
    pants_lining = st.selectbox("裤里布", ["无夹里", "前夹里", "前后夹里"])
    hem_pants = st.selectbox("裤脚口", ["常规平边", "翻遍裤"])
    suspender_loops = st.selectbox("马王袢", ["有", "无"])
    pants_button = st.text_input("纽扣（裤子）")
    side_seam = st.selectbox("裤子侧缝", [
        "做1CM宽色丁", "做2CM宽色丁", "做3CM宽色丁", "正常"
    ])
    front_pocket = st.selectbox("前口袋", ["正常斜口袋", "月牙型口袋", "无口袋"])
    pants_note = st.text_area("注意（裤子）", height=80)

    # 7. 马甲版型
    st.subheader("🧥 马甲版型")
    vest_collar = st.selectbox("领型", [
        "假平驳领", "假戗驳领", "假青果领", "假大青果领", "V领", "特殊款式来图"
    ])
    vest_closure = st.selectbox("门禁", [
        "单排2扣", "单排3扣", "单排4扣", "单排5扣", "单排6扣", "单排7扣",
        "双排4扣2", "双排6扣2", "双排6扣3", "双排8扣4", "双排10扣4", "双排10扣5",
        "双排斜门襟5扣3", "双排8扣3", "双排斜门襟4扣2", "双排斜门襟6扣3", "双排斜门襟8扣4", "双排斜门襟8扣3", "双排斜门襟10扣5"
    ])
    vest_hem = st.selectbox("下摆", ["尖下摆", "直角下摆", "弧型尖下摆"])
    vest_side_pocket = st.selectbox("侧袋", [
        "双线袋", "一字袋嵌线宽2cm", "平袋有带盖", "无口袋", "贴袋"
    ])
    vest_back = st.selectbox("后背", [
        "后片本布有袢", "后片本布无袢", "后片色丁缎面有袢", "后片色丁缎面无袢",
        "后片撞色里布", "AB面", "自备里布扣子扣袢"
    ])
    vest_handkerchief = st.selectbox("手巾袋", ["有", "无", "贴袋", "双线袋", "一字袋", "船型袋"])
    vest_lapel_width = st.selectbox("驳头宽度", [
        "4c'm", "5c'm", "6c'm", "7c'm", "8c'm", "9c'm", "10c'm", "11c'm", "12c'm", "13c'm"
    ])

    # 8. 特殊体型
    st.subheader("📊 特殊体型（可多选）")
    body_features = st.multiselect(
        "请选择存在的体态特征",
        ["挺胸", "平胸", "斜肩", "冲肩", "平肩", "凹腰", "驼背", "肚大", "后围大", "宽松"]
    )

    # 9. 客户图片
    st.subheader("📸 客户图片")
    uploaded_files = st.file_uploader("上传客户图片（可多张）", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

    # 10. 其他说明
    st.subheader("📝 其他说明")
    other_notes = st.text_area("其他说明", placeholder="例如：客户偏好、紧急程度、交付时间等")

    submitted = st.form_submit_button("✅ 提交登记")


# ========== 提交处理 ==========
if submitted:
    if not name or not phone:
        st.error("❌ 请填写姓名和手机号！")
    else:
        data = {
            "提交时间": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "姓名": name,
            "手机号": phone,
            "所属门店": store,
            "工艺要求": process,

            # 上衣尺寸（inch）
            "胸围 (inch)": chest,
            "腰围 (inch)": waist_coat,
            "肩宽 (inch)": shoulder,
            "袖长 (inch)": sleeve,
            "衣长 (inch)": cloth_length,
            "颈围 (inch)": neck,
            "前胸 (inch)": front_chest,
            "后背 (inch)": back,
            "胸高 (inch)": bust_point,
            "袖肥/臂围 (inch)": sleeve_width,
            "下摆 (inch)": bottom_hem_coat,

            # 上衣版型
            "驳头凤眼款式": lapel_eye,
            "驳头领型": lapel_style,
            "门襟": front_closure,
            "后叉": back_slit,
            "下摆（上衣）": hem_style,
            "驳头宽度（上衣）": lapel_width,
            "手巾袋形状": handkerchief_pocket,
            "侧袋（上衣）": side_pocket,
            "小票袋款式": ticket_pocket,
            "袖口": cuff,
            "里布备注": lining_note,
            "纽扣（上衣）": coat_button,

            # 裤子尺寸（inch）
            "裤腰围 (inch)": waist_pants,
            "臀围 (inch)": hip,
            "大腿围 (inch)": thigh,
            "内长 (inch)": inseam,
            "外长 (inch)": outseam,
            "膝围 (inch)": knee,
            "脚口 (inch)": bottom_pants,

            # 裤子版型
            "裤腰头": waist_style,
            "裤子前褶": front_pleat,
            "裤子后口袋": back_pocket,
            "裤里布": pants_lining,
            "裤脚口": hem_pants,
            "马王袢": suspender_loops,
            "纽扣（裤子）": pants_button,
            "裤子侧缝": side_seam,
            "前口袋": front_pocket,
            "注意（裤子）": pants_note,

            # 马甲版型
            "领型（马甲）": vest_collar,
            "门禁（马甲）": vest_closure,
            "下摆（马甲）": vest_hem,
            "侧袋（马甲）": vest_side_pocket,
            "后背（马甲）": vest_back,
            "手巾袋（马甲）": vest_handkerchief,
            "驳头宽度（马甲）": vest_lapel_width,

            # 特殊体型 & 其他
            "特殊体型": ", ".join(body_features),
            "其他说明": other_notes
        }

        image_count = len(uploaded_files) if uploaded_files else 0

        if send_email(data, image_count):
            st.success("✅ 登记成功！数据已发送至你的邮箱。")
            st.balloons()
        else:
            st.warning("⚠️ 提交成功，但邮件未送达，请检查配置。")
