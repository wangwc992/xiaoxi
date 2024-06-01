import os

from langchain_core.prompts import PromptTemplate

from xiaoxi_ai.MVC.model.intelligent_calibration.intelligent_calibration import IntelligentCalibration
from xiaoxi_ai.database.mysql import country_info_mapper, zn_school_info_mapper, zn_school_department_project_mapper, \
    school_info_britain_req_mapper, student_matriculate_case_mapper, service_confirm_school_mapper, school_china_mapper
from xiaoxi_ai.database.mysql.school_info_britain_req_mapper import SchoolInfoBritainReq
from xiaoxi_ai.database.mysql.student_matriculate_case_mapper import StudentMatriculateCase


def intelligent_calibration(intelligentCalibration: IntelligentCalibration):
    # 判断提供的信息是否满足
    is_enough = intelligentCalibration.is_enough_information()
    if not is_enough:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_dir, '../../../prompt/calibration_information_insufficient.txt')
        template = PromptTemplate.from_file(file_path)
        prompt = template.format(input=intelligentCalibration)
        return prompt

    # 获取学校和专业的名称，英文名优先
    school_name = intelligentCalibration.school_name_en if intelligentCalibration.school_name_en else intelligentCalibration.school_name_zh
    major_name = intelligentCalibration.major_name_en if intelligentCalibration.major_name_en else intelligentCalibration.major_name_zh
    gpa_req = intelligentCalibration.grade_score if intelligentCalibration.grade_type == 'gpa' else None

    # 获取国家，学校，留学学校，留学专业
    country_info = None
    zn_school_info = None
    zn_school_department_project = None
    school_china = None

    # 获取国家，留学学校，留学专业的信息
    if intelligentCalibration.country_name:
        country_info = country_info_mapper.select_by_name(intelligentCalibration.country_name)
    if school_name:
        zn_school_info = zn_school_info_mapper.select_by_name(school_name)
    if major_name:
        zn_school_department_project = zn_school_department_project_mapper.select_noe_by_name(major_name)
    if intelligentCalibration.background_institution:
        school_china = school_china_mapper.select_by_name(major_name)

    project_id_list = []
    school_id_list = []
    student_matriculate_case_list = []

    # 英国学校专业，用这个判断GPA school_info_britain_req
    if intelligentCalibration.country_name == '英国':
        schoolInfoBritainReq = SchoolInfoBritainReq(school_id=zn_school_info.id,
                                                    project_id=zn_school_department_project.id,
                                                    china_school_id=school_china.id,
                                                    pa_req=gpa_req)
        school_info_britain_req_list = school_info_britain_req_mapper.select_by_model(schoolInfoBritainReq)

        # 提取school_info_britain_req_list的project_id变成一个列表
        project_id_list = [school_info_britain_req.project_id for school_info_britain_req in
                           school_info_britain_req_list]
        school_id_list = [school_info_britain_req.school_id for school_info_britain_req in school_info_britain_req_list]
    elif intelligentCalibration.major_name_zh:
        project_id_list = [zn_school_department_project.id]
        school_id_list = [zn_school_department_project.school_id]

    if not project_id_list:
        # 没有提供专业，根据提供的信息去案例库查询,案例库使用对的国家id是文签的
        studentMatriculateCase = StudentMatriculateCase(offer_country_id=1,
                                                        education_gpa=float(gpa_req),
                                                        offer_college_name_zh=school_name,
                                                        education_school_name_zh=intelligentCalibration.background_institution,
                                                        offer_degree_name=intelligentCalibration.academic_degree)
        student_matriculate_case_list = student_matriculate_case_mapper.select_by_student_matriculate_case(
            studentMatriculateCase)
        # 案例库获取的文签的学校、专业id，与开放平台的学校、专业id不一样，需要转换
        service_confirm_school_id_list = [student_matriculate_case.service_confirm_school_id for
                                          student_matriculate_case in student_matriculate_case_list]
        service_confirm_school_list = service_confirm_school_mapper.select_by_ids(service_confirm_school_id_list)
        # 从学生案例中获取学校和专业id
        school_id_list = [service_confirm_school.school_id for service_confirm_school in service_confirm_school_list]
        project_id_list = [service_confirm_school.project_id for service_confirm_school in service_confirm_school_list]

    # 查询专业详情 zn_school_department_project
    zn_school_department_project_list = zn_school_department_project_mapper.select_by_ids(project_id_list)
    # 查询学校详情 zn_school_info
    zn_school_info_list = zn_school_info_mapper.select_by_ids(school_id_list)

    # 将学校和专业信息整合到一个字典中
    school_dict = {school.id: school for school in zn_school_info_list}
    result_dict = {school_id: {"school_info": school_info, "projects": []} for school_id, school_info in
                   school_dict.items()}
    for project in zn_school_department_project_list:
        if project.school_id in result_dict:
            result_dict[project.school_id]["projects"].append(project)

    project_data_list = object_to_list(zn_school_department_project_list)
    school_data_list = object_to_list(zn_school_info_list)
    matriculate_case_data_list = object_to_list(student_matriculate_case_list)

    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, '../../../prompt/intelligent_calibration.txt')
    template = PromptTemplate.from_file(file_path)
    prompt = template.format(input=intelligentCalibration,
                             school_Information=school_data_list,
                             professional_information=project_data_list,
                             admission_case=matriculate_case_data_list)
    return prompt


def object_to_list(zn_school_info_list):
    # 获取对象的属性名列表
    if zn_school_info_list:
        attribute_names = list(zn_school_info_list[0].__dict__.keys())
    else:
        attribute_names = []
    # 创建一个新的列表，第一行是属性名
    data_list = [attribute_names]
    # 往后每一行是每一个对象的属性值
    for obj in zn_school_info_list:
        data_list.append([getattr(obj, attr) for attr in attribute_names])
    return data_list
