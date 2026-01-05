field_to_snake_case = {
    "Year": "year",
    "Country": "country",
    "Avg Temperature (°C)": "avg_temp_deg_c",
    "CO2 Emissions (Tons/Capita)": "co2_tons_p_capita",
    "Sea Level Rise (mm)": "sea_level_rise_mm",
    "Rainfall (mm)": "rainfall_mm",
    "Population": "population",
    "Renewable Energy (%)": "renewable_energy_%",
    "Extreme Weather Events": "extreme_weather_events",
    "Forest Area (%)": "forest_area_%",
}


def convert_field_name_to_snake_case(csv_field: str) -> str:
    """
    convert_field_name_to_snake_case takes in a field name from the csv file, and
    returns a snake_case version of the name.

    Args:
        csv_field: field name provided in the csv.

    Returns:
        Snake case version of the string.

    Raises:
        KeyError: if csv_field is not present in the string map.

    Example:
        >>> print(convert_field_name_to_snake_case("Avg Temperature (°C)"))
        "avg_temp_deg_c"
    """
    return field_to_snake_case[csv_field]
