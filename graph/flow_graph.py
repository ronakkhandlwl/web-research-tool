from langgraph.graph import StateGraph, END
from agents.web_search_agent import web_search
from agents.summarizer_agent import summarize_links
from agents.insight_generator_agent import generate_insight
from .state import ResearchState


def coordinator(state):
    if not state.links:
        return "web_search"
    elif not state.summary:
        return "summarizer"
    elif not state.insight:
        return "insight_gen"
    else:
        return END


def web_search_node(state: ResearchState):
    links = web_search(state.query)
    state.links = links
    return state


def summarizer_node(state: ResearchState):
    state.summary = summarize_links(state.links)
    return state


def insight_gen_node(state: ResearchState):
    state.insight = generate_insight(state.summary)
    return state



def build_graph():
    graph = StateGraph(ResearchState)
    
    graph.add_node("web_search", web_search_node)
    graph.add_node("summarizer", summarizer_node)
    graph.add_node("insight_gen", insight_gen_node)
    graph.add_node("coordinator", coordinator)

    graph.set_entry_point("coordinator")
    graph.add_conditional_edges("coordinator", coordinator, {
        "web_search": "web_search",
        "summarizer": "summarizer",
        "insight_gen": "insight_gen",
        END: END
    })

    graph.add_edge("web_search", "coordinator")
    graph.add_edge("insight_gen", END)

    return graph.compile()
