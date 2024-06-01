import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm


# --------------- Create Database ---------------------
# This line configures the connection string to a SQLite database file named "database.db"
# located in the current working directory (./).
SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db"

# By default, SQLite only allows a single connection thread at a time. This can be
# problematic in multi-threaded Python applications because database operations can
# block other threads. To address this, we set the `check_same_thread` argument
# to `False` when creating the SQLAlchemy engine. This disables the same-thread
# check, allowing multiple threads to interact with the database concurrently.
# However, it's important to use connection pooling or other techniques to manage
# database connections effectively in a multi-threaded environment.
engine = _sql.create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# This line creates a sessionmaker object using the `SessionLocal` name. A
# sessionmaker is a factory that creates SQLAlchemy database sessions. The
# arguments passed here configure the session behavior:
#   - `autocommit=False`: Disables automatic transaction commits after every
#     database operation. You'll need to explicitly commit or rollback changes
#     using the session object's methods.
#   - `autoflush=False`: Disables automatic flushing of changes to the database
#     after every query or operation. You'll need to call `session.flush()`
#     manually to synchronize with the database.
#   - `bind=engine`: Binds the sessionmaker to the previously created engine,
#     specifying the database connection pool it should use.
SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

# This line creates a base class named `Base` for defining database models.
# Models that inherit from `Base` will be automatically mapped to database tables
# by SQLAlchemy.
Base = _declarative.declarative_base()

# -----------------------------------------------------