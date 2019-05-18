from PIL import Image
from functools import reduce
import glob
import pandas as pd

total_image=glob.glob(r'F:\spring-2019\Multimedia Systems\proj2\paris_2\paris\triomphe/*.jpg')
length=len(total_image)
features = []
for f in total_image:
    try:
        list1=[]
        im = Image.open(f)
        im = im.resize((8, 8), Image.ANTIALIAS).convert('L')
        avg = reduce(lambda x, y: x + y, im.getdata()) / 64
        im_data = map(lambda x: 0 if x < avg else 1, im.getdata())
        im_data=list(im_data)
        list1.append(f)
        # print(im_data)
        for i in range(0,len(im_data),1):
            list1.append(im_data[i])
        # features.append((f,im_data))
        features.append(list1)
        # print(features)
        print("image: %s\t avg: %f\t" % (f, avg))
    except OSError:
        pass

csv=pd.DataFrame(data=features)
print(csv)
csv.to_csv('triomphe.csv',encoding='UTF-8')
