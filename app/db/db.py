from sqlachemy import DeclarativeBase


# This create a shared base class for all models to inherit from
# This is used by SQLAlchemy to map python classes to database tables.
class Base(DeclarativeBase):
    pass
