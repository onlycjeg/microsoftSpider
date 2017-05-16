#! -*- coding:utf-8 -*-

'''
__author__="nMask"
__Date__="2017年5月15日"
__Blog__="http://thief.one"
__version__="1.0"
__Python__="2.7.11"

rethinkdb数据库操作模块
'''
import rethinkdb as r
import hashlib
import json

class oprethinkdb:
    host=""
    port=28015

    def __init__(self,dbname,tablename):
        self.conn = r.connect(host=oprethinkdb.host,port=oprethinkdb.port)
        self.table = r.db(dbname).table(tablename)

    def Insert(self,document,keyword):
        '''
        需要制定能够标识唯一的参数keyword。
        插入记录到数据库，如果id一样，则更新覆盖原来的记录。
        id：DN即url的hash值
        '''
        try:
            dicthash=hashlib.md5(json.dumps(document[keyword])).hexdigest()
            document["id"]=dicthash
            return self.table.insert(document, conflict="update").run(self.conn)
        except Exception,e:
            print e

    def query(self,filters=""):
        '''
        自定义查询,需要传入查询规则
        '''
        f=self.table.filter(filters).run(self.conn)  ##选择网站名称为空的记录。
        for i in f:
            yield i

    def delete(self,filters=""):
        '''
        自定义删除语句,需要传入查询规则
        '''
        f=self.table.filter(filters).delete().run(self.conn) ##删除记录
        print f


if __name__=="__main__":
    cur=oprethinkdb("","")
    result=cur.query()
    f=open("ms_kb.txt","wb")

    for i in result:
        f.write(json.dumps(i)+"\n")

