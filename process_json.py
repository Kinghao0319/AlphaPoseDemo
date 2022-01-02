# Kinghao 2022/1/2

import json,os
json_file=open('./examples/res/alphapose-results.json')
res_file=open('./examples/res/point-results.json',"w+")
if __name__ == "__main__":
    # print(os.getcwd())

    str=json_file.read()
    content=json.loads(str)

    for obj in content:
        # print(obj)
        obj['points']=[]
        for i in range(17):
            cur_point=[obj['keypoints'][i*3],obj['keypoints'][i*3+1]]
            obj['points'].append(cur_point)
        del obj['keypoints']
        del obj['category_id']
        del obj['score']
        # obj['points_num']=len(obj['points'])
        # print(obj)

    res_file.write(json.dumps(content,indent=4))

    json_file.close()
    res_file.close()