import os

# 默认配置
root_dir = 'NBD'  # 需要统计md的根目录名称, 默认为我个人的笔记目录 NBD (NoteBookDirectory)
exclude_dirs = ['assets', 'images']  # 排除的目录名称, 默认为图片目录 assets 和 images
output_file = 'NoteTree.log'  # 输出记录的文件名, 默认为 NoteTree.log
threshold_lines = 3  # 统计的最小行数, 默认为 3
default_encode = 'utf-8'  # 默认编码格式, 默认为 utf-8
file_ext = '.md'  # 统计的文件扩展名, 默认为 .md
surpress_ext = ['.gitkeep', '.log']  # 不统计的文件拓展名


### 主程序 ###
def main():
    print("玄桃K的笔记本字数统计器...开始运行\n\n")
    if not os.path.exists(root_dir):
        print(f"需要的目录 '{root_dir}' 跑丢了.")
        return

    # 生成文档树
    tree = "文档树\n\n" + scan_directory(root_dir, exclude_dirs)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(tree)

    # 统计字数 -> 输出到文件
    log_stats, _, _ = log_statistics(root_dir, exclude_dirs)
    with open(output_file, 'a', encoding='utf-8') as f:
        f.write("\n\n" + "-" * 100 + "\n\n")
        f.write("\n字数统计\n\n")
        f.write(log_stats)

    # 统计字数 -> 输出到控制台
    console_stats, total_chars, total_lines = console_statistics(root_dir, exclude_dirs)
    print(console_stats)
    total_chars_display = f"{total_chars / 1000:.1f}k" if total_chars > 10000 else str(total_chars)
    total_lines_display = f"{total_lines / 1000:.1f}k" if total_lines > 10000 else str(total_lines)
    print(f"{root_dir} 笔记本总计:"
          f" {total_chars_display}字, {total_lines_display}块\n")
    print(f"玄桃K的笔记本字数统计器...运行结束, 详细对象结果见生成的{output_file}文件\n\n"
          "note:由于包含代码块与其他字符, 实际文件字符数预计是统计结果的200%左右.")
    print(" -> 我了解以上内容, 按任意键退出.")
    input()


# 递归扫描目录, 生成树状结构
def scan_directory(directory, ex, level=0):
    tree = ""
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            if item not in ex:
                tree += "\t" * level + f"{item}/\n"
                tree += scan_directory(item_path, ex, level + 1)  # 递归
                tree += "\n\n"
        elif item.endswith(file_ext):
            tree += "\t" * level + f"{item[:item.rfind('.')]}\n"
            tree += "\n"
    return tree


# 递归统计
def log_statistics(directory, ex, level=0):
    stats = ""
    total_chars, total_lines = 0, 0

    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)  # 拼接路径

        # 目录
        if os.path.isdir(item_path):
            if item not in ex:
                sub_stats, sub_chars, sub_lines = log_statistics(item_path, ex, level + 1)
                if sub_lines >= threshold_lines:  # 只统计大于等于阈值行数的文件
                    stats += "\t" * level + f"{item}/ --共计{sub_chars}字, {sub_lines}行\n\n"
                    stats += sub_stats
                total_chars += sub_chars
                total_lines += sub_lines

        # 文件
        elif item.endswith(file_ext):
            chars, lines = count_words(item_path)
            if lines >= threshold_lines:
                stats += "\t" * level + f"{item[:item.rfind('.')]} --共计{chars}字, {lines}行\n\n"
            total_chars += chars
            total_lines += lines
        elif item.endswith(tuple(surpress_ext)):
            continue
        else:
            stats += "\t" * level + f"{item} --未知文件类型\n\n"  # 提示未知文件类型
    return stats, total_chars, total_lines


# 针对文件统计字数
def count_words(file_path):
    with open(file_path, 'r', encoding=default_encode) as f:
        text = f.read()
        lines = text.splitlines()
        return len(text), len(lines)


# 统计根目录字数到控制台
def console_statistics(directory, ex):
    stats = ""
    total_chars, total_lines = 0, 0

    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            if item not in ex:
                sub_stats, sub_chars, sub_lines = log_statistics(item_path, ex, 1)
                if sub_lines >= threshold_lines:
                    stats += f"{item}/  共计{sub_chars}字, {sub_lines}行\n\n"
                total_chars += sub_chars
                total_lines += sub_lines
    return stats, total_chars, total_lines


if __name__ == "__main__":
    main()
