Testing Documentation

Objective

The objective of testing is to verify that the Online Booking System works correctly for valid and invalid user inputs.

Testing Tool

Python pytest was used for automated testing.

Test Cases

Test Case| Expected Result| Actual Result| Status
Home Page| Page opens successfully| Page opened successfully| PASS
Event Details| Event details page opens| Page opened successfully| PASS
Booking Page| Booking form opens| Form opened successfully| PASS
Successful Booking| Booking is created| Booking created successfully| PASS
Booking History| Booking history opens| Page opened successfully| PASS
Invalid Event ID| Invalid event is handled| Tested successfully| PASS
Zero Seats| Invalid booking is handled| Tested successfully| PASS
Negative Seats| Invalid booking is handled| Tested successfully| PASS
More Seats Than Available| Booking is handled/rejected| Tested successfully| PASS

Final Test Result

All automated tests were executed using pytest.

Final Result: All tests passed.

Conclusion

The testing process verifies the major functionalities of the Online Booking System, including event viewing, event details, booking, booking history, and handling of invalid booking inputs.
