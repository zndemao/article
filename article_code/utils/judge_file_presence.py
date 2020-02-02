import os


def judge_file_presence(city, name):
    path = os.path.abspath(os.path.join(os.getcwd(), '..'))
    file_path = path + '/images/' + city + '/' + name
    exists = os.path.exists(file_path)
    # print(exists)
    return exists
    pass


if __name__ == "__main__":
    judge_file_presence('开封', '清明上河园.jpg')
