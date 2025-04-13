import streamlit as st


st.set_page_config(page_title="Unit Converter")
st.title("Unit Converter")


length_units = {
    "Kilometre": 1000,
    "Metre": 1, 
    "Centimetre": 0.01, 
    "Millimetre": 0.001
}

length_calculation = {
    "meterToKilometer": 0.001,
    "meterToCentimeter": 100,
    "meterToMillimeter": 1000,
    "kilometerToMeter": 1000,
    "kilometerToCentimeter": 100000,
    "kilometerToMillimeter": 1000000,
    "centimeterToKilometer": 0.00001,
    "centimeterToMeter": 0.01,
    "centimeterToMillimeter": 10,
    "millimeterToKilometer": 0.000001,
    "millimeterToMeter": 0.001,
    "millimeterToCentimeter": 0.1
}

time_units = {
    "Hour": 3600, 
    "Minute": 60, 
    "Second": 1, 
    "Millisecond": 0.001
    }

time_calculation = {
    "hourToMinute": 60,
    "hourToSecond": 3600,
    "hourToMillisecond": 3600000,
    "minuteToHour": 1 / 60,
    "minuteToSecond": 60,
    "minuteToMillisecond": 60000,
    "secondToHour": 1 / 3600,
    "secondToMinute": 1 / 60,
    "secondToMillisecond": 1000,
    "millisecondToHour": 1 / 3600000,
    "millisecondToMinute": 1 / 60000,
    "millisecondToSecond": 1 / 1000

}

temperature_units = ["Celsius", "Fahrenheit", "Kelvin"]


def convert_temperature(value, from_unit, to_unit):
    
    if from_unit == "Celsius":
        c = value
    elif from_unit == "Fahrenheit":
        c = (value - 32) * 5 / 9
    elif from_unit == "Kelvin":
        c = value - 273.15

    
    if to_unit == "Celsius":
        return c
    elif to_unit == "Fahrenheit":
        return (c * 9 / 5) + 32
    elif to_unit == "Kelvin":
        return c + 273.15


category = st.selectbox("Select Category", ["Length", "Time", "Temperature"])


if category == "Temperature":
    unit_list = temperature_units
    units = None  
else:
    unit_dict = {
        "Length": length_units,
        "Time": time_units
    }
    units = unit_dict[category]
    unit_list = list(units.keys())


col1, col2 = st.columns(2)

with col1:
    from_unit = st.selectbox("From", unit_list, index=0)
    input_value = st.number_input(" ", value=1.0, label_visibility="collapsed", key="input_value")

