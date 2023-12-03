from pydantic import BaseModel,Field

class ElementModel(BaseModel):
    selector: str = Field(description="元素的定位符，尽量使用css，尽量使用有业务含义的关键标记")
    name: str = Field(description="给页面元素起一个有业务含义的名字")
