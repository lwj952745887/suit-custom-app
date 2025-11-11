import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="西服定制登记系统", layout="wide")
st.title("👔 西服定制客户登记表")

# 表单
with st.form("suit_form"):
    # 客户信息
    st.subheader("👤 客户信息")
    col1, col2, col3 = st.columns(3)
    name = col1.text_input("姓名 *", max_chars=20)
    phone = col2.text_input("手机号 *", max_chars=11)
    store = col3.text_input("所属门店", value="总部")

    # 基础尺寸
    st.subheader("📏 基础尺寸")
    col1, col2 = st.columns(2)
    height = col1.number_input("身高 (cm)", min_value=140, max_value=220, value=175)
    weight = col2.number_input("体重 (kg)", min_value=30, max_value=200, value=70)

    # 上衣尺寸
    st.subheader("👕 上衣尺寸")
    col1, col2, col3 = st.columns(3)
    chest = col1.number_input("胸围 (cm)", min_value=70, max_value=150, value=95)
    waist_coat = col2.number_input("腰围 (cm)", min_value=60, max_value=140, value=85)
    shoulder = col3.number_input("肩宽 (cm)", min_value=30, max_value=60, value=45)
    sleeve = col1.number_input("袖长 (cm)", min_value=40, max_value=80, value=60)
    length = col2.number_input("衣长 (cm)", min_value=50, max_value=90, value=75)

    # 裤装尺寸
    st.subheader("👖 裤装尺寸")
    col1, col2, col3 = st.columns(3)
    waist_pants = col1.number_input("裤腰围 (cm)", min_value=60, max_value=140, value=85)
    hip = col2.number_input("臀围 (cm)", min_value=70, max_value=150, value=100)
    inseam = col3.number_input("内裤长 (cm)", min_value=60, max_value=100, value=80)
    thigh = col1.number_input("大腿围 (cm)", min_value=40, max_value=90, value=60)

    # 偏好设置
    st.subheader("🎨 定制偏好")
    fit = st.radio("版型偏好", ["修身", "标准", "宽松"], horizontal=True)
    fabric = st.selectbox("面料选择", ["精纺羊毛", "棉麻混纺", "意大利进口", "其他"])
    notes = st.text_area("特殊需求或备注", placeholder="例如：左肩稍高、喜欢短袖口等")

    # 提交按钮
    submitted = st.form_submit_button("✅ 提交登记")

# 处理提交
if submitted:
    if not name or not phone:
        st.error("❌ 请填写姓名和手机号！")
    else:
        # 构建数据行（未来可对接持久化存储）
        data = {
            "提交时间": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "姓名": name,
            "手机号": phone,
            "门店": store,
            "身高(cm)": height,
            "体重(kg)": weight,
            "胸围(cm)": chest,
            "上衣腰围(cm)": waist_coat,
            "肩宽(cm)": shoulder,
            "袖长(cm)": sleeve,
            "衣长(cm)": length,
            "裤腰围(cm)": waist_pants,
            "臀围(cm)": hip,
            "内裤长(cm)": inseam,
            "大腿围(cm)": thigh,
            "版型偏好": fit,
            "面料选择": fabric,
            "备注": notes
        }

        # 暂存到会话状态（重启会丢失，后续可加持久化）
        if "records" not in st.session_state:
            st.session_state.records = []
        st.session_state.records.append(data)

        st.success("✅ 登记成功！感谢您的定制需求。")
        st.balloons()
