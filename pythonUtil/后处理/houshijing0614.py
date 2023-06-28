
def post_process(detect_results, part_number, qty, part_name_cn):
    # part_number = {'造型': '莱茵蓝外后视镜', '360': '有', 'arabic': '无', '照地灯': '无', '零件号': '601000687AAAVQ'}
    part_number_raw = eval(part_number)
    # part_number_raw = part_number

    # 颜色编码对应
    colorcode_dict = {
        "AAAUD": "ganlanhui",  # 橄榄灰
        "AAAUF": "haiyanhui",  # 海岩灰
        "AAAKV": "yizeyin",  # 依泽银
        "AAACL": "xintanjinghei",  # 新碳晶黑
        "AAABW": "xinkaqibai",  # 新卡其白
        "AAAGV": "huanyinghui",  # 幻影灰
        "AAAVQ": "laiyinlan",  # 莱茵蓝
        "AAAJK": "luolanzi",  # 罗兰紫
        "AAAKH": "nasidakayin",  # 纳斯达克银
        "AAAWB": "shenyelan",  # 深夜蓝
        "AAANL": "xueshihong",  # 血石红
        "AAAGW": "hawanahui",  # 哈瓦那灰
        "AAASJ": "jiguanglv",  # 极光绿
        "AAAGX": "kejihui",  # 科技灰
    }

    car_type = "None"
    new_partnum = "None"
    if part_number_raw["零件号"][:9] == "601000484":
        car_type = "T26"
        new_partnum = f"{car_type}_{colorcode_dict[part_number_raw['零件号'][-5:]]}_bai"
    elif part_number_raw["零件号"][:9] == "601000480":
        car_type = "T26"
        new_partnum = f"{car_type}_{colorcode_dict[part_number_raw['零件号'][-5:]]}_hei"
    elif part_number_raw["零件号"][:9] == "601000478":
        return False, 0

    elif part_number_raw["零件号"][:9] in [
        "601000017",
        "601000085",
        "601000667",
        "601000669",
        "601000673",
        "601000687",
        "601000689",
        "601000671",
        "601001032",
        "601001038",
        "601001074",
        "601001197"
    ]:
        car_type = "T1AD"
        ######################################
        new_partnum = f"{car_type}_{colorcode_dict[part_number_raw['零件号'][-5:]]}"
        ######################################
    elif part_number_raw["零件号"][:9] in [
        "601000592",
        "601000594",
        "601000699"
    ]:
        car_type = "T18"
        ######################################
        new_partnum = f"{car_type}_{colorcode_dict[part_number_raw['零件号'][-5:]]}"
        ######################################

    # houshijing_dict = {
    #     "360": "360",
    #     "arabic": "arabic",
    #
    #     part_number_raw['零件号']: new_partnum
    # }

    list_360 = []

    # 提前统计360摄像头
    for results in detect_results:
        for result in results:
            #############################
            # list_360.append(houshijing_dict[result['label']])
            list_360.append(result['label'])
            ###############################

    # 进行360和落地灯判定，目前模型都标注为360。
    flag_360 = False
    if part_number_raw['360'] == "有" and part_number_raw['照地灯'] == "有":
        # 如果要求是有360和有落地灯，则【360】总数是2
        if int(list_360.count("360")) >= 1:
            flag_360 = True
    elif part_number_raw['360'] == "无" and part_number_raw['照地灯'] == "有":
        # 如果要求是无360和有落地灯，则【360】总数是1
        if int(list_360.count("360")) >= 1:
            flag_360 = True
    elif part_number_raw['360'] == "有" and part_number_raw['照地灯'] == "无":
        # 如果要求是有360和无落地灯，则【360】总数是1
        if int(list_360.count("360")) >= 1:
            flag_360 = True
    elif part_number_raw['360'] == "无" and part_number_raw['照地灯'] == "无":
        # 如果要求是无360和无落地灯，则【360】总数是0
        if int(list_360.count("360")) == 0:
            flag_360 = True

    # 阿拉伯文判定
    flag_word = False
    if part_number_raw['arabic'] == "有":
        # 要求有
        if int(list_360.count("arabic")) >= 1:
            flag_word = True
        else:
            flag_word = False
    else:
        # 要求没有
        if int(list_360.count("arabic")) == 0:
            flag_word = True
        else:
            flag_word = False

    for results in detect_results:
        for result in results:
            if result['label'] in ["360", "arabic"]:
                continue
            elif flag_360 and flag_word and new_partnum == result['label']:
                return True, 0
    return False, 0


if __name__ == '__main__':
    detect_results = [[{'label': 'T1AD_laiyinlan', 'score': 0.9706354737281799, 'boundary': [1072, 498, 1858, 1018]},
      {'label': '360', 'score': 0.8995456099510193, 'boundary': [1523, 745, 1619, 831]}], []]
    part_number = {'造型': '莱茵蓝外后视镜', '360': '有', 'arabic': '无', '照地灯': '无', '零件号': '601000687AAAJK'}
    print(post_process(detect_results, part_number, 'qty', 'part_name_cn'))





