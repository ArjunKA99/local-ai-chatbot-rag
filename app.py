import streamlit as st
from ollama_client import (generate_response_stream,summarize_conversation)
from vector_store import search

MAX_MESSAGES = 5
SUMMARY_TRIGGER = 10


st.set_page_config(page_title="My AI Chatbot")

st.title("🤖 My AI Chatbot")

# -----------------------------
# Session State
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "summary" not in st.session_state:
    st.session_state.summary = ""

# -----------------------------
# Display Previous Conversation
# -----------------------------
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# Chat Input
# -----------------------------
if prompt := st.chat_input("Ask me anything..."):

    # Display User Message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Save User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )
    # -----------------------------
    # Retrieve Relevant Chunks
    # -----------------------------
    results = search(prompt)

    context = ""

    for result in results:
        context += (
        f"Source: {result['source']}\n"
        f"Chunk: {result['chunk_id']}\n\n"
        f"{'-'*40}\n"
        f"{result['text']}\n\n"
        )

    # -----------------------------
    # Build prompt
    # -----------------------------
    conversation = """

You are a helpful AI assistant.

Answer the user's question using the provided context.

If the answer exists in the context, prioritize it.

If it is not found, clearly say that it was not found in the uploaded documents and then use your general knowledge if appropriate.

Context:


    """

    # Add Retrieved Context
    conversation += "Context:\n"
    conversation += context
    conversation += "\n\n"

    # Add Summary
    if st.session_state.summary:

        conversation += "Conversation Summary:\n"
        conversation += st.session_state.summary
        conversation += "\n\n"

    # Only send recent messages
    recent_messages = st.session_state.messages[-MAX_MESSAGES:]

    for msg in recent_messages:

        if msg["role"] == "user":
            conversation += f"User: {msg['content']}\n\n"
        else:
            conversation += f"Assistant: {msg['content']}\n\n"

    # Tell the model it's now the assistant's turn
    conversation += "Assistant: "

    # -----------------------------
    # Generate Streaming Response
    # -----------------------------
    with st.chat_message("assistant"):

        placeholder = st.empty()

        answer = ""

        try:
            for chunk in generate_response_stream(conversation):

                answer += chunk

                placeholder.markdown(answer)

        except Exception as e:

            answer = f"Error : {e}"

            placeholder.markdown(answer)

    # -----------------------------
    # Save Assistant Message
    # -----------------------------
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    # -----------------------------
    # Summarize Older Messages
    # -----------------------------
    if len(st.session_state.messages) > SUMMARY_TRIGGER:

        old_messages = st.session_state.messages[:-MAX_MESSAGES]

        st.session_state.summary = summarize_conversation(
            st.session_state.summary,
            old_messages
        )


        # Keep only latest messages
        st.session_state.messages = (
            st.session_state.messages[-MAX_MESSAGES:]
        )

        



# -----------------------------
# Debug Sidebar
# -----------------------------
with st.sidebar:

    st.header("🔍 Debug")

    st.subheader("Summary")

    if st.session_state.summary:
        st.write(st.session_state.summary)
    else:
        st.write("No summary yet")

    st.divider()

    st.subheader("Messages")

    for msg in st.session_state.messages:

        st.write(f"**{msg['role'].capitalize()}**")
        st.write(msg["content"])
        st.write("---")


    st.divider()

    st.subheader("Prompt Sent To LLM")

    if "conversation" in locals():
        st.text_area("Final Prompt",
        conversation,
        height=300
    )