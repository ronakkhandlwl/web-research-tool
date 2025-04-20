from graph.agenthub_graph import build_agenthub_graph
from graph.state import AgentHubState
from dotenv import load_dotenv


load_dotenv()


def main():
    query = input("🧠 Enter your research topic: ")

    graph = build_agenthub_graph()
    state = AgentHubState(user_query=query)

    print("🚀 Running AgentHub Graph...")
    final_state = graph.invoke(state)

    with open("output/final_report.md", "w") as f:
        f.write(final_state["insights"])


if __name__ == "__main__":
    main()
