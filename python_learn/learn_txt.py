print({
    "str": {
                "replace()": "替换",
                "split()": "分割",
                "join()": "合并",
                "startswith()": "字符串开头",
                "endswitch()": "字符串结尾",
                "find()": "字符串第一次出现的位置",
                "rfind()": "字符串最后一次出现的位置",
                "count()": "统计字符串出现的次数",
                "isalnum()": "统计字符串内容是否都是字母或数字",
                "strip()": "删除字符串开头与结尾的数据",
                "capitalize()": "字符串首字母大写",
                "title()": "所有单词开头字母大写",
                "upper()": "所有字母大写",
                "lower()": "所有字母小写",
                "swapcase()": "所有字母大小写转换",
                "center()": "字符位居中",
                "ljust()": "左对齐",
                "rjust()": "右对齐",
                "string.printable": "预定义100个可打印的ASCII字符",
    },
    "list": {
                "append()": "添加元素至尾部",
                "extend()": "列表合并",
                "insert()": "指定位置插入元素",
                "del": "删除指定位置的元素",
                "remove()": "删除指定值的元素",
                "pop()": "获取并删除指定位置的元素",
                "index()": "查询具有特定值的元素位置",
                "count()": "记录特定值出现的次数",
                "join()": "可转换为字符串",
                "sort(), '改变原列表'/sorted()'不改变原列表'": "重新排列元素",    
                "copy函数,list()转换函数,列表分片[:]": "会获取新的对象与值",
                "=": "只是引用,改变原数据会影响新数据",
                "reverse()": "列表反转",
    },
    "tuple": {
                "PASS": "pass",
    },
    "dict": {
                "dict()": "可对包含双值子序列的序列使用dict()",
                "update()": "合并字典,相同的键会导致覆盖键的值",
                "del": "删除具有指定键的元素",
                "clear()": "删除所有元素",
                "get()": "获取值,不存在返回None, 可指定返回的可选值",
                "keys()": "获取所有的键",
                "values()": "获取所有的值",
                "items()": "获取所有的键值对. 返回的是元组",
                "copy()": "复制",
                "setdefault()": "当键不存在时会在字典中添加一项",
                "defaultdict()": "返回赋给缺失键的值",
                "Counter": "降序返回所有元素,若传入参数会返回该数字前的元素",
                "OrderedDict()": "创建一个有序的字典,{[('Moe', 'A wise guy, huh?'),('Larry', 'Ow!'),]}",
                "deque()": "双端队列: 栈+队列, popleft()去掉最左边的项, pop()去掉最右边的项",
                "deque()用处": "可用于快速判断回文的程序,只需把字符串反转和原字符串进行比较",
    },
    "set": {
                "&": "交集, 无则返回空集, 即False",
                "|/union()": "并集, ",
                "-/differenct()": "差集",
                "^/symmetric_differenct()": "获得两个集合的异或集(仅在两个集合中出现一次)",
                "<=/issubset(b)": "子集",
                "<": "真子集",
                ">=/issuperset()": "与子集相反",
                ">": "与真子集相反",
    },
    "locals()": "返回局部命名空间内容的字典",
    "globals()": "返回全局命名空间内容的字典",
    "itertools": {
                "itertools.chain()": "通过参数迭代对象",
                "cycle()": "参数间循环的无限迭代器",
                "accumulate()": "计算累积的值,默认为累加的和, 接收第二个参数方法",
    },
    "encode()": "将字符串转化为一系列字节的过程",
    "decode()": "字节串转换为Unicode字符串",
    "re": {
                "match()": "从源字符串的开头开始匹配",
                ".": "代表任何单一字符,除\n外",
                "*": "代表任意一个它之前的字符, .*代表任意多个字符(包括0)",
                "search()": "寻找首次匹配",
                "findall()": "寻找所有匹配",
                "?": "字符可选(0个或1个)",
                "split()": "按匹配切分",
                "sub()": "替换匹配",
                "\d": "一个数字字符",
                "\D": "一个非数字字符",
                "\w": "一个字符或数字字符",
                "\W": "一个非字母非数字字符",
                "\s": "空白字符",
                "\S": "非空白字符",
                "\b": "单词边界",
                "\B": "非单词边界",
                "abc": "文本值abd",
                "(expr)": "expr",
                "^": "源字符串的开头",
                "$": "源字符串的结尾",
                "prev?": "0个或1个prev",
                "prev*": "0个或多个prev, 尽可能多地匹配",
                "prev*?": "0个或多个prev, 尽可能少地匹配",
                "prev+": "1个或多个prev, 尽可能地多匹配",
                "prev+?": "1个或多个prev，尽可能少地匹配",
                "prev{m}": "m个连续的prev",
                "prev{m, n}": "m到n个连续的prev，尽可能多地匹配",
                "prev{m, n}?": "m到n个连续的prev, 尽可能少地匹配",
                "[abc]": "a或b或c(和a|b|c)一样",
                "[^abc]": "非a或b或c",
                "prev(?=next)": "如果后面为next, 返回prev",
                "prev(?!next)": "如果后面非next, 返回prev",
                "(?<=prev)next": "如果前面非prev, 返回next",
                "(?<!prev)next": "如果前面非prev，返回next",
                "groups()": "使用match()或search()时,匹配结果返回元祖",
    },
    "文件输入/输出": {
                "fileobj = open(filename, mode)": {
                    "fileobj": "open返回的文件对象",
                    "filename": "是该文件的字符串名",
                    "mode": {
                        "r": "表示读模式",
                        "w": "表示写模式,如果文件不存在则新建,存在则重写新内容",
                        "x": "表示在文件不存在的情况下新创建并写入文件",
                        "a": "表示如果文件存在,在文件末尾追加写内容",
                        "t(或者省略)": "代表文本类型",
                        "b": "代表二进制文件",
                    }
                    "sep分隔符": "默认是一个空格' '",
                    "end结束符": "默认是一个换行符'\n'",
                    "read()": "一次返回,可通过chunk设置最大的读入字符数",
                    "readline()": "每次读入文件的一行",
                    "readlines()": "每次读取一行,并返回单行字符串的列表",
                    "tell()": "返回距离文件开始处的字节偏移量",
                    "seek(offset, origin)允许跳转到文件其他字节偏移量的位置"{
                        "origin=0": "默认为0,从开头偏移offset个字节",
                        "origin=1": "从当前位置处偏移offset个字节",
                        "origin=2": "距离最后结尾处偏移offset个字节",
                    }
                },
    },
    "SQL": {
        "CREATE DATABASE dbname": "创建数据库",
        "USE dbname": "选择当前数据库",
        "DROP DATABASE dbname": "删除数据库以及表单",
        "CREATE TABLE tbname": "创建表单",
        "DEOP TABLE tbname": "删除表单",
        "TRUNCATE TABLE tbname": "删除表单中所有的行",
        "Create": "使用INSERT语句创建",
        "Read": "使用SELECT语句选择",
        "Update": "使用UPDATE语句更新",
        "Delete": "使用DELETE语句删除", 
        "INSERT INTO tbname VALUES(...)": "增加行",
        "SELECT * FROM tbname": "选择全部行和全部列",
        "SELECT cols FORM tbname": "选择全部行和部分列",
        "SELECT cols FORM tbname WHERE condition": "选择部分行部分列",
        "UPDATE tbname SET col=value WHERE condition": "修改一列的部分行",
        "DELETE FROM tbname WHERE condition": "删除部分行",
        "connect()": "连接数据库,包含参数用户名,密码,服务器地址",
        "cursor": "创建一个cursor对象来管理查询",
        "execute()/executemany()": "对数据库执行一个或多个SQL命令",
        "fetchone()/fetchmany()/fetchall()": "得到execute之后的结果",
    },
    "SQLite": {
        "critter": "可变长度的字符串, 作为主键",
        "count": "某动物的总数的整数值",
        "damages": "人和动物的互动中损失的美元数目",
    },
    "SQLAlchemy": {
        "dialect+driver://user:password@host:port/dbname":{
            "dialect": "数据库类型",
            "driver": "使用该数据库的特定驱动程序",
            "user/password": "数据库认证字符串",
            "host/port": "数据库服务器位置与端口号",
            "dbname": "初始连接到服务器中的数据库",
            },
    },
    "NoSQL":{
        "dbm family": {
            "r": "读",
            "w": "写",
            "c": "表示读和写",
            "del": "删除值",
            "keys()": "遍历键(类似于遍历字典)",
        },
        "redis": {
            "set": "赋值",
            "get": "通过key获取值",
            "setnx()": "当键不存在时设定值",
            "getset()": "返回旧的值,并赋新的值",
            "getrange()": "获取值(get.key)的偏移量",
            "setrange()": "替换值(get.key)的偏移量, setrange('key', 0, 'newvalue')",
            "mset()": "设置多个键值对",
            "delete()": "删掉一个键",
            "incr()/incrbyfloat()": "数值计算,增加值, 可使用负数",
            "decr()": "数值计算, 减少值",
            "list/仅能包含字符串": {
                "lpush()": "在开始处插入",
                "linsert()": {
                    "linsert('listname', 'before', 'oldvalue', 'newvalue')": "在一个值(oldvalue)的前面插入新值(newvalue)",
                    "linsert('listname', 'after', 'oldvalue', 'newvalue')": "在一个值(oldvalue)的后面插入新值(newvalue)",
                    },
            "lset()": "函数在偏移量出插入(列表必须已经存在)",
            "rpush()": "结尾处插入",
            "lindex()": "函数取到给定偏移量处的值",
            "lrange()": "函数取到给定偏移量范围(0, -1)的值",
            "ltrim()": "函数仅保留列表中给定范围的值",
            },
            "哈希表, 只能有一层结构,不能进行嵌套": {
                "hset()/conn.hmset('song', 'do': 'a deer')": "创建哈希表song, 并设置字段do的值, 多值使用字典包裹".
                "hget()/conn.hget('song', 'do')": "使用函数hget()获取字段do的值",
                "hmget()": "获取多个字段的值",
                "hkeys()": "获取所有字段的键",
                "hvals()/conn.hvals('song')": "取到song所有字段的值",
                "hlen()/conn.hlen('song')": "返回song字段的总数",
                "hgetall()/conn.hgetall()": "取到所有字段的键和值, 字典结构",
                "hsetnx()": "对字段中不存在的键赋值"
            },
            "集合": {
                "sadd()/conn.sadd('zoo', 'duck', 'goat', 'turkey')": "zoo集合添加值",
                "scard()/conn.scard('zoo')": "返回zoo集合中的数目(长度)",
                "smembers()/conn.smembers('zoo')": "返回zoo集合中的所有值",
                "srem()/conn.srem('zoo', 'turkey')": "从zoo集合中删除一个值turkey",
                "sinter()/conn.sinter('zoo', 'better_zoo')": "返回集合zoo和better_zoo的交集",
                "sinterstore()/sinterstore('fowl_zoo', 'zoo', 'better_zoo')": "获得集合zoo和better_zoo的交集,并存储到新集合fowl_zoo",
                "sunion()/sunion('zoo', 'better_zoo')": "返回集合的并集",
                "sunionstore()": "存储并集结果到新集合(), 同交集使用方法相同",
                "sdiff()": "返回集合的差集",
                "sdiffstore()": "存储集合的差集到新集合()",
            },
            "位图/bit()": "省空间且快速处理超大集合数字的方式",

        }
    },
    
})

