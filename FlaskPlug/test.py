# import redis
#
#
# conn = redis.Redis(host='localhost', port=6379, decode_responses=True)
# print(conn.keys())

from sqlalchemy import create_engine, ForeignKey, UniqueConstraint, Index
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm import relationship
from sqlalchemy import Index, UniqueConstraint


conn = create_engine(
    "mysql+pymysql://root:123abc@127.0.0.1:3306/test?charset=utf8",
    max_overflow=0,  # 超过连接池大小外最多创建的连接数
    pool_size=5,  # 连接池大小
    pool_timeout=30,  # 连接池中没有线程最多等待时间，否则报错
    pool_recycle=-1,  # 多久之后对连接池中的连接进行回收（重置）-1不回收
)

Base = declarative_base()

class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    title = Column(String(64), nullable=False)
    publisher_id = Column(Integer, ForeignKey('publisher.id'))
    publisher = relationship('Publisher', backref='books')
    tags = relationship('Tag', backref='books', secondary='book2tag')

    __table_args__ = (
        # UniqueConstraint联合唯一，这个联合唯一的字段名为：uni_id_name
        UniqueConstraint("id", "title", name="uni_id_title"),
        # 联合索引
        Index("id", "title")
    )


class Publisher(Base):
    __tablename__ = 'publisher'

    id = Column(Integer, primary_key=True)
    title = Column(String(64), nullable=False)


class Tag(Base):
    __tablename__ = 'tag'

    id = Column(Integer, primary_key=True)
    title = Column(String(64), nullable=False)

    def __repr__(self):
        return self.title


class Book2Tag(Base):
    __tablename__ = 'book2tag'

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('book.id'))
    tag_id = Column(Integer, ForeignKey('tag.id'))


def create_db():
    # metadata.create_all创建所有表
    Base.metadata.create_all(conn)


def drop_db():
    # metadata.drop_all删除所有表
    Base.metadata.drop_all(conn)


# 每次执行数据库操作的时候，都需要创建一个session,相当于管理器(相当于Django的ORM的objects)
Session = sessionmaker(bind=conn)
# 线程安全，基于本地线程实现每个线程用同一个session
session = scoped_session(Session)


if __name__ == '__main__':
    # create_db()
    # drop_db()

    # publisher_obj = Publisher(title='西丽出版社')
    # book_obj = Book(title='时间简史', publisher=publisher_obj)
    # tag_obj1 = Tag(title='python')
    # tag_obj2 = Tag(title='go')
    # tag_obj3 = Tag(title='linux')
    # session.add(publisher_obj)
    # session.add(book_obj)
    # session.add_all([tag_obj1, tag_obj2, tag_obj3])
    # session.commit()
    # session.close()

    # ret1 = session.query(Tag).filter(Tag.id==1).first()
    # ret2 = session.query(Tag).filter_by(id=2).first()
    # print(ret1)
    # print(ret2)

    # session.query(Tag).filter_by(id=2).update({"title": 'golang'})
    tag_obj = Tag(title='heihei2')
    # tag_obj.books = [Book(title='时间简史'), Book(title='吃屎')]
    tag_obj.books = [session.query(Book).filter_by(id=1).first()]
    session.add(tag_obj)
    session.commit()




