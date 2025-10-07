from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage,HumanMessage
from dotenv import load_dotenv
import streamlit as st

# Load environment variables
load_dotenv()

# Initialize model
model=ChatOpenAI(model='gpt-5')

# Create prompt template
chat_template=ChatPromptTemplate(
    [
    ('system',"you are a helpful and experienced {domain} expert"),
    ('human',"Explain in simple terms, what is {topic}")
    ]
)

# Streamlit UI
# Giving a title to app 
st.title('Data Science Research Tool')

# Asking for a data science topic from user 
topic=st.text_input('Enter Any Data Science Topic ')



# Creating a search button 
if st.button('Search'):
    prompt=chat_template.invoke({'domain':'Data Science','topic':topic})
    response=model.invoke(prompt)
    # Writing the model response
    st.write(response.content)