# bit
def bitset()
    days = ['2013-02-25', '2013-02-26', '2013-02-27']
    big_spender = 1089
    tire_kicker = 40459
    late_joiner = 550212
    # 每天是一个单独的键, 对应用户的ID设置位,
    # 例如days[0]有来自big_spender(ID 1089)与tire_kicter(ID 40459)
    # 第一天
    conn.setbit(days[0], big_spender, 1)
    conn.setbit(days[0], tire_kicker, 1)
    # 第二天
    conn.setbit(days[1], big_spender, 1)
    # 第三天
    conn.setbit(days[2], big_spender, 1)
    conn.setbit(days[2], bit_spender, 1)
    # 统计三天的日访客数
    for day in days:
        conn.bitcount(day)
    # 212    



# dbm family
def dbmfamily_learn():
    import dbm
    db = dbm.open("definitions", "c")
    db["mustard"] = "yellow"
    db["pesto"] = "green"


# SQLAlchemy_ORM
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
conn = sa.create_engine("sqlite:///zoo.db")
Base = declarative_base()
class Zoo(Base):
    __tablename__ == "zoo"
    critter = sa.Column("critter", sa.String, primary_key=True)
    count = sa.Column("count", sa.Integer)
    damage = sa.Column("damages", sa.Float)

    def __init__(self, critter, count, damages):
        self.critter = critter
        self.count = count
        self.damages = damages

    def __repr__(self):
        return "<Zoo({}, {}, {})>".format(self.critter, self.count, self.damages

Base.metadata.create_all(conn)
first = Zoo('duck', 10, 0.0)
second = Zoo('bear', 2, 1000.0)
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=conn)
session = Session()
session.add(first)
session.commit()


