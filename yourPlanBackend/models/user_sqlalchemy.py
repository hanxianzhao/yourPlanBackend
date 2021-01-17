# # -*- coding: utf-8 -*-
# """
# @author:韩先钊
# @file: user_sqlalchemy.py
# @time: 2021/1/13  22:32
# """
#
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint, Index
# from sqlalchemy.orm import relationship
# import datetime
#
# Base = declarative_base()
#
#
# class Users(Base):
#     __tablename__ = 'users'
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String(32))
#     age = Column(Integer, default=18)
#     email = Column(String(32), unique=True)
#     city = Column(String(64), default="")
#     ctime = Column(DateTime, default=datetime.datetime.now)
#     openid = Column(String(64), index=True)
#     extra = Column(Text, nullable=True)
#
#     __table_args__ = (
#         # UniqueConstraint('id', 'name', name='uix_id_name'),
#         # Index('ix_id_name', 'name', 'extra'),
#     )
#
#
# def init_db():
#     """
#     根据类创建数据库表
#     :return:
#     """
#     engine = create_engine(
#         "mysql+pymysql://root:0819@127.0.0.1:3306/test_sqlalchemy?charset=utf8",
#         max_overflow=0,  # 超过连接池大小外最多创建的连接
#         pool_size=5,  # 连接池大小
#         pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
#         pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
#     )
#
#     Base.metadata.create_all(engine)
#
#
# def drop_db():
#     """
#     根据类删除数据库表
#     :return:
#     """
#     engine = create_engine(
#         "mysql+pymysql://root:0819@127.0.0.1:3306/test_sqlalchemy?charset=utf8",
#         max_overflow=0,  # 超过连接池大小外最多创建的连接
#         pool_size=5,  # 连接池大小
#         pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
#         pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
#     )
#
#     Base.metadata.drop_all(engine)
#
# init_db()
# # drop_db()