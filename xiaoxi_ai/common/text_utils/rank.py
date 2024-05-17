
def rrf(ranks, k=1):
    ret = {}
    ids = []
    # 遍历每次的排序结果
    for rank in ranks:
        # 遍历排序中每个元素
        score = len(rank)
        for val in rank:
            id = str(val.uuid)
            if id not in ids:
                ret[id] = {"score": 0, "text": val.instruction + ' ' + val.output}
                ids.append(id)
            # 计算 RRF 得分
            ret[id]["score"] += score
            score -= 1
    # 按 RRF 得分排序，并返回列表
    # 按 RRF 得分排序，并返回列表
    sorted_list = sorted(ret.values(), key=lambda x: x['score'], reverse=True)
    return sorted_list