# SQLAlchemy
def SQLAlchemy_learn2()
    import sqlalchemy as sa
    conn = sa.create_engine("sqlite://")
    meta = sa.MetaData()
    zoo = sa.Table("zoo", meta,
        sa.Column("critter", sa.String, primary_key = True),
        sa.Column("count", sa.Integer),
        sa.Column("damages", sa.Float)
    )
    meta.create_all(conn)
    conn.execute(zoo.insert(('bear', 2, 1000.0)))
    conn.execute(zoo.insert(('weasel', 1, 2000.0)))
    result = conn.execute(zoo.select())
    rows = result.fetchall()
    print(rows)
    # [('bear', 2, 1000.0), ('weasel', 1, 2000.0), ('duck', 10, 0.0)]


# SQLAlchemy
def SQLAlchemy_learn():
    import sqlalchemy as sa
    conn = sa.create_engine("sqlite://")
    # conn.execute()会返回一个SQLAlchemy的对象ResultProxy
    conn.execute("""CREATE TABLE zoo
    (critter VARCHAR(20) PRIMARY KEY,
    count INT,
    damages FLOAT)""")
    ins = 'INSERT INTO zoo (critter, count, damages) VALUES (?, ?, ?)'
    conn.execute(ins, 'duck', 10, 0.0)
    conn.execute(ins, 'bear', 2, 1000.0)
    # rows不是一个列表,不可直接输出,可像列表迭代(for in)
    rows = conn.execute("SELECT * FROM zoo")


