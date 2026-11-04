import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from prompts import bioinformatics_prompt, parser


load_dotenv()


def get_llm():
    
    api_key = (
        os.getenv("GEMINI_API_KEY") 
        or st.secrets.get("GEMINI_API_KEY")
    )

    if not api_key:
        raise ValueError("Google Gemini API key not found.")

    model_name = (
        os.getenv("MODEL_NAME")
        or st.secrets.get("MODEL_NAME", "gemini-3.5-flash")
    )

    llm = ChatGoogleGenerativeAI(
        model=model_name,
        google_api_key=api_key,
        temperature=0.3
    )

    return llm


def generate_bioinformatics_answer(
    question,
    audience_level,
    answer_style,
    include_examples,
    include_tools
):

    llm = get_llm()

    chain = bioinformatics_prompt | llm | parser

    response = chain.invoke({

        "question": question,
        "audience_level": audience_level,
        "answer_style": answer_style,
        "include_examples": include_examples,
        "include_tools": include_tools

    })

    return response
