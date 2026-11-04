# AI Bioinformatics Guide
https://ai-bioinformatics-guide-8khab4urffhurn8jwenhhs.streamlit.app/

An AI-powered bioinformatics learning assistant built using **Python, Streamlit, LangChain and Google Gemini**.

Ask questions about bioinformatics and computational biology, from foundational biological concepts to computational methods, analysis workflows, tools and databases. The assistant adapts explanations to the learner's knowledge level and preferred style.

## Features

- Ask open-ended questions about bioinformatics and computational biology
- Explanations tailored to the learner's knowledge level
- Multiple explanation styles:
  - Detailed explanation
  - Simple explanation
  - Step-by-step explanation
  - Research-oriented explanation
- Covers biological and computational fundamentals
- Step-by-step descriptions of methods, algorithms and workflows
- Practical examples when requested
- Relevant bioinformatics tools and databases when requested
- Structured AI responses using Pydantic
- Streamlit interface for interactive learning

## Topics Covered

The assistant can help explain topics including:

- Molecular biology, genetics, genomics and evolution
- DNA, RNA, proteins, genes, genomes and gene expression
- Sequence alignment, BLAST and scoring matrices
- Biological databases, ontologies and common data formats
- Next-generation sequencing (NGS), including quality control, read mapping, genome assembly, variant calling and annotation
- RNA-seq, differential gene expression and functional enrichment
- Proteomics, protein structure, molecular modelling and docking
- Phylogenetics, population genetics and comparative genomics
- Systems biology, biological networks and pathway analysis
- Machine learning, statistics, Python and R for bioinformatics
- Linux, command-line tools, pipelines and high-performance computing

The assistant's coverage depends on the question and the underlying model's knowledge. It does not automatically retrieve live scientific literature or query biological databases.

## Tech Stack

- Python
- Streamlit
- LangChain
- Google Gemini API (`langchain-google-genai`)
- Pydantic
- python-dotenv

## Installation

1. Clone the repository

2. Create a virtual environment

   python -m venv venv

3. Activate the environment

   venv\Scripts\Activate.ps1

4. Install dependencies

   pip install -r requirements.txt

5. Configure environment variables

6. Run the application

   streamlit run app.py

## How to Use

1. Start the Streamlit application.
2. Select your bioinformatics knowledge level.
3. Choose the explanation style.
4. Choose whether to include practical examples and relevant tools or databases.
5. Enter a bioinformatics question in the text area.
6. Select **Explain This Topic**.
7. Read the generated explanation, fundamentals, workflow, examples and related concepts.

## Important Notes and Limitations

- A valid Google Gemini API key and access to the selected model are required.
- API usage may be subject to Google AI Studio quotas, rate limits and model availability.
- The assistant generates explanations from the model's knowledge; it does not currently perform live web searches, retrieve scientific papers, or query biological databases.
- AI-generated content can contain errors or omissions. Verify important technical details using authoritative documentation, primary literature and established databases.
- Do not use the application as a substitute for qualified clinical interpretation or medical advice.

## Future Improvements

Possible extensions include:

- Scientific literature search and paper summarisation
- Integration with biological databases and APIs
- Interactive Python, R and Linux code assistance
- Guided NGS and other bioinformatics workflow explanations
- Conversation history and follow-up questions
- Upload and explanation of research papers or bioinformatics files

**Developed as an AI-powered learning assistant for bioinformatics and computational biology.**

## Acknowledgements

This project was developed as part of the hands-on training and learning experience at **Innomatics Research Labs**.

I would like to express my sincere gratitude to the trainers and mentors who guided me throughout the workshop, helped me understand the concepts, and provided practical exposure to AI application development using Python, LangChain and Streamlit.

Their guidance and support contributed to the development of this project.
