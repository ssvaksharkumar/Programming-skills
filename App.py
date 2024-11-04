import streamlit as st
st.title("Title ----> Geeks for Geeks")
st.header("Header ---> Geeks for Geeks")
st.subheader("Subheader ----> Geeks for Geeks")
st.text("Text -----> Geeks for Geeks")

st.markdown("# Hi")
st.markdown("## Hi")
st.markdown("### Hi")
st.markdown("#### Hi")

st.success("Success!")
st.info("Information!")
st.warning("Warning!")
st.error("Error!")
st.exception(ZeroDivisionError("Division not possible with 0"))

st.subheader("Help")
st.help(ZeroDivisionError)

st.subheader("Write")
st.write("range(1,10)")
st.write(range(1,10))
st.write("1*2*3")
st.write(1*2*3)

st.subheader("Code")
st.code(" x = 10 \n"
        "for i in range(x):\n"
        "\tprint(i)")

st.subheader("Checkbox")
st.checkbox("Male")
if(st.checkbox("Adult")):
    st.write("You are an Adult")

st.subheader("Radiobutton")
RadioButton = st.radio("Select :",("Male","Female","Other"))
if(RadioButton == "Male"):
    st.write("You are Male")
elif(RadioButton == "Female"):
    st.write("You are Female")
elif(RadioButton == "Other"):
    st.write("You are Other")

st.subheader("SelectBox")
Select = st.selectbox("Enter Data Science Category:", ["Data Analysis", "Machine Learning", "Natural Language Processing", "Web Scraping", "Data Processing"])
st.write("Enter you have selected:", Select)

st.subheader("MultiselectBox")
Multiselect = st.multiselect("Enter Data Science Category:", ["Data Analysis", "Machine Learning", "Natural Language Processing", "Web Scraping", "Data Processing"])
st.write("Enter you have selected:", len(Multiselect), "courses")

st.subheader("Button")
if(st.button("Click me")):
    st.write("Thanks for clicking me!")

st.subheader("Slider")
Slider_value = st.slider("Enter the Volume:", 0, 100, step = 1)
st.write("Your selected value is:", Slider_value)

st.subheader("TextInput")
Text = st.text_input("Enter your username:")
st.write("Hi", Text)
st.text_input("Enter your Password:", type = "password")

st.subheader("Text Area")
st.text_area("Write something about yourself")

st.subheader("Input Number")
st.number_input("Enter your Age:", 18, 110)

st.subheader("Input Date")
st.date_input("Enter your date:")

st.subheader("Input Time")
st.time_input("Enter your time:")