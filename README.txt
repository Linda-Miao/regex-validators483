REGEX VALIDATORS ASSIGNMENT
Student: Linda Miao
Course: TCSS 483 - Software Security
Professor: Tom Capaul
Date: February 1, 2026


----- OVERVIEW -----

This assignment implements 12 regular expression validators in Python with comprehensive unit testing.
All regex patterns use Python's 're' module with proper anchoring (^ and $) to ensure exact matches.

Language: Python 3.13
Testing Framework: pytest
Total Tests: 216 (192 base + 24 extra credit)
All tests passed

-----IMPLEMENTATION DECISIONS & GRAY AREAS-----

1. SOCIAL SECURITY NUMBER
   - Accepts: 123-45-6789, 123 45 6789, 123456789
   - Decision: Separators must be CONSISTENT (all dashes, all spaces, or none)
   - Does NOT accept mixed formats like "123-45 6789"
   - EXTRA CREDIT: Validates SSA numbering rules (area ≠ 000/666/900-999, group ≠ 00, serial ≠ 0000)

2. PHONE NUMBER
   - Accepts: (253)123-4567, 253-123-4567, 2531234567, 253 123 4567
   - Decision: Parentheses optional for area code
   - Separators can be dashes or spaces
   - EXTRA CREDIT: Validates against official US area codes (400+ codes including toll-free)

3. EMAIL ADDRESS
   - Basic validation: local@domain.tld
   - Allows: letters, digits, dots, underscores, hyphens in local part
   - Requires: at least 2-character TLD (.com, .org, .edu, etc)
   - Does NOT validate against full RFC 5322 spec (too complex for this assignment)

4. ROSTER NAME
   - Format: Last, First, MI
   - Decision: Allows 0-3 middle initials (as specified)
   - Names must start with capital letters
   - Allows hyphens and apostrophes (for names like O'Brien, Smith-Jones)
   - Middle initials must be capital letters with optional periods

5. DATE VALIDATION
   - Accepts: MM-DD-YYYY or MM/DD/YYYY
   - Decision: Allows 1 or 2 digits for month/day (1-15-2026 or 01-15-2026 both valid)
   - Separators must be consistent (both dashes or both slashes)
   - FULLY validates calendar rules:
     * Months: 1-12
     * Days: appropriate for each month (30/31 days)
     * Leap years: Full algorithm (÷4 except centuries unless ÷400)
   - Uses helper code beyond regex for validation

6. HOUSE ADDRESS
   - Format: Number StreetName Type
   - Accepts: St, Street, Rd, Road, Blvd, Boulevard, Ave, Avenue
   - Decision: Only these 4 street types supported (as specified)
   - Street names can have multiple words with single spaces only
   - Does NOT accept: Dr, Ln, Ct, Pkwy (could add for future enhancement)

7. CITY, STATE, ZIP
   - Format: City, ST ZIP or City, ST ZIP-XXXX
   - State must be 2 uppercase letters
   - City names can have multiple words (New York, San Francisco)
   - Accepts extended ZIP+4 format as optional
   - EXTRA CREDIT: Validates against official 51 state/territory codes (50 states + DC)

8. MILITARY TIME
   - Format: 0000-2359 (4 digits, no colons)
   - Validates: Hours 00-23, Minutes 00-59
   - Leading zeros required (0900, not 900)

9. US CURRENCY
   - Format: $X,XXX,XXX.XX
   - Decision: Commas are OPTIONAL but if used, must be in correct positions
   - Decimal point and 2 cent digits are REQUIRED
   - Accepts: $0.01, $123.45, $1,234.56, $123,456,789.23

10. URL
    - Optional http:// or https:// prefix
    - Accepts upper and lowercase letters
    - Requires valid domain extension (at least 2 characters)
    - Allows subdomains and paths
    - Does NOT validate all possible protocols (ftp, etc)

11. PASSWORD
    - At least 10 characters total
    - Must contain: 1 uppercase, 1 lowercase, 1 digit, 1 punctuation
    - NO MORE than 3 consecutive lowercase letters (most challenging rule)
    - Uses multiple regex checks to validate all requirements

12. WORDS ENDING IN "ION"
    - Must end with "ion"
    - Must have ODD total number of letters
    - Examples: "ion" (3-odd-YES), "union" (5-odd-YES), "action" (6-even-NO)
    - Uses regex for pattern matching plus length check

----- TESTING STRATEGY -----

- Total tests: 216 (16+ per category)
- Base tests: 192 (16 per category × 12 categories)
- Extra credit tests: 24 (8 per extra credit feature × 3 features)
- Each category has at least 8 valid and 8 invalid test cases
- Tests cover edge cases including:
  * Boundary values (min/max lengths)
  * Format variations
  * Invalid separators
  * Missing required components
  * Special characters
  * Empty/malformed inputs
  * Extra credit validation rules

All 216 tests pass successfully.

----- EXTRA CREDIT IMPLEMENTED (6 POINTS TOTAL) -----

1. SSN NUMBERING RULES (2 points)
   Validates Social Security numbers against SSA rules:
   - Area number (first 3 digits): Cannot be 000, 666, or 900-999
   - Group number (middle 2 digits): Cannot be 00
   - Serial number (last 4 digits): Cannot be 0000
   Implementation: Uses regex groups to extract components, then validates with conditional logic
   Tests: 8 additional tests verify these rules

2. OFFICIAL PHONE AREA CODES (2 points)
   Validates against 400+ official US area codes
   - Includes all active area codes as of 2026
   - Includes toll-free numbers (800, 833, 844, 855, 866, 877, 888)
   - Rejects invalid codes like 000, 111, 999
   Implementation: Hardcoded set of valid area codes validated after regex match
   Tests: 8 additional tests verify valid/invalid area codes

3. VALID STATE ABBREVIATIONS (2 points)
   Validates 2-letter state codes against official USPS abbreviations
   - All 50 states plus DC (51 total valid codes)
   - Rejects invalid codes like ZZ, XX, AA
   Implementation: Hardcoded set of valid states validated after regex match
   Tests: 8 additional tests verify state validation

Total Extra Credit Points: 6
Total Project Tests: 216 (192 base + 24 extra credit)

----- KNOWN LIMITATIONS & DESIGN CHOICES ----- 

- Email validation is basic; does not implement full RFC 5322 specification
- URL validation does not check for all valid protocols (only http/https)
- Address validator limited to 4 street types (St, Rd, Blvd, Ave) as specified
- Password validator may be overly strict with consecutive lowercase rule
- Date validator uses helper code (not pure regex) for leap year calculations
- Extra credit implementations use hardcoded lookup sets for validation

----- HOW TO RUN -----

REQUIREMENTS:
- Python 3.7 or higher
- pytest module

INSTALLATION:
pip install pytest

RUN ALL TESTS:
pytest test_regex_validators.py -v

RUN WITH OUTPUT CAPTURE:
pytest test_regex_validators.py -v > test_output.txt

RUN SPECIFIC TEST CATEGORY:
pytest test_regex_validators.py -v -k "military_time"
pytest test_regex_validators.py -v -k "test_ec"(runs only extra credit tests)

----- FILES INCLUDED -----
- regex_validators.py         : All 12 regex validation functions + extra credit
- test_regex_validators.py    : 216 unit tests (192 base + 24 extra credit)
- test_output.txt             : Captured test results showing all 216 tests passing
- README.txt                  : This file (documentation and implementation notes)


