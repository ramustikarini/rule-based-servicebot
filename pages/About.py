import streamlit as st
import pandas as pd

st.title(':blue[$About$ $This$ $Bot$]')
#st.divider()
with st.container(border=True):
    st.markdown('''I'm a service bot to help you get the information needed regarding our dental clinic. I can only 
            serve and answer questions about our clinic and services because I'm a rule-based chatbot.
            I have limited knowledge, but my creator will keep on feeding me informations and new command if necessary. 
            I'm sorry for the inconvinience if there are some questions I can't answer.''')

data = {
    "Command":["Schedule", "Registration", "Location", "Services"],
    "Description": ["Information of the clinic's schedule","Information for registration and appointment","Information of the clinic's location","Information of the available services and treatments"]
}

"The informations you can get from me are:"
df = pd.DataFrame(data)
st.dataframe(df, hide_index=True, use_container_width=True)