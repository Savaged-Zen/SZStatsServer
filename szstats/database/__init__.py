from szstats.database.base import AbstractTable
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm.session import sessionmaker


DBSession = scoped_session(sessionmaker())
Base = declarative_base(cls=AbstractTable)

def populate_data():
    from szstats.database.schema import Device
    session = DBSession()

    # Create some fake testing entries.
    obj1 = Device()
    obj1.hash = "XYZ1"
    obj1.country = "ca"
    obj1.carrier_id = "310260"
    obj1.kang = 0
    obj1.version = "Nightly"
    obj1.name = "passion"

    obj2 = Device()
    obj2.hash = "XYZ2"
    obj2.country = "us"
    obj2.carrier_id = "310260"
    obj2.kang = 0
    obj2.version = "Nightly"
    obj2.name = "vision"

    session.add(obj1)
    session.add(obj2)
    session.commit()

def init_database(engine):
    DBSession.configure(bind=engine)

    # Import ORM mapped objects.
    __import__("szstats.database.schema", globals(), locals(), ["*"])

    # Bind metadata to engine.
    Base.metadata.bind = engine

    # Create all tables (if necessary)
    Base.metadata.create_all(engine)

    try:
        populate_data()
    except:
        DBSession.rollback()
