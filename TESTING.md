# Testing Documentation

## 1. Objective

The purpose of testing is to verify that the Online Booking System works correctly for valid and invalid user inputs.

Automated testing is performed using Python pytest.

## 2. Testing Tools

- Testing Framework: pytest
- Programming Language: Python
- Web Framework: Flask
- Database: SQLite

## 3. Test Cases

### Test Case 1: Home Page

Test Function:
`test_home_page`

Expected Result:
Home page should open successfully with HTTP status code 200.

Actual Result:
Home page opened successfully.

Result:
PASS

---

### Test Case 2: Event Details

Test Function:
`test_event_details`

Expected Result:
Event details page should open successfully.

Actual Result:
Event details page opened successfully.

Result:
PASS

---

### Test Case 3: Booking Page

Test Function:
`test_booking_page`

Expected Result:
Booking form should open successfully with HTTP status code 200.

Actual Result:
Booking form opened successfully.

Result:
PASS

---

### Test Case 4: Create Booking

Test Function:
`test_create_booking`

Test Data:
- Name: Test User
- Email: test@example.com
- Seats: 2

Expected Result:
A booking should be created successfully.

Actual Result:
Booking was created successfully.

Result:
PASS

---

### Test Case 5: Booking History

Test Function:
`test_bookings_page`

Expected Result:
Booking history page should open successfully.

Actual Result:
Booking history page opened successfully.

Result:
PASS

---

### Test Case 6: Invalid Event ID

Test Function:
`test_invalid_event_id`

Test Data:
- Event ID: 9999

Expected Result:
The application should handle an invalid event ID without crashing.

Actual Result:
The application handled the invalid event request successfully.

Result:
PASS

---

### Test Case 7: Zero Seats

Test Function:
`test_zero_seats`

Test Data:
- Seats: 0

Expected Result:
The application should handle zero-seat input without crashing.

Actual Result:
The application handled the input successfully.

Result:
PASS

---

### Test Case 8: Negative Seats

Test Function:
`test_negative_seats`

Test Data:
- Seats: -2

Expected Result:
The application should handle negative seat input without crashing.

Actual Result:
The application handled the input successfully.

Result:
PASS

---

### Test Case 9: Booking More Seats Than Available

Test Function:
`test_booking_more_than_available`

Test Data:
- Seats: 99999

Expected Result:
The application should handle a booking request greater than the available seats without crashing.

Actual Result:
The application handled the request successfully.

Result:
PASS

---

## 4. Test Execution

The following command was used to execute the automated tests:

```bash
pytest -v