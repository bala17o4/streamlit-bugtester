import streamlit as st
from textinput import *
from file import *
st.title("Bug Tester")




def tab1():

    inputab1, inputab2 = st.tabs(["Text Input","File upload"])
    with inputab1:
        with st.form('Input Form',clear_on_submit=True):
            st.header("text")
            id = st.text_input("ID*")
            market = st.text_input("By Market")
            data = st.text_area("Data")
            date = st.date_input("Last Updated Date")
            time = st.time_input("Last Updated Time")
            choice = st.selectbox("Status of the bug",('OPEN','IN PROGRESS','FIXED','RETESTED','CLOSED'))
            if st.form_submit_button("Submit"):
                if not id:
                    st.warning("Enter ID")
                elif(id in df.values):
                    st.warning("Record already exists")
                else:
                    add_data(id,market,data,date,time,choice)
    with inputab2:
        with st.form('Input form', clear_on_submit=True):
            file = st.file_uploader('Drop the excel file', type = ['csv','xlsx'])
            id = st.text_input("column name for id")
            market = st.text_input("column name for market")
            data = st.text_input("column name for data")
            date_time = st.text_input("column name for last updated")
            status = st.text_input("column name for status")
            if st.form_submit_button("Submit"):
                if not file or not id or not market or not data or not date_time or not status:
                    st.warning("Fill all the fields")
                else:
                    file_add_data(file,id,market,data,date_time,status)
            

def tab2():
    summarytab1, summarytab2 = st.tabs(["Data","Summary"])
    with summarytab1:
        dis = display()
        st.dataframe(dis, use_container_width=True)
    with summarytab2:
        summary = summarize()
        st.dataframe(summary, use_container_width=True)
        # pass

def tab3():
    pass

pages_to_func = {
    "Input": tab1,
     "Summary":tab2,
      "Update":tab3
}
pages = st.sidebar.selectbox(" ",pages_to_func.keys())
pages_to_func[pages]()
