from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_groq import ChatGroq
import os


def generate_insight(summary):
    prompt = PromptTemplate(
        input_variables=["summary"],
        template="""
        Based on the below summary, generate an executive insight report with:
        - Key findings
        - Actionable takeaways
        - Suggested follow-ups

        Summary:
        {summary}
        """
    )

    groq_api_key = os.getenv('GROQ_API_KEY')
    llm = ChatGroq(
        groq_api_key=groq_api_key,
        model_name="meta-llama/llama-4-scout-17b-16e-instruct")

    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.invoke({"summary": summary})
