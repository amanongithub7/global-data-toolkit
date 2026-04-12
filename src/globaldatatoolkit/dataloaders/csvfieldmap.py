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


def convert_csv_field_name_to_snake_case(csv_field: str) -> str:
    """convert csv column headings to snake_case.
    convert_field_name_to_snake_case takes in a column heading from the csv file, and
    returns a snake_case version of the name.

    Parameters
    ----------
    csv_field: str
        field name provided in the csv.

    Returns
    -------
    String in snake_case.

    Raises
    ------
    KeyError if csv_field is not present in the string map.

    Example
    -------
    >>> print(convert_field_name_to_snake_case("Avg Temperature (°C)"))
    "avg_temp_deg_c"
    """
    return field_to_snake_case[csv_field]
