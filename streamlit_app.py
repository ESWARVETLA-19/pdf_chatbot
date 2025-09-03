# import streamlit as st
# from app.rag_pipeline import build_qa_pipeline

# st.set_page_config(page_title="🧠 PDF Chatbot", layout="centered")
# st.title("📄 Local RAG Chatbot")

# # Initialize pipeline and chat history
# if "qa_pipeline" not in st.session_state:
#     with st.spinner("🔄 Loading QA pipeline..."):
#         st.session_state.qa_pipeline = build_qa_pipeline()
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []   # [(user, bot), (user, bot), ...]

# # Display chat history
# for user_msg, bot_msg in st.session_state.chat_history:
#     with st.chat_message("user"):
#         st.markdown(user_msg)
#     with st.chat_message("assistant"):
#         st.markdown(bot_msg)

# # Input box
# if question := st.chat_input("Ask a question based on your PDFs..."):
#     with st.spinner("🤔 Thinking..."):
#         result = st.session_state.qa_pipeline({"question": question})
#         answer = result["answer"]

#         # Save to history
#         st.session_state.chat_history.append((question, answer))

#         # Display response immediately
#         with st.chat_message("assistant"):
#             st.markdown(answer)

# # Reset conversation
# if st.button("🧹 Clear History"):
#     st.session_state.qa_pipeline = build_qa_pipeline()
#     st.session_state.chat_history = []
#     st.rerun()



# import streamlit as st
# from app.rag_pipeline import build_qa_pipeline

# st.set_page_config(page_title="🧠 PDF Chatbot", layout="centered")
# st.title("📄 Local RAG Chatbot")

# # Initialize pipeline and chat history
# if "qa_pipeline" not in st.session_state:
#     with st.spinner("🔄 Loading QA pipeline..."):
#         st.session_state.qa_pipeline = build_qa_pipeline()
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []   # [(role, msg), ...]

# # Display all past messages
# for role, msg in st.session_state.chat_history:
#     with st.chat_message(role):
#         st.markdown(msg)

# # Input box
# if question := st.chat_input("Ask a question based on your PDFs..."):

#     # Save and render the user message immediately
#     st.session_state.chat_history.append(("user", question))
#     with st.chat_message("user"):
#         st.markdown(question)

#     # Create placeholder for assistant response
#     with st.chat_message("assistant"):
#         message_placeholder = st.empty()
#         message_placeholder.markdown("🤔 Thinking...")

#         # Run pipeline
#         result = st.session_state.qa_pipeline({"question": question})
#         answer = result["answer"]

#         # Update placeholder with real answer
#         message_placeholder.markdown(answer)

#     # Save assistant message
#     st.session_state.chat_history.append(("assistant", answer))

# # Reset conversation
# if st.button("🧹 Clear History"):
#     st.session_state.qa_pipeline = build_qa_pipeline()
#     st.session_state.chat_history = []
#     st.rerun()


# import streamlit as st
# from app.rag_pipeline import build_qa_pipeline

# st.set_page_config(page_title="🧠 PDF Chatbot", layout="centered")

# # --- Custom CSS for bubble styling ---
# st.markdown("""
# <style>
# .chat-message {
#     padding: 10px;
#     border-radius: 15px;
#     margin-bottom: 10px;
#     max-width: 80%;
#     word-wrap: break-word;
# }
# .user-message {
#     background-color: #f1f0f0;
#     margin-left: auto;
#     text-align: right;
# }
# .assistant-message {
#     background: linear-gradient(90deg, #5d9fff, #0066ff);
#     color: white;
#     margin-right: auto;
#     text-align: left;
# }
# .assistant-footer {
#     font-size: 11px;
#     color: #ddd;
#     margin-top: 3px;
# }
# </style>
# """, unsafe_allow_html=True)

# st.title("📄 Local RAG Chatbot")

# # Initialize pipeline
# if "qa_pipeline" not in st.session_state:
#     with st.spinner("🔄 Loading QA pipeline..."):
#         st.session_state.qa_pipeline = build_qa_pipeline()

# # Initialize history
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# # Render chat history
# for role, msg in st.session_state.chat_history:
#     if role == "user":
#         st.markdown(f"""
#         <div class="chat-message user-message">
#             {msg}
#         </div>
#         """, unsafe_allow_html=True)
#     else:
#         st.markdown(f"""
#         <div class="chat-message assistant-message">
#             {msg}
#             <div class="assistant-footer">✨ Answered by AI</div>
#         </div>
#         """, unsafe_allow_html=True)

# # Input box
# if question := st.chat_input("Ask a question..."):
#     # Save user message
#     st.session_state.chat_history.append(("user", question))
#     st.markdown(f"""
#     <div class="chat-message user-message">
#         {question}
#     </div>
#     """, unsafe_allow_html=True)

