#-*- encoding:UTF-8 -*-
import os, shutil


# 获取文件夹下所有文件夹路径，包含子文件夹，以列表返回
def get_folder_path(path):
    path_list = []
    for dirpath, dirnames, filenames in os.walk(path):
        path_list.append(dirpath)
    return path_list[1:]


# 获取文件夹下所有文件夹名（不含路径），包含子文件夹，以列表返回
def get_folder_name(path):
    path_name_list = []
    for dirpath, dirnames, filenames in os.walk(path):
        for dirname in dirnames:
            path_name_list.append(dirname)
    return path_name_list


# 获取文件夹下所有文件路径，包含子文件夹下所有文件，以列表返回
def get_file_path(path):
    file_path_list = []
    for dirpath, dirnames, filenames in os.walk(path):
        for name in filenames:
            file_path_list.append(os.path.join(dirpath,name))
    return file_path_list


# 获取文件夹下所有文件名（不含路径），包含子文件夹下所有文件，以列表返回
def get_file_name(path):
    file_name_list = []
    for dirpath, dirnames, filenames in os.walk(path):
        for name in filenames:
            file_name_list.append(name)
    return file_name_list


# 获取当前路径下文件和文件夹的数量，不包含子文件夹下文件
def get_file_amount(path):
    count = 0
    for fn in os.listdir(path):  # fn 表示的是文件名
        count = count + 1
    return count


# 查找以name为开头的文件，以列表形式返回带路径的文件名
def find_startswith_file_path(path, name):
    new_file_list = []
    file_list = get_file_name(path)
    for file in file_list:
        if file.startswith(name):
            new_file_list.append(os.path.join(path,file))
        else:
            continue
    return new_file_list


# 查找以name为开头的文件，以列表形式返回文件名（不包含路径）
def find_startswith_file_name(path, name):
    new_file_list = []
    file_list = get_file_name(path)
    for file in file_list:
        if file.startswith(name):
            new_file_list.append(file)
        else:
            continue
    return new_file_list


# 查找以name为结尾的文件，以列表形式返回带路径的文件名
def find_endswith_file_path(path, name):
    new_file_list = []
    file_list = get_file_name(path)
    for file in file_list:
        if file.endswith(name):
            new_file_list.append(os.path.join(path, file))
        else:
            continue
    return new_file_list


# 查找以name为结尾的文件，以列表形式返回文件名（不包含路径）
def find_endswith_file_name(path, name):
    new_file_list = []
    file_list = get_file_name(path)
    for file in file_list:
        if file.endswith(name):
            new_file_list.append(file)
        else:
            continue
    return new_file_list


# 查找包含name的文件，以列表形式返回带路径的文件名
def find_in_file_path(path, name):
    new_file_list = []
    file_list = get_file_name(path)
    for file in file_list:
        if name in file:
            new_file_list.append(os.path.join(path, file))
        else:
            continue
    return new_file_list


# 查找包含name的文件，以列表形式返回文件名（不包含路径）
def find_in_file_name(path, name):
    new_file_list = []
    file_list = get_file_name(path)
    for file in file_list:
        if name in file:
            new_file_list.append(file)
        else:
            continue
    return new_file_list

'''
# -----------复制-----------

# 复制带path的文件到新的path
shutil.copyfile(old_path, new_path)


# -----------跨平台----------

# 可以取代操作系统特定的路径分隔符。windows下为 “\\”
os.sep

# 字符串指示你正在使用的平台。比如对于Windows，它是'nt'，而对于Linux/Unix用户，它是'posix'。
os.name

# 字符串给出当前平台使用的行终止符。例如，Windows使用'\r\n'，Linux使用'\n'而Mac使用'\r'。
os.linesep


# ------------路径-------------

# 函数得到当前工作目录，即当前Python脚本工作的目录路径。
os.getcwd()

# 改变工作目录到dirname
os.chdir(dirname)

# 返回当前目录（'.')
os.curdir

# 连接目录与文件名或目录;使用“\”连接
os.path.join(path,name)

# 返回文件路径
os.path.dirname(path)

# 判断路径是否为一个文件
os.path.isfile()

# 判断路径是否为一个目录
os.path.isdir()

# 函数用来检验给出的路径是否真地存在
os.path.existe()

# 获得绝对路径
os.path.abspath(name)

# 规范path字符串形式
os.path.normpath(path)

# 将path分割成目录和文件名二元组返回。
os.path.split(path)


# -----------获取文件属性--------

# 遍历文件夹
# dirnames：目录下的所有文件夹带路径
# filenames：目录下的所有文件
# dirpath：要列出指定目录的路径
for dirpath,dirnames,filenames in os.walk(path):

# 返回指定目录下的所有文件和目录名
os.listdir(path)

# 返回文件名
os.path.basename(path)

# 获得文件大小，如果name是目录返回0L
os.path.getsize(name)

# 分离文件名与扩展名
os.path.splitext()


# ------------删除------------

# 函数用来删除一个文件
os.remove(path)


# ------------shell----------

# 函数用来运行shell命令。
os.system(command)

'''


