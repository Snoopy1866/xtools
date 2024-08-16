import os
import glob
import re

def sas2txt(sas_dir_path, line_pattern_s=None, line_pattern_e=None):
    """
    将SAS程序文件中的特定内容转换为TXT格式并保存
    
    参数:
    sas_dir_path: str, SAS程序文件所在的目录路径
    line_pattern_s: str, 正则表达式，用于匹配开始截取的行模式，如果为None，则从文件开始截取
    line_pattern_e: str, 正则表达式，用于匹配结束截取的行模式，如果为None，则截取到文件末尾
    """
    txt_dir_path = os.path.join(sas_dir_path, "submit")

    # 创建txt目录
    if not os.path.exists(txt_dir_path):
        os.makedirs(txt_dir_path)

    # 获取sas文件列表
    sas_file_list = glob.glob(os.path.join(sas_dir_path, "*.sas"))

    # 逐个处理sas文件
    for i in range(max(1, len(sas_file_list))):
        sas_file = sas_file_list[i]
        sas_file_name = os.path.basename(sas_file)
        txt_file = os.path.join(txt_dir_path, sas_file_name.replace(".sas", ".txt"))

        flag_s = line_pattern_s is None # 截取开始标志
        flag_e = False # 截取结束标志

        with open(sas_file, "r") as fr:
            with open(txt_file, "w") as fw:
                for fr_line in fr.readlines():
                    if line_pattern_s is not None and re.match(line_pattern_s, fr_line):
                        flag_s = True
                        continue
                    if line_pattern_e is not None and re.match(line_pattern_e, fr_line):
                        flag_e = True
                        break
                    if flag_s and not flag_e:
                        fw.write(fr_line)
