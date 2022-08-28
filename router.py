import pydantic
from fastapi import APIRouter, HTTPException
from utils import get_pattern_time_query, get_host
from settings import PORT, HOST
from redis import Redis
from time import time
import schemas


api_router = APIRouter()
redis_conn = Redis(host=HOST, port=PORT)


@api_router.get('/')
async def test():
    return {'status': 'ok'}


@api_router.post('/visited_links')
async def create_domains(list_links: schemas.Domain):
    list_ = [get_host(host) for host in list_links.links]
    try:
        list_links = schemas.CheckDomain(links=list_)
        list_host = [link.host for link in list_links.links]
    except pydantic.ValidationError:
        raise HTTPException(status_code=422,
                            detail="hosts is not valid")
    redis_conn.lpush(int(time()), *list_host)
    return {'status': 'ok'}


@api_router.get('/visited_domains')
async def read_visited_domains(from_: int, to: int):
    if from_ > to:
        return {"status": "error", "description": "field 'to' must be  large than field 'from_' "}

    pattern = get_pattern_time_query(from_, to) + '*'
    list_keys = redis_conn.keys(pattern=pattern)
    list_links = set()

    for key in list_keys:
        print(key)
        for link in redis_conn.lrange(key, 0, -1):
            list_links.add(link.decode())
    print(list_links)
    return {"domains": list_links,
            'status': 'ok'}
