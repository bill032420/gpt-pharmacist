# gpt-pharmacist
GPT 臨床藥師助理 Klin
import streamlit as st

# 定義藥品資料庫
drug_info = {
    "Amlodipine": {
        "適應症": "高血壓、慢性穩定型心絞痛",
        "副作用": "下肢水腫、頭痛、潮紅",
        "禁忌症": "對 dihydropyridine 類藥物過敏者",
        "來源": "TFDA / drugtw.com"
    },
    "Metformin": {
        "適應症": "第二型糖尿病",
        "副作用": "腸胃不適、腹瀉、乳酸中毒風險（腎功能不良時）",
        "禁忌症": "eGFR < 30, 代謝性酸中毒",
        "來源": "TFDA / drugtw.com"
    },
    "Warfarin": {
        "適應症": "心房顫動、血栓預防",
        "副作用": "出血、紫癜、皮膚壞死",
        "禁忌症": "懷孕、活動性出血",
        "來源": "TFDA / drugtw.com"
    },
    "Atorvastatin": {
        "適應症": "高膽固醇血症、心血管疾病預防",
        "副作用": "肝酵素上升、肌肉痠痛、腹瀉",
        "禁忌症": "肝病、懷孕、哺乳",
        "來源": "TFDA / drugtw.com"
    },
    "Omeprazole": {
        "適應症": "胃潰瘍、GERD、除幽門桿菌",
        "副作用": "腹瀉、頭痛、B12 缺乏（長期使用）",
        "禁忌症": "對 benzimidazole 過敏",
        "來源": "TFDA / drugtw.com"
    }
}

st.title("💊 GPT 藥師 Demo")

question = st.text_input("請輸入藥物名稱（英文）：")

if question:
    drug = drug_info.get(question.strip().title())
    if drug:
        st.subheader(f"📋 {question.strip().title()} 的藥品資訊")
        st.markdown(f"**適應症**：{drug['適應症']}")
        st.markdown(f"**常見副作用**：{drug['副作用']}")
        st.markdown(f"**禁忌症**：{drug['禁忌症']}")
        st.markdown(f"**資料來源**：{drug['來源']}")
    else:
        st.warning("找不到該藥品，請確認輸入的英文藥名正確。")
streamlit
