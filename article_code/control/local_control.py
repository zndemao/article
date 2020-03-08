from MongoDB import locad_jd_find
from base import home_and_locad_data
from utils import judge_file_presence, download_image
import os


class Local_Control():
    city_info_list = []
    display_list = []
    city_info_list_len = 0
    count = 1
    temp_test = 1

    def __init__(self):
        self.data = home_and_locad_data.Data()
        location = self.data.get_location()

        city = locad_jd_find.Locad_Find()
        # 这个程序需要修改。指的是不带 市
        Local_Control.city_info_list = city.query_ctiy(location[0:-1])
        Local_Control.city_info_list_len = len(Local_Control.city_info_list) // 2
        print(Local_Control.city_info_list_len)

    def temp(self):
        Local_Control.temp_test = 0

    # 默认内容
    def init_local(self):
        info_len = len(Local_Control.city_info_list)
        if info_len == 0:
            return
        # print(Loacl_Control.city_info_list[0: 2])
        local_info = Local_Control.city_info_list[0: 2]
        return self.set_local_info(local_info)

        pass

    def set_local_info(self, local_info):
        info_1 = local_info[0]
        info_2 = local_info[1]
        self.data.set_locad_scenic_name_1(info_1.get('scenic'))
        self.data.set_locad_scenic_introduction_1(info_1.get('introduction'))
        if judge_file_presence.judge_file_presence(info_1.get('city'), info_1.get('image_path')):
            path = os.path.abspath(os.path.join(os.getcwd(), '..'))
            file_path = path + '/images/' + info_1.get('city') + '/' + info_1.get('image_path')
            # QPixmap(path + '/images/我的宝贝.jpg')
            self.data.set_locad_scenic_image_1(file_path)
        else:
            self.data.set_locad_scenic_image_1(info_1.get('image_path'))
        self.data.set_locad_scenic_name_2(info_2.get('scenic'))
        self.data.set_locad_scenic_introduction_2(info_2.get('introduction'))
        if judge_file_presence.judge_file_presence(info_2.get('city'), info_2.get('image_path')):
            path = os.path.abspath(os.path.join(os.getcwd(), '..'))
            file_path = path + '/images/' + info_2.get('city') + '/' + info_2.get('image_path')
            # QPixmap(path + '/images/我的宝贝.jpg')
            self.data.set_locad_scenic_image_2(file_path)
        else:
            self.data.set_locad_scenic_image_2(info_2.get('image_path'))
        self.data.set_locad_scenic_info_1(info_1)
        self.data.set_locad_scenic_info_2(info_2)

        return local_info

    # 点下一页
    def next_page_info(self):
        if Local_Control.count == Local_Control.city_info_list_len:
            return []
        Local_Control.count = Local_Control.count + 1
        count_temp = Local_Control.count * 2
        Local_Control.display_list = Local_Control.city_info_list[
                                     count_temp - 2:  count_temp]
        self.set_local_info(Local_Control.display_list)
        # print(Local_Control.display_list)
        # print(count_temp - 2, count_temp)
        return Local_Control.display_list

    # 点击上一页
    def previous_page_info(self):
        # print(Loacl_Control.count)
        if Local_Control.count <= 1:
            # print('return')
            return []
        Local_Control.count = Local_Control.count - 1
        count_temp = Local_Control.count * 2
        Local_Control.display_list = Local_Control.city_info_list[
                                     count_temp - 2:  count_temp]
        # print(Local_Control.display_list)
        # print(count_temp - 2, count_temp)
        self.set_local_info(Local_Control.display_list)

        return Local_Control.display_list

    pass


if __name__ == '__main__':
    control = Local_Control()
    # loacd_control = Loacd_Control()
    # Loacd_Control.city_info_list = [1]
    # l = Loacd_Control()
    # loacd_control.temp()
    # control.temp_test = 3
    # print(loacd_control.temp_test)
    # print(control.temp_test)

    # print(control.city_info_list)
    control.init_local()
    control.next_page_info()
    control.next_page_info()
    control.previous_page_info()
    control.previous_page_info()
    control.previous_page_info()
