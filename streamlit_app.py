import streamlit as st

st.set_page_config(
    page_title="Inside an LLM",
    page_icon="🧠",
    layout="wide"
)

st.markdown("""
<style>
.main {
    background-color: #f7f8fc;
}
h1 {
    color: #243b67;
}
h2 {
    color: #344d7c;
}
div.stButton > button {
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)


st.title("🧠 Inside an LLM")
st.subheader("From Word Completion to Logical Reasoning")

st.markdown("""
Welcome to this interactive educational website!

Explore how Large Language Models (LLMs) generate text,
learn patterns, recognize questions, and imitate logical reasoning.
""")

st.divider()

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Next Token Prediction",
    "Pre-training",
    "Question Recognition",
    "Logical Reasoning",
    "Text Generation",
    "Conclusion"
])


# TAB 1
with tab1:

    st.header("1. Next Token Prediction")

    st.write("""
    Large Language Models generate text by predicting
    the next token based on previous context.

    This process repeats until a complete response is generated.
    """)

    prompt = st.text_input(
        "Enter a sentence:",
        "Can a sparrow fly?"
    )

    if st.button("Predict Next Token"):

        st.success("Predicted next token: YES")

        st.write("""
        The model uses patterns learned during training
        to estimate which token is most likely to come next.
        """)

    st.info("This is an educational simulation, not a live AI prediction.")


# TAB 2
with tab2:

    st.header("2. Pre-training Knowledge")

    st.write("""
    Pre-training allows language models to learn patterns
    from massive amounts of text data.
    """)

    st.subheader("Three Main Stages")

    st.markdown("""
    **1. Massive Data**

    Books, articles, websites and other text sources.

    **2. Pattern Learning**

    The model learns relationships between words and concepts.

    **3. Model Parameters**

    Learned statistical patterns are stored in numerical parameters.
    """)

    st.success(
        "Pre-training provides the foundation for many LLM capabilities."
    )


# TAB 3
with tab3:

    st.header("3. Question Type Recognition")

    st.write("""
    Different question structures can lead to different
    response styles.
    """)

    question_type = st.selectbox(
        "Choose a question type:",
        [
            "Common-sense Question",
            "Informational Description",
            "Sentence Creation"
        ]
    )

    if question_type == "Common-sense Question":

        st.write("Can a sparrow fly?")

        st.success(
            "Yes. A sparrow is a bird and generally has the ability to fly."
        )

    elif question_type == "Informational Description":

        st.write("Describe a sparrow's flying ability.")

        st.success(
            "A sparrow uses its wings to fly, usually over relatively short distances."
        )

    else:

        st.write("Write a sentence using the word sparrow.")

        st.success(
            "A sparrow landed quietly on the garden fence."
        )


# TAB 4
with tab4:

    st.header("4. Syllogism and Logical Reasoning")

    st.write("""
    A syllogism is a form of reasoning involving
    two premises and a conclusion.
    """)

    st.subheader("Example")

    st.markdown("""
    **Major Premise:**

    All birds can fly.

    **Minor Premise:**

    A sparrow is a bird.

    **Conclusion:**

    A sparrow can fly.
    """)

    st.divider()

    st.subheader("Interactive Logic Test")

    premise = st.radio(
        "Choose a major premise:",
        [
            "All birds can fly.",
            "All birds cannot fly."
        ]
    )

    if st.button("Test Logical Conclusion"):

        if premise == "All birds can fly.":

            st.success("Conclusion: A sparrow can fly.")

        else:

            st.warning("Conclusion: A sparrow cannot fly.")

    st.info(
        "This example demonstrates how changing a premise "
        "can change the resulting conclusion."
    )


# TAB 5
with tab5:

    st.header("5. Long-Text Generation")

    st.write("""
    Language models generate longer texts by using
    previous tokens as context.
    """)

    st.subheader("Sampling Strategies")

    st.markdown("""
    **Temperature**

    Controls the randomness of token selection.

    **Top-K Sampling**

    Limits selection to the K most probable tokens.

    **Top-P Sampling**

    Selects tokens from a probability-based candidate pool.
    """)

    temperature = st.slider(
        "Adjust Temperature:",
        0.0,
        1.5,
        0.7
    )

    if temperature < 0.4:

        st.info("Low temperature: More predictable responses.")

    elif temperature > 1.0:

        st.warning("High temperature: More diverse responses.")

    else:

        st.success("Moderate temperature: Balanced responses.")


# TAB 6
with tab6:

    st.header("6. Key Takeaways")

    st.markdown("""
    ### What have we learned?

    1. LLMs predict the next token to generate text.

    2. Pre-training helps models learn language patterns.

    3. Question structures influence response styles.

    4. Models can generate text that follows logical structures.

    5. Context and sampling strategies influence text generation.
    """)

    st.balloons()

    st.success(
        "Congratulations! You have completed the interactive LLM lesson."
    )


st.divider()

st.caption(
    "Interactive Educational Project | Artificial Intelligence"
)

st.caption(
    "Based on the lecture: The Underlying Truth of Large Language Model Capabilities"
)
