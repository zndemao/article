import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["db_tourism"]
mycol = mydb["tourism_data"]

# mydict = {"name": "cat2", "age": 17}
mydict = {"city": "test_city", "scenic": "test_scenic", "level": "test_level", "introduction": "text_introduction",
          "price": 99,
          "sales": 99}

# x = mycol.insert_one(mydict)
# print(x)
# print(x)

x = mycol.find()
for x in mycol.find():
    print(x)