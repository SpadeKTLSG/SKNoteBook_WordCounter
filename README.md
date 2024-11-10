# SKNoteBook-WordCounter
个人笔记本字数统计器




## 结构 Construction

main.py - 脚本文件

默认配置:
- root_dir = 'NBD'  # 需要统计md的根目录名称, 默认为我个人的笔记目录 NBD (NoteBookDirectory)
- exclude_dirs = ['assets', 'images']  # 排除的目录名称, 默认为图片目录 assets 和 images
- output_file = 'NoteTree.log'  # 输出记录的文件名, 默认为 NoteTree.log 
- threshold_lines = 3  # 统计的最小行数, 默认为 3 
- default_encode = 'utf-8'  # 默认编码格式, 默认为 utf-8 
- file_ext = '.md'  # 统计的文件扩展名, 默认为 .md 
- surpress_ext = ['.gitkeep', '.log']  # 不统计的文件拓展名



## 使用 Usage

可执行脚本制作攻略

### 安装制作器

PyInstaller

```cmd
pip install pyinstaller
```


### 创建

导航到包含‘ main.py’脚本的目录并运行
这个命令将生成一个可执行文件
“—— onefile”选项确保将所有依赖项绑定到单个可执行文件中(捆绑所有依赖项)


```cmd
pyinstaller —— onefile main.py
```


### 找到对象

PyInstaller 将创建一个“ dist”目录

找到‘ main’可执行文件, 测试其


## 其他 Others
