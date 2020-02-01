import os
import re
import requests


def download_image(url, name, city):
    path = os.path.abspath(os.path.join(os.getcwd(), '..'))
    file_extension = re.search(r'https://imgs.qunarzz.com\S*(.\S{3})', url).group(1)
    os.makedirs(path + '/images/' + city, exist_ok=True)
    file_path = path + '/images/' + city + '/' + name + file_extension
    # print(file_path)

    response = requests.get(url)
    # 获取的文本实际上是图片的二进制文本

    img = response.content
    # 将他拷贝到本地文件 w 写  b 二进制  wb代表写入二进制文本
    with open(file_path, 'wb') as f:
        f.write(img)
    pass


def download_date(url):
    return requests.get(url)


if __name__ == '__main__':
    download_image('https://imgs.qunarzz.com/sight/p0/1701/88/885ec9c1584a572aa3.img.png_280x200_91ebdc7b.png', 'test',
                   't')
    download_image('https://imgs.qunarzz.com/sight/p0/1505/70/70499b1ac3c6449f.water.jpg_280x200_9410f4b5.jpg', '大相国寺',
                   't')
