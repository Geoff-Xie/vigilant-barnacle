# author:GeoffXie
# 开发时间 2022/9/18 15:09
import csv
import os
import shutil
import time
import zipfile


def crzip(): #创建压缩文件
    path = 'D:\\xyylssj\\'
    c = os.listdir(path)
    zipna=input('请输入文件名:')
    newZip = zipfile.ZipFile('D:\\'+zipna+'.zip', 'w')
    for i in c:
        newZip.write(path + i, compress_type=zipfile.ZIP_DEFLATED)
    newZip.close()


def opzip(filelist):
    zipp = zipfile.ZipFile(zppath)
    for i in filelist:
        try:
            zipp.extract(i, 'D:\\xyylssj')
        except BaseException:
            pass
    zipp.close()


def getdata():
    csvfiles = open(csvpath, encoding='UTF-8')
    a = csv.reader(csvfiles)
    f = list(a)
    f = f[1:]
    csvfiles.close()
    # print(f)
    filelist = []
    m = 5
    # m=input('请输入文件名起始所在列号:')
    filelist = [row[int(m) - 1] for row in f]
    # print(len(filelist))
    print(filelist)

    m = 3
    # m = input('请输入学号所在列号')
    stid = [row[int(m) - 1] for row in f]
    # print('学号')
    # print(stid)

    m = 4
    # m=input('请输入姓名所在列号')
    stna = [row[int(m) - 1] for row in f]
    # print(stna)

    i = len(filelist)
    for n in range(0, i):
        filelist[n] = filelist[n].replace('/', "-")
        filelist[n] = filelist[n].replace(':', "-")
        filelist[n] = filelist[n].replace('*', "_")
        filelist[n] = filelist[n].replace('\n', "_")
    return stid, stna, filelist


def rnname(filelist):
    path = 'D:\\xyylssj'
    n = 0
    for i in filelist:
        try:
            # print(filelist[n])
            oldname = path + os.sep + filelist[n]  # os.sep添加系统分隔符
            newname = stid[n] + stna[n]
            # print(newname)
            filetype = os.path.splitext(oldname)[1]  # 文件类型
            # print(filetype)
            # nwname=path+os.sep+str(n)+filetype
            # nwname=path+os.sep+str(n)+filetype
            nwname = path + os.sep + newname+ filetype
            os.rename(oldname, nwname)  # 用os模块中的rename方法对文件改名
            print(oldname, '======>', nwname)

        except BaseException:
            pass
        n += 1


timms = time.time()
# zppath=input('请输入压缩文件地址')
zppath = 'D:\附件下载_文学导论论文（收集结果）.zip' #压缩文件地址
csvpath = 'D:\文学导论论文（收集结果）-文学导论论文.csv' #导出的CSV文件地址
stid, stna, filelist = getdata()
opzip(filelist) #打开压缩文件
rnname(filelist) #修改文件名
timmb = time.time()
crzip()
shutil.rmtree('D:\\xyylssj')
print(timmb - timms)
a=input('是否删除文件，是请输入1:')
if a=='1':
    os.remove(zppath)
    os.remove(csvpath)
