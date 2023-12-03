from langchain.llms import ChatGLM
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

import os

def test_langChain():
    template = """{question}"""
    prompt = PromptTemplate(template=template, input_variables=["question"])


    llm = ChatGLM(
        endpoint_url=endpoint_url,
        max_token=80000,
        history=[["你是一名互联网大佬", " 欢迎问我任何问题。"]],
        top_p=0.9,
        model_kwargs={"sample_model_args": False},
    )
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    question = "如何落地AI大模型在TO B 人力方向"
    rs=llm_chain.run(question)
    print(rs)

if __name__ == '__main__':
    test_langChain()