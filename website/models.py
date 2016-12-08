# coding: utf-8
from sqlalchemy import Column, Date, Float, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Cpu(Base):
    __tablename__ = 'cpu'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    model = Column(Text)
    clock = Column(Text)
    max_turbo = Column(Text)
    integrated_gpu = Column(Text)
    stock_cooler = Column(Integer)
    manufacturer = Column(Text)
    cpu_series = Column(Text)
    logical_cores = Column(Integer)
    physical_cores = Column(Integer)
    socket = Column(Text)
    superscore = Column(Integer)
    avg_critic_score = Column(Integer)
    avg_user_score = Column(Integer)
    oldest_review_date = Column(Date)
    newest_review_date = Column(Date)


class Gpu(Base):
    __tablename__ = 'gpu'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    model = Column(Text)
    processor_manufacturer = Column(Text)
    manufacturer = Column(Text)
    graphic_processor = Column(Text)
    mem_size = Column(Text)
    boosted_clock = Column(Text)
    superscore = Column(Integer)
    avg_critic_score = Column(Integer)
    avg_user_score = Column(Integer)
    oldest_review_date = Column(Date)
    newest_review_date = Column(Date)


class Review(Base):
    __tablename__ = 'review'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer)
    date = Column(Date)
    is_critic = Column(Integer)
    url = Column(String(255), nullable=False, unique=True)
    title = Column(Text, nullable=False)
    author = Column(String(255))
    rating = Column(Float)
    content = Column(String)
