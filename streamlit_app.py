import streamlit as st
import re

st.title("🎈Furnace Age")
st.write(
    "Select Brand Name and Provide Serial Number and Click on Calculate"
)

decoding_rules = { 
    "Amanda": lambda serial: decode_carrier(serial),
    "Airquest": lambda serial: decode_airquest(serial),
    "Arcoaire": lambda serial: decode_arcoaire(serial),
    "Bard": lambda serial: decode_bard(serial),
    "Bryant": lambda serial: decode_bryant(serial),
    "Buderus": lambda serial: decode_buderus(serial),
    "Carrier": lambda serial: decode_carrier(serial),
    "Chrysler": lambda serial: decode_chrysler(serial),
    "Climatemaster": lambda serial: decode_climatemaster(serial),
    "Coleman": lambda serial: decode_coleman(serial),
    "Comfortmaker": lambda serial: decode_comfortmaker(serial),
    "Daynight": lambda serial: decode_daynight(serial),
    "Ducane": lambda serial: decode_ducane(serial),
    "Enterprise": lambda serial: decode_enterprise(serial),
    "Fedders": lambda serial: decode_fedders(serial),
    "Generalelectric": lambda serial: decode_generalelectric(serial),
    "Goodman": lambda serial: decode_goodman(serial),
    "Heil": lambda serial: decode_heil(serial),
    "Icp": lambda serial: decode_icp(serial),
    "Keeprite": lambda serial: decode_keeprite(serial),
    "Kenmore": lambda serial: decode_kenmore(serial),
    "Lenox": lambda serial: decode_lennox(serial),
    "Peerless": lambda serial: decode_peerless(serial),
    "Airquest": lambda serial: decode_airquest(serial),
                  # Add other brands and their decoding functions here
                  }


brand = st.selectbox("Select Brand", list(decoding_rules.keys()))

serial = st.text_input("Enter Serial Number")

def get_manufacture_year(brand, serial): 
    if brand in decoding_rules: 
        return decoding_rules[brand](serial) 
    else: return


def decode_amana(serial):
    """Decodes the manufacturing year for Amana furnaces."""
    year_codes = {
        'B': 1971, 'L': 1972, 'A': 1973, 'C': 1974, 'K': 1975, 'H': 1976,
        'O': 1977, 'R': 1978, 'S': 1979, 'E': 1980
    }
    try:
        first_char = serial[0].upper()
        if first_char in year_codes:
            year = year_codes[first_char]
            return year if 1970 <= year <= 2010 else None
        else:
            print("Amana year code not found in serial number")
            return None
    except (IndexError, TypeError):
        print("Invalid Amana serial number format")
        return None

def decode_airquest(serial):
    """Decodes the year from the Airquest serial number (International Comfort Products)"""
    try:
        if len(serial) == 10 and serial[0].isalpha() and serial[1:3].isdigit() and serial[3:5].isdigit():
            year = int(serial[1:3])
            return 1900 + year if year < 100 else year
        else:
            print("Invalid serial number format for Airquest")
            return None
    except (IndexError, ValueError):
        print("Invalid Airquest serial number format")
        return None


def decode_arcoaire(serial):
    """Decodes the year from the Arcoaire serial number."""
    try:
        if len(serial) == 10 and serial[0].isalpha() and serial[1:3].isdigit() and serial[3:5].isdigit():
            year = int(serial[1:3])
            return 1900 + year if year < 100 else year
        else:
            print("Invalid serial number format for Arcoaire")
            return None
    except (IndexError, ValueError):
        print("Invalid Arcoaire serial number format")
        return None


