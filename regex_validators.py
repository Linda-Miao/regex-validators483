import re
# --- EXTRA CREDIT DATA ---

# Valid US state abbreviations (50 states + DC)
VALID_STATES = {
    'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
    'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD',
    'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
    'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
    'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY', 'DC'
}

# Valid US area codes (as of 2026)
VALID_AREA_CODES = {
    '201', '202', '203', '204', '205', '206', '207', '208', '209', '210',
    '212', '213', '214', '215', '216', '217', '218', '219', '220', '223',
    '224', '225', '226', '228', '229', '231', '234', '236', '239', '240',
    '242', '246', '248', '250', '251', '252', '253', '254', '256', '260',
    '262', '263', '264', '267', '268', '269', '270', '272', '274', '276',
    '279', '281', '283', '284', '289', '301', '302', '303', '304', '305',
    '306', '307', '308', '309', '310', '312', '313', '314', '315', '316',
    '317', '318', '319', '320', '321', '323', '325', '326', '327', '330',
    '331', '332', '334', '336', '337', '339', '340', '341', '343', '345',
    '346', '347', '351', '352', '360', '361', '364', '365', '367', '380',
    '385', '386', '401', '402', '403', '404', '405', '406', '407', '408',
    '409', '410', '412', '413', '414', '415', '416', '417', '418', '419',
    '423', '424', '425', '430', '431', '432', '434', '435', '437', '438',
    '440', '442', '443', '445', '447', '448', '450', '456', '458', '463',
    '464', '469', '470', '472', '473', '474', '475', '478', '479', '480',
    '484', '501', '502', '503', '504', '505', '506', '507', '508', '509',
    '510', '512', '513', '514', '515', '516', '517', '518', '519', '520',
    '530', '531', '534', '539', '540', '541', '548', '551', '559', '561',
    '562', '563', '564', '567', '570', '571', '572', '573', '574', '575',
    '579', '580', '581', '585', '586', '587', '601', '602', '603', '604',
    '605', '606', '607', '608', '609', '610', '612', '613', '614', '615',
    '616', '617', '618', '619', '620', '623', '626', '628', '629', '630',
    '631', '636', '639', '640', '641', '646', '647', '650', '651', '657',
    '659', '660', '661', '662', '667', '669', '670', '671', '672', '678',
    '680', '681', '682', '684', '689', '701', '702', '703', '704', '705',
    '706', '707', '708', '709', '712', '713', '714', '715', '716', '717',
    '718', '719', '720', '721', '724', '725', '726', '727', '731', '732',
    '734', '737', '740', '743', '747', '754', '757', '760', '762', '763',
    '764', '765', '769', '770', '772', '773', '774', '775', '778', '779',
    '780', '781', '782', '784', '785', '786', '787', 
    '800', '801', '802', '803',  # ADDED 800 HERE
    '804', '805', '806', '808', '810', '812', '813', '814', '815', '816',
    '817', '818', '819', '820', '825', '826', '828', '830', '831', '832',
    '833',  # ADDED toll-free
    '838', '839', '840', '843', '844', '845', '847', '848', '849', '850',  # ADDED 844
    '854', '855', '856', '857', '858', '859', '860', '862', '863', '864',  # ADDED 855
    '865', '866', '867', '870', '872', '873', '876', '877', '878',  # ADDED 866, 877
    '888',  # ADDED toll-free
    '901', '903', '904', '905', '906',
    '907', '908', '909', '910', '912', '913', '914', '915', '916', '917',
    '918', '919', '920', '925', '928', '929', '930', '931', '934', '936',
    '937', '938', '939', '940', '941', '945', '947', '949', '951', '952',
    '954', '956', '959', '970', '971', '972', '973', '975', '978', '979',
    '980', '984', '985', '986', '989'
}
def validate_military_time(text):
    """
    Validates military time format: 0000-2359
    - No colons
    - Leading zero for times under 10
    - Valid hours: 00-23
    - Valid minutes: 00-59
    """
    pattern = r'^([01]\d|2[0-3])([0-5]\d)$'
    return bool(re.match(pattern, text))

def validate_currency(text):
    """
    Validates US currency format: $X,XXX,XXX.XX
    - Must start with $
    - Commas optional 
    - Must have decimal and cents
    """
    pattern = r'^\$\d{1,3}(,\d{3})*\.\d{2}$'
    return bool(re.match(pattern, text))

def validate_url(text):
    """
    Validates URL format
    - Optional http:// or https://
    - Domain name with optional subdomains
    - Optional path
    """
    pattern = r'^(https?://)?[a-zA-Z0-9]([a-zA-Z0-9\-]*[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9\-]*[a-zA-Z0-9])?)*(\.[a-zA-Z]{2,})(\/.*)?$'
    return bool(re.match(pattern, text))

def validate_ssn(text):
    """
    Social Security Number validation (WITH EXTRA CREDIT)
    - Accepts: 123-45-6789, 123 45 6789, 123456789
    - Validates SSA numbering rules:
      * Area number (first 3): Cannot be 000, 666, or 900-999
      * Group number (middle 2): Cannot be 00
      * Serial number (last 4): Cannot be 0000
    """
    # Pattern: must use same separator throughout OR no separators
    pattern1 = r'^(\d{3})-(\d{2})-(\d{4})$'  # All dashes
    pattern2 = r'^(\d{3}) (\d{2}) (\d{4})$'  # All spaces
    pattern3 = r'^(\d{3})(\d{2})(\d{4})$'    # No separators
    
    match = re.match(pattern1, text) or re.match(pattern2, text) or re.match(pattern3, text)
    
    if not match:
        return False

    # EXTRA CREDIT: Validate SSA rules
    area = int(match.group(1))
    group = int(match.group(2))
    serial = int(match.group(3))
    
    # Area cannot be 000, 666, or 900-999
    if area == 0 or area == 666 or area >= 900:
        return False
    
    # Group cannot be 00
    if group == 0:
        return False
    
    # Serial cannot be 0000
    if serial == 0:
        return False
    
    return True

