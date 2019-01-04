from uploadCode import db


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))

    code_record = db.relationship("CodeRecord", backref="user")


class CodeRecord(db.Model):
    __tablename__ = "codeRecord"

    id = db.Column(db.Integer, primary_key=True)
    upload_date = db.Column(db.Date)
    code_nums = db.Column(db.Integer)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
