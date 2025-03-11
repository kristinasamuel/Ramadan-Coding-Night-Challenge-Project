import streamlit as st

def convert_units(value,unit_from,unit_to):
    """Convert a """
    conversions = {
        "meter_kilometer": 0.001,     #1 meter = 0.001 kilometer
        "kilometer_meter": 1000,      # 1 kilo meter = 1000meter
        "gram_kilogram": 0.001,       #1 gram = 0.001 kilogram
        "kilogram_gram":1000          # 1 kilogram = 1000 gram
    }

    key = f"{unit_from}_{unit_to}"
    if key in conversions:
        conversion = conversions[key]
        return  value * conversion
    else:
        return "Conversion not available"
    

st.title("Unit Converter💡🔄")
st.markdown("""
    Welcome to the **Unit Converter**! 🚀
    Choose your units, enter a value, and hit **Convert** to get the result.
    """, unsafe_allow_html=True)
value = st.number_input("Enter the value to convert 🧮:  ", min_value=1.0,step = 1.0)
unit_from = st.selectbox("Convert From 📏:",["meter","kilometer","gram","kilogram"])
unit_to = st.selectbox("Convert to 🔄:",["meter","kilometer","gram","kilogram"])

if st.button("Convert 🔄"):
    result = convert_units(value,unit_from,unit_to)
    # st.write(f"converted value: {result}")
    st.success(f"Converted value: **{result:.2f}** {unit_to} ✅", icon="🎉")
st.markdown("--------------------------------------")
st.write("Designed with ❤️ by Kristina.© All creations reserved.")
