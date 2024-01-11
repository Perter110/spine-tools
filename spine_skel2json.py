import os
import shutil

srcpath = './charactor'
dstpath = './charactor_new'

dirlist = os.listdir(srcpath)
exportcfg_path = './export_spine.export.json'

def createDir(dirpath):
    if os.path.exists(dirpath):
        shutil.rmtree(dirpath)
    os.mkdir(dirpath)

for dirname in dirlist:
    workpath = os.path.join(srcpath, dirname)
    if os.path.isdir(workpath):
        spine_proj = workpath + '/%s.spine'%dirname
        if os.path.exists(spine_proj):
            # print(spine_proj)
            saveTopath = dstpath+'/'+dirname
            createDir(saveTopath)

            shutil.copyfile(workpath+ '/%s.atlas'%dirname,saveTopath+ '/%s.atlas'%dirname)
            shutil.copyfile(workpath+ '/%s.png'%dirname,saveTopath+ '/%s.png'%dirname)
            cmd = 'Spine -i "%s" -o "%s" -e "%s"'%(spine_proj, saveTopath, exportcfg_path)
            os.system(cmd)
            pass
        else:
            print("%s.spine文件不存在"%dirname)
