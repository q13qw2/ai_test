from pydantic import BaseModel,Field
from .element_model import ElementModel

class PageObjectModel(BaseModel):

    '''
    直接生成数据
    比直接生成代码的好处是可以人工维护
    '''
    # 为了让大模型更理解我们的参数，所以需要加一些注释，通过Field
    elements: list[ElementModel] = Field(description="elements是存放所有的关键页面元素的列表，是一个列表，每个元素都有selector和name组成")
    method:list = Field(description="页面所提供的可能得行为列表")

    def generate_source(self):
        ...