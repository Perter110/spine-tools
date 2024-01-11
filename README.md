# spine-tools
1、批量.skel转换至.json; 2、批量降版本

自用

1.安装spine</br>
2.将spine.exe的路径加入环境变量，用于指令操作</br>
3.再spine里面导出保存配置，将改配置路径修改至spine_skel2json.py里面的 exportcfg_path =</br>
4.spine_skel2json.py 修改需要源目录，和输出的目录，开始将skel转成json</br>
  我这边的源目录格式是  srcpath/spineName/spineName.skel ,按需修改</br>
5.如果需要降版本，再运行一下spine_downbatch.py,修改好上一个输出的目录至dstpath</br>
</br>
如果失败了，尝试用python3.x版本运行</br>
