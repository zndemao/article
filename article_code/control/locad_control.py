from MongoDB import locad_jd_find
class loacd_control():
    # 默认内容
    def init_locad(self):
        ctiy = locad_jd_find.Locad_Find()

        query_ctiy = ctiy.query_ctiy('开封市'[0:-1])
        print(query_ctiy)
        pass

    # 点下一页
    # 点击上一页
    pass
if __name__ == '__main__':
    control = loacd_control()
    control.init_locad()