#     # Run model
#     result = st.session_state.qa_pipeline({"question": question})
#     answer = result["answer"]

#     # Save assistant reply
#     st.session_state.chat_history.append(("assistant", answer))
#     st.markdown(f"""
#     <div class="chat-message assistant-message">
#         {answer}
#         <div class="assistant-footer">✨ Answered by AI</div>
#     </div>
#     """, unsafe_allow_html=True)

# # Reset
# if st.button("🧹 Clear History"):
#     st.session_state.chat_history = []
#     st.rerun()
# import streamlit as st
# from app.rag_pipeline import build_qa_pipeline

# st.set_page_config(page_title="🧠 PDF Chatbot", layout="centered")

# # --- Custom CSS ---
# st.markdown("""
# <style>
# .chat-box {
#     max-height: 500px;
#     overflow-y: auto;
#     padding: 10px;
# }
# .chat-message {
#     margin-bottom: 10px;
#     word-wrap: break-word;
#     display: inline-block;
#     line-height: 1.4;
#     vertical-align: top;
#     padding: 0;
#     max-width: 100%;
# }

# .user-message {
#     background-color: #f1f0f0;
#     color: black;             /* User text color */
#     padding: 8px 12px;
#     border-radius: 15px;
#     display: inline-block;
#     max-width: 70%;
#     word-wrap: break-word;
# }

# .assistant-message {
#     background: linear-gradient(90deg, #5d9fff, #0066ff);
#     color: white;
#     padding: 8px 12px;
#     border-radius: 15px;
#     display: inline-block;
#     max-width: 70%;
#     word-wrap: break-word;
# }

# .assistant-footer {
#     font-size: 11px;
#     color: #ddd;
#     margin-top: 3px;
# }
# </style>
# """, unsafe_allow_html=True)

# st.title("📄 Local RAG Chatbot")

# # Initialize pipeline
# if "qa_pipeline" not in st.session_state:
#     with st.spinner("🔄 Loading QA pipeline..."):
#         st.session_state.qa_pipeline = build_qa_pipeline()

# # Initialize history and processing flag
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# if "is_processing" not in st.session_state:
#     st.session_state.is_processing = False

# # --- Chat container ---
# with st.container():
#     st.markdown('<div class="chat-box">', unsafe_allow_html=True)

#     for role, msg in st.session_state.chat_history:
#         if role == "user":
#             st.markdown(f"""
#             <div class="chat-message user-message">{msg}</div>
#             """, unsafe_allow_html=True)
#         else:
#             st.markdown(f"""
#             <div class="chat-message assistant-message">
#                 {msg}
#                 <div class="assistant-footer">✨ Answered by AI</div>
#             </div>
#             """, unsafe_allow_html=True)

#     st.markdown('</div>', unsafe_allow_html=True)

# # --- Input box with blocking ---
# if not st.session_state.is_processing:
#     if question := st.chat_input("Ask a question..."):
#         st.session_state.chat_history.append(("user", question))
#         st.session_state.is_processing = True  # block input

# # --- Run model if processing ---
# if st.session_state.is_processing:
#     with st.spinner("🤖 AI is thinking..."):
#         last_question = st.session_state.chat_history[-1][1]
#         result = st.session_state.qa_pipeline({"question": last_question})
#         answer = result["answer"]

#         st.session_state.chat_history.append(("assistant", answer))
#         st.session_state.is_processing = False  # unblock input

#     st.rerun()

# # --- Reset ---
# if st.button("🧹 Clear History"):
#     st.session_state.chat_history = []
#     st.session_state.is_processing = False
#     st.rerun()


# import streamlit as st
# from app.rag_pipeline import build_qa_pipeline

# st.set_page_config(page_title="🧠 PDF Chatbot", layout="centered")

# # --- Custom CSS ---
# st.markdown("""
# <style>
# .chat-box {
#     max-height: 500px;
#     overflow-y: auto;
#     padding: 10px;
# }
# .chat-message {
#     margin-bottom: 10px;
#     word-wrap: break-word;
#     display: inline-block;
#     line-height: 1.4;
#     vertical-align: top;
#     padding: 0;
#     max-width: 100%;
# }

# .user-message {
#     background-color: #f1f0f0;
#     color: black;  /* Make user text visible */
#     padding: 8px 12px;
#     border-radius: 15px;
#     display: inline-block;
#     max-width: fit-content;  /* Auto width */
#     word-wrap: break-word;
# }

# .assistant-message {
#     background: linear-gradient(90deg, #5d9fff, #0066ff);
#     color: white;
#     padding: 8px 12px;
#     border-radius: 15px;
#     display: inline-block;
#     max-width: fit-content;  /* Auto width */
#     word-wrap: break-word;
# }

