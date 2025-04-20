from agents.web_search_agent import web_search
from agents.summarizer_agent import summarize_links
from agents.insight_generator_agent import generate_insight
from dotenv import load_dotenv


load_dotenv()


def main():
    query = input("Enter your research topic: ")
    results = web_search(query)

    print("🔍 Searching complete. Summarizing...")
    summary = summarize_links(results)

    print("🧠 Generating insights...")
    insight = generate_insight(summary)

    with open("output/final_report.md", "w") as f:
        f.write(insight["text"])

    print("✅ Report generated at output/final_report.md")


if __name__ == "__main__":
    main()
