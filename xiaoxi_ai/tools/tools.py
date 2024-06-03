from langchain_core.tools import StructuredTool, BaseTool
from pydantic import ValidationError

from xiaoxi_ai.MVC.service.intelligent_calibration.Intelligent_calibration import intelligent_calibration
from xiaoxi_ai.tools.student_info import get_student_info
from typing import Optional, Dict, Any
from langchain_core.pydantic_v1 import BaseModel, Field
from xiaoxi_ai.MVC.service.knowledge.knowledge import information_consultant


class Action(BaseModel):
    name: str = Field(description="Tool name")
    args: Optional[Dict[str, Any]] = Field(description="Tool input arguments, containing arguments names and values")


def __find_tool(tools: list, tool_name: str) -> Optional[BaseTool]:
    for tool in tools:
        if tool.name == tool_name:
            return tool
    return None


def exec_action(tools, action: Action) -> str:
    # 查找工具
    tool = __find_tool(tools, action.name)
    if tool is None:
        observation = (
            f"Error: 找不到工具或指令 '{action.name}'. "
            f"请从提供的工具/指令列表中选择，请确保按对顶格式输出。"
        )
    else:
        try:
            # 执行工具
            observation = tool.run(action.args)
        except ValidationError as e:
            # 工具的入参异常
            observation = (
                f"Validation Error in args: {str(e)}, args: {action.args}"
            )
        except Exception as e:
            # 工具执行异常
            observation = f"Error: {str(e)}, {type(e).__name__}, args: {action.args}"

    return observation


search_student_info_tool = StructuredTool.from_function(
    func=get_student_info,
    name="tableDescriptiona",
    description="获取学生信息",
)

information_consultant = StructuredTool.from_function(
    func=information_consultant,
    name="informationConsultant",
    description="没有命中其他的function calling时，调用这个function",
)

intelligent_calibration = StructuredTool.from_function(
    func=intelligent_calibration,
    name="intelligentCalibration",
    description="学生想去留学，推荐学校和专业",
)
