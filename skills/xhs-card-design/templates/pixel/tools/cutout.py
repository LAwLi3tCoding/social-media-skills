#!/usr/bin/env python3
"""把纯色底插图按等宽切成 N 个并抠掉底色（从四边泛洪）。
用法：python3 cutout.py 输入图 输出前缀 名字1 名字2 ...   （横向一排、间距均匀的道具图）
      python3 cutout.py --single 输入图 输出.png           （单个角色/物件，整张抠图）"""
import sys
from collections import deque
from PIL import Image
import numpy as np
def cutout(im, tol=18):
    a=np.array(im.convert('RGBA')).astype(int); h,w=a.shape[:2]
    bg=np.median(np.concatenate([a[0,:,:3],a[-1,:,:3],a[:,0,:3],a[:,-1,:3]]),axis=0)
    near=(np.abs(a[:,:,:3]-bg).max(axis=2)<=tol); seen=np.zeros((h,w),bool); q=deque()
    for x in range(w): q+=[(0,x),(h-1,x)]
    for y in range(h): q+=[(y,0),(y,w-1)]
    while q:
        y,x=q.popleft()
        if 0<=y<h and 0<=x<w and not seen[y,x] and near[y,x]:
            seen[y,x]=True; q.extend([(y+1,x),(y-1,x),(y,x+1),(y,x-1)])
    a[seen,3]=0; o=Image.fromarray(a.astype('uint8')); return o.crop(o.getbbox())
if sys.argv[1]=='--single':
    cutout(Image.open(sys.argv[2])).save(sys.argv[3])
else:
    im=Image.open(sys.argv[1]); pre=sys.argv[2]; names=sys.argv[3:]; n=len(names); W=im.width/n
    for i,nm in enumerate(names):
        cutout(im.crop((int(i*W),0,int((i+1)*W),im.height))).save(f'{pre}{nm}.png')
