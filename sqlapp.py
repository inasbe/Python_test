import sqlite3

# Connect to database (or create it)
conn = sqlite3.connect("test.db")
cursor = conn.cursor()

# Create a sample table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    department TEXT,
    salary REAL
)
""")

# Insert sample data
cursor.executemany("INSERT INTO employees (name, age, department, salary) VALUES (?, ?, ?, ?)", [
    ("Alice", 30, "HR", 50000),
    ("Bob", 25, "IT", 60000),
    ("Charlie", 35, "Finance", 70000)
])

conn.commit()
conn.close()

import sqlite3

def run_query(query):
    try:
        conn = sqlite3.connect("test.db")
        cursor = conn.cursor()
        
        cursor.execute(query)  # Execute query
        results = cursor.fetchall()  # Fetch results
        
        conn.commit()
        conn.close()
        
        return results
    except Exception as e:
        return f"Error: {e}"

# Example usage
user_query = "SELECT * FROM employees;"
print(run_query(user_query))

import time

def analyze_query(query):
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()

    start_time = time.time()
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        execution_time = time.time() - start_time
    except Exception as e:
        return f"Error: {e}"
    
    conn.close()

    # Basic optimization: Check for SELECT *
    suggestions = []
    if "SELECT *" in query.upper():
        suggestions.append("Avoid SELECT *, specify columns instead.")

    return {
        "results": results,
        "execution_time": execution_time,
        "suggestions": suggestions
    }

# Example usage
query = "SELECT * FROM employees;"
print(analyze_query(query))


import streamlit as st

st.title("SQL Query Analyzer")

query = st.text_area("Enter your SQL query")

if st.button("Run Query"):
    result = analyze_query(query)
    st.write(f"Execution Time: {result['execution_time']:.4f} seconds")
    st.write("Results:", result["results"])
    
    if result["suggestions"]:
        st.write("Optimization Suggestions:")
        for suggestion in result["suggestions"]:
            st.write(f"- {suggestion}")