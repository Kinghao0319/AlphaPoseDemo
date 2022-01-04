# Kinghao 2022/1/2
import functools
import json, os

json_file = open('./examples/res/runRes/alphapose-results.json')
res_file = open('./examples/res/runRes/point-results.json', "w+")


def compare(a, b):
    if a['image_id'] < b['image_id']:
        return -1
    else:
        return 1


def get_image_id(elem):
    return elem['image_id']


if __name__ == "__main__":
    # print(os.getcwd())

    str = json_file.read()
    content = list(json.loads(str))

    for obj in content:
        # print(obj)
        obj['points'] = []
        for i in range(17):
            cur_point = [obj['keypoints'][i * 3], obj['keypoints'][i * 3 + 1]]
            obj['points'].append(cur_point)
        del obj['keypoints']
        del obj['category_id']
        del obj['score']
        # obj['points_num']=len(obj['points'])
        # print(obj)

    # content.sort(key=get_image_id)
    content.sort(key=functools.cmp_to_key(compare)) # 按image_id排序的第二种写法

    res_file.write(json.dumps(content, indent=4))

    json_file.close()
    res_file.close()
