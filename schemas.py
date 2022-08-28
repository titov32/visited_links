from pydantic import BaseModel, HttpUrl, AnyUrl
from utils import get_host
from typing import List


class Domain(BaseModel):
    links: list[str]


class CheckDomain(BaseModel):
    links: list[HttpUrl]