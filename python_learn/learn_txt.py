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
                ".": "代表任何单一字符",
                "*": "代表任意一个它之前的字符, .*代表任意多个字符(包括0)",
                "search()": "寻找首次匹配"
    }
})


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






