import pytest
from regex_validators import (
    validate_military_time,
    validate_currency,
    validate_url,
    validate_ssn,
    validate_phone,
    validate_email,
    validate_roster_name,
    validate_address,
    validate_city_state_zip,
    validate_date,
    validate_password,
    validate_ion_words
)

# --- MILITARY TIME TESTS ---
def test_valid_military_time_midnight():
    assert validate_military_time("0000") == True

def test_valid_military_time_noon():
    assert validate_military_time("1200") == True

def test_valid_military_time_morning():
    assert validate_military_time("0900") == True

def test_valid_military_time_afternoon():
    assert validate_military_time("1534") == True

def test_valid_military_time_late_night():
    assert validate_military_time("2359") == True

def test_valid_military_time_early_morning():
    assert validate_military_time("0001") == True

def test_valid_military_time_twenty_three_hundred():
    assert validate_military_time("2300") == True

def test_valid_military_time_ten_hundred():
    assert validate_military_time("1000") == True

def test_invalid_military_time_with_colon():
    assert validate_military_time("12:34") == False

def test_invalid_military_time_hour_24():
    assert validate_military_time("2400") == False

def test_invalid_military_time_hour_25():
    assert validate_military_time("2500") == False

def test_invalid_military_time_minutes_60():
    assert validate_military_time("1260") == False

def test_invalid_military_time_minutes_99():
    assert validate_military_time("1299") == False

def test_invalid_military_time_three_digits():
    assert validate_military_time("123") == False

def test_invalid_military_time_five_digits():
    assert validate_military_time("12345") == False

def test_invalid_military_time_letters():
    assert validate_military_time("12ab") == False


# --- CURRENCY TESTS ---
def test_valid_currency_simple():
    assert validate_currency("$123.45") == True

def test_valid_currency_with_comma():
    assert validate_currency("$1,234.56") == True

def test_valid_currency_large():
    assert validate_currency("$123,456,789.23") == True

def test_valid_currency_single_digit():
    assert validate_currency("$1.00") == True

def test_valid_currency_two_digits():
    assert validate_currency("$99.99") == True

def test_valid_currency_three_digits():
    assert validate_currency("$999.99") == True

def test_valid_currency_pennies():
    assert validate_currency("$0.01") == True

def test_valid_currency_multiple_commas():
    assert validate_currency("$1,234,567.89") == True

def test_invalid_currency_no_dollar_sign():
    assert validate_currency("123.45") == False

def test_invalid_currency_no_cents():
    assert validate_currency("$123") == False

def test_invalid_currency_one_cent_digit():
    assert validate_currency("$123.4") == False

def test_invalid_currency_three_cent_digits():
    assert validate_currency("$123.456") == False

def test_invalid_currency_comma_wrong_position():
    assert validate_currency("$12,34.56") == False

def test_invalid_currency_comma_at_start():
    assert validate_currency("$,123.45") == False

def test_invalid_currency_no_decimal():
    assert validate_currency("$12345") == False

def test_invalid_currency_letters():
    assert validate_currency("$abc.de") == False


# ==================== URL TESTS ====================
def test_valid_url_simple():
    assert validate_url("google.com") == True

def test_valid_url_with_http():
    assert validate_url("http://google.com") == True

def test_valid_url_with_https():
    assert validate_url("https://google.com") == True

def test_valid_url_with_www():
    assert validate_url("www.google.com") == True

def test_valid_url_with_subdomain():
    assert validate_url("mail.google.com") == True

def test_valid_url_with_path():
    assert validate_url("google.com/search") == True

def test_valid_url_complete():
    assert validate_url("https://www.google.com/search") == True

def test_valid_url_two_letter_tld():
    assert validate_url("site.co") == True

def test_invalid_url_no_tld():
    assert validate_url("google") == False

def test_invalid_url_starts_with_dot():
    assert validate_url(".google.com") == False

def test_invalid_url_ends_with_dot():
    assert validate_url("google.com.") == False

def test_invalid_url_double_dot():
    assert validate_url("google..com") == False

def test_invalid_url_space():
    assert validate_url("google .com") == False

def test_invalid_url_only_protocol():
    assert validate_url("https://") == False

def test_invalid_url_wrong_protocol():
    assert validate_url("htp://google.com") == False

