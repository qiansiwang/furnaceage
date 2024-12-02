import streamlit as st

st.title("🎈Furnace Age")
st.write(
    "Select Brand Name and Provide Serial Number and Click on Calculate"
)

decoding_rules = { "Carrier": lambda serial: decode_carrier(serial), 
                  # Add other brands and their decoding functions here
                  }


brand = st.selectbox("Select Brand", list(decoding_rules.keys()))

serial = st.text_input("Enter Serial Number")

def get_manufacture_year(brand, serial): 
    if brand in decoding_rules: 
        return decoding_rules[brand](serial) 
    else: return


def decode_carrier(serial):
    # Example decoding logic for Carrier 
    if len(serial) == 10:
        year = int(serial[0:2])
        week = int(serial[2:4]) 
        if year < 50:
            year += 2000 
        else:
            year += 1900
        return year, week
    # Add more decoding logic based on different serial number formats 
    return None


if st.button("Calculate"): 
    result = get_manufacture_year(brand, serial) 
    if result: 
        year, week = result 
        st.write(f"The heating unit was manufactured in year {year}, week {week}") 
    else: 
        st.write("Invalid serial number or brand not supported")