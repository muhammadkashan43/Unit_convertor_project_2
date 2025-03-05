import streamlit as st
#funtionality

def Distance_convertor(from_unit,to_unit,value):
    if from_unit == "Miles" and to_unit == "Kilometers":
        return value * 1.60934
    if from_unit == "Miles" and to_unit == "Meters":
        return value * 1609.34
    if from_unit == "Miles" and to_unit == "feet":
        return value * 5280
    if from_unit == "Kilometers" and to_unit == "Miles":
        return value / 1.60934
    if from_unit == "Kilometers" and to_unit == "Meters":
        return value * 1000
    if from_unit == "Kilometers" and to_unit == "feet":
        return value * 3280.84
    if from_unit == "Meters" and to_unit == "Miles":
        return value / 1609.34
    if from_unit == "Meters" and to_unit == "Kilometers":
        return value / 1000
    if from_unit == "Meters" and to_unit == "feet":
        return value * 3.28084
    if from_unit == "feet" and to_unit == "Miles":
        return value / 5280
    if from_unit == "feet" and to_unit == "Kilometers":
        return value / 3280.84
    if from_unit == "feet" and to_unit == "Meters":
        return value / 3.28084

def Length_convertor(from_unit,to_unit,value):
    if from_unit == "Miles" and to_unit == "Kilometers":
        return value * 1.60934
    if from_unit == "Miles" and to_unit == "Meters":
        return value * 1609.34
    if from_unit == "Miles" and to_unit == "feet":
        return value * 5280
    if from_unit == "Kilometers" and to_unit == "Miles":
        return value / 1.60934
    if from_unit == "Kilometers" and to_unit == "Meters":
        return value * 1000
    if from_unit == "Kilometers" and to_unit == "feet":
        return value * 3280.84
    if from_unit == "Meters" and to_unit == "Miles":
        return value / 1609.34
    if from_unit == "Meters" and to_unit == "Kilometers":
        return value / 1000
    if from_unit == "Meters" and to_unit == "feet":
        return value * 3.28084
    if from_unit == "feet" and to_unit == "Miles":
        return value / 5280
    if from_unit == "feet" and to_unit == "Kilometers":
        return value / 3280.84
    if from_unit == "feet" and to_unit == "Meters":
        return value / 3.28084

def Temperature_convertor(from_unit,to_unit,value):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    if from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    if from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    if from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value + 459.67) * 5/9
    if from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    if from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value * 9/5) - 459.67
    
def Weight_convertor(from_unit,to_unit,value):
    if from_unit == "Kilograms" and to_unit == "Pounds":
        return value * 2.20462
    if from_unit == "Kilograms" and to_unit == "Ounces":
        return value * 35.274
    if from_unit == "Kilograms" and to_unit == "Grams":
        return value * 1000
    if from_unit == "Pounds" and to_unit == "Kilograms":
        return value / 2.20462
    if from_unit == "Pounds" and to_unit == "Ounces":
        return value * 16
    if from_unit == "Pounds" and to_unit == "Grams":
        return value * 453.592
    if from_unit == "Ounces" and to_unit == "Kilograms":
        return value / 35.274
    if from_unit == "Ounces" and to_unit == "Pounds":
        return value / 16
    if from_unit == "Ounces" and to_unit == "Grams":
        return value * 28.3495
    if from_unit == "Grams" and to_unit == "Kilograms":
        return value / 1000
    if from_unit == "Grams" and to_unit == "Pounds":
        return value / 453.592
    if from_unit == "Grams" and to_unit == "Ounces":
        return value / 28.3495

def Pressure_convertor(from_unit,to_unit,value):
    if from_unit == "Pascal" and to_unit == "Bar":
        return value / 100000
    if from_unit == "Pascal" and to_unit == "Atmosphere":
        return value / 101325
    if from_unit == "Pascal" and to_unit == "Torr":
        return value / 133.322
    if from_unit == "Bar" and to_unit == "Pascal":
        return value * 100000
    if from_unit == "Bar" and to_unit == "Atmosphere":
        return value / 1.01325
    if from_unit == "Bar" and to_unit == "Torr":
        return value * 750.062
    if from_unit == "Atmosphere" and to_unit == "Pascal":
        return value * 101325
    if from_unit == "Atmosphere" and to_unit == "Bar":
        return value * 1.01325
    if from_unit == "Atmosphere" and to_unit == "Torr":
        return value * 760
    if from_unit == "Torr" and to_unit == "Pascal":
        return value * 133.322
    if from_unit == "Torr" and to_unit == "Bar":
        return value / 750.062
    if from_unit == "Torr" and to_unit == "Atmosphere":
        return value / 760


st.write("# Unit Convertor")

category = st.selectbox("Select category", ["Distance","Temperature", "Weight","Pressure"])

if category == "Distance":
    from_unit = st.selectbox("From", ["Miles", "Kilometers", "Meters", "feet"])
    to_unit = st.selectbox("To", ["Miles", "Kilometers", "Meters", "feet"])
    value = st.number_input("Enter value")
    if st.button("Convert"):
        Distance_convertor(from_unit,to_unit,value)
        st.success(f"{value} {from_unit} is equal to {Distance_convertor(from_unit,to_unit,value)} {to_unit}")

elif category == "Temperature":
    from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])
    value = st.number_input("Enter value")
    if st.button("Convert"):
        Temperature_convertor(from_unit,to_unit,value)
        st.success(f"{value} {from_unit} is equal to {Temperature_convertor(from_unit,to_unit,value)} {to_unit}")

elif category == "Weight":
    from_unit = st.selectbox("From", ["Kilograms", "Pounds", "Ounces", "Grams"])
    to_unit = st.selectbox("To", ["Kilograms", "Pounds", "Ounces", "Grams"])
    value = st.number_input("Enter value")
    if st.button("Convert"):
        Weight_convertor(from_unit,to_unit,value)
        st.success(f"{value} {from_unit} is equal to {Weight_convertor(from_unit,to_unit,value)} {to_unit}")

elif category == "Pressure":
    from_unit = st.selectbox("From", ["Pascal", "Bar", "Atmosphere", "Torr"])
    to_unit = st.selectbox("To", ["Pascal", "Bar", "Atmosphere", "Torr"])
    value = st.number_input("Enter value")
    if st.button("Convert"):
        Pressure_convertor(from_unit,to_unit,value)
        st.success(f"{value} {from_unit} is equal to {Pressure_convertor(from_unit,to_unit,value)} {to_unit}")
