import numpy as np
import cv2
from PIL import Image
from functools import reduce

def img2cols(img):
    img = img.reshape(img.size, order="C")
    # convert the data type as np.float64
    img = img.astype(np.float64)
    return img

def getSift():
    img_path1 = 'image/paris_defense_000000.jpg'

    img = cv2.imread(img_path1)
    print(img.shape)
    gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    sift = cv2.xfeatures2d.SIFT_create()
    kp = sift.detect(gray,None)
    print(type(kp),type(kp[0]))
    print(kp[0].pt)
    des = sift.compute(gray,kp)
    print(type(kp),type(des))
    print(type(des[0]), type(des[1]))
    print(des[0],des[1])
    print(des[1].shape,len(des[0]))
    img=cv2.drawKeypoints(gray,kp,img)
    cv2.imshow("SIFT", img)
    cv2.waitKey(0)


# getSift()
def phash(img):

    img = img.resize((256, 256), Image.ANTIALIAS).convert('L')
    # img.show()
    avg = reduce(lambda x, y: x + y, img.getdata()) / 65536.
    hash_value=reduce(lambda x, y: x | (y[1] << y[0]), enumerate(map(lambda i: 0 if i < avg else 1, img.getdata())), 0)
    return hash_value


path1='image/paris_defense_000054.jpg'
path2='image/paris_defense_000056.jpg'
box = (130, 17, 843, 732)
img1 = Image.open(path1)
# img3 = Image.open(path1)
# area = (130, 17, 834, 723)
# img3 = img3.crop(area)
# cropped_img.show()
img2 = Image.open(path2)
# hamming distance
distance = bin(phash(img1) ^ phash(img2)).count('1')
print(bin(phash(img1)))
similary = 1 - distance / max(len(bin(phash(img1))), len(bin(phash(img2))))
print(similary,distance)
print(phash(img1))
