import sys
import os

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

import pytest

from app import app, init_db


@pytest.fixture
def client(tmp_path, monkeypatch):

    test_database = tmp_path / "test_bookings.db"

    monkeypatch.setattr(
        "app.DATABASE",
        str(test_database)
    )

    init_db()

    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_home_page(client):

    response = client.get("/")

    assert response.status_code == 200
    assert b"Upcoming Events" in response.data


def test_event_details(client):

    response = client.get("/event/1")

    assert response.status_code == 200
    assert b"Tech Fest 2026" in response.data


def test_booking_page(client):

    response = client.get("/book/1")

    assert response.status_code == 200
    assert b"Book Your Seats" in response.data


def test_create_booking(client):

    response = client.post(
        "/book/1",
        data={
            "name": "Test User",
            "email": "test@example.com",
            "seats": "2"
        }
    )

    assert response.status_code == 200
    assert b"Booking Confirmed" in response.data


def test_bookings_page(client):

    response = client.get("/bookings")

    assert response.status_code == 200
    assert b"My Bookings" in response.data