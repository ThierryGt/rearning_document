# 创建一个字典,解决了在一个字典中对一个键进行嵌套赋值时，如果这个键不存在，会触发keyError异常
def collections_defaultdict():
    import collections
    import json
    tree = lambda: collections.defaultdict(tree)
    some_dict = tree()
    some_dict['colours']['favourite'] = "yellow"
    print(json.dumps(some_dict))


# 可用来针对某项数据进行计数
def counter_methods():
    from collections import Counter
    colours = (
        ('Yasoob', 'Yellow'),
        ('Ali', 'Blue'),
        ('Arham', 'Green'),
        ('Ali', 'Black'),
        ('Yasoob', 'Red'),
        ('Ahmed', 'Silver'),)
favs = ounter(name for name, colour in colours)
print(favs)


# deque
def deque_methods():
    from collections import deque
    d = deque()
    # 与列表类似
    # 也可从两端取出数据
    d.popleft()
    d.pop()
    # 扩展数据
    d.extendleft()


# namedtuple
def namedtuple_methods():
    from collections import namedtuple
    Animal = namedtuple('Animal', 'name age type')
    perry = Animal(name="Perry", age=31, type="cat")
    print(perry._asdict())

# enum.Enum
from collections import namedtuple
from enum import Enum
class Species(Enum):
    cat = 1
# 访问
Species(1)
Species['cat']
Species.cat


