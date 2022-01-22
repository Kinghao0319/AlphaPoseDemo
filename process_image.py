# Kinghao 2022/1/22
import os,json
from PIL import Image
points_file=open('./examples/res/point-results.json')
if __name__ == '__main__':
    if not os.path.exists('examples/res/image'):
        os.makedirs('examples/res/image')

    frame0=Image.open('examples/frames/frame00005.jpg')
    print("宽："+str(frame0.width)+" 高："+str(frame0.height))
    content_list = json.loads(points_file.read())

    count=1
    for c in content_list:
        points_list=c['points']
        cur_image=Image.new('RGB',(frame0.width,frame0.height),(256,256,256))
        i=0
        for p in points_list:
            for x in range(int(p[0])-2,int(p[0])+3):
                for y in range(int(p[1])-2,int(p[1])+3):
                    if i==5 or i==6:
                        cur_image.putpixel((x, y), (0, 0, 255))
                    elif i==7 or i==8:
                        cur_image.putpixel((x, y), (0, 255, 0))
                    elif i==9 or i==10:
                        cur_image.putpixel((x, y), (0, 0, 0))
                    else:
                        cur_image.putpixel((x,y),(255,0,0))
            i+=1
        cur_image.save("examples/res/image/frame"+str(count*5)+".jpg")
        count+=1
