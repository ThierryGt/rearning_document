from mongoengine import *
from datetime import datetime

connect("mydb", host="127.0.0.1", username="", password="")

# 定义分类文档(集合名即为类名)
class Categories(Document):
    # 继承的Decument类,为普通文档
    name = StringField(max_length=30, required=True)
    artnum = IntField(default=0, required=True)
    date = DateTimeField(default=datetime.now(), required=True)

# 如果required为True则必须赋予初始值,默认为False
# 如果有default,赋予初始值则使用默认值
cate = Categories(name="Linux")
# 保存到数据库
cate.save()
# 返回集合里的所有文档对象列表,
cate = Categories.objects.all()
# 返回所有符合查询条件的结果的文档对象列表
cate = Categories.objects(name="Python")
# 更新查询到的文档
cate.name="kali"
cate.update()
# 查询数组,默认查询数组“=”代表的意思是in


class Posts(Document):
    title = StringField(max_length=100, required=True)
    content = StringField(required=True)
    tags = ListField(StringField(max_length=20, required=True), required=True)
    categories = ReferenceField(Categories) 

# 通过ReferenceField引用字段可以通过文档直接获取引用字段引用的那个文档
# 插入引用字段
cate =Categories(name="Linux")
cate.save()
post = Posts(title="Linuxzen.com", content="Linuxzen.com",tags=["Linux","web"], categories=cate)
post.save()
# 一般文档查询会返回一个列表,可以使用first()获取第一个文档对象,
cate = Posts.objects.all().first().categories
# 可以通过cate.name获取到Categories.object(name)的属性

# 查询包含Linux分类的文章
cate = Categories.objects(name="Linux").first()
Posts.objects(categories=cate)


# EmbeddedDocument嵌入文档
class Tags(EmbeddedDocument):
    name = StringField()
    date = DateTimeField(default=datetime.now())


class Posts(Document):
    title = StringField(max_length=100, required=True)
    content = StringField(required=True)
    tags = ListField(EmbeddedDocumentField('Tags'), required=True)
    categories = ReferenceField(Categories)

# 使用
tag = Tags(name="Linuxzen")
post = Posts(title="Linuxzen.com", content="Linuxzen.com", tags=[tag], categories=cate)
tag = Tags(name="mysite")
post.tags.append(tag)
post.save()
tags = post.tags
for teg in tags:
    print(tag.name)
Linuxzen
mysite

# slice用于分片
# 使用原始语句查询,可以使用__raw__操作符Page.objects(raw={"tags":"coding"})使用$inc和$set操作符
# 更新嵌入文档comments字段by的值为joe的文档字段votes增加1
Page.objects(comments_by="joe").update(inc__votes=1)
# 更新嵌入文档comments字段by的值为joe的文档字段votes设置为1
Page.objects(comments_by="joe").update(set__votes=1)
#查询结果转换成字典
users_dict = User.objects().to_mongo()
# 排序,按日期排列
user = User.objects.order_by("date")
# 按日期倒序
user = User.objects.order_by("-date")


# flask 中的应用

db_field
# MongoDB字段名称,(默认:无)

required
# 如果设置为True,并且该字段未在文档实例上设置,ValidationError会在验证文档时引发a(默认False)

default
# 未为此字段设置时使用的值(默认无)

unique
# 如果为True,则该集合中的任何文档都不会具有该字段的相同值(默认False)

unique_with
# 与此字段一起使用的字段名称(或字段名称列表)将不会具有相同值的集合中的两个文档(默认无)

primary_key
# 如果为True，则使用此字段作为集合的主键。 DictField 和EmbeddedDocuments都支持作为文档的主键。 
# 如果设置，该字段也可通过PK字段访问(默认False)

choices
# 一个可迭代的（例如列表，元组或集合）选项，这个字段的值应该被限制到这个选项(默认无)

**kwargs
# 提供额外的元数据作为任意附加关键字参数,无法覆盖现有的属性
# 常用选项包括help_text和verbose_name，通常由窗体和小部件库使用

class SurveyResponse(Document):
    date = DateTimeField()
    user = ReferenceField(User)
    answers = DictField()

survey_response = SurveyResponse(date=datetime.utcnow(), user=request.user)
response_form = ResponseForm(request.POST)
survey_response.answers = response_form.cleaned_data()
survey_response.save()


