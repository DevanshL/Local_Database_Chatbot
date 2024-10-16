# Gemini-Powered SQL Query Bot

## Overview

This is an AI-powered SQL query bot that generates SQL queries from natural language questions. The bot leverages Google's Gemini AI to translate user questions about a database into SQL queries and returns the corresponding data. It's built using Python, Streamlit for the frontend, and Google Generative AI for the query generation.

![Chat Interface](/home/devansh/Pictures/img1_sql.png) 

## Features

- Natural language input to SQL conversion
- Query execution and result display
- Chat history for tracking interactions
- Easy-to-use interface with conversational flow

## Technologies Used

- **Streamlit**: A Python framework for building web applications.
- **Google Generative AI (Gemini)**: Used to convert natural language into SQL queries.
- **Python**: For backend logic and data processing.
- **MySQL**: The database for executing SQL queries.
  
Application chat       |  Database check
:-------------------------:|:-------------------------:
![App output](/home/devansh/Pictures/img2_sql.png)  |  ![Database output](/home/devansh/Pictures/output.png)


## Setup Instructions

### Prerequisites

- Python 3.x installed
- Virtual environment (optional but recommended)
- A Google Cloud account with access to Generative AI APIs
- MySQL or PostgreSQL database configured

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/sql-query-bot.git
   cd sql-query-bot
   ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Configure environment variables:**
    * Create a .env file in the root of your project with the following details:
    ```bash
    GOOGLE_API_KEY=<your_google_api_key>
    MYSQL_USER=<your_mysql_username>
    MYSQL_PASSWORD=<your_mysql_password>
    MYSQL_DATABASE=<your_database_name>
    MYSQL_HOST=<your_mysql_host>
    ```

4. **To Run Application**:
    ```bash
    streamlit run app.py
    ```

5. **Interact with the SQL Query Bot:**:
    * Open your browser and navigate to the Streamlit app (http://localhost:8501 by default).
    * Ask questions about your database, and the bot will generate and execute SQL queries based on your inputs.

### How it Works
* `Input`: User types a natural language question (e.g., "How many employees are there?").

* `Gemini AI`: The query is processed by Google Gemini to generate the appropriate SQL statement.

* `Query Execution`: The generated SQL query is executed against the connected MySQL or PostgreSQL database.

* `Result`: The query results are displayed in the app, and the interaction is stored in the chat history.

## Contributions

Feel free to fork this repository and submit pull requests to enhance the bot or fix bugs. We welcome all contributions!

## License

This project is licensed under the MIT License. See the LICENSE file for details.

