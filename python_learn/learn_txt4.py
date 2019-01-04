import unittest
import cap
from PIL import Image
from nose.tools import eq_
print({
    "pylint/pyflakes/pep8": "检查代码",
    "unittest": {
        "setUp()": "会在每个测试方法执行之前执行",
        "testDown()": "会在每个测试方法执行之后执行",
    },
    "nose": "任何名称中带test的函数都会被执行, nosetests file.py",
    "vars()": "提取本地变量的值, 包括函数参数",
    "logging": {
        "level": "错误等级",
        "filename": "写入的文件名",
        "format": "改变格式, '%(asctime)s %(levelname)s %(lineno)s %(message)s'",
    },
    "python库": {
        "imghdr": "用于检测图片文件的文件格式",
        "colorsys": "在不同的颜色系统(RGB, YIQ, HSV以及HLS)间进行转换",
        "PIL和Pillow": "python 2D图片处理库",
        "format": "获取文件属性",
        "size": "获取文件大小",
        "show": "屏幕上显示图片, 需先安装ImageMagick",
        "crop": "以水平坐标x与垂直坐标y计量图片, 传入四个参数",
        "save": "存储图片",
    }


})

# PIL Pillow
class PilImage():
    # 打开一个图片文件
    img = Image.open("file.png")
    # 


# unittest
def just_do_it(text):
    return text.capitalize()

def test_one_word():
    text = "duck"
    result = just_do_it(text)
    eq_(result, "Duck")

def test_multiple_words():
    text = "a veritable flock of ducks"
    result = just_do_it(text)
    eq_(result, "A Veritable Flock Of Ducks")

"""
# unittest
class TestCap(unittest.TestCase):
    # setUp()会在每个测试方法执行之前执行.
    def setUp(self):
        pass
    
    # testDown()在每个测试方法执行之后执行.
    def testDown(self):
        pass

    def test_one_word(self):
        text = "duck"
        result = cap.just_do_it(text)
        self.assertEqual(result, "Duck")

    def test_multiple_words(self):
        text = "a veritable flock of ducks"
        result = cap.just_do_it(text)
        self.assertEqual(result, "A Veritable Flock of Ducks")
"""








