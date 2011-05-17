from szstats.database import Base, DBSession
from szstats.utils.string import parse_modversion
from szstats.utils.string import parse_kernelversion
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql.expression import func
import datetime


class Device(Base):
    __tablename__ = "devices"

    id = Column('id', Integer, primary_key=True)
    hash = Column('hash', String(32), unique=True)
    name = Column('name', String(50), index=True)
    version = Column('version', String(255), index=True)
    version_raw = Column('version_raw', String(255))
    kernel_version = Column('kernel_version', String(255), index=True)
    kernel_version_raw = Column('kernel_version_raw', String(255))
    country = Column('country', String(50), index=True)
    carrier_id = Column('carrier_id', String(50), index=True)
    kang = Column('kang', Integer, index=True)
    date_added = Column('date_added', DateTime)
    date_updated = Column('date_updated', DateTime)

    @classmethod
    def count_kang(cls):
        session = DBSession()
        q = session.query(cls).filter(cls.kang == 1).count()
        return q

    @classmethod
    def count_nonkang(cls):
        session = DBSession()
        q = session.query(cls).filter(cls.kang == 0).count()
        return q

    @classmethod
    def device_count(cls):
        session = DBSession()

        q = session.query(func.count(cls.name), cls.name) \
            .group_by(cls.name).all()

        q = sorted(q, key=lambda x: x[0], reverse=True)

        return q

    @classmethod
    def version_count(cls):
        session = DBSession()

        q = session.query(func.count(cls.version), cls.version) \
            .filter(cls.kang == 0) \
            .group_by(cls.version).all()

        q = sorted(q, key=lambda x: x[0], reverse=True)

        return q

    @classmethod
    def country_count(cls):
        session = DBSession()
        q = session.query(cls.country, func.count('*').label('count')).group_by(cls.country).all()
        return q

    @classmethod
    def count_last_day(cls):
        timestamp = datetime.datetime.now() - datetime.timedelta(hours=24)
        session = DBSession()
        q = session.query(cls).filter(cls.date_added > timestamp).count()
        return q

    @classmethod
    def add(cls, **kwargs):
        # Clean up the version.
        version = parse_modversion(kwargs['version'])
        kernel_version = parse_kernelversion(kwargs['version'])

        # Grab a session
        session = DBSession()

        # Grab device record, if it already exists.
        try:
            obj = session.query(cls).filter(cls.hash == kwargs['hash']).one()
        except:
            obj = cls()
            obj.date_added = func.now()

        # Flag this as a KANG if necessary.
        if version == None:
            version = kwargs['version']
            obj.kang = 1
        else:
            obj.kang = 0

        if kernel_version == None:
            kernel_version = kwargs['kernel_version']
            obj.kang = 1
        else:
            obj.kang = 0

        # Populate the rest of the records.
        obj.hash = kwargs['hash']
        obj.name = kwargs['name']
        obj.version = version
        obj.version_raw = kwargs['version']
        obj.kernel_version = kernel_version
        obj.kernel_version_raw = kwargs['kernel_version']
        obj.country = kwargs['country']
        obj.carrier_id = kwargs['carrier_id']
        obj.date_updated = func.now()

        session.add(obj)
        session.commit()
