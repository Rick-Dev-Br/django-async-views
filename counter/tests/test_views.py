from django.urls import reverse


def test_index_returns_project_summary(client):
    response = client.get(reverse("index"))

    assert response.status_code == 200
    assert response.json()["counter_url"] == "/contador/"


def test_async_time_counter_returns_counter_payload(client):
    response = client.get(reverse("async-counter"), {"seconds": 0})
    payload = response.json()

    assert response.status_code == 200
    assert payload["mode"] == "async"
    assert payload["requested_seconds"] == 0
    assert payload["ticks"] == []


def test_async_time_counter_limits_large_values(client, monkeypatch):
    async def instant_sleep(seconds):
        return None

    monkeypatch.setattr("counter.views.asyncio.sleep", instant_sleep)

    response = client.get(reverse("async-counter"), {"seconds": 99})
    payload = response.json()

    assert response.status_code == 200
    assert payload["requested_seconds"] == 10
