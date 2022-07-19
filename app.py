from email.mime import image
from multiprocessing.sharedctypes import Value
import streamlit as st
st.title("Welcome to Streamlit")
st.header("Demo of Stream App")
st.text("Hello Everyone")
st.markdown("Markdown")
st.success("Successful")
st.info("I am Information")
st.warning("I am worning")
st.error("You have entered wrong value")
st.exception("Nameerror('Div zero error')")

from PIL import Image
img=Image.open("1.png")
st.image(img,width=500,caption='Graph')
status=st.checkbox("show/Hide")
st.text("Showing")
status1=st.radio("what is your status",("Active","deactive"))
if status1=="Active":
    st.success("u r active")
else:
    st.warning(" U r not active")

occupation=st.selectbox("u R Occupation",["Programmer","DS","DE","DA","ML"])
st.write("U have selectted option",occupation)

## Multiset
location=st.multiselect("where do you work",("pune","Mumbai","Newyork","Delhi"))
st.write("You are selected",str(location))

# Slider
level=st.slider("What is your level",1,5)

#Buttons
#st.button("Click_me")
if st.button("click_ME"):
    st.text("Love You")

## input from user (Text_imput)
fname=st.text_input("Enter First name","Type here")
if st.button("Submit_name"):
    result=fname.title()
    st.success(result)

## Balloons
st.balloons()
st.header("Thank u")

## Functions
def run_fun():
    n1=st.text_input("Enter 1st no")
    n2=st.text_input("Enter second number")
    if st.button("Click me for ADD"):
        sum=int(n1)+int(n2)
        st.write("Addition is",sum)
    else:
        st.warning("Not added")
st.write(run_fun())
df={"Name":["A","B","C","D","E","F"],
    "Gender":["MAle","Female","MAle","Female","Male","Male"],
    "Mark":[23,33,55,66,88,12]}   
st.dataframe(df) 
   



