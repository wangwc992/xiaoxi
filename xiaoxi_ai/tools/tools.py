from langchain_core.tools import StructuredTool

from xiaoxi_ai.tools.student_info import get_student_info

get_student_info = StructuredTool.from_function(
    func=get_student_info,
    name="getStudentinfo",
    description="获取学生信息",
)