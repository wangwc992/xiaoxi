import re
import urllib.request
from urllib.parse import urlparse

from bs4 import BeautifulSoup, Comment


def getSoup(url):
    # Referer:
    # https://www.sydney.edu.au/courses/courses/pc/master-of-urban-and-regional-planning.html
    # Sec-Ch-Ua:
    # "Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"
    # Sec-Ch-Ua-Mobile:
    # ?0
    # Sec-Ch-Ua-Platform:
    # "Windows"
    # User-Agent:
    # Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'Referer': url,
        'Sec-Ch-Ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"'

    }
    if not url.startswith('http'):
        url = 'https://' + url
    parsed_url = urlparse(url)
    if not all([parsed_url.scheme, parsed_url.netloc]):
        print(f"Invalid URL: {url}")
        raise ValueError(f"Invalid URL: {url}")
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return BeautifulSoup(content, 'html.parser')


def reduced_structure(soup):
    # soup 里面有且仅有一个 main 标签，提取出main和第一个title为新的soup
    main_tag = soup.find('main')
    title_tag = soup.find('title')
    new_soup = BeautifulSoup(features='html.parser')
    if title_tag:
        new_soup.append(title_tag)
    if main_tag:
        new_soup.append(main_tag)
        soup = new_soup

    # 如果一个 url <ul> <li> <a>View all courses</a> <span>|</span></li><li> <a>收到撒发大水</a> </li></ul>标签里面只有 a标签里面有数据则 soup将这整个ul标签删除
    for ul in soup.find_all('ul'):
        non_a_text = ''.join(t.strip() for t in ul.find_all(text=True, recursive=True) if not t.parent.name == 'a')
        if not non_a_text:
            ul.decompose()
        #   non_a_text里面包含 || 则删除这个ul标签
        elif '|||' in non_a_text:
            ul.decompose()

    ignore_tags = ['header', 'style', 'script', 'link', 'img', 'input', 'button', 'form','a', 'aside', 'footer']
    tags = ['meta', 'div', 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'span', 'strong', 'em', 'blockquote', 'li', 'td',
            'th']
    '''
    返回简化后的HTML内容: Str
    '''
    # 简化HTML内容，删除不必要的标签和属性
    for ignore_tag in ignore_tags:
        for element in soup.find_all(ignore_tag):
            element.decompose()  # 删除指定标签
    for element in soup(text=lambda text: isinstance(text, Comment)):
        element.extract()  # 删除注释
    for tag in soup.find_all():
        tag.attrs = {}  # 删除标签的属性
    for line in soup.find_all('br'):
        line.decompose()  # 删除换行标签
    for tag in soup.find_all():
        if not tag.get_text().strip():
            tag.decompose()  # 删除空标签
    for tag in soup.find_all():
        if tag.parent.name == tag.name:
            tag.unwrap()  # 删除重复的父标签
    # 从上到下，一个一个的获取标签内的文本数据，不能嵌套的标签获取重复的数据，如果遇见h标签，判断上一个获取的文本数据结尾是否是标点符号，如果不是则加上句号号
    c = process_tags(soup)
    # simplify_structure_txt = str(soup.get_text()).replace('\n', '')
    return soup


from bs4 import BeautifulSoup, NavigableString


def process_tags(soup):
    punctuations = ['.', '!', '?', '。', '！', '？']
    previous_text = ''
    flag = False
    for tag in soup.recursiveChildGenerator():
        if flag:
            flag = False
            continue
        if isinstance(tag, NavigableString):
            text = tag.strip()
            if text:
                if previous_text and previous_text[-1]:
                    previous_text += ' '
                previous_text += ' ' + text
        elif tag.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            if previous_text and previous_text[-1]:
                previous_text += ' '
        elif tag.name == 'a':
            text = tag.get_text().strip()
            flag = True
            if len(text) >= 4:
                if previous_text and previous_text[-1] not in punctuations:
                    previous_text += ' '
                previous_text += ' ' + text
    return previous_text


def replace_link_with_url(html_text):
    def replacer(match):
        a_tag = match.group()
        url_match = re.search(r'href="(.*?)"', a_tag)
        text_match = re.search(r'>(.*?)<', a_tag)
        if url_match and text_match:
            url = url_match.group(1)
            text = text_match.group(1)
            return f' {text} ({url}) '
        else:
            return ''

    html_text = re.sub(r'<a .*?>.*?</a>', replacer, html_text)
    html_text = re.sub(r'<.*?>|&nbsp;', ' ', html_text).replace('  ', '')
    return html_text.strip()


def cleat_text(text):  # 定义清理文本的方法
    text = text.strip().replace("\n\n", "").replace("\n", " ").replace(" ", " ")
    # 多空格变成一个空格
    return re.sub(r'\s+', ' ', text)  # 返回去除空格和换行符的文本内容
