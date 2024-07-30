import os
from dotenv import load_dotenv
import streamlit as st
import sqlite3
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))


def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-1.5-pro')

    response = model.generate_content([question, prompt])

    return response.text


def read_sql_query(sql, db):
    connect = sqlite3.connect(db)
    cursor = connect.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    return rows



    