def test_invalid_url_one_letter_tld():
    assert validate_url("google.c") == False
    
# --- SSN TESTS ---
def test_valid_ssn_with_dashes():
    assert validate_ssn("123-45-6789") == True

def test_valid_ssn_with_spaces():
    assert validate_ssn("123 45 6789") == True

def test_valid_ssn_no_separators():
    assert validate_ssn("123456789") == True

def test_valid_ssn_zeros():
    assert validate_ssn("000-00-0000") == False

def test_valid_ssn_all_nines():
    assert validate_ssn("999-99-9999") == False

def test_valid_ssn_spaces_no_leading_zeros():
    assert validate_ssn("123 65 4321") == True

def test_valid_ssn_dashes_middle_range():
    assert validate_ssn("555-55-5555") == True

def test_valid_ssn_no_separator_varied():
    assert validate_ssn("246813579") == True

def test_invalid_ssn_too_short():
    assert validate_ssn("12-34-567") == False

def test_invalid_ssn_too_long():
    assert validate_ssn("123-45-67890") == False

def test_invalid_ssn_wrong_grouping():
    assert validate_ssn("12-345-6789") == False

def test_invalid_ssn_mixed_separators():
    assert validate_ssn("123-45 6789") == False

def test_invalid_ssn_letters():
    assert validate_ssn("abc-de-fghi") == False

def test_invalid_ssn_special_chars():
    assert validate_ssn("123@45#6789") == False

def test_invalid_ssn_only_dashes():
    assert validate_ssn("---") == False

def test_invalid_ssn_extra_dash():
    assert validate_ssn("123--45-6789") == False

# --- PHONE TESTS ---
def test_valid_phone_with_parens_dash():
    assert validate_phone("(253)123-4567") == True

def test_valid_phone_all_dashes():
    assert validate_phone("253-123-4567") == True

def test_valid_phone_no_separators():
    assert validate_phone("2531234567") == True

def test_valid_phone_with_spaces():
    assert validate_phone("253 123 4567") == True

def test_valid_phone_parens_space():
    assert validate_phone("(253) 123-4567") == True

def test_valid_phone_parens_no_dash():
    assert validate_phone("(253)1234567") == True

def test_valid_phone_all_zeros():
    assert validate_phone("(000)000-0000") == False

def test_valid_phone_high_numbers():
    assert validate_phone("(253)999-9999") == True

def test_invalid_phone_too_short():
    assert validate_phone("253-123-456") == False

def test_invalid_phone_too_long():
    assert validate_phone("253-123-45678") == False

def test_invalid_phone_missing_closing_paren():
    assert validate_phone("(253123-4567") == False

def test_invalid_phone_wrong_separator():
    assert validate_phone("253.123.4567") == False

def test_invalid_phone_letters():
    assert validate_phone("abc-def-ghij") == False

def test_invalid_phone_only_area_code():
    assert validate_phone("(253)") == False

def test_invalid_phone_mixed_formats():
    assert validate_phone("(253-123-4567") == False

def test_invalid_phone_extra_dash():
    assert validate_phone("253--123-4567") == False

# --- EMAIL TESTS ---
def test_valid_email_simple():
    assert validate_email("linda@uw.edu") == True

def test_valid_email_subdomain():
    assert validate_email("user@mail.google.com") == True

def test_valid_email_with_dot():
    assert validate_email("john.doe@company.com") == True

def test_valid_email_with_underscore():
    assert validate_email("user_name@site.org") == True

def test_valid_email_with_dash():
    assert validate_email("first-last@domain.net") == True

def test_valid_email_numbers():
    assert validate_email("user123@test456.com") == True

def test_valid_email_long_tld():
    assert validate_email("info@example.museum") == True

def test_valid_email_two_letter_tld():
    assert validate_email("contact@site.co") == True

def test_invalid_email_no_at():
    assert validate_email("usermail.com") == False

def test_invalid_email_no_domain():
    assert validate_email("user@") == False

def test_invalid_email_no_tld():
    assert validate_email("user@domain") == False

def test_invalid_email_double_at():
    assert validate_email("user@@domain.com") == False

def test_invalid_email_space():
    assert validate_email("user @domain.com") == False

