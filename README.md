# spine-tools
1、批量.skel转换至.json; 2、批量降版本

自用

1.将spine破解版解压，并按里面的安装说明进行操作
2.将spine.exe的路径加入环境变量，用于指令操作
3.再spine里面导出保存配置，将改配置路径修改至spine_skel2json.py里面的 exportcfg_path =
4.spine_skel2json.py 修改需要源目录，和输出的目录，开始将skel转成json
    我这边的源目录格式是  srcpath/spineName/spineName.skel ,按需修改
5.如果需要降版本，再运行一下spine_downbatch.py,修改好上一个输出的目录至dstpath
如果失败了，尝试用python3.x版本运行
