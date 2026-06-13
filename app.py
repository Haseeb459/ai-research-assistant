import streamlit as st
from agent.orchestrator import run_agent

st.set_page_config(page_title="AI Research Assistant")

st.title("🔍 AI Research Assistant")
st.caption("Ask questions and get AI-powered research summaries with sources")

# Sidebar
st.sidebar.title("⚙️ Settings")
st.sidebar.write("AI Research Assistant v1")

st.sidebar.markdown("""
### Features:
- Web Search
- AI Summarization (if enabled)
- Structured Answers
""")

# Input
query = st.text_input("Enter your question")

# Button click
if st.button("Search"):
    if query:

        with st.spinner("🔎 Searching and analyzing sources..."):
            result = run_agent(query)
            st.success(f"Found {len(result)} relevant sources")

        st.subheader("📄 Results")

        # Safety check
        if isinstance(result, list) and len(result) > 0:
            for item in result:
                st.markdown(f"### 🔹 {item['title']}")
                st.write(item['summary'])
                st.markdown(f"🔗 [Open Source]({item['url']})")
                st.divider()
        else:
            st.error("No results returned from agent. Check backend.")

    else:
        st.warning("Please enter a question")