from FlaskPlug import db
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index, Float
from sqlalchemy.orm import relationship


class Book(db.Model):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    title = Column(String(64), nullable=False)
    price = Column(Float)
    publisher_id = Column(Integer, ForeignKey('publisher.id'))
    publisher = relationship('Publisher', backref='books')
    tags = relationship('Tag', backref='books', secondary='book2tag')

    __table_args__ = (
        # UniqueConstraint联合唯一，这个联合唯一的字段名为：uni_id_name
        UniqueConstraint("id", "title", name="uni_id_title"),
        # 联合索引
        Index("id", "title")
    )

    def __repr__(self):
        return self.title


class Publisher(db.Model):
    __tablename__ = 'publisher'

    id = Column(Integer, primary_key=True)
    title = Column(String(64), nullable=False)

    def __repr__(self):
        return self.title


class Tag(db.Model):
    __tablename__ = 'tag'

    id = Column(Integer, primary_key=True)
    title = Column(String(64), nullable=False)

    def __repr__(self):
        return self.title


class Book2Tag(db.Model):
    __tablename__ = 'book2tag'

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('book.id'))
    tag_id = Column(Integer, ForeignKey('tag.id'))
