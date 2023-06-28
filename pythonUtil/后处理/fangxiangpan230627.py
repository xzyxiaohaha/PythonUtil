def post_process(detect_results, part_number, qty, part_name_cn):
    label2partnum = {
        '404000190AA': 'fxp1',
        '404000184AA': 'fxp1',
        '404000584AA': 'fxp1',
        '404000085AA': 'fxp1',
        'fxp1': 'fxp1',

        '404000217AA': 'fxp2',
        '404000258AA': 'fxp2',
        '404000062AA': 'fxp2',
        '404000719AA': 'fxp2',
        'fxp2': 'fxp2',

        '404000385AA': 'fxp3',
        '404000476AA': 'fxp3',
        '404000914AA': 'fxp3',
        '404000913AA': 'fxp3',
        'fxp3': 'fxp3',

        '404000478AA': 'fxp4',
        '404000479AA': 'fxp4',
        'fxp4': 'fxp4',

        '404000498AA': 'fxp5',
        '404000526AA': 'fxp5',
        '404000745AA': 'fxp5',
        'fxp5': 'fxp5',

        '404000500AA': 'fxp6',
        '404000879AA': 'fxp6',
        '404001076AA': 'fxp6',
        'fxp6': 'fxp6',

        '404000637AABBK': 'fxp7',
        '404000638AAABK': 'fxp7',
        'fxp7': 'fxp7',

        '404000137AA': 'fxp8',
        'fxp8': 'fxp8',
    }

    index = -1
    for results in detect_results:
        index += 1
        for result in results:
            if part_number in label2partnum.keys() and result['label'] in label2partnum.keys():
                if label2partnum[result['label']] == label2partnum[part_number]:
                    final_result = True
                    return final_result, index
            else:
                if result['label'] == part_number:
                    final_result = True
                    return final_result, index
    final_result = False
    img_index = 0
    return final_result, img_index
