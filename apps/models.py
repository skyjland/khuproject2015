# -*- coding:utf-8 -*-
from apps import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    name = db.Column(db.String(255))
    join_date = db.Column(db.DateTime(),default = db.func.now())
    level = db.Column(db.Integer, default = 0)
    comments = db.relationship('Comment', backref=db.backref('user', cascade='all, delete-orphan', lazy='dynamic'))
    user = db.relationship('Article',backref=db.backref('user', cascade='all, delete-orphan', lazy='dynamic'))
    rating = db.relationship('Rating',backref=db.backref('user', cascade='all, delete-orphan', lazy='dynamic'))
    likeComment = db.relationship('LikeComment',backref=db.backref('user', cascade='all, delete-orphan', lazy='dynamic'))
    likeArticle = db.relationship('LikeArticle',backref=db.backref('user', cascade='all, delete-orphan', lazy='dynamic'))

class Article(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(255))

    userID = db.Column(db.String(255), db.ForeignKey(User.id))

    title = db.Column(db.String(255))
    content = db.Column(db.Text(db.Text(length=None, collation=None, convert_unicode=False, unicode_error=None, _warn_on_bytestring=False)))
    comments = db.relationship("Comment", backref = db.backref('article', cascade = 'all, delete-orphan'))

    like = db.Column(db.relationship("LikeArticle", backref = db.backref('article', cascade = 'all, delete-orphan')))
    date_created = db.Column(db.DateTime(), default=db.func.now())


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    userId = db.Column(db.String(255), db.ForeignKey(User.id))
    articleId = db.Column(db.Integer, db.ForeignKey(Article.id))
    content = db.Column(db.Text(db.Text(length=None, collation=None, convert_unicode=False, unicode_error=None, _warn_on_bytestring=False)))
    date_created = db.Column(db.DateTime(), default = db.func.now())



#강의평가와 관련된 부분

class Teacher(db.Model):
    id = db.Column(db.integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    major = db.Column(db.String(255))
    age = db.Column(db.Integer, default = 0)
    filmo = db.relationship('Filmo', backref=db.backref('teacher', cascade='all, delete-orphan', lazy='dynamic'))

class Lecture(db.Model):
    id = db.Column(db.integer, primary_key=True)
    name = db.Column(db.String(255))
    major = db.Column(db.String(255))
    room = db.Column(db.String(255))
    sTime = db.Column(db.Time)
    eTime = db.Column(db.Time)
    filmo = db.relationship('Filmo', backref=db.backref('lecture', cascade='all, delete-orphan', lazy='dynamic'))
    reviews = db.relationship('Review', backref=db.backref('lecture',cascade='all, delete-orphan', lazy='dynamic'))
    ratings = db.relationship('Rating', backref=db.backref('lecture',cascade='all, delete-orphan', lazy='dynamic'))

class Filmo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    teacherID = db.Column(db.Intger, db.ForeignKey(Teacher.id))
    lectureID = db.Column(db.Intger, db.ForeignKey(Lecture.id))

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.String(255), db.ForeignKey(User.id))
    LectureID = db.Column(db.Integer, db.ForeignKey(Lecture.id))
    content = db.Column(db.Text(db.Text(length=None, collation=None, convert_unicode=False, unicode_error=None, _warn_on_bytestring=False)))
    like = db.relationship('LikeReview', backref=db.backref('review', cascade='all, delete-orphan', lazy='dynamic'))


# 강의별 별점
class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    userID = db.Colum(db.Integer,db.ForeignKey(User.id))
    lectureID = db.Column(db.Integer,db.ForeignKey(Lecture.id))


#리뷰 좋아요
class LikeReview(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    like = db.Column(db.Integer)
    userID = db.Column(db.Integer, db.ForeignKey(User.id))
    reviewID = db.Column(db.Integer ,db.ForeignKey(Review.id))



# 좋아요
class LikeComment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    like = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey(User.id))
    commentID = db.Column(db.Integer, db.ForeignKey(Comment.id))

#게시글 좋아요
class LikeArticle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    like = db.Column(db.Integer)
    userID = db.Column(db.Integer, db.ForeignKey(User.id))
    articleID = db.Column(db.Integer ,db.ForeignKey(Article.id))




