# Kinghao 2022/1/22
import os,json,math
from PIL import Image
points_file=open('./examples/res/point-results.json')
frame1=5
frame2=150

def cacl_arm_rotation(frame1,frame2):
    content_list = json.loads(points_file.read())
    f1,f2=content_list[frame1//5-1]['points'],content_list[frame2//5-1]['points']
    #计算左边手臂
    left_f1_x1,left_f1_y1=f1[8][0],f1[8][1]
    left_f1_x2,left_f1_y2=f1[6][0],f1[6][1]
    vector1=[left_f1_x1-left_f1_x2,left_f1_y1-left_f1_y2]
    left_f2_x1, left_f2_y1 = f2[8][0], f2[8][1]
    left_f2_x2, left_f2_y2 = f2[6][0], f2[6][1]
    vector2=[left_f2_x1-left_f2_x2,left_f2_y1-left_f2_y2]
    # 夹角余弦计算公式：向量内积除以向量模的乘积
    cal_up=vector1[0]*vector2[0]+vector1[1]*vector2[1]
    cal_down=math.sqrt(vector1[0]**2+vector1[1]**2)*math.sqrt(vector2[0]**2+vector2[1]**2)
    cos_a=cal_up/cal_down
    # 弧度值转角度值
    left_a=math.acos(cos_a)*180/math.pi

    #计算右边手臂
    right_f1_x1, right_f1_y1 = f1[7][0], f1[7][1]
    right_f1_x2, right_f1_y2 = f1[5][0], f1[5][1]
    vector1 = [right_f1_x1 - right_f1_x2, right_f1_y1 - right_f1_y2]
    right_f2_x1, right_f2_y1 = f2[7][0], f2[7][1]
    right_f2_x2, right_f2_y2 = f2[5][0], f2[5][1]
    vector2 = [right_f2_x1 - right_f2_x2, right_f2_y1 - right_f2_y2]
    cal_up = vector1[0] * vector2[0] + vector1[1] * vector2[1]
    cal_down = math.sqrt(vector1[0] ** 2 + vector1[1] ** 2) * math.sqrt(vector2[0] ** 2 + vector2[1] ** 2)
    cos_a = cal_up / cal_down
    right_a=math.acos(cos_a)*180/math.pi

    origin_a=float(input("原左arm骨骼Rotation值："))
    print("大臂抬动角度："+str(left_a))
    print("输入Rotation值："+str(origin_a-left_a))

    origin_a = float(input("原右arm骨骼Rotation值："))
    print("大臂抬动角度：" + str(right_a))
    print("输入Rotation值：" + str(origin_a + right_a))

#在unity中素材的左右肩坐标
left_shoulder=[-0.48,5.54]
right_shoulder=[0.56,5.32]
# 为i号点计算坐标变化
def calc_transform(i,frame1,frame2):
    content_list = json.loads(points_file.read())
    f1, f2 = content_list[frame1 // 5 - 1]['points'], content_list[frame2 // 5 - 1]['points']
    f1_ls,f1_rs=[f1[6][0],f1[6][1]],[f1[5][0],f1[5][1]]
    length_unity=math.sqrt((right_shoulder[0]-left_shoulder[0])**2+(right_shoulder[1]-left_shoulder[1])**2)
    length_f1=math.sqrt((f1_rs[0]-f1_ls[0])**2+(f1_rs[1]-f1_ls[1])**2)
    var_x,var_y=f2[i][0]-f1[i][0],f2[i][1]-f1[i][1]
    res_x,res_y=var_x*length_unity/length_f1,var_y*length_unity/length_f1
    origin_x = float(input("原坐标x值："))
    print("x方向坐标变化："+str(var_x)+" transform变化：" + str(res_x))
    print("输入transform_x：" + str(origin_x+res_x))
    origin_y = float(input("原坐标y值："))
    print("y方向坐标变化：" + str(var_y) + " transform变化：" + str(res_y))
    print("输入transform_y：" + str(origin_y + res_y))

if __name__ == '__main__':
    # cacl_arm_rotation(frame1,frame2)
    calc_transform(6,frame1,frame2)