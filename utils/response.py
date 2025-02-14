from pydantic import BaseModel
from typing import Generic, TypeVar, Optional
from fastapi import status

# 定义泛型类型 T
T = TypeVar("T")


# 定义统一的响应模型
class BaseResponse(BaseModel, Generic[T]):
    code: int
    message: str
    data: Optional[T] = None


# 成功响应工具函数
def res_success(
    data: T = None, message: str = "成功", code: int = status.HTTP_200_OK
) -> BaseResponse[T]:
    return BaseResponse(code=code, message=message, data=data)


# 错误响应工具函数
def res_error(
    message: str, code: int = status.HTTP_400_BAD_REQUEST
) -> BaseResponse[None]:
    return BaseResponse(code=code, message=message, data=None)
