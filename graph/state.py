from typing import List, Optional
from langgraph.graph import StateGraph


class ResearchState:
    query: Optional[str] = None
    links: Optional[List[str]] = []
    summary: Optional[str] = ""
    insight: Optional[str] = ""
    feedback: Optional[str] = ""
