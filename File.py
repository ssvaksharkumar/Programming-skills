import streamlit as st
import pandas as pd

st.subheader("Uploading the CSV File")
df = st.file_uploader("Uploading the CSV File", type = ["csv","xlsx"])

st.subheader("Reading the CSV File")
df = pd.read_csv("Products.csv")
if df is not None:
    st.table(df.head())

st.subheader("Displaying the image file")
st.image("img.png")

st.subheader("Uplading the image file")
Img = st.file_uploader("Uploading the Image file", type = ["png","jpeg"])
if Img is not None:
    st.image(Img)


st.subheader("Uploading the video file")

Video_file = st.file_uploader("Uploading the Video file", type = ["mp4","mpv"])
if Video_file is not None:
    st.video(Video_file, start = 0)

st.subheader("Uploading the Audio files")

audio_files = st.file_uploader("Uploading the Audio files", type = ["mp3","mev"])
if audio_files is not None:
    st.audio(audio_files)
