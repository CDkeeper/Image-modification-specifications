import os

class BatchRename():  #定义一个重命名的类
    def __init__(self):
        self.path = 'C:/Users/chenda/Desktop/7/result/Our'

    def rename(self):
        filelist = os.listdir(self.path)
        total_num = len(filelist)
        i = 1
        for item in filelist:
            if item.endswith('.jpg'):   #将当前格式的图片改为下面格式的图片
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(os.path.abspath(self.path), '' + str(i) + '.png') #重新命名并改格式
                try:
                    os.rename(src, dst)
                    print('converting %s to %s ...' % (src, dst))
                    i = i + 1
                except:
                    continue

        # for item in filelist:
        #     if item.endswith('.jpg'):
        #         src = os.path.join(os.path.abspath(self.path), item)
        #         dst = os.path.join(os.path.abspath(self.path), 'flower' + str(i) + '.jpg')  ##重新命名
        #         try:
        #             os.rename(src, dst)
        #             print('converting %s to %s ...' % (src, dst))
        #             i = i + 1
        #         except:
        #             continue

if __name__ == '__main__':
    demo = BatchRename()
    demo.rename()