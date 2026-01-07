# Global Climate Change Indicators (2000-2024)

Source:
[Environmental Trends Dataset from OpenML](https://www.openml.org/search?type=data&sort=qualities.NumberOfInstances&status=active&id=46731)

## Description

This dataset provides a comprehensive overview of key climate change indicators
collected across different countries from the year 2000 to 2024. It includes
1000 data points capturing various environmental and socio-economic factors that
reflect the global impact of climate change. The dataset focuses on average
temperature, CO2 emissions, sea-level rise, rainfall patterns, and more,
enabling users to analyze trends, correlations, and anomalies.

Summary provided by
[Bhadra Mohit on Kaggle](https://www.kaggle.com/datasets/bhadramohit/climate-change-dataset).

### Fields Explanation

#### Year

The year in which the data was recorded, ranging from 2000 to 2024.

#### Country

The country or region where the climate data was collected. The dataset includes
a diverse set of countries from across the globe, representing different
geographic regions and climates.

#### Average Temperature (°C)

The average annual temperature recorded in each country, measured in degrees
Celsius. This field allows for comparisons of temperature changes across regions
and time.

#### CO2 Emissions (Metric Tons per Capita)

The average amount of CO2 emissions per capita in metric tons, reflecting the
country's contribution to greenhouse gases. This field is useful for analyzing
the link between human activity and environmental changes.

#### Sea Level Rise (mm)

The recorded annual sea-level rise in millimeters for coastal regions. This
indicator reflects the global warming effect on melting glaciers and thermal
expansion of seawater, critical for studying impacts on coastal populations.

#### Rainfall (mm)

The total annual rainfall recorded in millimeters. This field highlights
changing precipitation patterns, essential for understanding droughts, floods,
and water resource management.

#### Population

The population of the country in the given year. Population data is important to
normalize emissions or other per-capita analyses and understand human impact on
the environment.

#### Renewable Energy (%)

The percentage of total energy consumption in a country that comes from
renewable energy sources (solar, wind, hydro, etc.). This metric is vital for
assessing the progress made toward sustainable energy and reducing reliance on
fossil fuels.

#### Extreme Weather Events

The number of extreme weather events recorded in each country, such as
hurricanes, floods, wildfires, and droughts. Tracking these events helps
correlate the increase in climate change with the frequency of natural
disasters.

#### Forest Area (%)

The percentage of the total land area of a country covered by forests. Forest
cover is a critical indicator of biodiversity and carbon sequestration, with
reductions often linked to deforestation and habitat loss.

## Preliminary Data Questions & Observations

### Precise location and time of measurements unknown

The dataset doesn't contain any information to indicate the exact geolocation
each data point was taken from, nor what time the data was recorded at.

Several questions are raised:

- Q: Are data points averages for a region/country in a particular year?
- Q: Or are they raw observations recorded from arbitrary locations and at
  arbitrary times, potentially multiple times a year?

The existence of fields such as "Forest Area (%)" and "Renewable Energy (%)"
implies that data points _might_ be regional averages. However, that remains to
be determined.

- Q: If there exist multiple data points for a region/country for the same year,
  what does that imply?

## Applications

### Climate Research

This dataset is invaluable for researchers and analysts studying global climate
trends. By focusing on multiple indicators, users can assess the relationships
between temperature changes, emissions, deforestation, and extreme weather
patterns.

### Environmental Policy Making

Governments and policy analysts can use this dataset to develop more effective
climate policies based on historical and regional data. For example, countries
can use emissions data to set realistic reduction goals in line with
international agreements.

### Renewable Energy Studies

Renewable energy data provides insights into how different regions are
transitioning toward greener energy sources, offering a comparison between
high-emission and low-emission countries.

### Predictive Modeling

The data can be used for machine learning models to predict future climate
scenarios, especially in relation to global temperature rise, sea-level changes,
and extreme weather events.

### Public Awareness & Education

This dataset is a useful educational tool for raising awareness about the
impacts of climate change. Students and the general public can use it to explore
real-world data and learn about the importance of sustainable development.
