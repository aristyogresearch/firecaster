## “FireCaster”: How Can We Use Data to Predict Domestic Fire Risk and Save Lives ? 

## Problem

Domestic fire incidents remains one of the leading causes of death that threatens human safety and increase the urban vulnerability [1](https://www.usfa.fema.gov/data/statistics/). It is considered as a real burden on economies’ shoulders around the world due to its devastating consequences that can turn a big full of life city into ashes in no time.

To address this problem, we developed `Firecaster`, a predictive analytics system for forecasting and prioritizing Fire Inspections in the city. The system provides insightful recommendations to help fire departments better plan both their fire fighting strategies and their awareness campaigns, and also help insurance companies to deal with damages and less importantly help indoor and outdoor fire prevention and alarm systems to better identify their customers.

# Context: The societal changes and the economical damage brought about by domestic fire incidents 

Domestic fire incidents may not be on everyone’s minds, but they happen more often than we realize. Each year numerous families and even entire communities are affected by fires in the US and all over the world. Over the year’s things have been put in place to lower the amount of fires occurring each year. 

A major domestic fire incident doesn’t only touch the victim. It touches the entire community. Not only can major domestic fire incidents kill and injure, they can destroy communities socially and economically. Take the recent [Fort McMurray fire](http://www.cbc.ca/news/canada/edmonton/fort-mcmurray-wildfire-by-the-numbers-1.3572193) in Alberta, Canada. Almost 1.5 million acres were destroyed and 88,000 people were evacuated. 2,400 homes and businesses were destroyed, making it the costliest natural disaster in that country’s history. The communities affected were paralyzed economically and socially, essentially turning them into temporary wastelands. Moreover, the [US Fire Administration](https://www.usfa.fema.gov/data/statistics/) took comprehensive figures from the year 2013. In that year, there were 1.2 million fires resulting in 3,240 deaths and 15,925 injuries. The overall level of economic loss was $11.5 billion. While these numbers are large, they represent major progress when compared with figures from 2004. The number of fires, since 2004, has dropped by 21.6%. The number of deaths and injuries, since 2004, has also fallen by 21% and 6.6% respectively. And total economic loss is down by 10.1%. The drop has happened due to government awareness campaigns, an increase in the number of fire alarms, and a renewed focus on firefighting over fire prevention. It should also be mentioned that since 1986 the number of firefighters per 1,000 of the population has remained constant [(source)](http://www.nfpa.org/news-and-research/fire-statistics-and-reports/fire-statistics/the-fire-service/administration/us-fire-department-profile).

Despite major increases in population numbers, the size of America’s fire departments has risen at the same rate. This has enabled a constant level of protection over the previous three decades.

But How Does the US Compare to Other Countries?

The number of deaths in 2012 in the United States from fire was 2847, according to the WHO. The only major countries surveyed that had more deaths were Pakistan, China, Russia, and India. Other first world nations had far fewer deaths in 2012. Great Britain, for example, had 335 deaths. France had 488 deaths. Germany had 422 deaths.

However, when population differences are considered, the United States is matching other first world countries in reducing deaths by fire. They have also seen reductions in the number of fires in general. From 2010 to 2014 the United States saw almost a 30,000 decline in the number of annual fires. Great Britain saw about a 90,000 decline in the number of annual fires. France saw about a 60,000 drop in the number of annual fires.

How Much Does the Government and Insurance Companies Spend on Domestic Fire Incidents?

Surprisingly, the average amount lost per property after fire has remained relatively unchanged since 1977.  One study on [fire loss in the United States](http://www.nfpa.org/news-and-research/fire-statistics-and-reports/fire-statistics/fires-in-the-us/overall-fire-problem/fire-loss-in-the-united-states) revealed that in 1977 the average loss was $14,600 and in 2015 it was $20,700. [The United States Fire Administration budget](https://fas.org/sgp/crs/homesec/RS20071.pdf) has declined in recent years, with the 2016 budget being $41.582 million, a 5.6% decrease compared to the previous year. But that’s also coupled with a decrease in the cost of fire prevention equipment. Take [home sprinkler system costs](http://www.nfpa.org/news-and-research/fire-statistics-and-reports/research-reports/suppression/home-fire-sprinklers/home-fire-sprinkler-cost-assessment-final-report) as an example. The cost in 2013 was a mere $1.35 per square foot, compared to $1.61 in 2008.

Actual [spending for fire prevention campaigns](http://www.nbcmontana.com/news/keci/u-s-government-spending-less-on-fire-prevention-more-on-firefighting/9089759) have decreased, whereas firefighting spending has increased. The Hazardous Fuels Reduction Program in Montana was given $500 million in 2012, up from $421 million in 2002, but with inflation this is a decrease. Similar trends have been seen across the country.

According to the [Geneva Association](https://www.genevaassociation.org/media/874729/ga2014-wfs29.pdf), losses for insurers have also been in decline, with (in millions) insurers shelling out 15,500 million in 2008. This number declined to 11,600 million in 2010, bucking the trend of other developed nations, which saw insurer losses remaining steady.

The main tools the government has are raising awareness and designing effective fire fighting strategies. There are no laws regarding any specific fire prevention equipment people must have in their home. It’s not a legal requirement to install a smoke alarm, for example. Identifying and strategically targeting people and places with hight risks of fire is the key component in reducing fire deaths, injuries, and economic loss.

# Solution 

Our project builds on top of a traditional stream of literature in social science that focused on studying the connection between fire incidents in urban zones and socio- demographic factors [1](https://github.com/tzano/firecaster#references)[2](https://github.com/tzano/firecaster#references)[3](https://github.com/tzano/firecaster#references). The early attempts revealed the underlying domestic risk factors that can be considered 
(1) Building conditions: The litterature showed that the age of the building and the materials that are used inside contribute strongly to ingestion of domestic fire accidents.
(2) Demographic and economic characteristics: while the overall demographics of neighborhoods differ from one to another, most of the people inhibiting the same neighborhood share relatively similar income, similar educational level, along with other demographic characteristics as they tend to live the same life style [4](https://github.com/tzano/firecaster#references).  
(3) Weather conditions: we hypothesized that the various weather features, in particular temperature and precipitation, would be a good proxy on the use of heater, AC. Other weather features like snow, wind, rain would commonly reflect some human behavioral attitudes towards staying at home. 

However, cities are highly heterogeneous, and commonly unequal in regards with social behavior of their citizens, and the structure of their architectures among other dimensions. Our capacity to understand and evaluate our methods is bound by availability of contextual relevant data in different cities. To overcome the challenge of accessing to local and real data, our study test the theoretical models using the public data from the city of New York. In this project, we conducted a series of experiments to demonstrate how we collected, filtered and merged different sources of data from open data portals (New York City as a case study) to develop our predictive dashboard.  

## Data 

In this section, we describe each of the datasets that we have used. This project relies on open data sources from the City of New York. All of the data is publicly available, and pulled using the city's open data APIs. The main data sources that we used in the project are the following: 

* [Fire Incident Dataset - FDNY Incidents](https://data.cityofnewyork.us/Public-Safety/Incidents-Responded-to-by-Fire-Companies/tm6d-hbzd): The dataset contains the daily detailed information about fire incidents that are handled by FDNY Fire units. The dataset has been collected using New York Fire Incident Reporting System (NYFIRS), which has been developed by the FDNY to provide data to the National Fire Incident Reporting System (NFIRS). This later is a modular all-incident reporting system designed primarily to understand the nature and causes of fire, as well as civilian fire casualties and fire-fighter injuries. The raw dataset contains 1.33M records spanned between 1st January 2013 and 31th Dec 2015.  This dataset includes information on where and when incidents have occurred, and what resources have been used to mitigate it. The limitation we faced when we used this data source is this later doesn’t provide information on the building location, but the street address. 

* [MapPluto](http://www1.nyc.gov/site/planning/data-maps/open-data/pluto-mappluto-archive.page)  (Primary Land Use Tax Lot Output) is a dataset provided by New York City Department of City Planning (NYCDCP), this dataset has been created by merging the Primary Land Use Tax Lot Output (PLUTO) database and geographic boundaries of tax lot features from the Department of Finance’s Digital Tax Map. It contains geographical features and information on land use, buildings’ age, number of units, and lot size.

* [Census](https://www.census.gov/developers/): The Census’ American Housing Survey is an annual panel conducted by the Census to track highly-specific details about households. As summarized in the literature review, there are some socio-demographic factors that relatively contribute to fire accidents.

* [Street Data](http://gis.ny.gov/gisdata/inventories/details.cfm?DSID=932) a digital vector file of public and private roads and streets of NYC. The dataset is maintained by the state Department of Transportation. 

* [Open Street Map](https://www.openstreetmap.org/) is an open source community project dedicated to mapping the world through community contributions. In order to obtain buildings’ characteristics, we query, filter, and parse OSM API to get relevant information on buildings as well as other geographic features related to roads, buildings, Points Of Interest.

* [Weather Data](https://www.wunderground.com/weather/api/) We obtained New York historical weather information through Weather Wunderground developer API. We collected daily weather summaries for our study period, and selected the following features: temperature, dew point, precipitation amount and type, visibility, wind, fog, pressure and humid-
ity. For some features such as temperature, we obtained more granular data by taking minimum, mean and maximum values. 


# Analysis

In order to study and analyze spatial patterns, we started investigating the different options taking in consideration the ability to analyze distinct spatial units. US Census Bureau has [designed a hierarchically nested spatial units](https://www.census.gov/geo/reference/hierarchy.html,2016.) to overcome any geographical overlap and to easily perform longitudinal analysis. In our study, the spatial granularity is defined based on the census tracts or the urban block. Census tract is a geographic unit used for census on demographic characteristics. It links geographic areas with socio-demographic dataset, to reflect the structure of homogeneous urban form regulated by current zoning ordinances. The urban block is a homogeneous physical territory bounded by streets. Census Blocks are distinct inside Census tracts, according to the 2010 Census, Manhattan is divided into 288 census tracts and 2870 urban blocks based on the PLUTO dataset. The advantage of adopting these spatial units is that both census tract, census blocks are officially used to document social and demographic statistics.

Fig.1 depicts the distribution of domestic fire accidents over time in the city of New York. We observe that there is periodic temporal pattern over the different years. The number of incidents fluctuates across the first three months of the year, indicating accidents may be in infuenced by dynamic temporal factors such as weather. There are also differences when comparing between different incidents distributions at the level of tracts. From the above observations, we decide to include data from other domains such as meteorological information to predict fire incidents. 

![ScreenShot](/docs/images/incidents_timeseries.png)
Fig.1: Number of domestic fire accidents per day 

In what follows, we describe the task of selecting proper feature sets to build our model. Feature engineering is the task of researching and creating features that represent the human’s understanding about the influencing factors of a phenomena. In our project, features are extracted from each individual domains, representing the influencing factors. The set of features are summarized below:

| Feature Type | Feature | Description |
| -------------|---------|-------------|
| Temporal | Day of week| The ordinal number of the day in a week |
| Temporal | Month | The month which the time interval is in |
| Temporal | Holiday | Is this day a holiday or no |
| Spatial | Tract | The administrative tract |
| Meteorological | Weather condition | The index of humidity in a given day |
| Meteorological | Temperature | The temperature in a given day |
| Meteorological | Wind | The orientation and speed of the wind in a given day |
| Meteorological | Humidity | The index of humidity in a given day |
| Meteorological | Snow | The depth of snow in a given day |
| Meteorological | pressure | The level of pressure in a given day |
| Meteorological | precipitation | The level of precipitation in a given day |
| Buildings | avg_yearbuilt | The average age of buildings in a give region | 
| Buildings | total_units  | Total number of units in a give region | 
| Buildings | avg_unitarea | The average unit area in a give region |
| Buildings | ratio_retailarea | Ratio of retail buildings in a give region |  
| Buildings | ratio_comarea |  Ratio of commercial buildings in a give region | 
| Buildings | ratio_resarea |  Ratio of residential buildings in a give region |
| Buildings | ratio_officerea | Ratio of office buildings in a give region | 
| Buildings | avg_numfloors | The average number of floors |
| Buildings | total_bldgarea | Total building area |
| Census | total_population | Total population |
| Census | family_households | family households |
| Census | household_type_by_units_in_structure | household type by units in structure |
| Census | households_income | households income |
| Census | average_household_size_of_occupied_housing_units | average household size of occupied housing units |
| Census | total_housing_units | Total housing units |
| Census | median_number_of_rooms | Median number of rooms |
| Census | median_contract_rent | Median contract rent |
| Census | median_gross_rent | Median gross rent |
| Census | median_household_income | Median household income |
| Census | aggregate_household_income | Aggregated household income |
| Census | owner_occupied_homes_median_value | Owner occupied homes median value |
| Census | value_for_owner_occupied_housing_units | Median value for owner occupied housing units |
| Census | owner_occupied_homes_median_value | Owner occupied homes median value |
| Census | total_vacancies | Total vacancies appartements|
| Census | sold_not_occupied | Sold non-occupied appartements |
| Census | for_rent | Appartements for rent |
| Census | median_age | Media age |
| Census | population_5_and_over | Population ages 5-18 |
| Census | adults_18_to_20 | Population ages 18-20  |
| Census | adults_25_to_64 | Population ages 25-64 |
| Census | adults_25_to_64_with_bachelors_degree | Population ages 25-64 with bechelor degree |
| Census | below_poverty_line | Population below poverty line |
| Census | foreign_born_population | Foreign-born population |
| Census | people_per_household | Number of persons per household |
| Census | built_total | Average of buildings age |
| Census | built_1970s | Number of buildings built on 1970s |
| Census | built_1960s | Number of buildings built on 1960s |
| Census | built_1950s | Number of buildings built on 1950s |
| Census | built_1940s | Number of buildings built on 1940s |
| Census | built_before_1940 | Number of buildings built before 1940s |
| Census | median_household_income | Media household income |
| Census | poverty_level_u100 | Poverty level |



**Results**
We evaluate the performance of our model. We chronologically order the samples and test the model using k-folds cross validation for evaluation to prevent over-fitting. The best performing model with K=3 is summarized in Table 3. 


| Metric | Score   |
|--------|----------|
| Accuracy | 0.890 |
| ROC AUC | 0.902 |
| Recall | 0.890 |
| Precision | 0.880 |
| F1 | 0.883 |

Table.3: The performance of the model 

To evaluate the effectiveness of features, we list the top 10 features with respect to feature importance in Table 5. We used Bagged decision trees like Random Forest and Extra Trees to estimate the importance of features. It can be easily observed that the most contributive features are Meteorological factors that can influence people's behaviour (indoor/outdoor activities). The buildings' conditions contribute strongly to these events.   


|Feature | Score   |
|-------|----------|
| min_temperature | 0.0950 |
| max_temperature | 0.0944 |
| mean_wind_speed | 0.0922 |
| average_units_residential | 0.0849 |
| average_year_built | 0.0501 |
| ratio_residential_area | 0.0482 |
| snow_depth | 0.0165 |
| average_number_floors|  0.0154 |
| total_units | 0.0099 |
| total_building_area | 0.0093 |  

Table 5: The TOP 10 features ranked by score importance

## Dashboard 

To ease the use of our system for further analysis and urban strategy making, we designed and developed a a map-centered system for users to navigate, query and visualize the results of `Firecaster`. Fig. X shows a screen shot of the system. The proposed system has been developed in a modular way, so that components can be updated easily as new technologies and algorithms become available. We use Bootstrap, JS & D3 to build the front-end basic page and Leaflet for map related elements on the page. For the back-end, we use  Flask (a python microframework for web application) to process the requests. A relational database is used to store spatial data and census information for every tract in a standard format. We use PostGis. From the user side, the prototype works as follows. After the user submits the address for a building and the current time, the result of the prediction will appear (see the left) using a color-coded message; Green for safe neighborhood and Red for dangerous neighborhood.  

![ScreenShot](/docs/images/dashboard.png)
Fig.3: FireCaster Dashboard v0.1

## Code Strucutre 

The project is structured in the following components:

* **FireCaster_Model** : Build and validate the model 

- **data_acquisition**: contains scripts to download the data 

- **data_processing**: contains scripts for our process of crawling and transforming the data to a usable format.

- **data_analysis**: contains scripts for supporting tasks carried out throughout the process of building the fire risk model.

* **FireCaster_Dashboard**: Map-centered web application to visualize the results. We run a cron-job to generate scores and read the scores directly from DB.

* **docs**: Documentation & presentation.


## Installation Guide


## Setup

- Install tools

```sh
sh setup/install.sh
```

- Create Postgres/Postgis database

```sh
psql -d postgres

createdb "<DB_NAME>"
psql -d "<DB_NAME>" -c "CREATE EXTENSION postgis"
```

- Init Postgis database
```sh
psql -f ./sql/init_firecaster_db.sql
```

- Create data folders
```sh
sh setup/init_skeleton.sh
```

When you finish setting up the environment, you can use the pipeline. The general framework is the following (1) load data into the database (2) generate features from the data (3) train model (4) evaluate the model performance. 

## Data Aquisition 

- Get New York Open Datasets. You can find the list of all the datasets under `config/data_sources.json`

```sh
sh data_acquisition/get_nyc_data.sh
```
- Get New York Mappluto data

```sh
sh data_acquisition/get_nyc_mappluto.sh
```

## Data pre-processing

Cleaning, processing, and joining the files.
```sh
python main.py -task CONTEXTUAL_DATA_COLLECTION
python main.py -task DATA_CLEANING
```

After processing all the files, you can find all the processed files under `data/processed`


- Data processing & feature engineering
```sh
python main.py -task FEATURE_ENGINEERING
```

- Data Analysis & model selection
```sh
python main.py -task MODEL_SELECTION
```


### Run the Dashboard 

As we have validated our model, we run a cron job (daily) to insert new data to the database, run the same model on the new data, infer the prediction score, update the file and then insert the new values to the database. The dashboard loads the data directly from the database.


- Run Scheduler job (on the server)

```sh
0 6 * * * python main.py -task SCHEDULER
```

- Run the dashaboard

```sh
cd firecaster_dashboard/
python run.py

```

## References:

[1] A. Clark and J. Smith. Experiencing a domestic fire: an overview of key findings from a post incident research programme. Safer Communities, 14(2):95–103, 2015.

[2] A. Clark, J. Smith, and C. Conroy. Domestic fire risk: a narrative review of social science literature and implications for further research. Journal of Risk Research, 18(9):1113–1129, 2015.

[3] L. S. Edelman. Social and economic factors associated with the risk of burn injury. Burns, 33(8):958–965, 2007.

## Team

This project has been developed during an internship at [Snips](https://labs.snips.ai/) on 2014, and it was refactored after that.

The project has been developed by [Tahar](http://twitter.com/T_Zano) & [Lilia](https://twitter.com/lilia_oud).

## Support

If you are having issues, please let us know or submit a pull request.

## License

The project is licensed under the MIT License.
