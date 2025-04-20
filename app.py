import streamlit as st
from graph.agenthub_graph import build_agenthub_graph
from graph.state import AgentHubState
from dotenv import load_dotenv


load_dotenv()


st.set_page_config(page_title="AgentHub - Research Assistant", layout="wide")

st.title("🧠 AgentHub – AI-Powered Research Assistant")

query = st.text_input("🔍 Enter a research topic/question")

if st.button("Run Research"):
    if not query:
        st.warning("Please enter a topic to research.")
    else:
        with st.spinner("Running agents..."):
            graph = build_agenthub_graph()
            state = AgentHubState(user_query=query)
            final_state = graph.invoke(state)

        st.success("✅ Research complete!")

        with st.expander("🔗 Web Search Results"):
            for i, res in enumerate(final_state["search_results"], 1):
                st.markdown(f"**{i}. [{res['title']}]({res['link']})**")
                st.caption(res["snippet"])

        st.subheader("📝 Summary")
        st.markdown(final_state["summary"])

        st.subheader("💡 Final Insights")
        st.markdown(final_state["insights"])

        with open("output/final_report.md", "w") as f:
            f.write(final_state["insights"])
