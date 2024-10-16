import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from sql import execute_query

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    
    print(response)
    
    if hasattr(response, 'parts'):
        return ' '.join(part.text for part in response.parts).strip()
    else:
        raise ValueError("Unexpected response structure from Gemini AI.")

# Define the AI prompt
prompt = [
    """
    You are an expert in converting English questions to SQL queries!
    The SQL database has the following tables:
    - Album: AlbumId, Title
    - Track: TrackId, Name, AlbumId, MediaTypeId, GenreId, Composer, Milliseconds, Bytes, UnitPrice
    - Artist: ArtistId, Name
    - Genre: GenreId, Name
    - MediaType: MediaTypeId, Name
    - Playlist: PlaylistId, Name
    - PlaylistTrack: PlaylistId, TrackId
    - Customer: CustomerId, FirstName, LastName, Country
    - Invoice: InvoiceId, CustomerId, InvoiceDate, Total
    - InvoiceLine: InvoiceLineId, InvoiceId, TrackId, UnitPrice, Quantity
    - Employee: EmployeeId, LastName, FirstName, Title, ReportsTo, BirthDate, HireDate, Address, City, State, Country, PostalCode, Phone, Fax, Email

    Example 1:
    Question: How many albums are there?
    SQL Query: SELECT COUNT(*) FROM Album;

    Example 2:
    Question: What are the titles of all albums?
    SQL Query: SELECT Title FROM Album;

    Example 3:
    Question: Who are the artists in the database?
    SQL Query: SELECT Name FROM Artist;

    Generate SQL without any code block markers.
    """
]

st.set_page_config(page_title="SQL Query Bot", layout="centered")
st.header("Gemini-Powered SQL Query Bot")

question = st.text_input("Ask a question about the database:", key="input")

# Button to trigger the bot
if st.button("Get SQL Query and Data"):
    # Generate SQL query using Google Gemini AI
    sql_query = get_gemini_response(question, prompt)
    st.subheader("Generated SQL Query")
    st.code(sql_query, language='sql')

    try:
        results = execute_query(sql_query)
        if results:
            st.subheader("Query Results")
            for row in results:
                st.write(row)
        else:
            st.write("No results found.")
    except Exception as e:
        st.error(f"Error executing query: {e}")