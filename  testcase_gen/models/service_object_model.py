from pydantic import BaseModel, Field, ValidationError
from typing import List, Optional

from pydantic import BaseModel

# 通用模型定义
class QueryPath(BaseModel):
    path: str  = Field(description="接口uri路径，一般放在请求host后方")
    params: List[str] =  Field(description="请求参数体，一般由json组成")

class ReqHeader(BaseModel):
    required: str
    _id: str
    name: str
    value: str

class ReqQuery(BaseModel):
    required: str
    _id: str
    name: str
    desc: Optional[str] = None

class APIModel(BaseModel):
    query_path: QueryPath  = Field(description="接口路径，一般放在请求host后方")
    edit_uid: int
    status: str
    type: str
    req_body_is_json_schema: bool
    res_body_is_json_schema: bool
    api_opened: bool
    index: int
    tag: List[str]
    _id: int
    method: str
    title: str
    path: str
    req_params: List[str]
    req_body_form: List[str]
    req_headers: List[ReqHeader]
    req_query: List[ReqQuery]
    req_body_type: str
    res_body_type: str
    res_body: str  # 可以进一步解析为更具体的模型
    req_body_other: str  # 可以进一步解析为更具体的模型
    project_id: int
    catid: int
    uid: int
    add_time: int
    up_time: int
    __v: int


# class APIList(BaseModel):
#     '''
#     封装API接口列表
#     这个模型代表了一组API接口的集合，每个接口都详细定义了其请求和响应的结构
#     '''
#     apis: List[APIModel] = Field(description="API接口的列表，每个接口包含路径、方法、请求和响应等详细信息")


# 定义 ServiceObjectModel
class ServiceObjectModel(BaseModel):
    api_list: List[APIModel] = Field(..., description="API接口的列表")

# 示例数据，包含所有必需字段
example_api_data = {
    "query_path": {"path": "/example/path", "params": []},
    "edit_uid": 0,
    "status": "done",
    "type": "static",
    "req_body_is_json_schema": True,
    "res_body_is_json_schema": True,
    "api_opened": False,
    "index": 0,
    "tag": ["api-controller"],
    "_id": 119851,
    "method": "POST",
    "title": "Example Title",
    "path": "/example/path",
    "req_params": [],
    "req_body_form": [],
    "req_headers": [{"required": "1", "_id": "656d9f2932d4cc002263c208", "name": "Content-Type", "value": "application/json"}],
    "req_query": [],
    "req_body_type": "json",
    "res_body_type": "json",
    "res_body": "{}",  # 示例 JSON 字符串
    "req_body_other": "{}",  # 示例 JSON 字符串
    "project_id": 535,
    "catid": 19370,
    "uid": 1057,
    "add_time": 1583806607,
    "up_time": 1701682985,
    "__v": 0
}


# 创建 ServiceObjectModel 实例
try:
    service_object_model = ServiceObjectModel(api_list=[example_api_data])
    print(service_object_model)
except ValidationError as e:
    print(e)