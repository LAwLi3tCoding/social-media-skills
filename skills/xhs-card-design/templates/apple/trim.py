# 去掉外框和多余白边，四周留 pad 像素白边
import sys
from PIL import Image, ImageChops
for f in sys.argv[1:]:
    im=Image.open(f).convert('RGB');im=im.crop((8,8,im.width-8,im.height-8))
    bb=ImageChops.difference(im,Image.new('RGB',im.size,'white')).point(lambda v:255 if v>12 else 0).getbbox()
    pad=36;im=im.crop((max(bb[0]-pad,0),max(bb[1]-pad,0),min(bb[2]+pad,im.width),min(bb[3]+pad,im.height)));im.save(f);print(f,im.size)
