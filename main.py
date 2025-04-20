from graph.flow_graph import build_graph
from graph.state import ResearchState
from dotenv import load_dotenv


load_dotenv()


def main():
    query = input("Enter your research topic: ")
    initial_state = ResearchState()
    initial_state.query = query

    graph = build_graph()

    final_state = graph.invoke(initial_state)

    with open("output/final_report.md", "w") as f:
        f.write(final_state.insight)

    print("✅ Insight saved to output/final_report.md")


if __name__ == "__main__":
    main()
