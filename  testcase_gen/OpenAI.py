from langchain.llms.openai import OpenAI


class MyOpenAI(OpenAI):
    def __init__(self):
        super(MyOpenAI, self).__init__(openai_api_key = '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',temperature=0.0)

