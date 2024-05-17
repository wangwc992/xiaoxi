from bs4 import NavigableString, BeautifulSoup
import xiaoxi_ai.common.text_utils.text_util as text_util
import xiaoxi_ai.common.text_utils.html_dispose as html_dispose

url = 'https://study.sydneyuniversity.cn/areas-of-study/'
url = 'https://www.southampton.ac.uk/courses/digital-marketing-masters-msc'
url = 'https://study.unimelb.edu.au/find/courses/graduate/master-of-instructional-leadership/'
url = 'https://www.monash.edu/study/courses/find-a-course/global-business-b6018?international=true'
url = 'https://www.manchester.ac.uk/study/masters/courses/list/04342/msc-mechanical-engineering-design/'
url = 'https://www.monash.edu/study/courses/find-a-course/information-technology-c6001?international=true'
url = '''https://www.manchester.ac.uk/study/masters/courses/list/08446/llm-law/'''
url = '''https://www.sydney.edu.au/courses/courses/pc/master-of-urban-and-regional-planning.html'''
url = '''https://study.unimelb.edu.au/?in_c=home-path'''
soup = html_dispose.getSoup(url)
title = soup.find('title').get_text() + " "
reduced_structure = html_dispose.reduced_structure(soup)
text = html_dispose.cleat_text(html_dispose.process_tags(reduced_structure))
sentence_list = text_util.split_text_sentence(text, 300, 100)
# text_list 里面有句子的长度大于600的，进行分割，并且在前面加上异常数据
new_list = list()
# sentence_list 里面有句子的长度不大于600的加到new_list里面，否则使用text_util.split_text_str，并且在前面加上异常数据，在加到new_list里面
for sentence in sentence_list:
    if len(sentence) > 600:
        new_list.extend([f"可能是异常数据：{title}{s}" for s in text_util.split_text_str(sentence, 300, 100)])
    else:
        new_list.append(title + sentence)

print(new_list)