def decode_bard(serial):
    """Decodes the year from the Bard serial number."""
    month_codes_1962_1980 = {
        "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6,
        "G": 7, "H": 8, "J": 9, "K": 10, "L": 11, "M": 12
    }
    
    year_codes_1962_1980 = {
        "B": 1962, "C": 1963, "D": 1964, "E": 1965, "F": 1966,
        "G": 1967, "H": 1968, "J": 1969, "K": 1970, "L": 1971,
        "M": 1972, "N": 1973, "O": 1974, "P": 1975, "R": 1976,
        "S": 1977, "T": 1978, "U": 1979, "V": 1980
    }
    
    month_codes_apr_may_1980 = {
        "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6,
        "G": 7, "H": 8, "J": 9, "K": 10, "L": 11, "M": 12
    }
    
    month_codes_june_1980_current = {
        "A": 1, "B": 2, "C": 3, "D": 4,  "F": 5, "H": 6,
         "J": 7, "K": 8, "L": 9, "M": 10, "N": 11, "P": 12
    }
    try:
        # Bard (1962 to March 1980)
        if len(serial) == 8 and serial[:6].isdigit() and serial[6].isalpha() and serial[7].isalpha():
            month_code = serial[6].upper()
            year_code = serial[7].upper()
            if month_code in month_codes_1962_1980 and year_code in year_codes_1962_1980:
                return year_codes_1962_1980[year_code]
        # Bard (April & May 1980)    
        elif len(serial) == 11 and serial[:3].isdigit() and serial[3].isalpha() and serial[4].isalpha():
            if serial[3].upper() in month_codes_apr_may_1980 and serial[4].upper() == "A":
                return 1980
        #Bard(June 1980 to Current)
        elif len(serial) >= 8 and serial[:3].isdigit() and serial[3].isalpha() and serial[4:6].isdigit():
            
            year_part = int(serial[4:6])
            if serial[3].upper() in month_codes_june_1980_current:

                if year_part >= 80 and year_part <=99:
                    return 1900 + year_part
                elif year_part < 24:
                    return 2000 + year_part
                else:
                    print("Invalid year format")
                    return None
        else:
            print("Invalid serial number format for Bard")
            return None
    except (IndexError, ValueError):
        print("Invalid Bard serial number format")
        return None



def decode_bryant(serial):
    """Decodes the year from the Bryant serial number."""
    year_codes_1964_1979 = {
        "R": 1964, "S": 1965, "T": 1966, "U": 1967, "V": 1968,
        "W": 1969, "X": 1970, "Y": 1971, "A": 1972, "B": 1973,
        "C": 1974, "D": 1975, "E": 1976, "F": 1977, "G": 1978, "H": 1979
    }
    try:
        if len(serial) >= 2 and serial[:2].isdigit():
                if len(serial) >= 3 and serial[2].isalpha() and serial[2].upper() in year_codes_1964_1979 :
                    year = year_codes_1964_1979[serial[2].upper()]
                    return year
                
                elif len(serial) >= 4 and serial[:2].isdigit() and serial[-2:].isdigit():
                    year = int(serial[-2:])
                    return 1900 + year if year < 100 else year
        else:
            print("Invalid Bryant Serial number format")
            return None
    except (IndexError, ValueError):
        print("Invalid Bryant serial number format")
        return None

def decode_buderus(serial):
    """Decodes the year from the Buderus serial number."""
    try:
        parts = serial.split("-")
        if len(parts) == 4:
            date_part = parts[2]
            if len(date_part) == 4:
               year_digit = int(date_part[0])
               if year_digit >= 0 and year_digit <= 9:
                    year = 2000 + year_digit
                    return year
        
        elif len(parts) == 5:
            date_part = parts[1]
            if len(date_part) == 5:
                year_digit = int(date_part[0:2])
                if year_digit >= 0 and year_digit <= 99:
                    year = 2000 + year_digit
                    return year
        else:
            print("Invalid Buderus Serial number format")
            return None
    except(IndexError, ValueError):
        print("Invalid Buderus serial number format")
        return None


def decode_carrier(serial):
    """Decodes the year from the Carrier serial number."""
    month_codes = {
            "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6,
            "G": 7, "H": 8, "J": 9, "K": 10, "L": 11, "M": 12
    }
    try:
        if len(serial) >= 4 and serial[0].isalpha() and serial[1].isdigit():
             year = int(serial[1])
             if year >= 0 and year <= 9 and serial[0].upper() in month_codes:
                return 1900 + year if year < 70 else 2000 + year
        
        elif len(serial) >= 6 and serial[:4].isdigit():
              year = int(serial[2:4])
              return 1900 + year if year < 100 else year
        
        else:
            print("Invalid Carrier serial number format")
            return None
    except(IndexError, ValueError):
        print("Invalid Carrier Serial number format")
        return None

