from utils import ip_get_location
import os


# from control import local_control


class Data(object):
    # 位置
    location = ip_get_location.get_location()
    # 主页
    name = '测试景点名称'
    image = os.path.abspath(os.path.join(os.getcwd(), '..')) + '/images/xjj.jpg'
    introduction = '测试内容，测试内容，测试内容，测试内容，测试内容，测试内容' \
                   '，测试内容，测试内容，测试内容，测试内容，测试内容，测试内容，' \
                   '测试内容，测试内容，测试内容，测试内容，测试内容，测试内容，测试内容，测试内容'
    # 本地
    # local_ = local_control.Loacl_Control()
    # local_info = local_.init_local()
    # info_1 = local_info[0]
    # info_2 = local_info[1]
    # print(info_1)
    # logging.info(info_2)

    locad_scenic_image_1 = ''
    locad_scenic_image_2 = ''
    locad_scenic_image_3 = ''
    locad_scenic_name_1 = ''
    locad_scenic_name_2 = ''
    locad_scenic_name_3 = ''
    locad_scenic_introduction_1 = ''
    locad_scenic_introduction_2 = ''
    locad_scenic_introduction_3 = ''

    # 推荐

    # 关于

    # print('data')

    def get_location(self):
        return Data.location

    def set_location(self):
        Data.location = ip_get_location.get_location()

    def get_name(self):
        return Data.name

    def set_name(self, name):
        Data.name = name

    def get_image(self):
        return Data.image

    def set_image(self, image):
        Data.image = image

    def get_introduction(self):
        return Data.introduction

    def set_introduction(self, introduction):
        Data.introduction = introduction

    def get_locad_scenic_image_1(self):
        return Data.locad_scenic_image_1

    def set_locad_scenic_image_1(self, path):
        Data.locad_scenic_image_1 = path
        pass

    def get_locad_scenic_image_2(self):
        return Data.locad_scenic_image_2

    def set_locad_scenic_image_2(self, path):
        Data.locad_scenic_image_2 = path
        pass

    def get_locad_scenic_image_3(self):
        return Data.locad_scenic_image_3

    def set_locad_scenic_image_3(self):
        pass

    def get_locad_scenic_name_1(self):
        return Data.locad_scenic_name_1

    def set_locad_scenic_name_1(self, name):
        Data.locad_scenic_name_1 = name
        pass

    def get_locad_scenic_name_2(self):
        return Data.locad_scenic_name_2

    def set_locad_scenic_name_2(self, name):
        Data.locad_scenic_name_2 = name
        pass

    def get_locad_scenic_name_3(self):
        return Data.locad_scenic_name_3

    def set_locad_scenic_name_3(self):
        pass

    def get_locad_scenic_introduction_1(self):
        return Data.locad_scenic_introduction_1

    def set_locad_scenic_introduction_1(self, introduction):
        Data.locad_scenic_introduction_1 = introduction
        pass

    def get_locad_scenic_introduction_2(self):
        return Data.locad_scenic_introduction_2

    def set_locad_scenic_introduction_2(self, introduction):
        Data.locad_scenic_introduction_2 = introduction
        pass

    def get_locad_scenic_introduction_3(self):
        return Data.locad_scenic_introduction_3

    def set_locad_scenic_introduction_3(self):
        pass

    pass


data = Data()
# print("state:" + data.get_location())
# print(data.get_name())
# print(data.get_image())
# print(data.get_introduction())
