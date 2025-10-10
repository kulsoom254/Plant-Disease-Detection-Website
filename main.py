import os
import streamlit as st
import google.generativeai as genai
from langchain.prompts import PromptTemplate
from datetime import datetime
from PIL import Image

genai.configure(api_key="AIzaSyB6p0bLwFyqiRQKNyWCKwCPLT3col91qlk")



def set_background():
    leafy_img_url = "hhttps://www.google.com/search?source=lns.web.cntpubb&vsdim=512,471&gsessionid=L2t2HYJzv5D2oEKEOT05LmctQl_feu1rm6Eo_GBfap0W0oBjuZa_pQ&lsessionid=TZ9i3COcEYs_HrwUvOgr3ZvSJ1gycFjUuehcGJYbHg1EGZQSyUvrOw&lns_surface=44&biw=512&bih=471&hl=en-US&vsrid=CIaQ_YWdroeNfRAGGAEiJDQxNTc1NEE0LTcwMTItNDQxNS1COTdCLUY0NTJDQTRCMkU4NjIGIgJzZCgeOMHD3cvO0o8D&udm=26&q&vsint=CAQqCgoCCAcSAggBIAE6IwoWDTTXMT8VFqQBPx23nOs-JQAAAD8wARCABBjXAyUAAIA_&lns_mode=un&qsubts=1757659159969&stq=1&cs=1&lei=EcDDaIeIHNmOseMPmuLqiQk"  # Use a direct PNG image link
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: #e6f7e6;
            background-image: url("{leafy_img_url}");
            background-size: 200px 200px;
            background-repeat: repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_background()

st.title("🌿 PLANT DOCTOR 🌿")

uploaded_file = st.file_uploader("Choose a plant image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    prompt = """
You are Plant Doctor.
You are tasked with diagnosing the health of the plant in the image.
If the plant is healthy, tell it is healthy and what can be done to make the improvements. ELse, What is the diagnosis and what is the treatment?
Today's date is {date}.
Mention on which dates what has to be done from today like a prescription.
Also Mention when should be the next checkup.
"""

    prompt_template = PromptTemplate(template=prompt)
    formatted_prompt = prompt_template.format(date=current_date)

    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content([image, formatted_prompt])

    st.subheader("Diagnosis and Prescription")
    st.write(response.text)