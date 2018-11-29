from mongoengine import *
from datetime import datetime
from mongoengine.context_managers import switch_db, switch_collection
connect("test", host="127.0.0.1", username="", password="")


class Comment(EmbeddedDocument):
    content = StringField()
    name = StringField(max_length=120)


class TestUser(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)


class TestPost(Document):
    title = StringField(max_length=120, required=True)
    # MapFields和DictFields目前不支持自动处理已删除的应用
    author = ReferenceField(TestUser, reverse_delete_rule=CASCADE)
    tags = ListField(StringField(max_length=30))
    comments = ListField(EmbeddedDocumentField(Comment))
    # allow_inheritance: 开启可继承
    meta = {"allow_inheritance": True}
    
    
class TextPost(TestPost):
    content = StringField()


class ImagePost(TestPost):
    image_path = StringField()


class LinkPost(TestPost):
    LINK_URL = StringField()


ross = TestUser(email="ross@example.com")
ross.first_name="ro"
ross.last_name = "ss"
# ross.save()

john = TestUser(email="ross@example.com")
john.first_name="jo"
john.last_name = "hn"
# john.save()

post1 = TextPost(title="Fun with MongoEngine", author=john)
post1.content = "post1contents"
post1.tags = ["mongodb", "mongoengine"]
# post1.save()

post2 = LinkPost(title="mongoengine Documentation", author=ross)
post2.LINK_URL = "http://docs.mongoengine.com"
post2.tags = ["mongoengine"]
# post2.save()


class Book(Document):
    name = StringField()
    # 指向book-db与Book集合
    meta = {"db_alias": "book-db"}
    
    # switch_db: 可访问archive-book-db(原数据库test)数据库下的Book集合文档
    # 保存到不同数据库同集合
    with switch_db(Book, "archive-book-db") as Book:
        Book(name="n").save()

    # switch_collection: 可访问test数据库下Book2000(原Book)集合文档
    # 保存到同数据库不同集合
    with switch_collection(Book, "Book2000"):
        Book(name="helloworld").save()



