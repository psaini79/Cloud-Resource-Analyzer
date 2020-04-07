"""
mysql client table structure
"""
from sqlalchemy import (Column, ForeignKey, PrimaryKeyConstraint)
from sqlalchemy import (Integer, String, DateTime, Date, Text, Float)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class PredictInfo(Base):
    __tablename__ = 'predict_info'

    #id = Column(String(256), nullable=False, primary_key=True)
    time_stamp = Column(DateTime(timezone=True), nullable=False, primary_key=True)
    cpu_utilization = Column(Float(12), nullable=False)

class CorpTenancyInfo(Base):
    __tablename__ = 'corp_tenancy_info'
	
    tenancy_id = Column(String(40), nullable=False, primary_key=True)
    company_name = Column(String(256), nullable=False)
    created_on = Column(DateTime(timezone=False), nullable=False)
    tenancy_name = Column(String(256), nullable=False)

class CorpTenancyUserInfo(Base):
    __tablename__ = 'corp_tenancy_user_info'
    user_id = Column(String(40), nullable=False, primary_key=True)
    first_name = Column(String(40), nullable=False)
    last_name = Column(String(40), nullable=False)
    email_id = Column(String(40), nullable=False)
    password = Column(String(128), nullable=False)
    role = Column(String(15), nullable=False)
    created_on = Column(DateTime(timezone=False), nullable=True)
    last_login = Column(DateTime(timezone=False), nullable=False)
    designation = Column(String(40), nullable=True)
    tenancy_id = Column(String(40), ForeignKey('corp_tenancy_info.tenancy_id'), nullable=True)
    mobile_num = Column(Integer, nullable=True)
    corp_tenancy_info = relationship("CorpTenancyInfo")
    