def decode_chrysler(serial):
    """Decodes the year from the Chrysler Air Temp serial number."""
    try:
        if len(serial) >= 1 and serial[0].isdigit():
            last_digit = int(serial[0])
            return 1900 + last_digit if last_digit >= 0 and last_digit <= 9 else None
        else:
            print("Invalid Chrysler Serial number format")
            return None
    except (IndexError, ValueError):
        print("Invalid Chrysler serial number format")
        return None

def decode_climatemaster(serial):
    """Decodes the year from the Climate Master serial number."""
    try:
        if len(serial) >= 4 and serial[0:4].isdigit():
             return int(serial[0:4])
        else:
            print("Invalid Climate Master Serial number format")
            return None
    except(IndexError, ValueError):
            print("Invalid Climate Master serial number format")
            return None

def decode_coleman(serial):
    """Decodes the year from the Coleman serial number."""
    try:
        if len(serial) >= 4 and serial[:2].isdigit() and serial[2:4].isdigit():
            month = int(serial[:2])
            year = int(serial[2:4])

            if year >= 70 and month <= 12:
                return 1900 + year
            elif year < 24 and month <=12:
                return 2000 + year
            else:
                print("Invalid Coleman serial number format")
                return None
    except(IndexError, ValueError):
        print("Invalid Coleman serial number format")
        return None

def decode_comfortmaker(serial):
    """Decodes the year from the Comfortmaker serial number."""
    try:
        if len(serial) == 10 and serial[0].isalpha() and serial[1:3].isdigit() and serial[3:5].isdigit():
            year = int(serial[1:3])
            return 1900 + year if year < 100 else year
        else:
           print("Invalid serial number format for Comfortmaker")
           return None
    except (IndexError, ValueError):
        print("Invalid Comfortmaker serial number format")
        return None

def decode_daynight(serial):
     """Decodes the year from the Day-Night serial number."""
     month_codes = {
        "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6,
        "G": 7, "H": 8, "J": 9, "K": 10, "L": 11, "M": 12
     }
     try:
        if len(serial) >= 2 and serial[0].isalpha() and serial[1].isalpha():
             year_code = serial[1].upper()
             if year_code in month_codes:
                return 1970 + month_codes[year_code] -1 
        else:
            print("Invalid Day Night serial number format")
            return None
     except (IndexError, ValueError):
          print("Invalid Day Night serial number format")
          return None

def decode_ducane(serial):
    """Decodes the year from the Ducane serial number."""
    try:
        if len(serial) == 10:
            if serial.isdigit():
                year = int(serial[-4:-2])
                return 1900 + year if year < 100 else year
            elif serial[0:4].isdigit() and serial[4].isalpha() and serial[5:].isdigit():
                year = int(serial[2:4])
                return 1900 + year if year < 100 else year
        else:
            print("Invalid Ducane serial number format")
            return None
    except (IndexError, ValueError):
        print("Invalid Ducane serial number format")
        return None

def decode_enterprise(serial):
     """Decodes the year from the Enterprise Fawcett serial number."""
     year_codes = {
            "A": 1975, "B": 1976, "C": 1977, "D": 1978, "E": 1979,
            "F": 1980, "G": 1981, "H": 1982, "I": 1983, "J": 1984,
            "K": 1985, "L": 1986, "M": 1987, "N": 1988, "O": 1989,
            "P": 1990, "Q": 1991, "R": 1992, "S": 1993, "T": 1994,
            "X": 1998, "Y": 1999, "Z": 2000
      }
     year_codes2 = {
            "A": 2001, "B": 2002, "C": 2003, "D": 2004, "E": 2005,
            "F": 2006, "G": 2007, "H": 2008, "I": 2009, "J": 2010,
            "K": 2011, "L": 2012, "M": 2013, "N": 2014, "O": 2015,
            "P": 2016, "Q": 2017, "R": 2018, "S": 2019, "T": 2020,
             "X": 2024, "Y": 2025, "Z": 2026
     }
     try:
        if len(serial) >= 2 and serial[0].isalpha() and serial[1].isalpha():
             first_letter = serial[1].upper()
             if first_letter in year_codes:
                return year_codes[first_letter]
             elif first_letter in year_codes2:
                return year_codes2[first_letter]
        else:
             print("Invalid Enterprise Serial number format")
             return None
     except(IndexError, ValueError):
          print("Invalid Enterprise Serial number format")
          return None

