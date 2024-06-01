from xiaoxi_ai.MVC.model.intelligent_calibration.intelligent_calibration import IntelligentCalibration
from xiaoxi_ai.database.mysql import country_info_mapper, zn_school_info_mapper, zn_school_department_project_mapper, \
    school_info_britain_req_mapper, student_matriculate_case_mapper, service_confirm_school_mapper
from xiaoxi_ai.database.mysql.school_info_britain_req_mapper import SchoolInfoBritainReq
from xiaoxi_ai.database.mysql.student_matriculate_case_mapper import StudentMatriculateCase


# 数据库连接参数


def intelligent_calibration(intelligentCalibration: IntelligentCalibration):
    intelligentCalibration.is_enough_information()

    # 获取学校和专业的名称，英文名优先
    school_name = intelligentCalibration.school_name_en if intelligentCalibration.school_name_en else intelligentCalibration.school_name_zh
    major_name = intelligentCalibration.major_name_en if intelligentCalibration.major_name_en else intelligentCalibration.major_name_zh
    gpa_req = intelligentCalibration.grade_score if intelligentCalibration.grade_type == 'gpa' else None

    # 获取国家，学校，留学学校，留学专业
    country_info = None
    zn_school_info = None
    zn_school_department_project = None

    # 获取国家，留学学校，留学专业的信息
    if intelligentCalibration.country_name:
        country_info = country_info_mapper.select_by_name(intelligentCalibration.country_name)
    if school_name:
        zn_school_info = zn_school_info_mapper.select_by_name(school_name)
    if major_name:
        zn_school_department_project = zn_school_department_project_mapper.select_noe_by_name(major_name)

    project_id_list = []
    school_id_list = []
    student_matriculate_case_list = []

    # 英国学校专业，用这个判断GPA school_info_britain_req
    if intelligentCalibration.country_name == '英国':
        schoolInfoBritainReq = SchoolInfoBritainReq(school_id=zn_school_info.id,
                                                    project_id=zn_school_department_project.id,
                                                    china_school_id=country_info.id, gpa_req=gpa_req)
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

    # 遍历案例列表
    # for case in student_matriculate_case_list:
    #     # 获取案例的专业ID
    #     project_id = case.offer_major_id
    #     # 遍历结果字典
    #     for school_id, school_info in result_dict.items():
    #         # 遍历学校的专业列表
    #         for project in school_info["projects"]:
    #             # 如果案例的专业ID与当前专业的ID匹配
    #             if project.id == project_id:
    #                 # 将案例添加到当前专业
    #                 project.append(case)

    # Now, result_dict is a dictionary where each key is a school_id and each value is another dictionary containing the zn_school_info and a list of zn_school_department_project

    # 查询学校排名 zn_school_rank

    # 是否提供录取案例

    print(result_dict)



