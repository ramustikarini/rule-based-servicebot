import streamlit as st
import json
import os
import csv
import random

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#JSON
with open("rules.json", "r") as file:
    rules = json.load(file)

#preprocess
intents = []
inputs = []
for rule in rules:
    for input in rule['query']:
        intents.append(rule['intent'])
        inputs.append(input)

#interface
with st.container(border=True):
    st.title(':blue[$Clinic$ $Service Bot$]')
    intro =('I am a clinic service bot. Please ignore if there is an attribute error and start your conversation in the chat box.')
    st.markdown(f'{intro}') 

#tumpuk chat/ mempertahankan chat utk setiap sesinya
if 'messages' not in st.session_state:
  st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#input bot
  
user_input = st.chat_input(placeholder="Type your message")

 
if user_input:
        with st.chat_message("User"):
            st.markdown(user_input)
        st.session_state.messages.append({'role': 'User', 'content':user_input})

#fungsi input-response
def rule_based_servicebot(input_text):
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(inputs)
    input_text = vectorizer.transform([input_text])
    similarities = cosine_similarity(input_text, tfidf)
    most_similar_index = similarities.argmax()
    max_similarity = similarities[0, most_similar_index]

    batas = 0.5
    if max_similarity < batas:
        return "I'm sorry, I don't have the answer for that question. For more information please contact **(number)**."
    
    intent = intents[most_similar_index]
    for rule in rules:
        if rule['intent'] == intent:
            response = random.choice(rule['responses'])
            return response

#respon bot
responses = rule_based_servicebot(user_input)
with st.chat_message("Assistant"):
    st.markdown(responses)
st.session_state.messages.append({'role': 'Assistant', 'content':responses})

#bikin chat log
if not os.path.exists('chat_history.csv'):
    with open('chat_history.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['User Input', 'Bot Response'])

#simpan chat history
with open('chat_history.csv', 'a', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow([user_input, responses])