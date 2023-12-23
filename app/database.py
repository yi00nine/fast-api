import contextlib
from functools import wraps

from app.config import settings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# create a database engine depends on database protocol
engine = create_engine(
    settings.mysql_url, pool_size=50, pool_recycle=25200, max_overflow=50
)
SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)

Base = declarative_base()


# 依赖注入db_session 生成器
def get_db_session():
    db_session = SessionLocal()
    db_session.commit()
    try:
        yield db_session
    except Exception as e:
        print(f"Error: {e}")
        db_session.rollback()
        raise

    finally:
        db_session.close()


@contextlib.contextmanager
def get_local_session():
    """上下文管理器的session
       自动提交
    Raises:
        e: _description_
    Yields:
        _type_: _description_
    with get_local_session() as s:
        print(s.query(User).all())
    """
    s = SessionLocal()
    try:
        yield s
        s.commit()
    except Exception as e:
        s.rollback()
        raise e
    finally:
        s.close()


def db_session_decorator(func):
    """
    非web服务的db_session装饰器
    @db_session_decorator
    def run_some_task(db_session):
        # 在此处进行数据库操作
        # example: result = db_session.query(SomeModel).all()
        pass
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        db_session = SessionLocal()

        try:
            result = func(db_session, *args, **kwargs)
            db_session.commit()
            return result

        except Exception as e:
            print(f"Error: {e}")
            db_session.rollback()
            raise

        finally:
            db_session.close()

    return wrapper
