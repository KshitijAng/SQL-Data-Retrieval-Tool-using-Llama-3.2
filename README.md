# SQLite Data Retrieval Tool using Llama 3.2

This project implements a simple local Streamlit-based application that leverages the Llama 3.2 model to convert English questions into SQL queries. It works with a SQLite database containing information about employees and departments. The assistant generates SQL queries based on user input and retrieves corresponding data from the database.

## Features

- Users can input questions related to employee and department data.
- The Llama 3.2 model converts these questions into SQL queries.
- The generated SQL queries are executed on a SQLite database (`company.db`) to retrieve data.
- The results are displayed in the Streamlit app.


## How the Assistant Works

### Llama Model Integration
The assistant uses the Llama 3.2 model via Ollama to convert user questions into SQL queries. It takes the question, appends it to a pre-defined prompt, and sends it to the Llama model for processing.

### SQL Query Execution
The generated SQL query is executed on the SQLite database (`company.db`) which is created after running sql1.py. The database contains two tables:

- **EMPLOYEES**: Stores employee information such as ID, Name, Department, Salary, and Hire Date.
- **DEPARTMENTS**: Stores department details like ID, Name, and Manager.

### Displaying Results
After executing the SQL query, the results are returned and displayed in the Streamlit interface.

## Steps to Run the Project Locally

### Prerequisites

- Python 3.7 or higher
- Streamlit
- SQLite
- Langchain
- Ollama model (for Llama 3.2)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repository-name.git
   cd your-repository-name
   ```

2. Install the required Python libraries:

    ```bash
    pip install -r requirements.txt
   ```

3. Run sql1.py: This creates a `company.db` file
    ```bash
    python run sql1.py
    ```

4. Finally run app1.py file using streamlit and Ollama:
    ```bash
    streamlit run app1.py
    ```

**Note: Ollama must be kept running back in the background to access the model.**