# .assistant-footer {
#     font-size: 11px;
#     color: #ddd;
#     margin-top: 3px;
# }
# </style>
# """, unsafe_allow_html=True)

# st.title("📄 Local RAG Chatbot")

# # Initialize pipeline
# if "qa_pipeline" not in st.session_state:
#     with st.spinner("🔄 Loading QA pipeline..."):
#         st.session_state.qa_pipeline = build_qa_pipeline()

# # Initialize history and processing flag
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# if "is_processing" not in st.session_state:
#     st.session_state.is_processing = False

# # --- Chat container ---
# with st.container():
#     st.markdown('<div class="chat-box">', unsafe_allow_html=True)

#     for role, msg in st.session_state.chat_history:
#         if role == "user":
#             st.markdown(f'<div class="chat-message user-message">{msg}</div>', unsafe_allow_html=True)
#         else:
#             st.markdown(f'''
#             <div class="chat-message assistant-message">
#                 {msg}
#                 <div class="assistant-footer">✨ Answered by AI</div>
#             </div>
#             ''', unsafe_allow_html=True)

#     st.markdown('</div>', unsafe_allow_html=True)

# # --- Input box ---
# if not st.session_state.is_processing:
#     if question := st.chat_input("Ask a question..."):
#         st.session_state.chat_history.append(("user", question))
#         st.session_state.is_processing = True  # block input

# # --- Run model if processing ---
# if st.session_state.is_processing:
#     last_question = st.session_state.chat_history[-1][1]
#     with st.spinner("🤖 AI is thinking..."):  # spinner visible while processing
#         result = st.session_state.qa_pipeline({"question": last_question})
#         answer = result["answer"]
#         st.session_state.chat_history.append(("assistant", answer))
#     st.session_state.is_processing = False  # unblock input
#     st.experimental_rerun()  # rerun to show new message


import streamlit as st
from app.rag_pipeline import build_qa_pipeline

st.set_page_config(page_title="🧠 PDF Chatbot", layout="centered")

# --- Custom CSS ---
st.markdown("""
<style>
.chat-box {
    max-height: 500px;
    overflow-y: auto;
    padding: 10px;
}
.chat-message {
    margin-bottom: 10px;
    word-wrap: break-word;
    display: inline-block;
    line-height: 1.4;
    vertical-align: top;
    padding: 0;
    max-width: 80vw;         /* Wider and more flexible */
    width: auto;
    min-width: 50px;
}
.user-message {
    background-color: #f1f0f0;
    color: black !important; /* Ensures text is always visible */
    padding: 8px 12px;
    border-radius: 15px;
    display: inline-block;
    max-width: 80vw;
    width: fit-content;      /* Auto width based on content */
    min-width: 50px;         /* Minimum width for very short messages */
    word-wrap: break-word;
}
.assistant-message {
    background: linear-gradient(90deg, #5d9fff, #0066ff);
    color: white !important;
    padding: 8px 12px;
    border-radius: 15px;
    display: inline-block;
    max-width: 80vw;
    width: fit-content;
    min-width: 50px;
    word-wrap: break-word;
}
.assistant-footer {
    font-size: 11px;
    color: #ddd;
    margin-top: 3px;
}
</style>
""", unsafe_allow_html=True)

st.title("📄 Local RAG Chatbot")

# Initialize pipeline
if "qa_pipeline" not in st.session_state:
    with st.spinner("🔄 Loading QA pipeline..."):
        st.session_state.qa_pipeline = build_qa_pipeline()

# Initialize history and processing flag
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "is_processing" not in st.session_state:
    st.session_state.is_processing = False

# --- Chat container ---
with st.container():
    st.markdown('<div class="chat-box">', unsafe_allow_html=True)
    for role, msg in st.session_state.chat_history:
        if role == "user":
            st.markdown(f'<div class="chat-message user-message">{msg}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'''
            <div class="chat-message assistant-message">
                {msg}
                <div class="assistant-footer">✨ Answered by AI</div>
            </div>
            ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- Input box ---
if not st.session_state.is_processing:
    question = st.chat_input("Ask a question...")
    if question:
        st.session_state.chat_history.append(("user", question))
        st.session_state.is_processing = True  # block input
        st.experimental_rerun()  # Immediately rerun to show spinner

# --- Run model if processing ---
if st.session_state.is_processing:
    last_question = st.session_state.chat_history[-1][9]
    with st.spinner("🤖 AI is thinking..."):  # Spinner visible while processing
        result = st.session_state.qa_pipeline({"question": last_question})
        answer = result["answer"]
        st.session_state.chat_history.append(("assistant", answer))
    st.session_state.is_processing = False  # unblock input
    st.experimental_rerun()  # rerun to show new message
