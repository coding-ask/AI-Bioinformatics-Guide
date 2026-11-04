import streamlit as st

from generator import generate_bioinformatics_answer


st.set_page_config(
    page_title="AI Bioinformatics Guide",
    page_icon="🧬",
    layout="wide"
)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("🧬 AI Bioinformatics Guide")

st.write(
    "Your interactive guide to bioinformatics. Ask questions about "
    "biological concepts, computational methods, databases, tools, "
    "workflows, genomics, transcriptomics, proteomics and more."
)


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.header("Learning Preferences")

audience_level = st.sidebar.selectbox(
    "Your Knowledge Level",
    [
        "Beginner",
        "Undergraduate",
        "Postgraduate",
        "Researcher / Professional"
    ]
)

answer_style = st.sidebar.selectbox(
    "Explanation Style",
    [
        "Detailed explanation",
        "Simple explanation",
        "Step-by-step explanation",
        "Research-oriented explanation"
    ]
)

include_examples = st.sidebar.checkbox(
    "Include practical examples",
    value=True
)

include_tools = st.sidebar.checkbox(
    "Mention relevant bioinformatics tools and databases",
    value=True
)

st.sidebar.divider()

st.sidebar.caption(
    "Tip: Ask a specific question for a more focused and useful answer."
)


# --------------------------------------------------
# QUESTION INPUT
# --------------------------------------------------

st.subheader("Ask your Bioinformatics Question")

question = st.text_area(
    "What would you like to understand?",
    placeholder=(
        "Example: What is the difference between genome sequencing "
        "and exome sequencing?\n"
        "Example: Explain how RNA-seq differential expression analysis works."
    ),
    height=130
)

if st.button(
    "🧬 Explain This Topic",
    type="primary",
    use_container_width=True
):

    if not question.strip():
        st.warning("Please enter a bioinformatics question first.")

    else:
        with st.spinner("Preparing your bioinformatics explanation..."):

            try:
                result = generate_bioinformatics_answer(
                    question,
                    audience_level,
                    answer_style,
                    include_examples,
                    include_tools
                )

                st.session_state["bioinformatics_result"] = result
                st.session_state["bioinformatics_question"] = question

            except Exception as e:
                st.error(f"Something went wrong: {str(e)}")


# --------------------------------------------------
# DISPLAY RESULTS
# --------------------------------------------------

if "bioinformatics_result" in st.session_state:

    result = st.session_state["bioinformatics_result"]

    st.divider()
    st.success("Explanation generated!")

    st.subheader(st.session_state.get("bioinformatics_question", "Your question"))

    st.markdown("### 📘 Core Explanation")
    st.markdown(result.core_explanation)

    st.divider()

    st.markdown("### 🔬 Underlying Fundamentals")
    st.markdown(result.fundamentals)

    st.divider()

    st.markdown("### ⚙️ How It Works")
    st.markdown(result.how_it_works)

    st.divider()

    st.markdown("### 🧪 Practical Example")
    st.markdown(result.practical_example)

    st.divider()

    st.markdown("### 🛠️ Relevant Tools and Databases")
    st.markdown(result.tools_and_databases)

    st.divider()

    st.markdown("### 🔗 Related Concepts")
    st.markdown(result.related_concepts)

    st.divider()

    st.markdown("### 📚 Further Learning")
    st.markdown(result.further_learning)

    st.info(
        "Use this explanation as a learning aid. For research or clinical "
        "work, verify important claims against primary literature and "
        "authoritative databases."
    )


else:

    st.info(
        "Enter any bioinformatics-related question above to get started. "
        "You can ask about fundamentals, algorithms, biological databases, "
        "NGS analysis, structural bioinformatics, computational biology "
        "or practical workflows."
    )
