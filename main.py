import streamlit as st
from transformers import AutoTokenizer, TFAutoModelForSequenceClassification
import tensorflow as tf

def predict(text, model, tokenizer):
    encoding = tokenizer(text, truncation=True, padding=True, max_length=500, return_tensors='tf')

    prediction = model(encoding)
    pred_label = tf.argmax(prediction.logits, axis=1).numpy()[0]

    label = {0: "HAM", 1: "SPAM"}
    return label[pred_label]


st.set_page_config(layout="wide")
path = 'iqbalpurba26/indobert-ham-spam-detection'
tokenizer = AutoTokenizer.from_pretrained(path)
model = TFAutoModelForSequenceClassification.from_pretrained(path)

st.title("SMS HAM OR SPAM DETECTION USING INDOBERT")

st.write('Mau tau pesan yang kamu dapat SPAM atau HAM? Yuk masukin teks nya ke form dibawah ini.')
st.write('Eiiits... teksnya berbahasa indonesia yaa')

input_text =st.text_area("", height=100)

if st.button("Cek Yuk"):
    if input_text:
        with st.spinner("Tunggu sebentar yaa.. Model sedang mempediksi"):
            categories = predict(input_text, model, tokenizer)

            if categories == 'SPAM':
                st.markdown(
                f"<h5 style='color:red;'> Pesan yang anda terima terdeteksi {categories}. Berhati-hati untuk membalas yaa...</h5>",
                unsafe_allow_html=True
            )
            else:
                st.markdown(
                f"<h5 style='color:green;'> Pesan yang anda terima terdeteksi {categories}. Silahkan dibalas</h5>",
                unsafe_allow_html=True
            )
        
            





