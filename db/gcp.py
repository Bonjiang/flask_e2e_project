from sqlalchemy import create_engine, inspect, Column, Integer, String, Date, ForeignKey
from sqlalchemy.engine.reflection import Inspector
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    gender = Column(String(10), nullable=False)
    contact_number = Column(String(100))
    is_deceased = Column(String(30), nullable=False)
    records = relationship('MedicalRecord', back_populates='patient')

class MedicalRecord(Base):
    __tablename__ = 'medical_records'

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    diagnosis = Column(String(100), nullable=False)
    treatment = Column(String(200))
    admission_date = Column(Date, nullable=False)
    discharge_date = Column(Date)

    patient = relationship('Patient', back_populates='records')

DATABASE_URL = "mysql+mysqlconnector://username:password@host/db_name"
engine = create_engine(DATABASE_URL)

inspector = Inspector.from_engine(engine)
inspector.get_table_names()

Base.metadata.create_all(engine)
