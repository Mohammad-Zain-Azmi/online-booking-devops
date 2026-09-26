from flask import Flask, render_template, request
import sqlite3
import uuid

app = Flask(__name__)

DATABASE = "/tmp/bookings.db" if os.path.exists("/.dockerenv") else "bookings.db"


def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():

    conn = get_db()

    # Create events table
    conn.execute("""
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            venue TEXT NOT NULL,
            description TEXT,
            available_seats INTEGER NOT NULL
        )
    """)

    # Create bookings table
    conn.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            booking_id TEXT NOT NULL,
            event_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            seats INTEGER NOT NULL,
            booking_date TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Check if events already exist
    count = conn.execute(
        "SELECT COUNT(*) FROM events"
    ).fetchone()[0]

    # Add sample events
    if count == 0:

        events = [
            (
                "Tech Fest 2026",
                "10 October 2026",
                "10:00 AM",
                "College Auditorium",
                "Technical event with coding competitions and workshops.",
                120
            ),
            (
                "Cultural Fest 2026",
                "15 October 2026",
                "11:00 AM",
                "College Ground",
                "Annual cultural event with music and performances.",
                250
            ),
            (
                "Career Seminar 2026",
                "20 October 2026",
                "2:00 PM",
                "Seminar Hall",
                "Career guidance and placement preparation seminar.",
                100
            )
        ]

        conn.executemany("""
            INSERT INTO events
            (name, date, time, venue, description, available_seats)
            VALUES (?, ?, ?, ?, ?, ?)
        """, events)

        conn.commit()

    conn.close()


@app.route("/")
def home():

    conn = get_db()

    events = conn.execute(
        "SELECT * FROM events"
    ).fetchall()

    conn.close()

    return render_template(
        "index.html",
        events=events
    )


@app.route("/event/<int:event_id>")
def event_details(event_id):

    conn = get_db()

    event = conn.execute(
        "SELECT * FROM events WHERE id = ?",
        (event_id,)
    ).fetchone()

    conn.close()

    if event is None:
        return "Event not found", 404

    return render_template(
        "event.html",
        event=event
    )


@app.route("/book/<int:event_id>", methods=["GET", "POST"])
def book(event_id):

    conn = get_db()

    event = conn.execute(
        "SELECT * FROM events WHERE id = ?",
        (event_id,)
    ).fetchone()

    if event is None:
        conn.close()
        return "Event not found", 404

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        try:
            seats = int(request.form["seats"])
        except ValueError:
            conn.close()
            return "Invalid number of seats"

        if seats <= 0:
            conn.close()
            return "Invalid number of seats"

        if seats > event["available_seats"]:
            conn.close()
            return "Not enough seats available"

        booking_id = "BK" + uuid.uuid4().hex[:8].upper()

        conn.execute("""
            INSERT INTO bookings
            (booking_id, event_id, name, email, seats)
            VALUES (?, ?, ?, ?, ?)
        """, (
            booking_id,
            event_id,
            name,
            email,
            seats
        ))

        conn.execute("""
            UPDATE events
            SET available_seats = available_seats - ?
            WHERE id = ?
        """, (
            seats,
            event_id
        ))

        conn.commit()

        booking = conn.execute("""
            SELECT *
            FROM bookings
            WHERE booking_id = ?
        """, (booking_id,)).fetchone()

        conn.close()

        return render_template(
            "confirmation.html",
            booking=booking,
            event=event
        )

    conn.close()

    return render_template(
        "booking.html",
        event=event
    )


@app.route("/bookings")
def bookings():

    conn = get_db()

    bookings = conn.execute("""
        SELECT
            bookings.*,
            events.name AS event_name
        FROM bookings
        JOIN events
        ON bookings.event_id = events.id
        ORDER BY bookings.id DESC
    """).fetchall()

    conn.close()

    return render_template(
        "bookings.html",
        bookings=bookings
    )


if __name__ == "__main__":

    init_db()

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )
    