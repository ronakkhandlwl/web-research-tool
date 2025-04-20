from agents.web_search_agent import web_search
from agents.summarizer_agent import summarize_links
from agents.insight_generator_agent import generate_insight
from graph.state import AgentHubState


def web_search_node(state: AgentHubState) -> AgentHubState:
    results = web_search(state.user_query)
    return state.model_copy(update={"search_results": results})


def summarizer_node(state: AgentHubState) -> AgentHubState:
    if not state.search_results:
        raise ValueError("No search results to summarize")
    summary = summarize_links(state.search_results)
    return state.model_copy(update={"summary": summary})


def insight_node(state: AgentHubState) -> AgentHubState:
    if not state.summary:
        raise ValueError("No summary to generate insight from")
    insights = generate_insight(state.summary)
    return state.model_copy(update={"insights": insights})
