from xiaoxi_ai.database.mysql import (zn_school_info_mapper, zn_school_rank_mapper, zn_school_intro_mapper,
                                      zn_school_selection_reason_mapper,
                                      zn_school_recruit_art_mapper, zn_school_recruit_graduate_mapper,
                                      zn_school_department_project_mapper,
                                      zn_school_deparment_admission_score_mapper)


class School:

    def getSchool(self, school_id):
        zn_school_info = zn_school_info_mapper.select_by_id(school_id)
        zn_school_rank = zn_school_rank_mapper.select_by_id(zn_school_info.id)
        zn_school_intro = zn_school_intro_mapper.select_by_id(zn_school_info.id)
        zn_school_selection_reason = zn_school_selection_reason_mapper.select_by_id(zn_school_info.id)
        zn_school_recruit_art = zn_school_recruit_art_mapper.select_by_id(zn_school_info.id)
        zn_school_recruit_graduate = zn_school_recruit_graduate_mapper.select_by_id(zn_school_info.id)
        # 学校的基本信息
        zn_school_info_str = (
                '学校名称：%s-%s,归属国家：%s,学校logo：%s,学校背景图：%s,学校标签：%s,学校位置：%s,官网地址：%s,院校简称：%s' %
                (zn_school_info.chinese_name, zn_school_info.english_name, zn_school_info.country_name,
                 zn_school_info.logo_url,
                 zn_school_info.cover_url, zn_school_info.market_tags, zn_school_info.city_path,
                 zn_school_info.website,
                 zn_school_info.school_abbreviations))

        # 学校的排名信息
        zn_school_rank_str = ('学校名称:%s-%s,学校排名：%s,世界排名：%s,地区排名：%s' % (
            zn_school_info.chinese_name, zn_school_info.english_name, zn_school_rank.world_rank_usnews,
            zn_school_rank.world_rank_the, zn_school_rank.world_rank_qs))

        # 学校的简介
        zn_school_intro_str = '学校名称：%s-%s,学校简介：%s, 国际学生比例：%s, 师生比例：%s, 男女比例：%s, 学生总数量：%s, 本科生数量：%s, 研究生数量：%s, 就业率：%s, 毕业薪资：%s, 院校历史：%s, 地理位置：%s, 校园环境：%s, 学校宿舍：%s, 图书馆：%s, 学校设施：%s, 招生办信息：%s, 防疫信息：%s, 介绍视频url：%s' % (
            zn_school_info.chinese_name, zn_school_info.english_name, zn_school_intro.introduction,
            zn_school_intro.international_ratio, zn_school_intro.faculty_ratio, zn_school_intro.boy_girl_ratio,
            zn_school_intro.student_amount, zn_school_intro.undergraduate_amount, zn_school_intro.graduate_amount,
            zn_school_intro.employment_rate, zn_school_intro.employment_salary, zn_school_intro.history,
            zn_school_intro.location, zn_school_intro.campus, zn_school_intro.accommodation, zn_school_intro.library,
            zn_school_intro.installation, zn_school_intro.admissions_office, zn_school_intro.covid_rule,
            zn_school_intro.video_url)

        # 学校的招生理由
        zn_school_selection_reason_str = '学校名称：%s-%s,招生理由：%s ,学校特色：%s, 强势专业：%s, 热门专业：%s, 院系设置：%s, 教学特色：%s, 差评项：%s, 好评项：%s' % (
            zn_school_info.chinese_name, zn_school_info.english_name, zn_school_selection_reason.selection_reason,
            zn_school_selection_reason.feature, zn_school_selection_reason.strong_majors,
            zn_school_selection_reason.hot_majors, zn_school_selection_reason.department_major,
            zn_school_selection_reason.teaching, zn_school_selection_reason.evaluation_bad,
            zn_school_selection_reason.evaluation_good)

        # 学校的本科招生信息
        zn_school_recruit_art_str = '学校名称：%s-%s,招生信息：%s, 录取率：%s, 申请费用：%s, 学费：%s, 书本费：%s, 生活费：%s, 交通费：%s, 住宿费用：%s, 其他费用：%s, 总花费：%s, 研究生专业：%s, 研究生雅思成绩：%s, 研究生托福成绩：%s, 研究生申请要求：%s, 研究生作品集要求：%s, 研究生申请截止日期：%s, 本科专业：%s, 本科雅思成绩：%s, 本科托福成绩：%s, 本科申请要求：%s, 本科作品集要求：%s, 本科申请截止日期：%s, 申请难度：%s, 申请经验：%s, 明星校友：%s' % (
            zn_school_info.chinese_name, zn_school_info.english_name, zn_school_recruit_art.strong_majors,
            zn_school_recruit_art.admission_rate, zn_school_recruit_art.fee_apply, zn_school_recruit_art.fee_tuition,
            zn_school_recruit_art.fee_book, zn_school_recruit_art.fee_life, zn_school_recruit_art.fee_traffic,
            zn_school_recruit_art.fee_accommodation, zn_school_recruit_art.fee_others, zn_school_recruit_art.fee_total,
            zn_school_recruit_art.graduate_majors, zn_school_recruit_art.graduate_score_ielts,
            zn_school_recruit_art.graduate_score_toefl, zn_school_recruit_art.graduate_requirements,
            zn_school_recruit_art.graduate_works_requirement, zn_school_recruit_art.graduate_apply_deadline,
            zn_school_recruit_art.undergraduate_majors, zn_school_recruit_art.undergraduate_score_ielts,
            zn_school_recruit_art.undergraduate_score_toefl, zn_school_recruit_art.undergraduate_requirements,
            zn_school_recruit_art.undergraduate_works_requirement, zn_school_recruit_art.undergraduate_apply_deadline,
            zn_school_recruit_art.difficulty_name, zn_school_recruit_art.apply_experience, zn_school_recruit_art.alumni)

        # 学校的研究生招生信息
        zn_school_recruit_graduate_str = '学校名称：%s-%s,录取率：%s, 申请截止时间：%s, 申请人数：%s, 申请学期：%s, Offer发放时间：%s, 申请费用：%s, 学费：%s, 书本费：%s, 生活费：%s, 交通费：%s, 住宿费用：%s, 其他费用：%s, 总花费：%s, GPA成绩：%s, ACT成绩：%s, SAT成绩：%s, SAT2成绩：%s, GRE成绩：%s, GMAT成绩：%s, 雅思成绩：%s, 托福成绩：%s, native成绩：%s, 其他成绩：%s, 奖学金：%s, 申请材料：%s, 申请流程：%s' % (
            zn_school_info.chinese_name, zn_school_info.english_name, zn_school_recruit_graduate.admission_rate,
            zn_school_recruit_graduate.time_apply_deadline, zn_school_recruit_graduate.apply_amount,
            zn_school_recruit_graduate.semester, zn_school_recruit_graduate.time_offer,
            zn_school_recruit_graduate.fee_apply,
            zn_school_recruit_graduate.fee_tuition, zn_school_recruit_graduate.fee_book,
            zn_school_recruit_graduate.fee_life,
            zn_school_recruit_graduate.fee_traffic, zn_school_recruit_graduate.fee_accommodation,
            zn_school_recruit_graduate.fee_others, zn_school_recruit_graduate.fee_total,
            zn_school_recruit_graduate.score_gpa,
            zn_school_recruit_graduate.score_act, zn_school_recruit_graduate.score_sat,
            zn_school_recruit_graduate.score_sat2,
            zn_school_recruit_graduate.score_gre, zn_school_recruit_graduate.score_gmat,
            zn_school_recruit_graduate.score_ielts,
            zn_school_recruit_graduate.score_toefl, zn_school_recruit_graduate.score_native,
            zn_school_recruit_graduate.score_others,
            zn_school_recruit_graduate.scholarship, zn_school_recruit_graduate.material,
            zn_school_recruit_graduate.recruit_flow)

        dataset = []

        zn_school_info_dict = {
            "instruction": f"学校名称：{zn_school_info.chinese_name}-{zn_school_info.english_name},归属国家,学校logo,学校背景图,学校标签,学校位置,官网地址,院校简称",
            "output": zn_school_info_str}
        zn_school_rank_dict = {
            "instruction": f"学校名称:{zn_school_info.chinese_name}-{zn_school_info.english_name},学校排名,世界排名,地区排名",
            "output": zn_school_rank_str}
        zn_school_intro_dict = {
            "instruction": f"学校名称:{zn_school_info.chinese_name}-{zn_school_info.english_name},学校简介,国际学生比例,师生比例,男女比例,学生总数量,本科生数量,研究生数量,就业率,毕业薪资,院校历史,地理位置,校园环境,学校宿舍,图书馆,学校设施,招生办信息,防疫信息,介绍视频url",
            "output": zn_school_intro_str}
        zn_school_selection_reason_dict = {
            "instruction": f"学校名称:{zn_school_info.chinese_name}-{zn_school_info.english_name},招生理由,学校特色,强势专业,热门专业,院系设置,教学特色,差评项,好评项",
            "output": zn_school_selection_reason_str}
        zn_school_recruit_art_dict = {
            "instruction": f"学校名称:{zn_school_info.chinese_name}-{zn_school_info.english_name},招生信息,录取率,申请费用,学费,书本费,生活费,交通费,住宿费用,其他费用,总花费,研究生专业,研究生雅思成绩,研究生托福成绩,研究生申请要求,研究生作品集要求,研究生申请截止日期,本科专业,本科雅思成绩,本科托福成绩,本科申请要求,本科作品集要求,本科申请截止日期,申请难度,申请经验,明星校友",
            "output": zn_school_recruit_art_str}
        zn_school_recruit_graduate_dict = {
            "instruction": f"学校名称:{zn_school_info.chinese_name}-{zn_school_info.english_name},录取率,申请截止时间,申请人数,申请学期,Offer发放时间,申请费用,学费,书本费,生活费,交通费,住宿费用,其他费用,总花费,GPA成绩,ACT成绩,SAT成绩,SAT2成绩,GRE成绩,GMAT成绩,雅思成绩,托福成绩,native成绩,其他成绩,奖学金,申请材料,申请流程",
            "output": zn_school_recruit_graduate_str}
        dataset.append(zn_school_info_dict)
        dataset.append(zn_school_rank_dict)
        dataset.append(zn_school_intro_dict)
        dataset.append(zn_school_selection_reason_dict)
        dataset.append(zn_school_recruit_art_dict)
        dataset.append(zn_school_recruit_graduate_dict)
        return dataset

    def getProject(self, school_id):
        zn_school_department_project_list = zn_school_department_project_mapper.select_by_id(school_id)
        dataset = []
        for zn_school_department_project in zn_school_department_project_list:
            zn_school_deparment_admission_score = zn_school_deparment_admission_score_mapper.select_by_id(
                zn_school_department_project.id)
            if zn_school_deparment_admission_score is None:
                continue
            print(zn_school_deparment_admission_score.atar_score)
            zn_school_deparment_admission_score_mapper_str = '学校名称：%s-%s,专业名称：%s-%s,ATAR分数：%s,UKAlevel三科分数：%s,UKAlevel三科分数（一）：%s,UKAlevel三科分数（二）：%s,UKAlevel三科分数（三）：%s,UKAlevel四科分数：%s,IB分数：%s,SAT分数：%s,ACT分数：%s,AP分数：%s,OSSD分数：%s,BC分数：%s,GAOKAO分数：%s,C9均分分数：%s,985均分分数：%s,211均分分数：%s,非211均分分数：%s,是否接受跨专业/需要相关背景：%s,ATAR要求：%s,UKAlevel三科要求：%s,UKAlevel四科要求：%s,IB要求：%s,SAT要求：%s,ACT要求：%s,AP要求：%s,OSSD要求：%s,BC要求：%s,GAOKAO要求：%s,C9均分要求：%s,985均分要求：%s,211均分要求：%s,非211均分要求：%s,是否接受跨专业/需要相关背景：%s' % (
                zn_school_department_project.chinese_name, zn_school_department_project.english_name,
                zn_school_department_project.chinese_name, zn_school_department_project.english_name,
                zn_school_deparment_admission_score.atar_score, zn_school_deparment_admission_score.ukalevel3_score,
                zn_school_deparment_admission_score.ukalevel3_score1,
                zn_school_deparment_admission_score.ukalevel3_score2,
                zn_school_deparment_admission_score.ukalevel3_score3,
                zn_school_deparment_admission_score.ukalevel4_score,
                zn_school_deparment_admission_score.ib_score, zn_school_deparment_admission_score.sat_score,
                zn_school_deparment_admission_score.act_score, zn_school_deparment_admission_score.ap_score,
                zn_school_deparment_admission_score.ossd_score, zn_school_deparment_admission_score.bc_score,
                zn_school_deparment_admission_score.gaokao_score, zn_school_deparment_admission_score.c9_score,
                zn_school_deparment_admission_score.s985_score, zn_school_deparment_admission_score.s211_score,
                zn_school_deparment_admission_score.sn211_score,
                zn_school_deparment_admission_score.b_accept_md_bg, zn_school_deparment_admission_score.atar_ask,
                zn_school_deparment_admission_score.ukalevel3_ask, zn_school_deparment_admission_score.ukalevel4_ask,
                zn_school_deparment_admission_score.ib_ask, zn_school_deparment_admission_score.sat_ask,
                zn_school_deparment_admission_score.act_ask, zn_school_deparment_admission_score.ap_ask,
                zn_school_deparment_admission_score.ossd_ask, zn_school_deparment_admission_score.bc_ask,
                zn_school_deparment_admission_score.gaokao_ask, zn_school_deparment_admission_score.c9_ask,
                zn_school_deparment_admission_score.s985_ask, zn_school_deparment_admission_score.s211_ask,
                zn_school_deparment_admission_score.sn211_ask,
                zn_school_deparment_admission_score.accept_md_bg)
            zn_school_department_project_str = '学校名称：%s-%s、项目名：%s-%s、院系名称：%s、项目介绍:%s、学位等级：%s、学位名称：%s、学位类型：%s、全日制学制：%s、学制时间：%s、非全日制学制：%s、开学时间：%s、申请截止时间：%s、Offer发放时间：%s、Offer发放截止时间：%s、学术要求：%s、专业链接：%s、申请费用：%s、学费：%s、书本费：%s、生活费：%s、交通费：%s、住宿费用：%s、其他费用：%s、总花费：%s、GPA成绩：%s、ACT成绩：%s、SAT成绩：%s、SAT2成绩：%s、GRE成绩：%s、GMAT成绩：%s、雅思成绩：%s、雅思总分：%s、托福成绩：%s、托福总分：%s、native成绩：%s、其他成绩：%s、申请材料：%s、申请要点：%s、是否减免：%s、减免条件：%s、爬虫ID：%s、是否删除：%s、创建人：%s、更新人：%s、创建人名称：%s、更新人名称：%s、创建时间：%s、更新时间：%s、关注总数：%s、评分：%s、标签：%s、排序：%s、申请费值：%s、币种id：%s、专业小方向：%s、专业简称：%s、开学月份：%s、洗数据保留原始表id：%s、职业规划：%s、澳洲专用：%s,排序权重：%s' % (
                zn_school_department_project.chinese_name, zn_school_department_project.english_name,
                zn_school_department_project.chinese_name, zn_school_department_project.english_name,
                zn_school_department_project.depart_name, zn_school_department_project.introduction,
                zn_school_department_project.degree_level, zn_school_department_project.degree_name,
                zn_school_department_project.degree_type, zn_school_department_project.length_of_full,
                zn_school_department_project.length_of_schoolings, zn_school_department_project.length_of_part,
                zn_school_department_project.semester, zn_school_department_project.time_apply_deadline,
                zn_school_department_project.time_offer, zn_school_department_project.time_offer_deadline,
                zn_school_department_project.science_requirement, zn_school_department_project.major_link,
                zn_school_department_project.fee_apply, zn_school_department_project.fee_tuition,
                zn_school_department_project.fee_book, zn_school_department_project.fee_life,
                zn_school_department_project.fee_traffic, zn_school_department_project.fee_accommodation,
                zn_school_department_project.fee_others, zn_school_department_project.fee_total,
                zn_school_department_project.score_gpa, zn_school_department_project.score_act,
                zn_school_department_project.score_sat, zn_school_department_project.score_sat2,
                zn_school_department_project.score_gre, zn_school_department_project.score_gmat,
                zn_school_department_project.score_ielts, zn_school_department_project.score_ielts_total,
                zn_school_department_project.score_toefl, zn_school_department_project.score_toefl_total,
                zn_school_department_project.score_native, zn_school_department_project.score_others,
                zn_school_department_project.material, zn_school_department_project.admission_elements,
                zn_school_department_project.reduce_status, zn_school_department_project.reduce_condition,
                zn_school_department_project.spider_id, zn_school_department_project.delete_status,
                zn_school_department_project.create_by, zn_school_department_project.update_by,
                zn_school_department_project.create_name, zn_school_department_project.update_name,
                zn_school_department_project.create_time, zn_school_department_project.update_time,
                zn_school_department_project.attention_total, zn_school_department_project.score,
                zn_school_department_project.market_tags, zn_school_department_project.orderby,
                zn_school_department_project.application_fee_value, zn_school_department_project.currency_id,
                zn_school_department_project.small_direction, zn_school_department_project.project_abbreviations,
                zn_school_department_project.opening_month, zn_school_department_project.org_id,
                zn_school_department_project.career_opportunities, zn_school_department_project.cricos_code,
                zn_school_department_project.weight)

            zn_school_deparment_admission_score_mapper_dict = {
                "instruction": f"专业详情信息：{zn_school_department_project.chinese_name}-{zn_school_department_project.english_name}之专业申请要求，学校名称:{zn_school_department_project.chinese_name}-{zn_school_department_project.english_name},专业名称:{zn_school_department_project.chinese_name}-{zn_school_department_project.english_name}ATAR分数、UKAlevel三科分数、UKAlevel三科分数（一）、UKAlevel三科分数（二）、UKAlevel三科分数（三）、UKAlevel四科分数、IB分数、SAT分数、ACT分数、AP分数、OSSD分数、BC分数、GAOKAO分数、C9均分分数、985均分分数、211均分分数、非211均分分数、是否接受跨专业/需要相关背景、ATAR要求、UKAlevel三科要求、UKAlevel四科要求、IB要求、SAT要求、ACT要求、AP要求、OSSD要求、BC要求、GAOKAO要求、C9均分要求、985均分要求、211均分要求、非211均分要求、是否接受跨专业/需要相关背景",
                "output": zn_school_deparment_admission_score_mapper_str}
            zn_school_department_project_dict = {
                "instruction": f"专业详情信息：{zn_school_department_project.chinese_name}-{zn_school_department_project.english_name}、学校名称:{zn_school_department_project.chinese_name}-{zn_school_department_project.english_name}、院系名称、项目介绍、学位等级、学位名称、学位类型、全日制学制、学制时间、非全日制学制、开学时间、申请截止时间、Offer发放时间、Offer发放截止时间、学术要求、专业链接、申请费用、学费、书本费、生活费、交通费、住宿费用、其他费用、总花费、GPA成绩、ACT成绩、SAT成绩、SAT2成绩、GRE成绩、GMAT成绩、雅思成绩、雅思总分、托福成绩、托福总分、native成绩、其他成绩、申请材料、申请要点、是否减免、减免条件、爬虫ID、是否删除、创建人、更新人、创建人名称、更新人名称、创建时间、更新时间、关注总数、评分、标签、排序、申请费值、币种id、专业小方向、专业简称、开学月份、洗数据保留原始表id、职业规划、澳洲专用、排序权重",
                "output": zn_school_department_project_str}
            dataset.append(zn_school_deparment_admission_score_mapper_dict)
            dataset.append(zn_school_department_project_dict)
        return dataset
