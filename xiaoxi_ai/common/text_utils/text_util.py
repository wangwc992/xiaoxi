from nltk.tokenize import sent_tokenize
import re


def split_text_sentence(paragraphs, chunk_size=300, overlap_size=100):
    '''
    按指定 chunk_size 和 overlap_size 交叠割文本
    '''
    # 分割文本句子，返回的是句子列表
    sentences = [s.strip() for s in sent_tokenize(paragraphs)]
    chunks = []
    i = 0
    merged = False  # Add a flag to track whether a merge has occurred
    while i < len(sentences):
        chunk = sentences[i]
        overlap = ''
        prev_len = 0
        prev = i - 1
        # 向前计算重叠部分
        while prev >= 0 and len(sentences[prev]) + len(overlap) <= overlap_size:
            overlap = sentences[prev] + ' ' + overlap
            prev -= 1
        chunk = overlap + chunk
        next = i + 1
        # 向后计算当前chunk
        while next < len(sentences) and len(sentences[next]) + len(chunk) <= chunk_size:
            chunk = chunk + ' ' + sentences[next]
            next += 1
        # chunk 太小，合并到前一个 chunk
        if len(chunk) < chunk_size / 2:
            if not merged:  # Only merge if a merge has not already occurred
                chunks[-1] += chunk
                merged = True  # Set the flag to True after a merge
            else:
                chunks.append(chunk)
                merged = False  # Reset the flag when starting a new chunk
        else:
            chunks.append(chunk)
            merged = False  # Reset the flag when starting a new chunk
        i = next
    return chunks


def split_text_str(paragraphs, chunk_size=300, overlap_size=100):
    '''
        分割字符串，chunk_size 为每个 chunk 的长度，overlap_size 为重叠部分的长度
    '''
    #
    chunks = []
    start = 0
    while start < len(paragraphs):
        end = min(start + chunk_size, len(paragraphs))
        chunks.append(paragraphs[start:end])
        start = end - overlap_size
        # 如果最后一个 chunk 的长度小于 overlap_size的二分之一，则合并到前一个 chunk，并且删除最后一个 chunk，结束循环
        if len(chunks[-1]) < chunk_size:
            if len(chunks[-1]) < chunk_size / 2:
                chunks[-2] += chunks[-1]
                chunks.pop()
            break
    return chunks