def test_invalid_email_no_local():
    assert validate_email("@domain.com") == False

def test_invalid_email_one_letter_tld():
    assert validate_email("user@domain.c") == False

def test_invalid_email_special_char():
    assert validate_email("user#name@domain.com") == False

# --- ROSTER NAME TESTS ---
def test_valid_roster_name_no_middle():
    assert validate_roster_name("Smith, John") == True

def test_valid_roster_name_one_initial():
    assert validate_roster_name("Smith, John, L") == True

def test_valid_roster_name_one_initial_with_dot():
    assert validate_roster_name("Smith, John, L.") == True

def test_valid_roster_name_two_initials():
    assert validate_roster_name("Smith, John, A, B") == True

def test_valid_roster_name_three_initials():
    assert validate_roster_name("Smith, John, A, B, C") == True

def test_valid_roster_name_with_hyphen():
    assert validate_roster_name("Smith-Jones, Mary") == True

def test_valid_roster_name_with_apostrophe():
    assert validate_roster_name("O'Brien, Patrick") == True

def test_valid_roster_name_hyphen_and_initial():
    assert validate_roster_name("Smith-Jones, Mary, K") == True

def test_invalid_roster_name_no_comma():
    assert validate_roster_name("Smith John") == False

def test_invalid_roster_name_no_space_after_comma():
    assert validate_roster_name("Smith,John") == False

def test_invalid_roster_name_lowercase_last():
    assert validate_roster_name("smith, John") == False

def test_invalid_roster_name_lowercase_initial():
    assert validate_roster_name("Smith, John, l") == False

def test_invalid_roster_name_four_initials():
    assert validate_roster_name("Smith, John, A, B, C, D") == False

def test_invalid_roster_name_number():
    assert validate_roster_name("Smith2, John") == False

def test_invalid_roster_name_extra_space():
    assert validate_roster_name("Smith,  John") == False

def test_invalid_roster_name_missing_first():
    assert validate_roster_name("Smith, ") == False


# ==================== ADDRESS TESTS ====================
def test_valid_address_street_abbreviated():
    assert validate_address("123 Main St") == True

def test_valid_address_street_full():
    assert validate_address("456 Oak Street") == True

def test_valid_address_road_abbreviated():
    assert validate_address("789 Pacific Rd") == True

def test_valid_address_road_full():
    assert validate_address("101 Sunset Road") == True

def test_valid_address_blvd_abbreviated():
    assert validate_address("202 Hollywood Blvd") == True

def test_valid_address_blvd_full():
    assert validate_address("303 Sunset Boulevard") == True

def test_valid_address_ave_abbreviated():
    assert validate_address("404 Park Ave") == True

def test_valid_address_ave_full():
    assert validate_address("505 Fifth Avenue") == True

def test_invalid_address_no_number():
    assert validate_address("Main Street") == False

def test_invalid_address_no_street_type():
    assert validate_address("123 Main") == False

def test_invalid_address_wrong_type():
    assert validate_address("123 Main Dr") == False

def test_invalid_address_only_number():
    assert validate_address("123") == False

def test_invalid_address_special_char():
    assert validate_address("123 Main St@") == False

def test_invalid_address_no_space():
    assert validate_address("123MainSt") == False

def test_invalid_address_multiple_spaces():
    assert validate_address("123  Main  St") == False

def test_invalid_address_trailing_space():
    assert validate_address("123 Main St ") == False


# --- CITY STATE ZIP TESTS ---
def test_valid_city_state_zip_basic():
    assert validate_city_state_zip("Seattle, WA 98101") == True

def test_valid_city_state_zip_extended():
    assert validate_city_state_zip("Seattle, WA 98101-1234") == True

def test_valid_city_state_zip_two_word_city():
    assert validate_city_state_zip("New York, NY 10001") == True

def test_valid_city_state_zip_three_word_city():
    assert validate_city_state_zip("San Los Angeles, CA 90001") == True

def test_valid_city_state_zip_lacey():
    assert validate_city_state_zip("Lacey, WA 98503") == True

def test_valid_city_state_zip_extended_lacey():
    assert validate_city_state_zip("Lacey, WA 98503-5678") == True

def test_valid_city_state_zip_different_state():
    assert validate_city_state_zip("Portland, OR 97201") == True

