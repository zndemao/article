'''
query_ctiy(self, city): 返回数据库中city的数据
'''
import pymongo


class Locad_Find():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["db_locad_tourism"]
    mycol = mydb["locad_tourism_data"]
    '''
    city_name, Scenic_name, Scenic_level, Scenic_Introduction, Scenic_price, Scenic_sales,scenic_image,scenic_image_path
    城市       景点名        景点等级        介绍                  价钱          销量              图片url
    '''

    # mydict = {"city": self.city_name, "scenic": self.scenic_name, "level": self.scenic_level,
    #           "introduction": self.scenic_introduction,
    #           "price": self.scenic_price,
    #           "sales": self.scenic_sales,
    #           "image": self.scenic_image,
    #           "image_path": self.scenic_image_path}


    def find_all(self):
        find = Locad_Find.mycol.find()
        for x in find:
            print(x)

    def query_ctiy(self, city):
        path_ = {'city': 1, 'scenic': 1, 'introduction': 1, 'image': 1, 'image_path': 1}
        find = Locad_Find.mycol.find({'city': city})
        # print(type(find))
        list = []
        # print(list)
        for x in find:
            list.append(x)
            # print(x)
            # print(type(x))

        # print(list)
        # print(len(list))
        return list

    def delete_user(self, name):
        '''
        删除用户
        :param user_phone: 用户的手机号
        :return: 删除了几条数据
        '''
        myquery = {"city": '开封市'}
        one = Locad_Find.mycol.delete_one(myquery)
        # print(type(one))
        # print(one)
        # print(one.deleted_count)
        # for x in one:
        #     print(x)
        print(one.deleted_count)
        return one.deleted_count

    pass


if __name__ == '__main__':
    find = Locad_Find()
    ctiy = find.query_ctiy('开封市市'[0:-1])
    print(ctiy)
    find.find_all()
    find.delete_user('市')

