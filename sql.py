import os
from dotenv import load_dotenv
import streamlit as st
import sqlite3
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))


def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-1.5-pro')

    response = model.generate_content([prompt[0],question])

    return response.text


def read_sql_query(sql, db:str):
    connect = sqlite3.connect(db)
    cursor = connect.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    connect.commit()
    connect.close()
    return rows


prompt = '''
You are an expert in converting English questions to SQL query!
The SQL database has name STUDENT and has the following columns - NAME, CLASS,
SECTION \n\n For example, \n Example 1 -How many entries of records are present?,
the SQL command will be something like this SECLECT COUNT(*) FROM STUDENT;
\nExample 2 - Tell me all the students studying in Data Science class?,
the SQL command will be something like this SELECT * FROM STUDENT where CLASS="Data Science";
also the sql code should not have ``` in beginning or end and sql word in output 

'''

st.set_page_config(page_title='Retrival Any SQl Query')

st.header('Gemini App to Retrival SQL Data')

question = st.text_input(label="Input", key='input')

submit = st.button(label="Ask some questions...")

if submit:
    response = get_gemini_response(question=question,prompt=prompt)
    print(response)
    response = read_sql_query(sql=response,db='student.db')

    st.subheader('The response:')

    for row in response:
        print(row)

        st.header(row)

    

