import streamlit as st
import json

# Step 1: 載入 JSON 資料
with open("fda_drug_info_sample.json", "r", encoding="utf-8") as f:
    fda_data = json.load(f)

# Step 2: Streamlit 使用介面
st.title("💊 GPT 藥師（FDA 資料版）")

# 使用者輸入欄位
query = st.text_input("請輸入藥品英文名稱（Generic Name 或 Brand Name）")

# 查詢邏輯
if query:
    found = False
    for drug_id, info in fda_data.items():
        if query.lower() in info.get("generic_name", "").lower() or \
           query.lower() in info.get("brand_name", "").lower():
            st.subheader(f"🧬 {info.get('brand_name') or info.get('generic_name')}")
            st.markdown(f"**適應症 (Indications)**：\n{info['indications']}")
            st.markdown(f"**劑量 (Dosage)**：\n{info['dosage']}")
            st.markdown(f"**副作用 (Adverse Effects)**：\n{info['adverse_effects']}")
            st.markdown(f"**禁忌症 (Contraindications)**：\n{info['contraindications']}")
            st.markdown(f"**警告 (Warnings)**：\n{info['warnings']}")
            st.markdown(f"[資料來源]({info['source']})")
            found = True
            break
    if not found:
        st.warning("❌ 查無此藥品，請確認英文拼字")
