import databases
import sqlalchemy
import ormar


metadata = sqlalchemy.MetaData()
database = databases.Database("sqlite:///sqlite.db")
engine = sqlalchemy.create_engine("sqlite:///sqlite.db")


class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database
