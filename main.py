import os
import shutil


def get_file_size(file_path):
    fsize = os.path.getsize(file_path)
    return fsize


def cp_file(path, file):
    file_name = os.path.join(path, file)
    shutil.copyfile(file, file_name)
    return file_name


if __name__ == '__main__':
    path = os.getcwd()
    file_dir = os.path.join(path,'test_file1')
    if not os.path.isdir(file_dir):
        os.mkdir(os.path.join(path,'test_file1'))
    file = './main.py'
    cp_file(file_dir, './main.py')
    print("file_size:",get_file_size(file))
    write_file = os.path.join(file_dir, 'reversed_file.py')
    with open(file,'r') as f:
        content = f.read()
        reversed_content = []
        with open(write_file , 'a') as w:
            for i in range(0, len(content)):
                w.write(content[len(content)-1-i])
    file_list = os.listdir('./')
    file_count = 0
    file_size_count = 0
    for i in file_list:
        if os.path.isdir(i):
            continue
        else:
            file_count += 1
            size = get_file_size(cp_file(file_dir, i))
            file_size_count += size
            print(i, size)
    print("total files :", file_count)
    print("total size  :", file_size_count)
