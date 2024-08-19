# xtools

## 导入模块

```py
import utils
```

## 用法举例

### sas2txt

根据正则表达式截取 SAS 程序文件，并在参数 `sas_dir_path` 的 submit 子目录下保存为 txt 文件

参数：

- `sas_dir_path`: `string`, SAS 程序文件所在的目录路径
- `line_pattern_s`: `string`, 正则表达式，用于匹配开始截取的行模式，如果为 `None`，则从文件开始截取
- `line_pattern_e`: `string`, 正则表达式，用于匹配结束截取的行模式，如果为 `None`，则截取到文件末尾

例子：

```py
utils.sas2txt(sas_dir_path = r"~\04 统计分析\04 ADS程序\01 主程序",
              line_pattern_s = r"\/\*Rest system automatic macro variable\*\/",
              line_pattern_e = r"\/\*输出日志\*\/")

utils.sas2txt(sas_dir_path = r"~\04 统计分析\05 TFL程序\01 主程序",
              line_pattern_s = r"\/\*=+分析程序开始=+\*\/",
              line_pattern_e = r"\/\*=+分析程序结束=+\*\/")

utils.sas2txt(sas_dir_path = r"~\04 统计分析\09 Macro")
```

### copy_dir_struct

复制目录结构（不复制文件）

参数：

- `old_dir_path`: `string`, 原目录路径
- `new_dir_path`: `string`, 新目录路径

例子：

```py
utils.copy_dir_struct(old_dir_path = r"~\原目录", new_dir_path = r"~\新目录")
```
