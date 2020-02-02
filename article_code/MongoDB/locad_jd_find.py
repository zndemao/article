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

    def query_ctiy(self, city):
        find = Locad_Find.mycol.find({'city': city},
                                     {'city': 1, 'scenic': 1, 'introduction': 1, 'image': 1, 'image_path': 1})
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

    pass


if __name__ == '__main__':
    find = Locad_Find()
    ctiy = find.query_ctiy('开封市'[0:-1])
    print(ctiy)
