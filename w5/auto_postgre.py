# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Integer, SmallInteger, String, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class City(Base):
    __tablename__ = 'city'

    city_id = Column(Integer, primary_key=True, server_default=text("nextval('city_city_id_seq'::regclass)"))
    city = Column(String(50), nullable=False)
    country_id = Column(ForeignKey('country.country_id', onupdate='CASCADE'), nullable=False)
    last_update = Column(DateTime)

    country = relationship('Country')


class Country(Base):
    __tablename__ = 'country'

    country_id = Column(Integer, primary_key=True, server_default=text("nextval('country_country_id_seq'::regclass)"))
    country = Column(String(50), nullable=False)
    last_update = Column(DateTime)
