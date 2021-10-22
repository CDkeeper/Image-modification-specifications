from PIL import Image
import os.path
import glob

def convertSize(jpgfile,outdir,width=256,height=256):  #修改后新图片需要的大小
    img=Image.open(jpgfile)
    try:
        new_img = img.resize((width, height), Image.BILINEAR)
        if new_img.mode == 'P':
            new_img = new_img.convert("RGB")
        if new_img.mode == 'RGBA':
            new_img = new_img.convert("RGB")
        new_img.save(os.path.join(outdir, os.path.basename(jpgfile)))
    except Exception as e:
        print(e)

for jpgfile in glob.glob("C:/Users/chenda/Desktop/7/result/Our/*.png"):  #修改该文件夹下的png图片
    convertSize(jpgfile,"C:/Users/chenda/Desktop/7/result/Our_n")  #另存为的文件夹路径