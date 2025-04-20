from langgraph.graph import StateGraph
from graph.state import AgentHubState
from graph.nodes import web_search_node, summarizer_node, insight_node


def build_agenthub_graph():
    builder = StateGraph(AgentHubState)

    builder.add_node("WebSearchAgent", web_search_node)
    builder.add_node("SummarizerAgent", summarizer_node)
    builder.add_node("InsightAgent", insight_node)

    builder.set_entry_point("WebSearchAgent")

    # Define the flow
    builder.add_edge("WebSearchAgent", "SummarizerAgent")
    builder.add_edge("SummarizerAgent", "InsightAgent")

    return builder.compile()