def decode_fedders(serial):
    """Decodes the year from the Fedders serial number."""
    month_codes = {
        "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6,
           "G": 7, "H": 8, "J": 9, "K": 10, "L": 11, "M": 12
    }
    year_codes = {
            "A":1964,"B":1965,"C":1966,"D":1967, "E":1968, "F":1969, "G":1970,"H":1971,
            "J":1972,"K":1973, "L":1974, "M":1975,"N":1976, "P":1977
          }
    try:
        if len(serial) >= 2 and serial[-2:].isalpha():
            year = serial[-1].upper()
            if serial[-2].upper() in month_codes and year in year_codes:
                return year_codes[year]
        else:
            print("Invalid Fedders Serial number format")
            return None
    except (IndexError, ValueError):
        print("Invalid Fedders Serial number format")
        return None

def decode_generalelectric(serial):
    """Decodes the year from the General Electric serial number."""
    try:
        if len(serial) >= 3 and serial[-3:].isdigit():
            year_digit = int(serial[-3])
            return 1900 + year_digit if year_digit >= 0 and year_digit <= 9 else 2000 + year_digit
        else:
            print("Invalid General Electric Serial number format")
            return None
    except (IndexError, ValueError):
        print("Invalid General Electric Serial number format")
        return None

def decode_goodman(serial):
    """Decodes the year from the Goodman serial number."""
    try:
        if len(serial) >= 4 and serial[:2].isdigit() and serial[2:4].isdigit():
            year = int(serial[:2])
            return 1900 + year if year < 100 else year
        else:
            print("Invalid Goodman Serial number format")
            return None
    except (IndexError, ValueError):
            print("Invalid Goodman serial number format")
            return None

def decode_heil(serial):
     """Decodes the year from the Heil serial number."""
     try:
        if len(serial) == 10 and serial[0].isalpha() and serial[1:3].isdigit() and serial[3:5].isdigit():
            year = int(serial[1:3])
            return 1900 + year if year < 100 else year
        else:
            print("Invalid serial number format for Heil")
            return None
     except (IndexError, ValueError):
        print("Invalid Heil serial number format")
        return None


def decode_icp(serial):
   """Decodes the year from the ICP (International Comfort Products) serial number."""
   try:
        if len(serial) == 10 and serial[0].isalpha() and serial[1:3].isdigit() and serial[3:5].isdigit():
            year = int(serial[1:3])
            return 1900 + year if year < 100 else year
        else:
            print("Invalid serial number format for ICP")
            return None
   except (IndexError, ValueError):
         print("Invalid ICP serial number format")
         return None


def decode_keeprite(serial):
    """Decodes the year from the Keeprite serial number."""
    try:
        if len(serial) == 10 and serial[0].isalpha() and serial[1:3].isdigit() and serial[3:5].isdigit():
            year = int(serial[1:3])
            return 1900 + year if year < 100 else year
        else:
            print("Invalid serial number format for Keeprite")
            return None
    except (IndexError, ValueError):
        print("Invalid Keeprite serial number format")
        return None

def decode_kenmore(serial):
     """Decodes the year from the Kenmore serial number."""
     try:
        if len(serial) == 10 and serial[0].isalpha() and serial[1:3].isdigit() and serial[3:5].isdigit():
            year = int(serial[1:3])
            return 1900 + year if year < 100 else year
        else:
            print("Invalid serial number format for Kenmore")
            return None
     except (IndexError, ValueError):
            print("Invalid Kenmore serial number format")
            return None


def decode_lennox(serial):
      """Decodes the year from the Lennox serial number."""
      print("Lennox serial decoder to be added")
      return None

def decode_peerless(serial):
    """Decodes the year from the Peerless serial number."""
    try:
        match = re.search(r'(\d{4})', serial)
        if match:
            year = int(match.group(1))
            if year >= 1984 and year <= 1999:
                return year
            elif year >= 2000 and year <= 2024:
                match = re.search(r'(\d{6})', serial)
                if match:
                    return int(match.group(1)[:4])
        else:
             print("Invalid Peerless serial number format")
             return None

    except(IndexError, ValueError):
        print("Invalid Peerless serial number format")
        return None


if st.button("Calculate"): 
    result = get_manufacture_year(brand, serial) 
    if result: 
        year = result 
        st.write(f"The heating unit was manufactured in year {year}") 
    else: 
        st.write("Invalid serial number or brand not supported")