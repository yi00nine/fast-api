from sqlalchemy.orm.session import Session
from app.models.test import Test

def get_tests(
    name,
    limit,
    offset,
    db_session: Session
):
    return Test.get_tests(name, limit=limit, offset=offset, session=db_session)