def test_valid_city_state_zip_texas():
    assert validate_city_state_zip("Austin, TX 78701") == True

def test_invalid_city_state_zip_no_comma():
    assert validate_city_state_zip("Seattle WA 98101") == False

def test_invalid_city_state_zip_no_space_after_comma():
    assert validate_city_state_zip("Seattle,WA 98101") == False

def test_invalid_city_state_zip_lowercase_state():
    assert validate_city_state_zip("Seattle, wa 98101") == False

def test_invalid_city_state_zip_three_letter_state():
    assert validate_city_state_zip("Seattle, WAS 98101") == False

def test_invalid_city_state_zip_four_digit_zip():
    assert validate_city_state_zip("Seattle, WA 9810") == False

def test_invalid_city_state_zip_six_digit_zip():
    assert validate_city_state_zip("Seattle, WA 981012") == False

def test_invalid_city_state_zip_wrong_extended_format():
    assert validate_city_state_zip("Seattle, WA 98101-12") == False

def test_invalid_city_state_zip_no_space_before_zip():
    assert validate_city_state_zip("Seattle, WA98101") == False


# ==================== DATE TESTS ====================
def test_valid_date_leap_year():
    assert validate_date("02-29-2024") == True

def test_valid_date_christmas():
    assert validate_date("12-25-2025") == True

def test_valid_date_slash_separator():
    assert validate_date("12/25/2025") == True

def test_valid_date_jan_first():
    assert validate_date("01-01-2026") == True

def test_valid_date_dec_last():
    assert validate_date("12-31-2026") == True

def test_valid_date_single_digit_month():
    assert validate_date("1-15-2026") == True

def test_valid_date_single_digit_day():
    assert validate_date("12-1-2026") == True

def test_valid_date_leap_year_2000():
    assert validate_date("02-29-2000") == True

def test_invalid_date_feb_30():
    assert validate_date("02-30-2026") == False

def test_invalid_date_april_31():
    assert validate_date("04-31-2026") == False

def test_invalid_date_leap_year_non_leap():
    assert validate_date("02-29-2026") == False

def test_invalid_date_month_13():
    assert validate_date("13-01-2026") == False

def test_invalid_date_month_0():
    assert validate_date("00-15-2026") == False

def test_invalid_date_day_0():
    assert validate_date("12-00-2026") == False

def test_invalid_date_mixed_separators():
    assert validate_date("12-25/2026") == False

def test_invalid_date_year_1900_not_leap():
    assert validate_date("02-29-1900") == False


# ==================== PASSWORD TESTS ====================
def test_valid_password_basic():
    assert validate_password("Abc123!Def") == True

def test_valid_password_all_requirements():
    assert validate_password("MyP@ssw0rd") == True

def test_valid_password_exactly_three_consecutive():
    assert validate_password("Abcd123!XYZ") == True  

def test_valid_password_mixed_case_digits():
    assert validate_password("TeSt1234!@") == True

def test_valid_password_long():
    assert validate_password("VerySecure1!Pass") == False

def test_valid_password_min_length():
    assert validate_password("Aa1!Bb2Cc3") == True

def test_valid_password_multiple_punctuation():
    assert validate_password("P@ssw0rd!#") == True

def test_valid_password_no_consecutive_lowercase():
    assert validate_password("A1!B2@C3#D") == False

def test_invalid_password_too_short():
    assert validate_password("Short1!") == False

def test_invalid_password_no_uppercase():
    assert validate_password("password123!") == False

def test_invalid_password_no_lowercase():
    assert validate_password("PASSWORD123!") == False

def test_invalid_password_no_digit():
    assert validate_password("Password!@#") == False

def test_invalid_password_no_punctuation():
    assert validate_password("Password123") == False

def test_invalid_password_four_consecutive_lowercase():
    assert validate_password("Pabcd123!") == False

def test_invalid_password_all_lowercase():
    assert validate_password("password1234!") == False

def test_invalid_password_only_nine_chars():
    assert validate_password("Pass123!") == False

# --- ION WORDS TESTS ---
def test_valid_ion_word_ion():
    assert validate_ion_words("ion") == True

def test_valid_ion_word_union():
    assert validate_ion_words("union") == True

