import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

# 创建数据库，名字runoobdb
mydb = myclient["test"]
print(mydb)

# 判断数据库是否已存在
dblist = myclient.list_database_names()
# dblist = myclient.list_database_names()
print(dblist)
if "test" in dblist:
    print("数据库已存在！")
else:
    # mydb = myclient["runoobdb"]
    print("创建数据库")



mycol=mydb['user']
print(mycol)
collist = mydb.list_collection_names()
print(collist)
# collist = mydb.collection_names()
if "user" in collist:   # 判断 user 集合是否存在
  print("集合已存在！")