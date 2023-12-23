from pydantic import BaseSettings


class Settings(BaseSettings):
    mysql_url: str = "mysql+pymysql://root:123456@localhost:3306/backend?charset=utf8"
    redis_url: str = "redis://default:barn@localhost:6379"

    common_service: str = "http://127.0.0.1:9005/v1"
    cleaning_service: str = "http://127.0.0.1:9002/v1"
    batch_service: str = "http://127.0.0.1:9001/v1"
    label_service: str = "http://127.0.0.1:9003/v1"


settings = Settings()