def test_valid_ion_word_onion():
    assert validate_ion_words("onion") == True

def test_valid_ion_word_champion_odd():
    assert validate_ion_words("communion") == True  # 9 letters - odd

def test_valid_ion_word_opinion():
    assert validate_ion_words("opinion") == True  # 7 letters - odd

def test_valid_ion_word_lion():
    assert validate_ion_words("lion") == False  # 4 letters - even

def test_valid_ion_word_million():
    assert validate_ion_words("million") == True  # 7 letters - odd

def test_valid_ion_word_pavilion():
    assert validate_ion_words("pavilion") == False  # 8 letters - even

def test_invalid_ion_word_action():
    assert validate_ion_words("action") == False  # 6 letters - even

def test_invalid_ion_word_region():
    assert validate_ion_words("region") == False  # 6 letters - even

def test_invalid_ion_word_nation():
    assert validate_ion_words("nation") == False  # 6 letters - even

def test_invalid_ion_word_passion():
    assert validate_ion_words("passion") == True  # 7 letters... wait that's odd! Let me recalculate: p-a-s-s-i-o-n = 7, should be True

def test_invalid_ion_word_session():
    assert validate_ion_words("session") == True  

def test_invalid_ion_word_not_ending_ion():
    assert validate_ion_words("lions") == False

def test_invalid_ion_word_ions():
    assert validate_ion_words("ions") == False

def test_invalid_ion_word_location():
    assert validate_ion_words("location") == False  # 8 letters - even
    
# --- EXTRA CREDIT: SSN NUMBERING RULES ---
def test_ec_ssn_valid_standard():
    assert validate_ssn("123-45-6789") == True

def test_ec_ssn_invalid_area_000():
    assert validate_ssn("000-45-6789") == False

def test_ec_ssn_invalid_area_666():
    assert validate_ssn("666-45-6789") == False

def test_ec_ssn_invalid_area_900():
    assert validate_ssn("900-45-6789") == False

def test_ec_ssn_invalid_area_999():
    assert validate_ssn("999-99-9999") == False

def test_ec_ssn_invalid_group_00():
    assert validate_ssn("123-00-6789") == False

def test_ec_ssn_invalid_serial_0000():
    assert validate_ssn("123-45-0000") == False

def test_ec_ssn_valid_edge_899():
    assert validate_ssn("899-45-6789") == True

# --- EXTRA CREDIT: PHONE AREA CODES ---
def test_ec_phone_valid_area_code_253():
    assert validate_phone("(253)123-4567") == True

def test_ec_phone_valid_area_code_206():
    assert validate_phone("206-123-4567") == True

def test_ec_phone_valid_area_code_425():
    assert validate_phone("4251234567") == True

def test_ec_phone_invalid_area_code_000():
    assert validate_phone("(000)123-4567") == False

def test_ec_phone_invalid_area_code_111():
    assert validate_phone("111-123-4567") == False

def test_ec_phone_invalid_area_code_999():
    assert validate_phone("(999)123-4567") == False

def test_ec_phone_valid_area_code_212():
    assert validate_phone("212-555-1234") == True

def test_ec_phone_valid_area_code_800():
    assert validate_phone("(800)555-1234") == True

# --- EXTRA CREDIT: STATE ABBREVIATIONS ---
def test_ec_state_valid_wa():
    assert validate_city_state_zip("Seattle, WA 98101") == True

def test_ec_state_valid_ca():
    assert validate_city_state_zip("Los Angeles, CA 90001") == True

def test_ec_state_valid_ny():
    assert validate_city_state_zip("New York, NY 10001") == True

def test_ec_state_valid_dc():
    assert validate_city_state_zip("Washington, DC 20001") == True

def test_ec_state_invalid_zz():
    assert validate_city_state_zip("Nowhere, ZZ 99999") == False

def test_ec_state_invalid_xx():
    assert validate_city_state_zip("Invalid, XX 12345") == False

def test_ec_state_invalid_aa():
    assert validate_city_state_zip("Fake, AA 11111") == False

def test_ec_state_valid_all_50_states():
    # Test a few more states to confirm
    assert validate_city_state_zip("Austin, TX 78701") == True
    assert validate_city_state_zip("Portland, OR 97201") == True