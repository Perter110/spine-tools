# coding:utf-8
import easygui as g
import os, sys


if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = g.fileopenbox('open file', default='F:/worktool/spinedown2.0/*.json', filetypes=['*.json'], multiple=True)
    if file_path is None:
        g.msgbox("您没有选择文件")
        sys.exit()
    for fp in file_path:
        isJson = str(fp)[-4:]
        if isJson != "json":
            g.msgbox("请选择正确的json文件")
            sys.exit()

        cmd = "java -cp " + current_dir + "\skeletonViewer.jar com.esotericsoftware.spine.JsonRollback " + str(fp) + " 3.7 " + str(fp)
        os.system(cmd)
    g.msgbox("Change Success!")


