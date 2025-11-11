# 文件名：app.py
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="西服定制登记", layout="centered")
st.title("👔 西服客户尺码登记系统")

with st.form("customer_form"):
    name = st.text_input("👤 客户姓名 *", placeholder="张三")
    phone = st.text_input("📱 手机号码 *", placeholder="13800138000")
    shoulder = st.number_input("📏 肩宽 (cm)", min_value=30.0, max_value=60.0, value=44.0)
    chest = st.number_input("🫁 胸围 (cm)", min_value=70.0, max_value=150.0, value=96.0)
    waist = st.number_input("🩳 腰围 (cm)", min_value=60.0, max_value=130.0, value=84.0)
    note = st.text_area("📝 备注（如特殊体型、偏好等）")
    submitted = st.form_submit_button("✅ 提交客户信息")

if submitted:
    if not name or not phone:
        st.error("❌ 姓名和电话为必填项！")
    else:
        # 准备数据
        new_data = pd.DataFrame([{
            "姓名": name,
            "电话": phone,
            "肩宽(cm)": shoulder,
            "胸围(cm)": chest,
            "腰围(cm)": waist,
            "备注": note
        }])
        
        # 保存到 CSV
        file = "customers.csv"
        if os.path.exists(file):
            new_data.to_csv(file, mode='a', header=False, index=False)
        else:
            new_data.to_csv(file, index=False)
        
        st.success(f"🎉 {name} 的信息已成功提交！")
        st.balloons()

# 查看数据（仅你作为管理员使用）
st.divider()
if st.checkbox("🔒 管理员：查看所有客户数据"):
    if os.path.exists("customers.csv"):
        df = pd.read_csv("customers.csv")
        st.dataframe(df, use_container_width=True)
        # 可加导出按钮（进阶）
    else:
        st.info("暂无客户数据")