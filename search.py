import math
from PIL import Image
from functools import reduce
import pandas as pd

target='image/paris_eiffel_000266.jpg'
img1 = Image.open(target)
# img1.show()
target_cut=[348.000000,3.000000,595.000000,508.000000]
# target_cut=[]
whole_feature='features-64.csv'
text=['defense','eiffel','general','invalides','louvre','moulinrouge','museedorsay','notredame','pantheon','pompidou','sacrecoeur','triomphe']

'''Initialize the target graph and extract the features'''

def image_initialize(size_list, target_path):
    target = Image.open(target_path)
    if len(size_list)==4:
        area = size_list
        img = target.crop(area)
        img = img.resize((8, 8), Image.ANTIALIAS).convert('L')
        avg = reduce(lambda x, y: x + y, img.getdata()) / 64
        im_data = map(lambda x: 0 if x < avg else 1, img.getdata())
        im_data = list(im_data)
        return im_data
    else:
        img = target.resize((8, 8), Image.ANTIALIAS).convert('L')
        avg = reduce(lambda x, y: x + y, img.getdata()) / 64
        im_data = map(lambda x: 0 if x < avg else 1, img.getdata())
        im_data = list(im_data)
        return im_data

'''
try to find the test graph's path whether contains text features like location information
So that, we can reduce the comparing size to increase speed
'''

def path(path1):
    a=str(path1)
    for i in range(0,len(text),1):
        t=str(text[i])
        result = t in a
        if result is True:
            p = 'features-csv/'+t+'.csv'
            return p
        else:
            continue
    return whole_feature

'''Opening feature file according to target graph'''

def data_source(address):
    data = pd.read_csv(address, header=None, sep=',', skiprows=1)
    data = data.drop([0], axis=1)
    hash = data.values
    return hash

'''Calculate the cosine distance of two features'''

def cos_dist(a, b):
    if len(a) != len(b):
        return None
    part_up = 0.0
    a_sq = 0.0
    b_sq = 0.0
    for x, y in zip(a, b):
        part_up += x * y
        a_sq += x ** 2
        b_sq += y ** 2
    part_down = math.sqrt(a_sq * b_sq)
    if part_down == 0.0:
        return None
    else:
        return part_up / part_down

'''Using the extracted feature of the target compare with the data features, and conduct a 12 length list '''
'''containing the 12 most similar results'''

def compare(source,target_feature):
    distance = []
    results = []
    for i in range(0, len(hash), 1):
        b = hash[i][1:]
        dist = cos_dist(a, b)
        distance.append((hash[i][0], dist))
    for f, dist in sorted(distance, key=lambda i: i[1], reverse=True):
        results.append((dist, f))
        print(dist,f)
    return results


a=image_initialize(target_cut,target)
testpath=path(target)
hash=data_source(testpath)
result= compare(hash,a)
add=[]
# print(result)
for a in range(0,len(result),1):
    add.append(result[a][1])
    # print(result[a][1])
    # img1 = Image.open(result[a][1])
    # img1.show()
add1=pd.DataFrame(add)
# print(add1)
add1.to_csv('eiffel_000266.csv',encoding='UTF-8')