def validate_phone(text):
    """
    US Phone number validation (WITH EXTRA CREDIT)
    - Accepts: (253)123-4567, 253-123-4567, 2531234567, 253 123 4567
    - Validates official US area codes
    """
    # Pattern: optional (XXX) or XXX, then XXX, then XXXX with optional separators
    pattern = r'^(\((\d{3})\)|(\d{3}))[\s-]?\d{3}[\s-]?\d{4}$'
    match = re.match(pattern, text)
    
    if not match:
        return False
    
    # EXTRA CREDIT: Validate area code
    # Group 2 is area code with parens, Group 3 is without
    area_code = match.group(2) if match.group(2) else match.group(3)
    
    if area_code not in VALID_AREA_CODES:
        return False
    
    return True

def validate_email(text):
    """
    Email address validation
    Basic format: local@domain.tld
    - Local part: letters, digits, dots, hyphens, underscores
    - Must have @ symbol
    - Domain: letters, digits, hyphens
    - Must have valid TLD (.com, .org, etc - at least 2 chars)
    """
    pattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, text))
def validate_roster_name(text):
    """
    Name on class roster: Last, First, MI
    - Names must start with capital letter
    - Last name and first name required
    - Middle initials (0-3) are capital letters with optional dots
    """
    # Pattern: Capitalized last, Capitalized first, optional MI
    pattern = r"^[A-Z][A-Za-z\-']*,\s[A-Z][A-Za-z\-']*(?:,\s[A-Z]\.?){0,3}$"
    return bool(re.match(pattern, text))

def validate_address(text):
    """
    House address validation
    - Single spaces only between parts
    """
    # Pattern: number + single space + street name + single space + street type
    street_types = r'(?:St(?:reet)?|Rd|Road|Blvd|Boulevard|Ave(?:nue)?)'
    pattern = rf'^\d+\s[A-Za-z]+(\s[A-Za-z]+)*\s{street_types}$'
    return bool(re.match(pattern, text))

def validate_city_state_zip(text):
    """
    City, State, Zip format (WITH EXTRA CREDIT)
    - Format: Seattle, WA 98101 OR Seattle, WA 98101-1234
    - Validates official 2-letter state abbreviations
    """
    # Pattern: City, ST ZIP or City, ST ZIP-XXXX
    pattern = r'^[A-Za-z\s]+,\s([A-Z]{2})\s\d{5}(?:-\d{4})?$'
    match = re.match(pattern, text)
    
    if not match:
        return False
    
    # EXTRA CREDIT: Validate state abbreviation
    state = match.group(1)
    
    if state not in VALID_STATES:
        return False
    
    return True
def validate_date(text):
    """
    Date in MM-DD-YYYY format with validation
    - Separators can be dashes or slashes
    - Must validate actual dates (no Feb 30, no April 31)
    - Must handle leap years correctly
    """
    import re
    
    # Pattern: MM separator DD separator YYYY
    pattern = r'^(\d{1,2})([-/])(\d{1,2})\2(\d{4})$'
    match = re.match(pattern, text)
    
    if not match:
        return False
    
    month, sep, day, year = match.groups()
    month = int(month)
    day = int(day)
    year = int(year)
    
    # Validate month
    if month < 1 or month > 12:
        return False
    
    # Days per month
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Check for leap year
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    if is_leap:
        days_in_month[1] = 29  # February has 29 days in leap year
    
    # Validate day
    if day < 1 or day > days_in_month[month - 1]:
        return False
    
    return True

def validate_password(text):
    """
    Password validation with complex rules:
    - At least 10 characters
    - At least 1 uppercase letter
    - At least 1 lowercase letter
    - At least 1 digit
    - At least 1 punctuation mark
    - No more than 3 consecutive lowercase characters
    """
    import re
    
    # Check length
    if len(text) < 10:
        return False
    
    # Check for at least one uppercase
    if not re.search(r'[A-Z]', text):
        return False
    
    # Check for at least one lowercase
    if not re.search(r'[a-z]', text):
        return False
    
    # Check for at least one digit
    if not re.search(r'\d', text):
        return False
    
    # Check for at least one punctuation
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', text):
        return False
    
    # Check for NO MORE than 3 consecutive lowercase letters
    if re.search(r'[a-z]{4,}', text):
        return False  # Found 4 or more consecutive lowercase
    
    return True

def validate_ion_words(text):
    """
    Words with odd number of alphabetic characters ending in 'ion'
    - Must end with 'ion' (3 letters)
    - Total length must be odd
    - Examples: "ion" (3 letters - odd), "action" (6 letters - even, NO), 
                "region" (6 letters - even, NO), "union" (5 letters - odd, YES)
    """
    # Pattern: word characters ending in 'ion'
    pattern = r'^[a-zA-Z]*ion$'
    
    if not re.match(pattern, text):
        return False
    
    # Check if total length is odd
    if len(text) % 2 == 1:  # Odd length
        return True
    
    return False