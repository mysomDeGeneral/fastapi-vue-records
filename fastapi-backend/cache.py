from fastapi_redis_cache import FastApiRedisCache, cache
from .config import settings

REDIS_URL = settings.REDIS_URL

redis_cache = FastApiRedisCache()


def init_cache():
    redis_cache.init(
        host_url=REDIS_URL,
        prefix="records-cache",
        response_header="X-RecordsApp-Cache",
        ignore_arg_types=[str, int, float, bool]
    )
