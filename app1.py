from langchain_community.llms import Ollama
from langchain_core.messages import HumanMessage, SystemMessage
import streamlit as st
import sqlite3


def get_llama_response(question, prompt):
    llm = Ollama(model="llama3.2:1b") 
    response = llm.invoke(f"{prompt[0]}\n{question}").strip()
    response = response.replace("```sql", "").replace("```", "").strip()
    return response  


def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows


# Define Prompt
prompt = [
    """
    You are an expert in converting English questions into SQL queries.
    The SQL database has two tables: EMPLOYEES and DEPARTMENTS.

    EMPLOYEES table has the following columns: ID, Name, Department, Salary, Hire_Date.
    DEPARTMENTS table has the following columns: ID, Name, Manager.

    For example:

    Example 1 - "Show me all employees in the Sales department."
    SQL Query: SELECT Manager FROM EMPLOYEES WHERE DEPARTMENTS = "Sales";

    Example 2 - "Who is the manager of the Engineering department?"
    SQL Query: SELECT Manager FROM DEPARTMENTS WHERE Name = "Engineering";

    Example 3 - "List all employees hired after 2021-01-01."
    SQL Query: SELECT Name FROM EMPLOYEES WHERE Hire_Date > "2021-01-01";

    Example 4 - "What is the total salary expense for the Marketing department?"
    SQL Query: SELECT SUM(Salary) FROM EMPLOYEES WHERE DEPARTMENTS = "Marketing";

    Your task is to generate only the SQL query (no explanations or additional text).
    Do not include any code block delimiters (` ``` `) or the word "sql" in the output.
    The query must be executable and can contain extraneous text.
    """
]


## Streamlit App
st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("SQL Data Retrieval Tool using Llama 3.2")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

# if submit is clicked
if submit:
    response=get_llama_response(question,prompt)
    print(response)
    response=read_sql_query(response,"company.db")
    st.subheader("The Response is")
    for row in response:
        print(row)
        st.header(str(row))