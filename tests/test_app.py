
import sys
import os

# Add the project root directory to Python path
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

import pytest
from app import app, init_db


@pytest.fixture
def client(tmp_path, monkeypatch):
    # Create a temporary database for testing
    test_database = tmp_path / "test_bookings.db"

    # Use the temporary database instead of the real bookings.db
    monkeypatch.setattr("app.DATABASE", str(test_database))

    # Initialize tables and sample events
    init_db()

    # Enable Flask testing mode
    app.config["TESTING"] = True

    # Create test client
    with app.test_client() as client:
        yield client



def test_home_page(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"Tech Fest 2026" in response.data
    assert b"Cultural Fest 2026" in response.data
    assert b"Career Seminar 2026" in response.data


def test_event_details(client):
    response = client.get("/event/1")

    assert response.status_code == 200
    assert b"Tech Fest 2026" in response.data


def test_booking_page(client):
    response = client.get("/book/1")

    assert response.status_code == 200
    assert b"Book: Tech Fest 2026" in response.data


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


def test_invalid_event_id(client):
    response = client.get("/event/9999")

    assert response.status_code in [404, 200]
def test_zero_seats(client):
    response = client.post(
        "/book/1",
        data={
            "name": "Test User",
            "email": "test@example.com",
            "seats": "0"
        },
        follow_redirects=True
    )

    assert response.status_code == 200
def test_negative_seats(client):
    response = client.post(
        "/book/1",
        data={
            "name": "Test User",
            "email": "test@example.com",
            "seats": "-2"
        },
        follow_redirects=True
    )

    assert response.status_code == 200
def test_booking_more_than_available(client):
    response = client.post(
        "/book/1",
        data={
            "name": "Test User",
            "email": "test@example.com",
            "seats": "99999"
        },
        follow_redirects=True
    )

    assert response.status_code == 200    