with col2:
    to_unit = st.selectbox("To", unit_list, index=1)

    
    if from_unit == to_unit:
        result = input_value
        formula_text = "**Formula:** No conversion needed."
    elif category == "Temperature":
        result = convert_temperature(input_value, from_unit, to_unit)

        formula = "Formula"

        if from_unit=="Celsius" and to_unit=="Fahrenheit":
            formula=f"(9/5) {input_value} + 32"

        elif from_unit=="Fahrenheit" and to_unit=="Celsius":
            formula=f"(5/9)( {input_value} - 32 )"

        elif from_unit=="Celsius" and to_unit=="Kelvin":
            formula=f"{input_value} + 273.15"

        elif from_unit=="Kelvin" and to_unit=="Celsius":
            formula=f"{input_value} - 273.15"

        elif from_unit=="Fahrenheit" and to_unit=="Kelvin":
            formula=f"(5/9)( {input_value} - 32 ) + 273.15"

        elif from_unit=="Kelvin" and to_unit=="Fahrenheit":
            formula=f"(9/5) ( {input_value} - 273.15 ) + 32"

        formula_text = f"**Formula : ** Convert {from_unit} → to → {to_unit} using this formula {formula}."
    else:
        formula="formula"
        if category == "Length":
            if from_unit=="Metre" and to_unit == "Kilometre":
                result = input_value * length_calculation["meterToKilometer"]

                formula = f"{input_value} x {length_calculation["meterToKilometer"]}"

            elif from_unit == "Metre" and to_unit == "Centimetre":
                result = input_value * length_calculation["meterToCentimeter"]

                formula = f"{input_value} x {length_calculation["meterToCentimeter"]}"

            elif from_unit == "Metre" and to_unit == "Millimetre":
                result = input_value * length_calculation["meterToMillimeter"]

                formula = f"{input_value} x {length_calculation["meterToMillimeter"]}"

            elif from_unit == "Kilometre" and to_unit == "Metre":
                result = input_value * length_calculation["kilometerToMeter"]

                formula = f"{input_value} x {length_calculation["kilometerToMeter"]}"

            elif from_unit == "Kilometre" and to_unit == "Centimetre":
                result = input_value * length_calculation["kilometerToCentimeter"]

                formula = f"{input_value} x {length_calculation["kilometerToCentimeter"]}"

            elif from_unit == "Kilometre" and to_unit == "Millimetre":
                result = input_value * length_calculation["kilometerToMillimeter"]

                formula = f"{input_value} x {length_calculation["kilometerToMillimeter"]}"

            elif from_unit == "Centimetre" and to_unit == "Kilometre":
                result = input_value * length_calculation["centimeterToKilometer"]

                formula = f"{input_value} x {length_calculation["centimeterToKilometer"]}"

            elif from_unit == "Centimetre" and to_unit == "Metre":
                result = input_value * length_calculation["centimeterToMeter"]

                formula = f"{input_value} x {length_calculation["centimeterToMeter"]}"

            elif from_unit == "Centimetre" and to_unit == "Millimetre":
                result = input_value * length_calculation["centimeterToMillimeter"]

                formula = f"{input_value} x {length_calculation["centimeterToMillimeter"]}"

            elif from_unit == "Millimetre" and to_unit == "Kilometre":
                result = input_value * length_calculation["millimeterToKilometer"]

                formula = f"{input_value} x {length_calculation["millimeterToKilometer"]}"

            elif from_unit == "Millimetre" and to_unit == "Metre":
                result = input_value * length_calculation["millimeterToMeter"]

                formula = f"{input_value} x {length_calculation["millimeterToMeter"]}"

            elif from_unit == "Millimetre" and to_unit == "Centimetre":
                result = input_value * length_calculation["millimeterToCentimeter"]

                formula = f"{input_value} x {length_calculation["millimeterToCentimeter"]}"



        elif category == "Time":
            if from_unit == "Hour" and to_unit == "Minute":
                result = input_value * time_calculation["hourToMinute"]

                formula = f"{input_value} x {time_calculation["hourToMinute"]}"

            elif from_unit == "Hour" and to_unit == "Second":
                result = input_value * time_calculation["hourToSecond"]

                formula = f"{input_value} x {time_calculation["hourToSecond"]}"
            elif from_unit == "Hour" and to_unit == "Millisecond":
                result = input_value * time_calculation["hourToMillisecond"]

                formula = f"{input_value} x {time_calculation["hourToMillisecond"]}"

            elif from_unit == "Minute" and to_unit == "Hour":
                result = input_value * time_calculation["minuteToHour"]

                formula = f"{input_value} x {time_calculation["minuteToHour"]}"

            elif from_unit == "Minute" and to_unit == "Second":
                result = input_value * time_calculation["minuteToSecond"]

                formula = f"{input_value} x {time_calculation["minuteToSecond"]}"

            elif from_unit == "Minute" and to_unit == "Millisecond":
                result = input_value * time_calculation["minuteToMillisecond"]

                formula = f"{input_value} x {time_calculation["minuteToMillisecond"]}"

            elif from_unit == "Second" and to_unit == "Hour":
                result = input_value * time_calculation["secondToHour"]

                formula = f"{input_value} x {time_calculation["secondToHour"]}"

            elif from_unit == "Second" and to_unit == "Minute":
                result = input_value * time_calculation["secondToMinute"]

                formula = f"{input_value} x {time_calculation["secondToMinute"]}"

            elif from_unit == "Second" and to_unit == "Millisecond":
                result = input_value * time_calculation["secondToMillisecond"]

                formula = f"{input_value} x {time_calculation["secondToMillisecond"]}"

            elif from_unit == "Millisecond" and to_unit == "Hour":
                result = input_value * time_calculation["millisecondToHour"]

                formula = f"{input_value} x {time_calculation["millisecondToHour"]}"

            elif from_unit == "Millisecond" and to_unit == "Minute":
                result = input_value * time_calculation["millisecondToMinute"]

                formula = f"{input_value} x {time_calculation["millisecondToMinute"]}"

            elif from_unit == "Millisecond" and to_unit == "Second":
                result = input_value * time_calculation["millisecondToSecond"]

                formula = f"{input_value} x {time_calculation["millisecondToSecond"]}"

        formula_text = f"**Formula : ** Convert {from_unit} → to → {to_unit} using this formula {formula}."
    
    st.number_input(" ", value=result, disabled=True, label_visibility="collapsed", key="result_output")


st.divider()
st.subheader("Formula")
st.markdown(formula_text)
