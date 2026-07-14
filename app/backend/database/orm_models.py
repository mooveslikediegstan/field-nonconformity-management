# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, Float, Date, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from backend.database.session import Base
from datetime import datetime


class CityORM(Base):
    __tablename__ = "city"

    city_id          = Column(Integer, primary_key=True, autoincrement=True)
    city_name        = Column(String, nullable=False)
    state            = Column(String, nullable=False)
    country          = Column(String, nullable=False)
    geolocation_lat  = Column(Float, nullable=False)
    geolocation_lon  = Column(Float, nullable=False)


class CustomerORM(Base):
    __tablename__ = "customer"

    customer_id     = Column(String, primary_key=True)
    customer_name   = Column(String, nullable=False)
    short_name      = Column(String, nullable=False)
    city_id         = Column(Integer, ForeignKey("city.city_id"), nullable=False)
    address         = Column(String, nullable=False)
    segment         = Column(String, nullable=False)
    sub_segment     = Column(String, nullable=False)
    region          = Column(String, nullable=False)

    city            = relationship("CityORM")
    projects        = relationship("ProjectORM", back_populates="customer")


class ProjectORM(Base):
    __tablename__ = "project"

    project_id      = Column(String, primary_key=True)
    project_name    = Column(String, nullable=False)
    customer_id     = Column(String, ForeignKey("customer.customer_id"), nullable=False)

    customer        = relationship("CustomerORM", back_populates="projects")

class ComponentORM(Base):
    __tablename__ = "components"

    component_key = Column(Integer, primary_key=True,autoincrement=True)
    nonconformity_id = Column(Integer, ForeignKey("nonconformity.nonconformity_id"),nullable=False)
    component_id =  Column(String, nullable=False)
    description =  Column(String, nullable=False)
    component_problem =  Column(String, nullable=False)
    quantity =  Column(Integer, nullable=False)
    is_missing_part = Column(Boolean, nullable=False)


class NonConformityORM(Base):
    __tablename__ = "nonconformity"

    nonconformity_id = Column(Integer, primary_key=True,autoincrement=True)
    title = Column(String, nullable=False)
    problem_description = Column(String, nullable=False)
    creator_id = Column(Integer, nullable=False)
    creation_date = Column(Date, nullable=False)
    project_id = Column(String, ForeignKey("project.project_id"), nullable=False)
    project_status = Column(String, nullable=False)   
    
