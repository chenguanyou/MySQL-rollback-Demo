#coding=utf-8
#0.检测账户A和账户B是否存在，2.检测账户A是否有100元，3.账户A减去100元，4.账户B加上100元，5.完成转账操作
import pymysql


'''银行'''
class Bank_db(object):
    def __init__(self, person):
        self.__conn = pymysql.connect(host="localhost", port=3306, user="root", password="admin123456", db="test", charset="utf8") #创建一个数据库的链接对象
        self.__cursor = self.__conn.cursor() #创建一个游标
        self.person = person

    #创建银行账户开户
    def open_account(self):
        try:
            self.adder_sql = "INSERT INTO test1(id_name, money) VALUES ('%s','%d')"%(self.person.name, self.person.money) #创建开户的SQL执行语句
            self.__cursor.execute(self.adder_sql)
            self.__conn.commit()
            print("%s开户成功!"%self.person.name)
        except Exception as e:
            self.__conn.rollback()
            print("开户出错, 错误编号：%s"%e)
        finally:
            self.__conn.close() #开户成功关闭数据库链接
            self.__cursor.close() #关闭游标链接
            print("关闭开户操作，释放资源")

    #创建账户互相转账
    def transfer_accounts(self):
        self.person_input_name = input("请输入您要转账的账户：")
        try:
            if self.__cursor.execute("SELECT * FROM test1 WHERE id_name='%s'"%self.person_input_name):
                self.person_input_me_name = input("请输入您的账户名：")
                if self.person_input_me_name == self.person_input_name:
                    print("不能给自己转账！")
                else:
                    self.person_input_tean = input("请输入您要转账的金额：")
                    if self.__cursor.execute("SELECT * FROM test1 WHERE id_name='%s' AND money >=%d"%(self.person_input_me_name, int(self.person_input_tean))):
                        he_sql = "UPDATE test1 SET money=money+%d WHERE id_name='%s'"%(int(self.person_input_tean), self.person_input_name)
                        me_sql = "UPDATE test1 SET money=money-%d WHERE id_name='%s'"%(int(self.person_input_tean), self.person_input_me_name)
                        self.__cursor.execute(he_sql)
                        self.__cursor.execute(me_sql)
                        self.__conn.commit()
                        print("转账成功")
                    else:
                        print("输入的金额大于当前账户的金额")
            else:
                print("账户不存在，不能转账")
        except Exception as e:
            self.__conn.rollback()
            print("转账出错, 错误编号：%s" % e)
        finally:
            self.__conn.close()  # 开户成功关闭数据库链接
            self.__cursor.close()  # 关闭游标链接
            print("关闭转账操作，释放资源")


'''人'''
class Person(object):
    #初始化人的属性，name:开户人的姓名，money:开户人的预存款最少100元
    def __init__(self, name, money):
        self.name = name
        self.money = money


if __name__ == "__main__":
    '''创建一个张三&李四'''
    zhangShan = Person("张三", 1000)
    liShi = Person("李四", 1300)
    '''创建银行的业务办理窗口'''
    gongShang1 = Bank_db(zhangShan)
    gongShang2 = Bank_db(liShi)
    '''进行银行开户操作'''
    # gongShang1.open_account()
    # print("-"*90)
    # gongShang2.open_account()
    '''转账操作'''
    gongShang1.transfer_accounts()