import os

directory_path = './bookdata/'  # 當前目錄，您可以修改這裡指定其他目錄
source_path = './source_data/'
key_word_arr = []
target_file = []

def read_list():
    with open('newbook.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        word_arr = content.split()
        for word in word_arr:
            key_word_arr.append(word)
        return


def search_book():
    print(key_word_arr)
    for filename in os.listdir(directory_path):
        filepath = os.path.join(directory_path, filename)
        # 檢查是否為文件
        if os.path.isfile(filepath):
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
                splited_arr = content.split('\n')
                if splited_arr[2][5:] in key_word_arr:
                    print(f"=== {filename} ===")
                    print(splited_arr[2][5:])
                    target_file.append(filename)
                    done_file = filename + ".done"
                    target_file.append(done_file)
    return

def rmfile():
    for filename in os.listdir(source_path):
        filepath = os.path.join(source_path, filename)
        if filename not in target_file:
            os.remove(filepath)
    return

if __name__ == "__main__":
    read_list()
    search_book()
    rmfile()
    print("end")
