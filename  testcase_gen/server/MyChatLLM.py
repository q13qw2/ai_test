from langchain.llms import ChatGLM

class MyChatLLM(ChatGLM):
    def __init__(self):
        endpoint_url = "http://localhost:8000"
        super(MyChatLLM, self).__init__(endpoint_url=endpoint_url, max_token=80000,
                                        history=[["你是一名互联网大佬", "欢迎问我任何问题。"]],
                                        top_p=0.9,
                                        model_kwargs={"sample_model_args": False,
                                                      "model_name" : "text-davinci-003",
                                                      "temperature":0.0})
