from langchain_core.tools import StructuredTool

from xiaoxi_ai.tools.student_info import get_student_info

search_student_info_tool = StructuredTool.from_function(
    func=get_student_info,
    name="tableDescriptiona",
    description="获取学生信息",
)