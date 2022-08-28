from utils import get_pattern_time_query, get_host
from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_domains():
    json = {"links": ["https://ya.ru",
                      "https://ya.ru?q=123",
                      "funbox.ru",
                      "https://stackoverflow.com/questions/111123/how-to"]}
    response = client.post("/visited_links", json=json)
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_read_visited_domains():
    time1=123321
    time2=1231231
    response = client.get(f"/visited_links?from_={time1}&to={time2}")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_pattern():
    assert get_pattern_time_query(166151437, 166150000) == str(16615)


def test_get_host():
    assert get_host('hh.ru') == 'http://hh.ru'
    assert get_host('https://hh.ru') == 'https://hh.ru'