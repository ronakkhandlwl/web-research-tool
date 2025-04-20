from typing import List, Optional
from pydantic import BaseModel


class AgentHubState(BaseModel):
    user_query: str
    search_results: Optional[List[dict]] = None
    summary: Optional[str] = None
    insights: Optional[str] = None
