from pydantic import BaseModel


class CodeModel(BaseModel):
    '''
    解析大模型提供的代码
    利用元编程反向解析代码中的所有类、方法、参数和属性、反向保存为page model数据
    '''
    code: str = None
    language: str = None