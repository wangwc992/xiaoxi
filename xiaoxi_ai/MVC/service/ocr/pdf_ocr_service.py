from langchain.output_parsers import OutputFixingParser
from langchain_core.prompts import PromptTemplate

from xiaoxi_ai.MVC.model.ocr.pdf_ocr_model import PdfOcrModel
from xiaoxi_ai.ai_client.client.langchain_client import llm
from langchain_core.output_parsers import PydanticOutputParser


class PdfOcrService:
    def analytic_ocr_attribute(self, query):
        parser = PydanticOutputParser(pydantic_object=PdfOcrModel)
        template = PromptTemplate.from_file(template_file="../../../prompt/pdf_ocr_prompt.txt")
        model_input = template.format(query=query,
                                      format_instructions={"format_instructions": parser.get_format_instructions()})
        # print("====Format Instruction=====")
        # print(parser.get_format_instructions())
        # print("====Prompt=====")
        # print(model_input)
        output = llm.invoke(model_input)
        print("====模型原始输出=====")
        print(output.content)
        # print("====Parse后的输出=====")
        output = output.content.replace("json", "")
        try:
            date = parser.parse(output)
            print(date)
        except Exception as e:
            # print("===出现异常===")
            # print(e)
            # 用OutputFixingParser自动修复并解析
            new_parser = OutputFixingParser.from_llm(
                parser=parser, llm=llm)
            date = new_parser.parse(output)
            print("===重新解析结果===")
            print(date.json())


if __name__ == '__main__':
    query = '''
204431,福建師乾大學,FUIAN NORMALUNIVFRSIIY,的能大学,Certification,We hereby certify that Hou Daning,male, was born on,December 16,2001, with student number 113012020117 and ID,card number 350583200112162210.He was enrolled by FNU in,September,2020 for a four-year undergraduate program . He is,now a full-time undergraduate at the College of Fine Arts, with a,major in Fine Arts (Teacher Education).,Tcacbing Affairs (officc,Fujian Nornal Univrrsity (FNU),Datc.Y1ay 14.2024,范大学,保注师范大学,规降范大学,保建师见大学,福建师范大学,斗收验联,范大学,微4卫服,福建砸靶大學,范大学,IUIAN NORMAIUNIVFRSIIY,8师依大学,在学证明,侯达宁，男，汉族，2001年12月16日出生，学号：,113012020117，身份证号：350583200112162210，2020年9月,入学，现为我校美术学院美术学(师范)专业2020级普通全日制,本科学生，学制4年。,特此证明！,临改师范大学,提政师部,福姆师范大学教务处,福检师范大学,福建师范大华,2021年5月11日,伦大学,师超大学,北规协范大学,地址：福建省福州市闽侯县上街镇学府南路8号福建师范大学旗山校区（350117）,该证明电子文档可通过下列渠道验证真伤：1，学信网官网：httpsi//www,chsi,eon.cn/ejidyz/index,出信政范大学,2、校内网站：httpsi//dxzn.fjnu.edu.cn/verify/,（打印时间：2024年5月14日 22:33:00）
'''
    pdfOcrService = PdfOcrService()
    pdfOcrService.analytic_ocr_attribute(query)