# SQLite
def SQLite_learn():
    import sqlite3
    # 创建数据库enterprise.db
    conn = sqlite3.connect("enterprise.db")
    # 创建操作对象
    curs = conn.cursor()
    curs.execute("""CREATE TABLE zoo
    (critter, VARCHAR(20) PRIMARY KEY,
     count INT,
     damages FLOAT)
    """)
    # 使用 placeholder 可以更安全, 使用三个问号表示要插入三个值
    ins = "INSERT INTO zoo(critter, count, damages) VALUES(?, ?, ?)"
    curs.execute(ins, ("weasel", 1, 2000.0))




# 合并及运算符
def set_test():
    drinks = { 
        'martini': {'vodka', 'vermouth'}, 
        'black russian': {'vodka', 'kahlua'}, 
        'white russian': {'cream', 'kahlua', 'vodka'}, 
        'manhattan': {'rye', 'vermouth', 'bitters'}, 
        'screwdriver': {'orange juice', 'vodka'} 
    }
    for name, contents in drinks.items():
        if contents & {"vermouth", "orange juice"}:
            print(name)


# 闭包: 一个被动态创建的可以记录外部变量的函数
# 调用会记录被knights2函数创建时的外部变量saying
def knights2(saying):
    # inner2()函数可以得到saying参数的值并且记录下来,
    def inner2():
        return "We are the %s"%saying
    # return inner2这行返回的是inner2函数的复制(没有直接调用)
    return inner2



class Duck():
    def __init__(self, input_name):
        self.__name = input_name

    @property
    def name(self):
        print("inside the getter")
        return self.__name

    @name.setter
    def name(self, input_name):
        print("self, ")
        self.__name = input_name


# 命名元组
# 可使用_replact来替换命名元组
class Duck2():
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail

    def about(self):
        print(bill, tail)


# Unicode字符串转换
def unicode_test(value):
    import unicodedata
    # name(): 接收一个Unicode字符,返回大写形式的名称
    name = unicodedata.name(value)
    # lookup(): 接受不区分大小写的标准名称,返回一个Unicode字符
    value2 = unicodedata.lookup(name)
    print("value='%s', name='%s', value2='%s'"%(value, name, value2))


if __name__ == "__main__":
    # set_test()
    parts = {'bill': 'wide orange', 'tail': 'long'}
    duck2 = Duck2(**parts)
    print(duck2)
    print(duck2.tail)






