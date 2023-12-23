from app.database import get_db_session
from fastapi import APIRouter, Depends
from loguru import logger
from typing import Union
from app.schemas.response import Response
from app.services.test import get_tests
from sqlalchemy.orm import Session

router = APIRouter(tags=['test'])


@router.get('/data')
def get_router_test(
    name: Union[str, None] = None, 
    limit: Union[str, None] = None, 
    offset: Union[str, None] = None, 
    db_session: Session = Depends(get_db_session),
):
    try:
        datas = get_tests(name, limit, offset, db_session)
        return Response(code=1, data=datas, msg="查询成功")
    except Exception as e:
        logger.error(str(e))
        return Response(code=1, msg="查询失败;{}".format(str(e)), data=None)
