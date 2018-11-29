# The Tale of Bikesharing in the United States

In this project we look at bikeshare data from bikeshare companies in
Boston (Hubway) and New York City (Citi Bikes). As bikesharing services
begin to roll out in many US cities, bike sharing is becoming a more
sustainable option for commuters. Or is it?? With the rise of
bikesharing services all across the United States, we decided that 2018
was a good time to look at the publicly available bikesharing data.

In the repository, we (Swopnil and Giang) have taken around 7 million
rides from publicly available data in both New York City and Boston and distributed our analysis into
many parts. Below is how we have documented the process of our data
analysis. This analysis will be divided into five parts.

## Overview of the Data

We began by combining the datasets from Boston and New York. We took the most relevant features and added them to our dataframes and wrote Python scripts to collect, combine and feature scale the information. The datasets included the following features:

1. Duration - time each bike was checked out for
1. Start time - the date and time that the bike was checked out
1. End time - the date and time that the bike was checked back in
1. Start longitude, Start latitude - the geographical coordinates of the station the bike was checked out from 
2. End longitude, End latitude - the geographical coordinates of the station the bike was checked back into
4. User Type - Whether the bike user was a registered user or one time user
5. Birth Year - Birth year of the user (some values were missing)
6. Gender - Male, Female, or Unknown

After making the dataset, we looked at the fundamental information of the dataset using Python Data Visulalization tools like `pandas` and `matplotlib`. 

### Distribution of Gender

![Riders by genders](images/1/distribution_by_gender_nyc.png) ![Riders by the hour](images/1/distribution_by_gender_bos.png)

Looking at the data, there was an immediate observation about the gender distribution of bikeshare riders. It was that women were using bikeshare services way less than men. In New York City, the ratio of men to women was 70% to 30% whereas in Boston, this ratio was close to 80% to 20%. In either case, men were three or four times more likely to use bikeshare services. 

As to why women don't ride bicycles as much as men, there have been many theories including factors such as percieved safety mentioned in [this article by FiveThirtyEight](https://fivethirtyeight.com/features/why-women-dont-cycle/), and the data holds true to its claim. 

### Distribution of Trip Duration

![Riders by the hour](images/1/general_ny_duration_distribution_nyc.png) ![Riders by the hour](images/1/general_boston_duration_distribution_bos.png)

In regards to the duration of the rides, people in Boston were much more likely to have checked out the bikes for a longer time. While the range of duration time in New York is from 0 to 70 minutes, that in Boston is from 0 - 9000 minutes (about 6 days).

Since Citi Bikes puts a restriction of 30 minutes on bicycle checkout, most of the rides in New York were under 30 minutes. 

However in Boston, people checked the bikes out for a much longer period as there was a longer checkout period for the bikes. Hence a lot of people even checked out the bikes for 5 days. We then wonder about the special case with trips from Station A all the way to Station A. We find out that the percentages of same station trips in New York and Boston are 2.5 % (13,707 trips out of 5,562,321 total trips ) and 4.8% (76, 311 trips out of 1,579,025 total trips). 

#### Members and Nonmembers

We then continued to do some distribution of trip duration by the user type (member, and non-member). Here below are the histograms of New York and Boston's trip durations by the user types. We can easily observe that the number of members and non-member in New York is quite the same while most of riders in Boston is non-member.


![Distribution of trip duration by user type](images/1/duration_distribution_by_usertype_nyc.png)  ![Distribution of trip duration by user type](images/1/boston_duration_distribution_by_usertype_bos.png)

#### Accidental Checkouts 

For Citibike, the first 30 minutes of each ride are included in the price of the pass, and you can take as many rides as you want while your pass is active. If you keep a bike out for more than 30 minutes at a time, it’s an extra $4 per additional 15 minutes. Therefore, we will look up for the distribution of trip duration less than 30 minutes:


![Distribution of trip duration < 30 in NY](images/1/nyc_duration_distribution_<30nyc.png) ![Distribution of trip duration < 30 in Boston](images/1/boston_duration_distribution_<30_bos.png)

We notice that lots of trip durations are less than 3 minutes. We can regard less than three-minute trip duration is the accidental checkout. Therefore, the number of accidentals checkouts in New York and Boston are 32668 and 4751 respectively. Here are the distribution of duration trips < 30 minutes of two cities after dropping all the accidental checkouts:


![Distribution of trip duration < 30 without accidental checkouts](images/1/ny_duration_distribution_without_accidentalcheckouts_nyc.png) ![Distribution of trip duration < 30 without accidental checkouts](images/1/boston_duration_distribution_without_accidentalcheckouts_bos.png)

We can observe that the graphs with and without accidental checkouts are not different a lot. Therefore, we can conclude that the number of accidental checkouts doesn't affect the model of two datasets a lot.

### Distribution by Age
The next question is "How does bikeshare service usage differ by age?". Taking a closer look at the main data. We can see that the distribution of age is skewed to the right. The majority of the users are between their 30s-50s. A reason for the use of bicycles for the current demographic could be 2 reasons in my opinion: 1. As people earn more, they stray away from bicycles. Hence people with higher median earnings (who generally tend to be older, could use other means of transportation) 2. While the bicycles are cheaper than taxis and ride hailing apps, they are more expensive than the metro in NYC or Boston. Demographics with a lower income, generally 20 year olds or older could use the metro otherwise.


![Users by age](images/1/duration_distribution_by_age_nyc.png) ![Users by age](images/1/duration_distribution_by_age_bos.png) !![Users by age](images/1/duration_distribution_by_age_all.png)


## What Happens in a Day

### In a day

In one day in a city like Boston or New York City, a lot of activity takes place in different areas of towns. In essence, the data is also a reflection of what New Yorkers or people in Boston live their lives. 

Looking at activity by time of day, we can see that even during late nights some New Yorkers are still active on their bicycles. 

![NYC by day](images/2/riders_by_hour_nyc.png)

In the midst of dusk and dawn around 3 am is the lowest bicycle traffic. The distribution is bimodal containing two peaks representing the two times that New Yorkers rush in and our of work; these take place around 8am and between 5-7pm. 

The higher peak in the evening hours could also have been affected by more tourists choosing to ride the bicycles or more people biking around for recreation. 

![BOS by day](images/2/riders_by_hour_bos.png)

Boston also follows a similar peak where the traffic drops drastically around 8pm until around 7am when it rises back to a peak and drops for the midday until around mega rush hour. 

The similarity of these peaks tells us that the location (in this case New York City or Boston) does not that that much effect on the bike riding trend. 

In fact, if we combine both plots we almost get the same plot again. 

![All by day](images/2/riders_by_hour_all.png)

### By day of the year

if we look at riders by the day of the week, the data adds a clear picture of the seasonal cycling trends in both cities. People tend to go out during the summer and spring month and enjoy the sun and the weather whereas stay indoors specially in the snowy northeast. 

This trend is reflected by the annual trends. 

![Nyc by year](images/2/riders_by_month_nyc.png)

In New York City, there is almost no traffic in the months of January and February, whereas as the seasons pass, fall has the highest traffic. This could also be directly related to weather trends. 

![Bos by year](images/2/riders_by_month_bos.png)

Boston contains a similar picture. Sometimes even the services close down during deep snow winter months in the cities so there is hardly any usage data for the rides during this time. Even Boston usage peaks around September and late August before the fall. 

## Looking from Above

### New York City

If we look into the availability of stations we can see that almost all of the stations in New York city are in Manhattan. While Manhattan has over 300 statations, Brooklyn has less than 20 combined. Queens, Staten Island and the Bronx don't even have a bikeshare station.

__Cluster location of stations__
[*Click to view projection*
![Bos by year](images/3/nyc_cluster.png)](images/3/nyc_bikeshare_stops_cluster.html)

Amongst those in availability in NYC, most of the density of usage takes place in midtown and downtown Manhattan. This makes sense as midtown consists of a lot of major businesses and tourist sites whereas downtown consists of areas such a Chinatown and Wall Street which is also a hub for greater traffic. 

This density map matches directly in proportion with the population density of these areas. 

__Density of usage__
[*Click to view projection*
![Bos by year](images/3/nyc_heat.png)](images/3/nyc_heatmap.html)

### Boston

The same case is in Boston where there are more stations in the downtown area. Boston is also a little different in this case as Boston consists of a hub of universities which the bikeshare company probably targetted by placing the stations near the universities or even inside them.

__Cluster location of stations__
[*Click to view projection*
![Bos by year](images/3/boston_cluster.png)](images/3/boston_bikeshare_stops_cluster.html)

However, the stations with university locations like Harvard, UMass or MIT are underused compared to the main Boston downtown areas. While these do provide a sustainable means of transportation for college students, these areas areas are underutilized.

__Density of usage__
[*Click to view projection*
![Bos by year](images/3/boston_heat.png)](images/3/boston_heatmap.html)

## From Here to There

### Most popular stations

Representing the same informaition in a chart, we can see that the downtown areas have the highest frequency of use. In fact, for both NYC and Boston, all of the top 20 stations are downtown. 

__New York City__

![Bos by year](images/4/20_popular_nyc.png)

__Boston__

![Bos by year](images/4/20_popular_bos.png)

### Next station by location
From where you are, where would you most likely go? 

#### New York City

<html><head>

<!-- Load require.js. Delete this if your page already loads require.js -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js" integrity="sha256-Ae2Vz/4ePdIu6ZyI/5ZGsYnb+m0JlOmKPjt6XZ9JJkA=" crossorigin="anonymous"></script>
<script src="https://unpkg.com/@jupyter-widgets/html-manager@*/dist/embed-amd.js" crossorigin="anonymous"></script>
<script type="application/vnd.jupyter.widget-state+json">
{
    "version_major": 2,
    "version_minor": 0,
    "state": {
        "2e90f566f32b4d4f86df59eebcf3e1de": {
            "model_name": "LayoutModel",
            "model_module": "@jupyter-widgets/base",
            "model_module_version": "1.1.0",
            "state": {}
        },
        "0b2ecdc13c3e4438b855e03538b5aaf0": {
            "model_name": "VBoxModel",
            "model_module": "@jupyter-widgets/controls",
            "model_module_version": "1.4.0",
            "state": {
                "_dom_classes": [
                    "widget-interact"
                ],
                "children": [
                    "IPY_MODEL_bc5487e59c9a400dba3c9621bf95a44a",
                    "IPY_MODEL_edec74f2582b4a7482144c7b5931abe7"
                ],
                "layout": "IPY_MODEL_2e90f566f32b4d4f86df59eebcf3e1de"
            }
        },
        "05aaef70006a433a89c2f1c3d2b7236f": {
            "model_name": "LayoutModel",
            "model_module": "@jupyter-widgets/base",
            "model_module_version": "1.1.0",
            "state": {}
        },
        "4daab3126eae4ca2808a48ed24fc8e9a": {
            "model_name": "DescriptionStyleModel",
            "model_module": "@jupyter-widgets/controls",
            "model_module_version": "1.4.0",
            "state": {
                "description_width": ""
            }
        },
        "bc5487e59c9a400dba3c9621bf95a44a": {
            "model_name": "DropdownModel",
            "model_module": "@jupyter-widgets/controls",
            "model_module_version": "1.4.0",
            "state": {
                "_options_labels": [
                    "W 11 St & 6 Ave",
                    "Cleveland Pl & Spring St",
                    "W 56 St & 6 Ave",
                    "8 Ave & W 33 St",
                    "St Marks Pl & 2 Ave",
                    "Front St & Washington St",
                    "Broadway & W 39 St",
                    "E 2 St & Avenue B",
                    "Clermont Ave & Park Ave",
                    "Harrison St & Hudson St",
                    "Wythe Ave & Metropolitan Ave",
                    "Pearl St & Hanover Square",
                    "W 25 St & 6 Ave",
                    "W 26 St & 8 Ave",
                    "Fulton St & Waverly Ave",
                    "Broadway & W 58 St",
                    "2 Ave & E 58 St",
                    "Cliff St & Fulton St",
                    "6 Ave & W 33 St",
                    "Front St & Maiden Ln",
                    "W 20 St & 7 Ave",
                    "University Pl & E 14 St",
                    "E 16 St & 5 Ave",
                    "E 15 St & 3 Ave",
                    "E 53 St & Lexington Ave",
                    "Vesey Pl & River Terrace",
                    "Spruce St & Nassau St",
                    "E 3 St & 1 Ave",
                    "St Marks Pl & 1 Ave",
                    "E 55 St & 2 Ave",
                    "E 43 St & 2 Ave",
                    "W 51 St & 6 Ave",
                    "E 11 St & 1 Ave",
                    "E 7 St & Avenue A",
                    "Park Pl & Church St",
                    "W 18 St & 6 Ave",
                    "9 Ave & W 22 St",
                    "Watts St & Greenwich St",
                    "Broadway & W 53 St",
                    "9 Ave & W 45 St",
                    "Broadway & Berry St",
                    "Henry St & Atlantic Ave",
                    "Broadway & E 22 St",
                    "Perry St & Bleecker St",
                    "Lefferts Pl & Franklin Ave",
                    "Centre St & Chambers St",
                    "W 17 St & 8 Ave",
                    "FDR Drive & E 35 St",
                    "Greenwich Ave & 8 Ave",
                    "Broadway & E 14 St",
                    "W 52 St & 5 Ave",
                    "Henry St & Grand St",
                    "W 16 St & The High Line",
                    "S 4 St & Wythe Ave",
                    "Washington St & Gansevoort St",
                    "W 4 St & 7 Ave S",
                    "W 52 St & 9 Ave",
                    "E 11 St & 2 Ave",
                    "1 Ave & E 15 St",
                    "W 31 St & 7 Ave",
                    "W 34 St & 11 Ave",
                    "W 41 St & 8 Ave",
                    "Broad St & Bridge St",
                    "Washington Pl & 6 Ave",
                    "Pershing Square S",
                    "Suffolk St & Stanton St",
                    "West St & Chambers St",
                    "W 20 St & 8 Ave",
                    "Allen St & E Houston St",
                    "Columbia St & Rivington St",
                    "W Houston St & Hudson St",
                    "W 37 St & 10 Ave",
                    "Broadway & W 55 St",
                    "Lexington Ave & E 26 St",
                    "W 20 St & 11 Ave",
                    "W 22 St & 8 Ave",
                    "MacDougal St & Washington Sq",
                    "Dean St & 4 Ave",
                    "1 Ave & E 30 St",
                    "2 Ave & E 31 St",
                    "Franklin Ave & Myrtle Ave",
                    "Bank St & Hudson St",
                    "W 13 St & 5 Ave",
                    "E 10 St & 5 Ave",
                    "Centre St & Worth St",
                    "W 53 St & 10 Ave",
                    "E 52 St & 2 Ave",
                    "W 14 St & The High Line",
                    "W 33 St & 7 Ave",
                    "1 Ave & E 18 St",
                    "Central Park S & 6 Ave",
                    "Broadway & W 24 St",
                    "Clinton Ave & Flushing Ave",
                    "9 Ave & W 18 St",
                    "E 59 St & Sutton Pl",
                    "W 24 St & 7 Ave",
                    "Front St & Gold St",
                    "W 56 St & 10 Ave",
                    "E 47 St & 1 Ave",
                    "Broadway & Battery Pl",
                    "S 3 St & Bedford Ave",
                    "Franklin St & W Broadway",
                    "E 4 St & 2 Ave",
                    "Lispenard St & Broadway",
                    "Allen St & Hester St",
                    "Lafayette St & E 8 St",
                    "Mott St & Prince St",
                    "W 38 St & 8 Ave",
                    "LaGuardia Pl & W 3 St",
                    "Broadway & W 29 St",
                    "E 17 St & Broadway",
                    "Reade St & Broadway",
                    "E 12 St & 3 Ave",
                    "9 Ave & W 14 St",
                    "Broadway & W 41 St",
                    "Rivington St & Chrystie St",
                    "W 13 St & 6 Ave",
                    "Great Jones St",
                    "Grand Army Plaza & Central Park S",
                    "Christopher St & Greenwich St",
                    "Rivington St & Ridge St",
                    "E 9 St & Avenue C",
                    "W 49 St & 8 Ave",
                    "W 15 St & 7 Ave",
                    "Duffield St & Willoughby St",
                    "E 55 St & Lexington Ave",
                    "Hudson St & Reade St",
                    "E 48 St & 3 Ave",
                    "Duane St & Greenwich St",
                    "Howard St & Centre St",
                    "W 47 St & 10 Ave",
                    "MacDougal St & Prince St",
                    "Broadway & W 51 St",
                    "E 16 St & Irving Pl",
                    "E 47 St & Park Ave",
                    "Lawrence St & Willoughby St",
                    "6 Ave & Broome St",
                    "E 47 St & 2 Ave",
                    "Mercer St & Spring St",
                    "W 39 St & 9 Ave",
                    "E 19 St & 3 Ave",
                    "Emerson Pl & Myrtle Ave",
                    "Metropolitan Ave & Bedford Ave",
                    "W 54 St & 9 Ave",
                    "Stanton St & Chrystie St",
                    "S 5 Pl & S 4 St",
                    "Pershing Square N",
                    "Grand St & Greene St",
                    "Bank St & Washington St",
                    "W 45 St & 8 Ave",
                    "Broadway & W 36 St",
                    "Greenwich St & N Moore St",
                    "Clinton Ave & Myrtle Ave",
                    "Broadway & W 49 St",
                    "Cumberland St & Lafayette Ave",
                    "Grand St & Havemeyer St",
                    "Fulton St & Rockwell Pl",
                    "8 Ave & W 31 St",
                    "Ashland Pl & Hanson Pl",
                    "E 53 St & Madison Ave",
                    "Old Fulton St",
                    "E 20 St & 2 Ave",
                    "Atlantic Ave & Fort Greene Pl",
                    "Mercer St & Bleecker St",
                    "E 39 St & 2 Ave",
                    "Liberty St & Broadway",
                    "Madison St & Montgomery St",
                    "Broadway & W 60 St",
                    "W 21 St & 6 Ave",
                    "Canal St & Rutgers St",
                    "W 42 St & 8 Ave",
                    "E 40 St & 5 Ave",
                    "E 45 St & 3 Ave",
                    "Lexington Ave & E 24 St",
                    "W Broadway & Spring St",
                    "Cadman Plaza E & Tillary St",
                    "W 22 St & 10 Ave",
                    "E 51 St & 1 Ave",
                    "Clinton St & Grand St",
                    "W 59 St & 10 Ave",
                    "E 39 St & 3 Ave",
                    "Church St & Leonard St",
                    "Stanton St & Mangin St",
                    "Allen St & Rivington St",
                    "W 27 St & 7 Ave",
                    "West Thames St",
                    "Washington Square E",
                    "Washington Pl & Broadway",
                    "10 Ave & W 28 St",
                    "Carmine St & 6 Ave",
                    "W 43 St & 10 Ave",
                    "E 10 St & Avenue A",
                    "W 43 St & 6 Ave",
                    "12 Ave & W 40 St",
                    "W 37 St & 5 Ave",
                    "Hancock St & Bedford Ave",
                    "E 56 St & Madison Ave",
                    "9 Ave & W 16 St",
                    "Barrow St & Hudson St",
                    "Lexington Ave & Classon Ave",
                    "E 6 St & Avenue B",
                    "Jay St & Tech Pl",
                    "E 32 St & Park Ave",
                    "State St & Smith St",
                    "E 31 St & 3 Ave",
                    "E 58 St & 3 Ave",
                    "W 45 St & 6 Ave",
                    "Sullivan St & Washington Sq",
                    "Washington Ave & Greene Ave",
                    "Murray St & West St",
                    "Bayard St & Baxter St",
                    "E 13 St & Avenue A",
                    "Elizabeth St & Hester St",
                    "E 33 St & 5 Ave",
                    "E 5 St & Avenue C",
                    "8 Ave & W 52 St",
                    "Division St & Bowery",
                    "Washington Ave & Park Ave",
                    "St James Pl & Oliver St",
                    "W 52 St & 11 Ave",
                    "Market St & Cherry St",
                    "Joralemon St & Adams St",
                    "E 27 St & 1 Ave",
                    "11 Ave & W 41 St",
                    "11 Ave & W 27 St",
                    "Forsyth St & Broome St",
                    "Willoughby St & Fleet St",
                    "South End Ave & Liberty St",
                    "DeKalb Ave & S Portland Ave",
                    "W 49 St & 5 Ave",
                    "E 25 St & 2 Ave",
                    "5 Ave & E 29 St",
                    "Sands St & Gold St",
                    "W 29 St & 9 Ave",
                    "Broadway & W 32 St",
                    "E 14 St & Avenue B",
                    "Lafayette St & Jersey St",
                    "Lafayette Ave & St James Pl",
                    "Norfolk St & Broome St",
                    "York St & Jay St",
                    "W 26 St & 10 Ave",
                    "Broadway & W 37 St",
                    "E 56 St & 3 Ave",
                    "E 43 St & Vanderbilt Ave",
                    "DeKalb Ave & Vanderbilt Ave",
                    "W 46 St & 11 Ave",
                    "E 33 St & 1 Ave",
                    "Bialystoker Pl & Delancey St",
                    "Forsyth St & Canal St",
                    "W 13 St & 7 Ave",
                    "Warren St & Church St",
                    "Greenwich St & Warren St",
                    "Gallatin Pl & Livingston St",
                    "6 Ave & Canal St",
                    "Avenue D & E 8 St",
                    "E 30 St & Park Ave S",
                    "John St & William St",
                    "E 11 St & Broadway",
                    "Lafayette Ave & Classon Ave",
                    "Clark St & Henry St",
                    "Bond St & Schermerhorn St",
                    "Little West St & 1 Pl",
                    "South St & Whitehall St",
                    "Pike St & E Broadway",
                    "State St",
                    "Pitt St & Stanton St",
                    "E 6 St & Avenue D",
                    "Avenue D & E 3 St",
                    "Carlton Ave & Park Ave",
                    "Avenue D & E 12 St",
                    "E 20 St & FDR Drive",
                    "E 25 St & 1 Ave",
                    "E 23 St & 1 Ave",
                    "Pike St & Monroe St",
                    "Madison St & Clinton St",
                    "1 Ave & E 44 St",
                    "Barclay St & Church St",
                    "Catherine St & Monroe St",
                    "Park Ave & St Edwards St",
                    "Willoughby Ave & Walworth St",
                    "Montague St & Clinton St",
                    "Cherry St",
                    "E 51 St & Lexington Ave",
                    "E 20 St & Park Ave",
                    "W 44 St & 5 Ave",
                    "Old Slip & Front St",
                    "E 37 St & Lexington Ave",
                    "Kent Ave & S 11 St",
                    "Hicks St & Montague St",
                    "Henry St & Poplar St",
                    "South St & Gouverneur Ln",
                    "Laight St & Hudson St",
                    "Washington Park",
                    "Concord St & Bridge St",
                    "E 2 St & 2 Ave",
                    "Cadman Plaza E & Red Cross Pl",
                    "Adelphi St & Myrtle Ave",
                    "Monroe St & Bedford Ave",
                    "E 2 St & Avenue C",
                    "Pearl St & Anchorage Pl",
                    "Fulton St & Clermont Ave",
                    "Clinton St & Joralemon St",
                    "Johnson St & Gold St",
                    "Columbia Heights & Cranberry St",
                    "Monroe St & Classon Ave",
                    "Myrtle Ave & St Edwards St",
                    "Willoughby Ave & Hall St",
                    "3 Ave & Schermerhorn St",
                    "Lafayette Ave & Fort Greene Pl",
                    "S Portland Ave & Hanson Pl",
                    "Clinton St & Tillary St",
                    "Atlantic Ave & Furman St",
                    "William St & Pine St",
                    "Bedford Ave & S 9th St",
                    "Macon St & Nostrand Ave",
                    "DeKalb Ave & Skillman St",
                    "Clermont Ave & Lafayette Ave",
                    "Maiden Ln & Pearl St",
                    "Water - Whitehall Plaza",
                    "Fulton St & Grand Ave",
                    "Hanover Pl & Livingston St",
                    "Greenwich Ave & Charles St",
                    "St James Pl & Pearl St",
                    "Nassau St & Navy St",
                    "Railroad Ave & Kay Ave",
                    "7 Ave & Farragut St",
                    "Flushing Ave & Carlton Ave",
                    "DeKalb Ave & Hudson Ave",
                    "Fulton St & William St",
                    "Shevchenko Pl & E 6 St"
                ],
                "description": "station",
                "index": 0,
                "layout": "IPY_MODEL_05aaef70006a433a89c2f1c3d2b7236f",
                "style": "IPY_MODEL_4daab3126eae4ca2808a48ed24fc8e9a"
            }
        },
        "49f34b16edc641a0974c5627c7e8c183": {
            "model_name": "LayoutModel",
            "model_module": "@jupyter-widgets/base",
            "model_module_version": "1.1.0",
            "state": {}
        },
        "edec74f2582b4a7482144c7b5931abe7": {
            "model_name": "OutputModel",
            "model_module": "@jupyter-widgets/output",
            "model_module_version": "1.0.0",
            "state": {
                "layout": "IPY_MODEL_49f34b16edc641a0974c5627c7e8c183",
                "outputs": [
                    {
                        "output_type": "display_data",
                        "data": {
                            "text/plain": "<Figure size 360x432 with 1 Axes>",
                            "image/png": "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\n"
                        },
                        "metadata": {
                            "needs_background": "light"
                        }
                    }
                ]
            }
        },
        "95037c1c8baf424d982104ef9415aa41": {
            "model_name": "LayoutModel",
            "model_module": "@jupyter-widgets/base",
            "model_module_version": "1.1.0",
            "state": {}
        },
        "6a5ff284a24d4a69addf4a3a1e8afc85": {
            "model_name": "VBoxModel",
            "model_module": "@jupyter-widgets/controls",
            "model_module_version": "1.4.0",
            "state": {
                "_dom_classes": [
                    "widget-interact"
                ],
                "children": [
                    "IPY_MODEL_bdccd70e812d46ddb473e30a4d8212e1",
                    "IPY_MODEL_ebb8f27481964c4fbd51ec3f44f2df2a"
                ],
                "layout": "IPY_MODEL_95037c1c8baf424d982104ef9415aa41"
            }
        },
        "dabf33cc57d94cf2be636096cd3fac3a": {
            "model_name": "LayoutModel",
            "model_module": "@jupyter-widgets/base",
            "model_module_version": "1.1.0",
            "state": {}
        },
        "e0d9427c351f49a0867501fc22534e1d": {
            "model_name": "DescriptionStyleModel",
            "model_module": "@jupyter-widgets/controls",
            "model_module_version": "1.4.0",
            "state": {
                "description_width": ""
            }
        },
        "bdccd70e812d46ddb473e30a4d8212e1": {
            "model_name": "DropdownModel",
            "model_module": "@jupyter-widgets/controls",
            "model_module_version": "1.4.0",
            "state": {
                "_options_labels": [
                    "Cross St. at Hanover St.",
                    "Lewis Wharf - Atlantic Ave.",
                    "South Station - 700 Atlantic Ave.",
                    "TD Garden - Legends Way",
                    "Boston Public Library - 700 Boylston St.",
                    "Yawkey Way at Boylston St.",
                    "Northeastern U / North Parking Lot",
                    "Overland St at Brookline Ave",
                    "Mayor Thomas M. Menino - Government Center",
                    "B.U. Central - 725 Comm. Ave.",
                    "Boylston St. at Arlington St.",
                    "Back Bay / South End Station",
                    "Aquarium Station - 200 Atlantic Ave.",
                    "Tremont St / W Newton St",
                    "Seaport Hotel",
                    "Washington St. at Rutland St.",
                    "Packard's Corner - Comm. Ave. at Brighton Ave.",
                    "Christian Science Plaza",
                    "HMS / HSPH - Ave. Louis Pasteur at Longwood Ave.",
                    "Rowes Wharf - Atlantic Ave",
                    "Stuart St. at Charles St.",
                    "Washington St. at Waltham St.",
                    "Roxbury Crossing Station",
                    "Union Square - Brighton Ave. at Cambridge St.",
                    "Kenmore Sq / Comm Ave",
                    "Seaport Square - Seaport Blvd. at Boston Wharf",
                    "Summer St. / Arch St.",
                    "Colleges of the Fenway",
                    "Faneuil Hall - Union St. at North St.",
                    "Post Office Square",
                    "Prudential Center / Belvidere",
                    "Cambridge St. at Joy St.",
                    "Landmark Centre",
                    "Boston Medical Center - 721 Mass. Ave.",
                    "Agganis Arena - 925 Comm Ave.",
                    "Harvard Real Estate - Brighton Mills - 370 Western Ave",
                    "Brigham Cir / Huntington Ave",
                    "Ruggles Station / Columbus Ave.",
                    "Harvard Real Estate - 219 Western Ave. at North Harvard St.",
                    "Longwood Ave / Binney St",
                    "Newbury St / Hereford St",
                    "New Balance - 38 Guest St.",
                    "Harvard University Housing - 111 Western Ave. at Soldiers Field Park",
                    "Boylston St / Berkeley St",
                    "Beacon St / Mass Ave",
                    "Washington St. at Lenox St.",
                    "Columbus Ave. at Mass. Ave.",
                    "Dudley Square",
                    "Boylston / Mass Ave",
                    "Tremont St. at Berkeley St.",
                    "Innovation Lab - 125 Western Ave. at Batten Way",
                    "Chinatown Gate Plaza - Surface Rd. at Beach St.",
                    "Tremont St / West St",
                    "Charles Circle - Charles St. at Cambridge St.",
                    "Fan Pier",
                    "The Esplanade - Beacon St. at Arlington St.",
                    "Boylston at Fairfield",
                    "Longwood Ave/Riverway",
                    "Dorchester Ave. at Gillette Park",
                    "Congress / Sleeper",
                    "Boston Convention & Exhibition Center",
                    "Harvard Square at Brattle St / Eliot St",
                    "Central Sq Post Office / Cambridge City Hall at Mass Ave / Pleasant St",
                    "Harvard Square at Mass Ave/ Dunster",
                    "Lafayette Square at Mass Ave / Main St / Columbia St",
                    "Central Square at Mass Ave / Essex St",
                    "Harvard Kennedy School at Bennett St / Eliot St",
                    "Union Square - Somerville",
                    "Somerville City Hall",
                    "Beacon St at Washington / Kirkland",
                    "Coolidge Corner - Beacon St @ Centre St",
                    "MIT at Mass Ave / Amherst St",
                    "Boylston St / Washington St",
                    "Allston Green District - Commonwealth Ave & Griggs St",
                    "Brookline Town Hall / Library Washington St",
                    "MIT Stata Center at Vassar St / Main St",
                    "South Bay Plaza",
                    "CambridgeSide Galleria - CambridgeSide PL at Land Blvd",
                    "Buswell Park",
                    "Andrew Station - Dorchester Ave at Humboldt Pl",
                    "Conway Park - Somerville Avenue",
                    "One Broadway / Kendall Sq at Main St / 3rd St",
                    "Brookline Village - Station Street @ MBTA",
                    "One Kendall Square at Hampshire St / Portland St",
                    "Lechmere Station at Cambridge St / First St",
                    "Inman Square at Vellucci Plaza / Hampshire St",
                    "nan",
                    "Harvard Law School at Mass Ave / Jarvis St",
                    "Harvard University Housing - 115 Putnam Ave at Peabody Terrace",
                    "JFK / UMASS Station",
                    "University of Massachusetts Boston",
                    "Charlestown - Warren St at Chelsea St",
                    "Charlestown - Main St at Austin St",
                    "Harvard  University River Houses at DeWolfe St / Cowperthwaite St",
                    "Cambridge Main Library at Broadway / Trowbridge St",
                    "Cambridge St - at Columbia St / Webster Ave",
                    "TD Garden - Causeway at Portal Park #2",
                    "Spaulding Rehabilitation Hospital - Charlestown Navy Yard",
                    "Boston Medical Center -  East Concord at Harrison Ave",
                    "Franklin St. / Arch St.",
                    "Harvard University River Houses / Plympton St at Memorial Drive",
                    "Washington Square at Washington St. / Beacon St.",
                    "New Balance - Guest St. at Life St.",
                    "Davis Square",
                    "Wilson Square",
                    "Ball Square",
                    "Powder House Circle",
                    "Harvard University Radcliffe Quadrangle at Shepard St / Garden St",
                    "Lower Cambridgeport at Magazine St/Riverside Rd",
                    "Kendall T at Main St",
                    "Mt Pleasant Ave / Dudley Town Common",
                    "Harvard University / SEAS Cruft-Pierce Halls at 29 Oxford St",
                    "TD Garden - Causeway at Portal Park #1",
                    "Harvard University Gund Hall at Quincy St / Kirkland S",
                    "JFK Crossing at Harvard St. / Thorndike St.",
                    "Porter Square Station",
                    "Mass Ave / Linear Park",
                    "359 Broadway - Broadway at Fayette Street",
                    "Somerville Hospital at Highland Ave / Crocker St",
                    "Packard Ave / Powderhouse Blvd",
                    "Teele Square at 239 Holland St",
                    "Biogen Idec - Binney St / Sixth St",
                    "Charles St at Beacon St",
                    "BIDMC - Brookline at Burlington St",
                    "West Broadway at Dorchester St",
                    "Egleston Square at Columbus Ave",
                    "Hyde Square at Barbara St",
                    "JP Centre - Centre Street at Myrtle Street",
                    "Milk St at India St",
                    "JP Monument - South St at Centre St",
                    "Hayes Square at Vine St.",
                    "South Boston Library - 646 East Broadway",
                    "E. Cottage St at Columbia Rd",
                    "Upham's Corner - Ramsey St at Dudley St",
                    "Summer St at Cutter St",
                    "Green St T",
                    "Jackson Square T at Centre St",
                    "New Balance Store - Boylston at Dartmouth"
                ],
                "description": "station",
                "index": 0,
                "layout": "IPY_MODEL_dabf33cc57d94cf2be636096cd3fac3a",
                "style": "IPY_MODEL_e0d9427c351f49a0867501fc22534e1d"
            }
        },
        "c456cf64c943431aa15f3ed707ea7c53": {
            "model_name": "LayoutModel",
            "model_module": "@jupyter-widgets/base",
            "model_module_version": "1.1.0",
            "state": {}
        },
        "ebb8f27481964c4fbd51ec3f44f2df2a": {
            "model_name": "OutputModel",
            "model_module": "@jupyter-widgets/output",
            "model_module_version": "1.0.0",
            "state": {
                "layout": "IPY_MODEL_c456cf64c943431aa15f3ed707ea7c53",
                "outputs": [
                    {
                        "output_type": "display_data",
                        "data": {
                            "text/plain": "<Figure size 360x432 with 1 Axes>",
                            "image/png": "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\n"
                        },
                        "metadata": {
                            "needs_background": "light"
                        }
                    }
                ]
            }
        },
        "259f27d4e80a48c894404b16c81c8db3": {
            "model_name": "LayoutModel",
            "model_module": "@jupyter-widgets/base",
            "model_module_version": "1.1.0",
            "state": {}
        },
        "4c18bfc755d54fc8a7b55ecd51185dad": {
            "model_name": "VBoxModel",
            "model_module": "@jupyter-widgets/controls",
            "model_module_version": "1.4.0",
            "state": {
                "_dom_classes": [
                    "widget-interact"
                ],
                "children": [
                    "IPY_MODEL_eef032b8dd93481588b7a9adccacec75",
                    "IPY_MODEL_6bb00aba74da4def87eed566dda99c56"
                ],
                "layout": "IPY_MODEL_259f27d4e80a48c894404b16c81c8db3"
            }
        },
        "0f5e7e3c502a4e6cac8086c51dc0b1f0": {
            "model_name": "LayoutModel",
            "model_module": "@jupyter-widgets/base",
            "model_module_version": "1.1.0",
            "state": {}
        },
        "b2704c2a1aaf4ab2b01e3c223040a08a": {
            "model_name": "DescriptionStyleModel",
            "model_module": "@jupyter-widgets/controls",
            "model_module_version": "1.4.0",
            "state": {
                "description_width": ""
            }
        },
        "eef032b8dd93481588b7a9adccacec75": {
            "model_name": "DropdownModel",
            "model_module": "@jupyter-widgets/controls",
            "model_module_version": "1.4.0",
            "state": {
                "_options_labels": [
                    "W 11 St & 6 Ave",
                    "Cleveland Pl & Spring St",
                    "W 56 St & 6 Ave",
                    "8 Ave & W 33 St",
                    "St Marks Pl & 2 Ave",
                    "Front St & Washington St",
                    "Broadway & W 39 St",
                    "E 2 St & Avenue B",
                    "Clermont Ave & Park Ave",
                    "Harrison St & Hudson St",
                    "Wythe Ave & Metropolitan Ave",
                    "Pearl St & Hanover Square",
                    "W 25 St & 6 Ave",
                    "W 26 St & 8 Ave",
                    "Fulton St & Waverly Ave",
                    "Broadway & W 58 St",
                    "2 Ave & E 58 St",
                    "Cliff St & Fulton St",
                    "6 Ave & W 33 St",
                    "Front St & Maiden Ln",
                    "W 20 St & 7 Ave",
                    "University Pl & E 14 St",
                    "E 16 St & 5 Ave",
                    "E 15 St & 3 Ave",
                    "E 53 St & Lexington Ave",
                    "Vesey Pl & River Terrace",
                    "Spruce St & Nassau St",
                    "E 3 St & 1 Ave",
                    "St Marks Pl & 1 Ave",
                    "E 55 St & 2 Ave",
                    "E 43 St & 2 Ave",
                    "W 51 St & 6 Ave",
                    "E 11 St & 1 Ave",
                    "E 7 St & Avenue A",
                    "Park Pl & Church St",
                    "W 18 St & 6 Ave",
                    "9 Ave & W 22 St",
                    "Watts St & Greenwich St",
                    "Broadway & W 53 St",
                    "9 Ave & W 45 St",
                    "Broadway & Berry St",
                    "Henry St & Atlantic Ave",
                    "Broadway & E 22 St",
                    "Perry St & Bleecker St",
                    "Lefferts Pl & Franklin Ave",
                    "Centre St & Chambers St",
                    "W 17 St & 8 Ave",
                    "FDR Drive & E 35 St",
                    "Greenwich Ave & 8 Ave",
                    "Broadway & E 14 St",
                    "W 52 St & 5 Ave",
                    "Henry St & Grand St",
                    "W 16 St & The High Line",
                    "S 4 St & Wythe Ave",
                    "Washington St & Gansevoort St",
                    "W 4 St & 7 Ave S",
                    "W 52 St & 9 Ave",
                    "E 11 St & 2 Ave",
                    "1 Ave & E 15 St",
                    "W 31 St & 7 Ave",
                    "W 34 St & 11 Ave",
                    "W 41 St & 8 Ave",
                    "Broad St & Bridge St",
                    "Washington Pl & 6 Ave",
                    "Pershing Square S",
                    "Suffolk St & Stanton St",
                    "West St & Chambers St",
                    "W 20 St & 8 Ave",
                    "Allen St & E Houston St",
                    "Columbia St & Rivington St",
                    "W Houston St & Hudson St",
                    "W 37 St & 10 Ave",
                    "Broadway & W 55 St",
                    "Lexington Ave & E 26 St",
                    "W 20 St & 11 Ave",
                    "W 22 St & 8 Ave",
                    "MacDougal St & Washington Sq",
                    "Dean St & 4 Ave",
                    "1 Ave & E 30 St",
                    "2 Ave & E 31 St",
                    "Franklin Ave & Myrtle Ave",
                    "Bank St & Hudson St",
                    "W 13 St & 5 Ave",
                    "E 10 St & 5 Ave",
                    "Centre St & Worth St",
                    "W 53 St & 10 Ave",
                    "E 52 St & 2 Ave",
                    "W 14 St & The High Line",
                    "W 33 St & 7 Ave",
                    "1 Ave & E 18 St",
                    "Central Park S & 6 Ave",
                    "Broadway & W 24 St",
                    "Clinton Ave & Flushing Ave",
                    "9 Ave & W 18 St",
                    "E 59 St & Sutton Pl",
                    "W 24 St & 7 Ave",
                    "Front St & Gold St",
                    "W 56 St & 10 Ave",
                    "E 47 St & 1 Ave",
                    "Broadway & Battery Pl",
                    "S 3 St & Bedford Ave",
                    "Franklin St & W Broadway",
                    "E 4 St & 2 Ave",
                    "Lispenard St & Broadway",
                    "Allen St & Hester St",
                    "Lafayette St & E 8 St",
                    "Mott St & Prince St",
                    "W 38 St & 8 Ave",
                    "LaGuardia Pl & W 3 St",
                    "Broadway & W 29 St",
                    "E 17 St & Broadway",
                    "Reade St & Broadway",
                    "E 12 St & 3 Ave",
                    "9 Ave & W 14 St",
                    "Broadway & W 41 St",
                    "Rivington St & Chrystie St",
                    "W 13 St & 6 Ave",
                    "Great Jones St",
                    "Grand Army Plaza & Central Park S",
                    "Christopher St & Greenwich St",
                    "Rivington St & Ridge St",
                    "E 9 St & Avenue C",
                    "W 49 St & 8 Ave",
                    "W 15 St & 7 Ave",
                    "Duffield St & Willoughby St",
                    "E 55 St & Lexington Ave",
                    "Hudson St & Reade St",
                    "E 48 St & 3 Ave",
                    "Duane St & Greenwich St",
                    "Howard St & Centre St",
                    "W 47 St & 10 Ave",
                    "MacDougal St & Prince St",
                    "Broadway & W 51 St",
                    "E 16 St & Irving Pl",
                    "E 47 St & Park Ave",
                    "Lawrence St & Willoughby St",
                    "6 Ave & Broome St",
                    "E 47 St & 2 Ave",
                    "Mercer St & Spring St",
                    "W 39 St & 9 Ave",
                    "E 19 St & 3 Ave",
                    "Emerson Pl & Myrtle Ave",
                    "Metropolitan Ave & Bedford Ave",
                    "W 54 St & 9 Ave",
                    "Stanton St & Chrystie St",
                    "S 5 Pl & S 4 St",
                    "Pershing Square N",
                    "Grand St & Greene St",
                    "Bank St & Washington St",
                    "W 45 St & 8 Ave",
                    "Broadway & W 36 St",
                    "Greenwich St & N Moore St",
                    "Clinton Ave & Myrtle Ave",
                    "Broadway & W 49 St",
                    "Cumberland St & Lafayette Ave",
                    "Grand St & Havemeyer St",
                    "Fulton St & Rockwell Pl",
                    "8 Ave & W 31 St",
                    "Ashland Pl & Hanson Pl",
                    "E 53 St & Madison Ave",
                    "Old Fulton St",
                    "E 20 St & 2 Ave",
                    "Atlantic Ave & Fort Greene Pl",
                    "Mercer St & Bleecker St",
                    "E 39 St & 2 Ave",
                    "Liberty St & Broadway",
                    "Madison St & Montgomery St",
                    "Broadway & W 60 St",
                    "W 21 St & 6 Ave",
                    "Canal St & Rutgers St",
                    "W 42 St & 8 Ave",
                    "E 40 St & 5 Ave",
                    "E 45 St & 3 Ave",
                    "Lexington Ave & E 24 St",
                    "W Broadway & Spring St",
                    "Cadman Plaza E & Tillary St",
                    "W 22 St & 10 Ave",
                    "E 51 St & 1 Ave",
                    "Clinton St & Grand St",
                    "W 59 St & 10 Ave",
                    "E 39 St & 3 Ave",
                    "Church St & Leonard St",
                    "Stanton St & Mangin St",
                    "Allen St & Rivington St",
                    "W 27 St & 7 Ave",
                    "West Thames St",
                    "Washington Square E",
                    "Washington Pl & Broadway",
                    "10 Ave & W 28 St",
                    "Carmine St & 6 Ave",
                    "W 43 St & 10 Ave",
                    "E 10 St & Avenue A",
                    "W 43 St & 6 Ave",
                    "12 Ave & W 40 St",
                    "W 37 St & 5 Ave",
                    "Hancock St & Bedford Ave",
                    "E 56 St & Madison Ave",
                    "9 Ave & W 16 St",
                    "Barrow St & Hudson St",
                    "Lexington Ave & Classon Ave",
                    "E 6 St & Avenue B",
                    "Jay St & Tech Pl",
                    "E 32 St & Park Ave",
                    "State St & Smith St",
                    "E 31 St & 3 Ave",
                    "E 58 St & 3 Ave",
                    "W 45 St & 6 Ave",
                    "Sullivan St & Washington Sq",
                    "Washington Ave & Greene Ave",
                    "Murray St & West St",
                    "Bayard St & Baxter St",
                    "E 13 St & Avenue A",
                    "Elizabeth St & Hester St",
                    "E 33 St & 5 Ave",
                    "E 5 St & Avenue C",
                    "8 Ave & W 52 St",
                    "Division St & Bowery",
                    "Washington Ave & Park Ave",
                    "St James Pl & Oliver St",
                    "W 52 St & 11 Ave",
                    "Market St & Cherry St",
                    "Joralemon St & Adams St",
                    "E 27 St & 1 Ave",
                    "11 Ave & W 41 St",
                    "11 Ave & W 27 St",
                    "Forsyth St & Broome St",
                    "Willoughby St & Fleet St",
                    "South End Ave & Liberty St",
                    "DeKalb Ave & S Portland Ave",
                    "W 49 St & 5 Ave",
                    "E 25 St & 2 Ave",
                    "5 Ave & E 29 St",
                    "Sands St & Gold St",
                    "W 29 St & 9 Ave",
                    "Broadway & W 32 St",
                    "E 14 St & Avenue B",
                    "Lafayette St & Jersey St",
                    "Lafayette Ave & St James Pl",
                    "Norfolk St & Broome St",
                    "York St & Jay St",
                    "W 26 St & 10 Ave",
                    "Broadway & W 37 St",
                    "E 56 St & 3 Ave",
                    "E 43 St & Vanderbilt Ave",
                    "DeKalb Ave & Vanderbilt Ave",
                    "W 46 St & 11 Ave",
                    "E 33 St & 1 Ave",
                    "Bialystoker Pl & Delancey St",
                    "Forsyth St & Canal St",
                    "W 13 St & 7 Ave",
                    "Warren St & Church St",
                    "Greenwich St & Warren St",
                    "Gallatin Pl & Livingston St",
                    "6 Ave & Canal St",
                    "Avenue D & E 8 St",
                    "E 30 St & Park Ave S",
                    "John St & William St",
                    "E 11 St & Broadway",
                    "Lafayette Ave & Classon Ave",
                    "Clark St & Henry St",
                    "Bond St & Schermerhorn St",
                    "Little West St & 1 Pl",
                    "South St & Whitehall St",
                    "Pike St & E Broadway",
                    "State St",
                    "Pitt St & Stanton St",
                    "E 6 St & Avenue D",
                    "Avenue D & E 3 St",
                    "Carlton Ave & Park Ave",
                    "Avenue D & E 12 St",
                    "E 20 St & FDR Drive",
                    "E 25 St & 1 Ave",
                    "E 23 St & 1 Ave",
                    "Pike St & Monroe St",
                    "Madison St & Clinton St",
                    "1 Ave & E 44 St",
                    "Barclay St & Church St",
                    "Catherine St & Monroe St",
                    "Park Ave & St Edwards St",
                    "Willoughby Ave & Walworth St",
                    "Montague St & Clinton St",
                    "Cherry St",
                    "E 51 St & Lexington Ave",
                    "E 20 St & Park Ave",
                    "W 44 St & 5 Ave",
                    "Old Slip & Front St",
                    "E 37 St & Lexington Ave",
                    "Kent Ave & S 11 St",
                    "Hicks St & Montague St",
                    "Henry St & Poplar St",
                    "South St & Gouverneur Ln",
                    "Laight St & Hudson St",
                    "Washington Park",
                    "Concord St & Bridge St",
                    "E 2 St & 2 Ave",
                    "Cadman Plaza E & Red Cross Pl",
                    "Adelphi St & Myrtle Ave",
                    "Monroe St & Bedford Ave",
                    "E 2 St & Avenue C",
                    "Pearl St & Anchorage Pl",
                    "Fulton St & Clermont Ave",
                    "Clinton St & Joralemon St",
                    "Johnson St & Gold St",
                    "Columbia Heights & Cranberry St",
                    "Monroe St & Classon Ave",
                    "Myrtle Ave & St Edwards St",
                    "Willoughby Ave & Hall St",
                    "3 Ave & Schermerhorn St",
                    "Lafayette Ave & Fort Greene Pl",
                    "S Portland Ave & Hanson Pl",
                    "Clinton St & Tillary St",
                    "Atlantic Ave & Furman St",
                    "William St & Pine St",
                    "Bedford Ave & S 9th St",
                    "Macon St & Nostrand Ave",
                    "DeKalb Ave & Skillman St",
                    "Clermont Ave & Lafayette Ave",
                    "Maiden Ln & Pearl St",
                    "Water - Whitehall Plaza",
                    "Fulton St & Grand Ave",
                    "Hanover Pl & Livingston St",
                    "Greenwich Ave & Charles St",
                    "St James Pl & Pearl St",
                    "Nassau St & Navy St",
                    "Railroad Ave & Kay Ave",
                    "7 Ave & Farragut St",
                    "Flushing Ave & Carlton Ave",
                    "DeKalb Ave & Hudson Ave",
                    "Fulton St & William St",
                    "Shevchenko Pl & E 6 St"
                ],
                "description": "station",
                "index": 17,
                "layout": "IPY_MODEL_0f5e7e3c502a4e6cac8086c51dc0b1f0",
                "style": "IPY_MODEL_b2704c2a1aaf4ab2b01e3c223040a08a"
            }
        },
        "fe81d23be3794cfda23bb73c74beb730": {
            "model_name": "LayoutModel",
            "model_module": "@jupyter-widgets/base",
            "model_module_version": "1.1.0",
            "state": {}
        },
        "6bb00aba74da4def87eed566dda99c56": {
            "model_name": "OutputModel",
            "model_module": "@jupyter-widgets/output",
            "model_module_version": "1.0.0",
            "state": {
                "layout": "IPY_MODEL_fe81d23be3794cfda23bb73c74beb730",
                "outputs": [
                    {
                        "output_type": "display_data",
                        "data": {
                            "text/plain": "<Figure size 360x432 with 1 Axes>",
                            "image/png": "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\n"
                        },
                        "metadata": {
                            "needs_background": "light"
                        }
                    }
                ]
            }
        },
        "f72199782ec04aeeabb91a6659ee3c92": {
            "model_name": "LayoutModel",
            "model_module": "@jupyter-widgets/base",
            "model_module_version": "1.1.0",
            "state": {}
        },
        "4a727d12332a453b87a358225a58adab": {
            "model_name": "VBoxModel",
            "model_module": "@jupyter-widgets/controls",
            "model_module_version": "1.4.0",
            "state": {
                "_dom_classes": [
                    "widget-interact"
                ],
                "children": [
                    "IPY_MODEL_c1531ee8d22247159946710d0440b3a1",
                    "IPY_MODEL_4e18a8afe61d4a54b05994a9a429f401"
                ],
                "layout": "IPY_MODEL_f72199782ec04aeeabb91a6659ee3c92"
            }
        },
        "76e3e01125c541fc9c954587dc573228": {
            "model_name": "LayoutModel",
            "model_module": "@jupyter-widgets/base",
            "model_module_version": "1.1.0",
            "state": {}
        },
        "4c9255a4260c4da783718b61af84cfe2": {
            "model_name": "DescriptionStyleModel",
            "model_module": "@jupyter-widgets/controls",
            "model_module_version": "1.4.0",
            "state": {
                "description_width": ""
            }
        },
        "c1531ee8d22247159946710d0440b3a1": {
            "model_name": "DropdownModel",
            "model_module": "@jupyter-widgets/controls",
            "model_module_version": "1.4.0",
            "state": {
                "_options_labels": [
                    "Cross St. at Hanover St.",
                    "Lewis Wharf - Atlantic Ave.",
                    "South Station - 700 Atlantic Ave.",
                    "TD Garden - Legends Way",
                    "Boston Public Library - 700 Boylston St.",
                    "Yawkey Way at Boylston St.",
                    "Northeastern U / North Parking Lot",
                    "Overland St at Brookline Ave",
                    "Mayor Thomas M. Menino - Government Center",
                    "B.U. Central - 725 Comm. Ave.",
                    "Boylston St. at Arlington St.",
                    "Back Bay / South End Station",
                    "Aquarium Station - 200 Atlantic Ave.",
                    "Tremont St / W Newton St",
                    "Seaport Hotel",
                    "Washington St. at Rutland St.",
                    "Packard's Corner - Comm. Ave. at Brighton Ave.",
                    "Christian Science Plaza",
                    "HMS / HSPH - Ave. Louis Pasteur at Longwood Ave.",
                    "Rowes Wharf - Atlantic Ave",
                    "Stuart St. at Charles St.",
                    "Washington St. at Waltham St.",
                    "Roxbury Crossing Station",
                    "Union Square - Brighton Ave. at Cambridge St.",
                    "Kenmore Sq / Comm Ave",
                    "Seaport Square - Seaport Blvd. at Boston Wharf",
                    "Summer St. / Arch St.",
                    "Colleges of the Fenway",
                    "Faneuil Hall - Union St. at North St.",
                    "Post Office Square",
                    "Prudential Center / Belvidere",
                    "Cambridge St. at Joy St.",
                    "Landmark Centre",
                    "Boston Medical Center - 721 Mass. Ave.",
                    "Agganis Arena - 925 Comm Ave.",
                    "Harvard Real Estate - Brighton Mills - 370 Western Ave",
                    "Brigham Cir / Huntington Ave",
                    "Ruggles Station / Columbus Ave.",
                    "Harvard Real Estate - 219 Western Ave. at North Harvard St.",
                    "Longwood Ave / Binney St",
                    "Newbury St / Hereford St",
                    "New Balance - 38 Guest St.",
                    "Harvard University Housing - 111 Western Ave. at Soldiers Field Park",
                    "Boylston St / Berkeley St",
                    "Beacon St / Mass Ave",
                    "Washington St. at Lenox St.",
                    "Columbus Ave. at Mass. Ave.",
                    "Dudley Square",
                    "Boylston / Mass Ave",
                    "Tremont St. at Berkeley St.",
                    "Innovation Lab - 125 Western Ave. at Batten Way",
                    "Chinatown Gate Plaza - Surface Rd. at Beach St.",
                    "Tremont St / West St",
                    "Charles Circle - Charles St. at Cambridge St.",
                    "Fan Pier",
                    "The Esplanade - Beacon St. at Arlington St.",
                    "Boylston at Fairfield",
                    "Longwood Ave/Riverway",
                    "Dorchester Ave. at Gillette Park",
                    "Congress / Sleeper",
                    "Boston Convention & Exhibition Center",
                    "Harvard Square at Brattle St / Eliot St",
                    "Central Sq Post Office / Cambridge City Hall at Mass Ave / Pleasant St",
                    "Harvard Square at Mass Ave/ Dunster",
                    "Lafayette Square at Mass Ave / Main St / Columbia St",
                    "Central Square at Mass Ave / Essex St",
                    "Harvard Kennedy School at Bennett St / Eliot St",
                    "Union Square - Somerville",
                    "Somerville City Hall",
                    "Beacon St at Washington / Kirkland",
                    "Coolidge Corner - Beacon St @ Centre St",
                    "MIT at Mass Ave / Amherst St",
                    "Boylston St / Washington St",
                    "Allston Green District - Commonwealth Ave & Griggs St",
                    "Brookline Town Hall / Library Washington St",
                    "MIT Stata Center at Vassar St / Main St",
                    "South Bay Plaza",
                    "CambridgeSide Galleria - CambridgeSide PL at Land Blvd",
                    "Buswell Park",
                    "Andrew Station - Dorchester Ave at Humboldt Pl",
                    "Conway Park - Somerville Avenue",
                    "One Broadway / Kendall Sq at Main St / 3rd St",
                    "Brookline Village - Station Street @ MBTA",
                    "One Kendall Square at Hampshire St / Portland St",
                    "Lechmere Station at Cambridge St / First St",
                    "Inman Square at Vellucci Plaza / Hampshire St",
                    "nan",
                    "Harvard Law School at Mass Ave / Jarvis St",
                    "Harvard University Housing - 115 Putnam Ave at Peabody Terrace",
                    "JFK / UMASS Station",
                    "University of Massachusetts Boston",
                    "Charlestown - Warren St at Chelsea St",
                    "Charlestown - Main St at Austin St",
                    "Harvard  University River Houses at DeWolfe St / Cowperthwaite St",
                    "Cambridge Main Library at Broadway / Trowbridge St",
                    "Cambridge St - at Columbia St / Webster Ave",
                    "TD Garden - Causeway at Portal Park #2",
                    "Spaulding Rehabilitation Hospital - Charlestown Navy Yard",
                    "Boston Medical Center -  East Concord at Harrison Ave",
                    "Franklin St. / Arch St.",
                    "Harvard University River Houses / Plympton St at Memorial Drive",
                    "Washington Square at Washington St. / Beacon St.",
                    "New Balance - Guest St. at Life St.",
                    "Davis Square",
                    "Wilson Square",
                    "Ball Square",
                    "Powder House Circle",
                    "Harvard University Radcliffe Quadrangle at Shepard St / Garden St",
                    "Lower Cambridgeport at Magazine St/Riverside Rd",
                    "Kendall T at Main St",
                    "Mt Pleasant Ave / Dudley Town Common",
                    "Harvard University / SEAS Cruft-Pierce Halls at 29 Oxford St",
                    "TD Garden - Causeway at Portal Park #1",
                    "Harvard University Gund Hall at Quincy St / Kirkland S",
                    "JFK Crossing at Harvard St. / Thorndike St.",
                    "Porter Square Station",
                    "Mass Ave / Linear Park",
                    "359 Broadway - Broadway at Fayette Street",
                    "Somerville Hospital at Highland Ave / Crocker St",
                    "Packard Ave / Powderhouse Blvd",
                    "Teele Square at 239 Holland St",
                    "Biogen Idec - Binney St / Sixth St",
                    "Charles St at Beacon St",
                    "BIDMC - Brookline at Burlington St",
                    "West Broadway at Dorchester St",
                    "Egleston Square at Columbus Ave",
                    "Hyde Square at Barbara St",
                    "JP Centre - Centre Street at Myrtle Street",
                    "Milk St at India St",
                    "JP Monument - South St at Centre St",
                    "Hayes Square at Vine St.",
                    "South Boston Library - 646 East Broadway",
                    "E. Cottage St at Columbia Rd",
                    "Upham's Corner - Ramsey St at Dudley St",
                    "Summer St at Cutter St",
                    "Green St T",
                    "Jackson Square T at Centre St",
                    "New Balance Store - Boylston at Dartmouth"
                ],
                "description": "station",
                "index": 0,
                "layout": "IPY_MODEL_76e3e01125c541fc9c954587dc573228",
                "style": "IPY_MODEL_4c9255a4260c4da783718b61af84cfe2"
            }
        },
        "81d52f1a222a47069d12e6a977bd1f8b": {
            "model_name": "LayoutModel",
            "model_module": "@jupyter-widgets/base",
            "model_module_version": "1.1.0",
            "state": {}
        },
        "4e18a8afe61d4a54b05994a9a429f401": {
            "model_name": "OutputModel",
            "model_module": "@jupyter-widgets/output",
            "model_module_version": "1.0.0",
            "state": {
                "layout": "IPY_MODEL_81d52f1a222a47069d12e6a977bd1f8b",
                "outputs": [
                    {
                        "output_type": "display_data",
                        "data": {
                            "text/plain": "<Figure size 360x432 with 1 Axes>",
                            "image/png": "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\n"
                        },
                        "metadata": {
                            "needs_background": "light"
                        }
                    }
                ]
            }
        }
    }
}
</script>
</head>
<body>

<script type="application/vnd.jupyter.widget-view+json">
{
    "version_major": 2,
    "version_minor": 0,
    "model_id": "4c18bfc755d54fc8a7b55ecd51185dad"
}
</script>

<script type="application/vnd.jupyter.widget-view+json">
{
    "version_major": 2,
    "version_minor": 0,
    "model_id": "4a727d12332a453b87a358225a58adab"
}
</script>

</body>
</html>

#### Boston

<html><head>


<!-- Load require.js. Delete this if your page already loads require.js -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.4/require.min.js" integrity="sha256-Ae2Vz/4ePdIu6ZyI/5ZGsYnb+m0JlOmKPjt6XZ9JJkA=" crossorigin="anonymous"></script>
<script src="https://unpkg.com/@jupyter-widgets/html-manager@*/dist/embed-amd.js" crossorigin="anonymous"></script>
<script type="application/vnd.jupyter.widget-state+json">
{
    "version_major": 2,
    "version_minor": 0,
    "state": {
        "2e90f566f32b4d4f86df59eebcf3e1de": {
            "model_name": "LayoutModel",
            "model_module": "@jupyter-widgets/base",
            "model_module_version": "1.1.0",
            "state": {}
        },
        "0b2ecdc13c3e4438b855e03538b5aaf0": {
            "model_name": "VBoxModel",
            "model_module": "@jupyter-widgets/controls",
            "model_module_version": "1.4.0",
            "state": {
                "_dom_classes": [
                    "widget-interact"
                ],
                "children": [
                    "IPY_MODEL_bc5487e59c9a400dba3c9621bf95a44a",
                    "IPY_MODEL_edec74f2582b4a7482144c7b5931abe7"
                ],
                "layout": "IPY_MODEL_2e90f566f32b4d4f86df59eebcf3e1de"
            }
        },
        "05aaef70006a433a89c2f1c3d2b7236f": {
            "model_name": "LayoutModel",
            "model_module": "@jupyter-widgets/base",
            "model_module_version": "1.1.0",
            "state": {}
        },
        "4daab3126eae4ca2808a48ed24fc8e9a": {
            "model_name": "DescriptionStyleModel",
            "model_module": "@jupyter-widgets/controls",
            "model_module_version": "1.4.0",
            "state": {
                "description_width": ""
            }
        },
        "bc5487e59c9a400dba3c9621bf95a44a": {
            "model_name": "DropdownModel",
            "model_module": "@jupyter-widgets/controls",
            "model_module_version": "1.4.0",
            "state": {
                "_options_labels": [
                    "W 11 St & 6 Ave",
                    "Cleveland Pl & Spring St",
                    "W 56 St & 6 Ave",
                    "8 Ave & W 33 St",
                    "St Marks Pl & 2 Ave",
                    "Front St & Washington St",
                    "Broadway & W 39 St",
                    "E 2 St & Avenue B",
                    "Clermont Ave & Park Ave",
                    "Harrison St & Hudson St",
                    "Wythe Ave & Metropolitan Ave",
                    "Pearl St & Hanover Square",
                    "W 25 St & 6 Ave",
                    "W 26 St & 8 Ave",
                    "Fulton St & Waverly Ave",
                    "Broadway & W 58 St",
                    "2 Ave & E 58 St",
                    "Cliff St & Fulton St",
                    "6 Ave & W 33 St",
                    "Front St & Maiden Ln",
                    "W 20 St & 7 Ave",
                    "University Pl & E 14 St",
                    "E 16 St & 5 Ave",
                    "E 15 St & 3 Ave",
                    "E 53 St & Lexington Ave",
                    "Vesey Pl & River Terrace",
                    "Spruce St & Nassau St",
                    "E 3 St & 1 Ave",
                    "St Marks Pl & 1 Ave",
                    "E 55 St & 2 Ave",
                    "E 43 St & 2 Ave",
                    "W 51 St & 6 Ave",
                    "E 11 St & 1 Ave",
                    "E 7 St & Avenue A",
                    "Park Pl & Church St",
                    "W 18 St & 6 Ave",
                    "9 Ave & W 22 St",
                    "Watts St & Greenwich St",
                    "Broadway & W 53 St",
                    "9 Ave & W 45 St",
                    "Broadway & Berry St",
                    "Henry St & Atlantic Ave",
                    "Broadway & E 22 St",
                    "Perry St & Bleecker St",
                    "Lefferts Pl & Franklin Ave",
                    "Centre St & Chambers St",
                    "W 17 St & 8 Ave",
                    "FDR Drive & E 35 St",
                    "Greenwich Ave & 8 Ave",
                    "Broadway & E 14 St",
                    "W 52 St & 5 Ave",
                    "Henry St & Grand St",
                    "W 16 St & The High Line",
                    "S 4 St & Wythe Ave",
                    "Washington St & Gansevoort St",
                    "W 4 St & 7 Ave S",
                    "W 52 St & 9 Ave",
                    "E 11 St & 2 Ave",
                    "1 Ave & E 15 St",
                    "W 31 St & 7 Ave",
                    "W 34 St & 11 Ave",
                    "W 41 St & 8 Ave",
                    "Broad St & Bridge St",
                    "Washington Pl & 6 Ave",
                    "Pershing Square S",
                    "Suffolk St & Stanton St",
                    "West St & Chambers St",
                    "W 20 St & 8 Ave",
                    "Allen St & E Houston St",
                    "Columbia St & Rivington St",
                    "W Houston St & Hudson St",
                    "W 37 St & 10 Ave",
                    "Broadway & W 55 St",
                    "Lexington Ave & E 26 St",
                    "W 20 St & 11 Ave",
                    "W 22 St & 8 Ave",
                    "MacDougal St & Washington Sq",
                    "Dean St & 4 Ave",
                    "1 Ave & E 30 St",
                    "2 Ave & E 31 St",
                    "Franklin Ave & Myrtle Ave",
                    "Bank St & Hudson St",
                    "W 13 St & 5 Ave",
                    "E 10 St & 5 Ave",
                    "Centre St & Worth St",
                    "W 53 St & 10 Ave",
                    "E 52 St & 2 Ave",
                    "W 14 St & The High Line",
                    "W 33 St & 7 Ave",
                    "1 Ave & E 18 St",
                    "Central Park S & 6 Ave",
                    "Broadway & W 24 St",
                    "Clinton Ave & Flushing Ave",
                    "9 Ave & W 18 St",
                    "E 59 St & Sutton Pl",
                    "W 24 St & 7 Ave",
                    "Front St & Gold St",
                    "W 56 St & 10 Ave",
                    "E 47 St & 1 Ave",
                    "Broadway & Battery Pl",
                    "S 3 St & Bedford Ave",
                    "Franklin St & W Broadway",
                    "E 4 St & 2 Ave",
                    "Lispenard St & Broadway",
                    "Allen St & Hester St",
                    "Lafayette St & E 8 St",
                    "Mott St & Prince St",
                    "W 38 St & 8 Ave",
                    "LaGuardia Pl & W 3 St",
                    "Broadway & W 29 St",
                    "E 17 St & Broadway",
                    "Reade St & Broadway",
                    "E 12 St & 3 Ave",
                    "9 Ave & W 14 St",
                    "Broadway & W 41 St",
                    "Rivington St & Chrystie St",
                    "W 13 St & 6 Ave",
                    "Great Jones St",
                    "Grand Army Plaza & Central Park S",
                    "Christopher St & Greenwich St",
                    "Rivington St & Ridge St",
                    "E 9 St & Avenue C",
                    "W 49 St & 8 Ave",
                    "W 15 St & 7 Ave",
                    "Duffield St & Willoughby St",
                    "E 55 St & Lexington Ave",
                    "Hudson St & Reade St",
                    "E 48 St & 3 Ave",
                    "Duane St & Greenwich St",
                    "Howard St & Centre St",
                    "W 47 St & 10 Ave",
                    "MacDougal St & Prince St",
                    "Broadway & W 51 St",
                    "E 16 St & Irving Pl",
                    "E 47 St & Park Ave",
                    "Lawrence St & Willoughby St",
                    "6 Ave & Broome St",
                    "E 47 St & 2 Ave",
                    "Mercer St & Spring St",
                    "W 39 St & 9 Ave",
                    "E 19 St & 3 Ave",
                    "Emerson Pl & Myrtle Ave",
                    "Metropolitan Ave & Bedford Ave",
                    "W 54 St & 9 Ave",
                    "Stanton St & Chrystie St",
                    "S 5 Pl & S 4 St",
                    "Pershing Square N",
                    "Grand St & Greene St",
                    "Bank St & Washington St",
                    "W 45 St & 8 Ave",
                    "Broadway & W 36 St",
                    "Greenwich St & N Moore St",
                    "Clinton Ave & Myrtle Ave",
                    "Broadway & W 49 St",
                    "Cumberland St & Lafayette Ave",
                    "Grand St & Havemeyer St",
                    "Fulton St & Rockwell Pl",
                    "8 Ave & W 31 St",
                    "Ashland Pl & Hanson Pl",
                    "E 53 St & Madison Ave",
                    "Old Fulton St",
                    "E 20 St & 2 Ave",
                    "Atlantic Ave & Fort Greene Pl",
                    "Mercer St & Bleecker St",
                    "E 39 St & 2 Ave",
                    "Liberty St & Broadway",
                    "Madison St & Montgomery St",
                    "Broadway & W 60 St",
                    "W 21 St & 6 Ave",
                    "Canal St & Rutgers St",
                    "W 42 St & 8 Ave",
                    "E 40 St & 5 Ave",
                    "E 45 St & 3 Ave",
                    "Lexington Ave & E 24 St",
                    "W Broadway & Spring St",
                    "Cadman Plaza E & Tillary St",
                    "W 22 St & 10 Ave",
                    "E 51 St & 1 Ave",
                    "Clinton St & Grand St",
                    "W 59 St & 10 Ave",
                    "E 39 St & 3 Ave",
                    "Church St & Leonard St",
                    "Stanton St & Mangin St",
                    "Allen St & Rivington St",
                    "W 27 St & 7 Ave",
                    "West Thames St",
                    "Washington Square E",
                    "Washington Pl & Broadway",
                    "10 Ave & W 28 St",
                    "Carmine St & 6 Ave",
                    "W 43 St & 10 Ave",
                    "E 10 St & Avenue A",
                    "W 43 St & 6 Ave",
                    "12 Ave & W 40 St",
                    "W 37 St & 5 Ave",
                    "Hancock St & Bedford Ave",
                    "E 56 St & Madison Ave",
                    "9 Ave & W 16 St",
                    "Barrow St & Hudson St",
                    "Lexington Ave & Classon Ave",
                    "E 6 St & Avenue B",
                    "Jay St & Tech Pl",
                    "E 32 St & Park Ave",
                    "State St & Smith St",
                    "E 31 St & 3 Ave",
                    "E 58 St & 3 Ave",
                    "W 45 St & 6 Ave",
                    "Sullivan St & Washington Sq",
                    "Washington Ave & Greene Ave",
                    "Murray St & West St",
                    "Bayard St & Baxter St",
                    "E 13 St & Avenue A",
                    "Elizabeth St & Hester St",
                    "E 33 St & 5 Ave",
                    "E 5 St & Avenue C",
                    "8 Ave & W 52 St",
                    "Division St & Bowery",
                    "Washington Ave & Park Ave",
                    "St James Pl & Oliver St",
                    "W 52 St & 11 Ave",
                    "Market St & Cherry St",
                    "Joralemon St & Adams St",
                    "E 27 St & 1 Ave",
                    "11 Ave & W 41 St",
                    "11 Ave & W 27 St",
                    "Forsyth St & Broome St",
                    "Willoughby St & Fleet St",
                    "South End Ave & Liberty St",
                    "DeKalb Ave & S Portland Ave",
                    "W 49 St & 5 Ave",
                    "E 25 St & 2 Ave",
                    "5 Ave & E 29 St",
                    "Sands St & Gold St",
                    "W 29 St & 9 Ave",
                    "Broadway & W 32 St",
                    "E 14 St & Avenue B",
                    "Lafayette St & Jersey St",
                    "Lafayette Ave & St James Pl",
                    "Norfolk St & Broome St",
                    "York St & Jay St",
                    "W 26 St & 10 Ave",
                    "Broadway & W 37 St",
                    "E 56 St & 3 Ave",
                    "E 43 St & Vanderbilt Ave",
                    "DeKalb Ave & Vanderbilt Ave",
                    "W 46 St & 11 Ave",
                    "E 33 St & 1 Ave",
                    "Bialystoker Pl & Delancey St",
                    "Forsyth St & Canal St",
                    "W 13 St & 7 Ave",
                    "Warren St & Church St",
                    "Greenwich St & Warren St",
                    "Gallatin Pl & Livingston St",
                    "6 Ave & Canal St",
                    "Avenue D & E 8 St",
                    "E 30 St & Park Ave S",
                    "John St & William St",
                    "E 11 St & Broadway",
                    "Lafayette Ave & Classon Ave",
                    "Clark St & Henry St",
                    "Bond St & Schermerhorn St",
                    "Little West St & 1 Pl",
                    "South St & Whitehall St",
                    "Pike St & E Broadway",
                    "State St",
                    "Pitt St & Stanton St",
                    "E 6 St & Avenue D",
                    "Avenue D & E 3 St",
                    "Carlton Ave & Park Ave",
                    "Avenue D & E 12 St",
                    "E 20 St & FDR Drive",
                    "E 25 St & 1 Ave",
                    "E 23 St & 1 Ave",
                    "Pike St & Monroe St",
                    "Madison St & Clinton St",
                    "1 Ave & E 44 St",
                    "Barclay St & Church St",
                    "Catherine St & Monroe St",
                    "Park Ave & St Edwards St",
                    "Willoughby Ave & Walworth St",
                    "Montague St & Clinton St",
                    "Cherry St",
                    "E 51 St & Lexington Ave",
                    "E 20 St & Park Ave",
                    "W 44 St & 5 Ave",
                    "Old Slip & Front St",
                    "E 37 St & Lexington Ave",
                    "Kent Ave & S 11 St",
                    "Hicks St & Montague St",
                    "Henry St & Poplar St",
                    "South St & Gouverneur Ln",
                    "Laight St & Hudson St",
                    "Washington Park",
                    "Concord St & Bridge St",
                    "E 2 St & 2 Ave",
                    "Cadman Plaza E & Red Cross Pl",
                    "Adelphi St & Myrtle Ave",
                    "Monroe St & Bedford Ave",
                    "E 2 St & Avenue C",
                    "Pearl St & Anchorage Pl",
                    "Fulton St & Clermont Ave",
                    "Clinton St & Joralemon St",
                    "Johnson St & Gold St",
                    "Columbia Heights & Cranberry St",
                    "Monroe St & Classon Ave",
                    "Myrtle Ave & St Edwards St",
                    "Willoughby Ave & Hall St",
                    "3 Ave & Schermerhorn St",
                    "Lafayette Ave & Fort Greene Pl",
                    "S Portland Ave & Hanson Pl",
                    "Clinton St & Tillary St",
                    "Atlantic Ave & Furman St",
                    "William St & Pine St",
                    "Bedford Ave & S 9th St",
                    "Macon St & Nostrand Ave",
                    "DeKalb Ave & Skillman St",
                    "Clermont Ave & Lafayette Ave",
                    "Maiden Ln & Pearl St",
                    "Water - Whitehall Plaza",
                    "Fulton St & Grand Ave",
                    "Hanover Pl & Livingston St",
                    "Greenwich Ave & Charles St",
                    "St James Pl & Pearl St",
                    "Nassau St & Navy St",
                    "Railroad Ave & Kay Ave",
                    "7 Ave & Farragut St",
                    "Flushing Ave & Carlton Ave",
                    "DeKalb Ave & Hudson Ave",
                    "Fulton St & William St",
                    "Shevchenko Pl & E 6 St"
                ],
                "description": "station",
                "index": 0,
                "layout": "IPY_MODEL_05aaef70006a433a89c2f1c3d2b7236f",
                "style": "IPY_MODEL_4daab3126eae4ca2808a48ed24fc8e9a"
            }
        },
        "49f34b16edc641a0974c5627c7e8c183": {
            "model_name": "LayoutModel",
            "model_module": "@jupyter-widgets/base",
            "model_module_version": "1.1.0",
            "state": {}
        },
        "edec74f2582b4a7482144c7b5931abe7": {
            "model_name": "OutputModel",
            "model_module": "@jupyter-widgets/output",
            "model_module_version": "1.0.0",
            "state": {
                "layout": "IPY_MODEL_49f34b16edc641a0974c5627c7e8c183",
                "outputs": [
                    {
                        "output_type": "display_data",
                        "data": {
                            "text/plain": "<Figure size 360x432 with 1 Axes>",
                            "image/png": "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\n"
                        },
                        "metadata": {
                            "needs_background": "light"
                        }
                    }
                ]
            }
        },
        "95037c1c8baf424d982104ef9415aa41": {
            "model_name": "LayoutModel",
            "model_module": "@jupyter-widgets/base",
            "model_module_version": "1.1.0",
            "state": {}
        },
        "6a5ff284a24d4a69addf4a3a1e8afc85": {
            "model_name": "VBoxModel",
            "model_module": "@jupyter-widgets/controls",
            "model_module_version": "1.4.0",
            "state": {
                "_dom_classes": [
                    "widget-interact"
                ],
                "children": [
                    "IPY_MODEL_bdccd70e812d46ddb473e30a4d8212e1",
                    "IPY_MODEL_ebb8f27481964c4fbd51ec3f44f2df2a"
                ],
                "layout": "IPY_MODEL_95037c1c8baf424d982104ef9415aa41"
            }
        },
        "dabf33cc57d94cf2be636096cd3fac3a": {
            "model_name": "LayoutModel",
            "model_module": "@jupyter-widgets/base",
            "model_module_version": "1.1.0",
            "state": {}
        },
        "e0d9427c351f49a0867501fc22534e1d": {
            "model_name": "DescriptionStyleModel",
            "model_module": "@jupyter-widgets/controls",
            "model_module_version": "1.4.0",
            "state": {
                "description_width": ""
            }
        },
        "bdccd70e812d46ddb473e30a4d8212e1": {
            "model_name": "DropdownModel",
            "model_module": "@jupyter-widgets/controls",
            "model_module_version": "1.4.0",
            "state": {
                "_options_labels": [
                    "Cross St. at Hanover St.",
                    "Lewis Wharf - Atlantic Ave.",
                    "South Station - 700 Atlantic Ave.",
                    "TD Garden - Legends Way",
                    "Boston Public Library - 700 Boylston St.",
                    "Yawkey Way at Boylston St.",
                    "Northeastern U / North Parking Lot",
                    "Overland St at Brookline Ave",
                    "Mayor Thomas M. Menino - Government Center",
                    "B.U. Central - 725 Comm. Ave.",
                    "Boylston St. at Arlington St.",
                    "Back Bay / South End Station",
                    "Aquarium Station - 200 Atlantic Ave.",
                    "Tremont St / W Newton St",
                    "Seaport Hotel",
                    "Washington St. at Rutland St.",
                    "Packard's Corner - Comm. Ave. at Brighton Ave.",
                    "Christian Science Plaza",
                    "HMS / HSPH - Ave. Louis Pasteur at Longwood Ave.",
                    "Rowes Wharf - Atlantic Ave",
                    "Stuart St. at Charles St.",
                    "Washington St. at Waltham St.",
                    "Roxbury Crossing Station",
                    "Union Square - Brighton Ave. at Cambridge St.",
                    "Kenmore Sq / Comm Ave",
                    "Seaport Square - Seaport Blvd. at Boston Wharf",
                    "Summer St. / Arch St.",
                    "Colleges of the Fenway",
                    "Faneuil Hall - Union St. at North St.",
                    "Post Office Square",
                    "Prudential Center / Belvidere",
                    "Cambridge St. at Joy St.",
                    "Landmark Centre",
                    "Boston Medical Center - 721 Mass. Ave.",
                    "Agganis Arena - 925 Comm Ave.",
                    "Harvard Real Estate - Brighton Mills - 370 Western Ave",
                    "Brigham Cir / Huntington Ave",
                    "Ruggles Station / Columbus Ave.",
                    "Harvard Real Estate - 219 Western Ave. at North Harvard St.",
                    "Longwood Ave / Binney St",
                    "Newbury St / Hereford St",
                    "New Balance - 38 Guest St.",
                    "Harvard University Housing - 111 Western Ave. at Soldiers Field Park",
                    "Boylston St / Berkeley St",
                    "Beacon St / Mass Ave",
                    "Washington St. at Lenox St.",
                    "Columbus Ave. at Mass. Ave.",
                    "Dudley Square",
                    "Boylston / Mass Ave",
                    "Tremont St. at Berkeley St.",
                    "Innovation Lab - 125 Western Ave. at Batten Way",
                    "Chinatown Gate Plaza - Surface Rd. at Beach St.",
                    "Tremont St / West St",
                    "Charles Circle - Charles St. at Cambridge St.",
                    "Fan Pier",
                    "The Esplanade - Beacon St. at Arlington St.",
                    "Boylston at Fairfield",
                    "Longwood Ave/Riverway",
                    "Dorchester Ave. at Gillette Park",
                    "Congress / Sleeper",
                    "Boston Convention & Exhibition Center",
                    "Harvard Square at Brattle St / Eliot St",
                    "Central Sq Post Office / Cambridge City Hall at Mass Ave / Pleasant St",
                    "Harvard Square at Mass Ave/ Dunster",
                    "Lafayette Square at Mass Ave / Main St / Columbia St",
                    "Central Square at Mass Ave / Essex St",
                    "Harvard Kennedy School at Bennett St / Eliot St",
                    "Union Square - Somerville",
                    "Somerville City Hall",
                    "Beacon St at Washington / Kirkland",
                    "Coolidge Corner - Beacon St @ Centre St",
                    "MIT at Mass Ave / Amherst St",
                    "Boylston St / Washington St",
                    "Allston Green District - Commonwealth Ave & Griggs St",
                    "Brookline Town Hall / Library Washington St",
                    "MIT Stata Center at Vassar St / Main St",
                    "South Bay Plaza",
                    "CambridgeSide Galleria - CambridgeSide PL at Land Blvd",
                    "Buswell Park",
                    "Andrew Station - Dorchester Ave at Humboldt Pl",
                    "Conway Park - Somerville Avenue",
                    "One Broadway / Kendall Sq at Main St / 3rd St",
                    "Brookline Village - Station Street @ MBTA",
                    "One Kendall Square at Hampshire St / Portland St",
                    "Lechmere Station at Cambridge St / First St",
                    "Inman Square at Vellucci Plaza / Hampshire St",
                    "nan",
                    "Harvard Law School at Mass Ave / Jarvis St",
                    "Harvard University Housing - 115 Putnam Ave at Peabody Terrace",
                    "JFK / UMASS Station",
                    "University of Massachusetts Boston",
                    "Charlestown - Warren St at Chelsea St",
                    "Charlestown - Main St at Austin St",
                    "Harvard  University River Houses at DeWolfe St / Cowperthwaite St",
                    "Cambridge Main Library at Broadway / Trowbridge St",
                    "Cambridge St - at Columbia St / Webster Ave",
                    "TD Garden - Causeway at Portal Park #2",
                    "Spaulding Rehabilitation Hospital - Charlestown Navy Yard",
                    "Boston Medical Center -  East Concord at Harrison Ave",
                    "Franklin St. / Arch St.",
                    "Harvard University River Houses / Plympton St at Memorial Drive",
                    "Washington Square at Washington St. / Beacon St.",
                    "New Balance - Guest St. at Life St.",
                    "Davis Square",
                    "Wilson Square",
                    "Ball Square",
                    "Powder House Circle",
                    "Harvard University Radcliffe Quadrangle at Shepard St / Garden St",
                    "Lower Cambridgeport at Magazine St/Riverside Rd",
                    "Kendall T at Main St",
                    "Mt Pleasant Ave / Dudley Town Common",
                    "Harvard University / SEAS Cruft-Pierce Halls at 29 Oxford St",
                    "TD Garden - Causeway at Portal Park #1",
                    "Harvard University Gund Hall at Quincy St / Kirkland S",
                    "JFK Crossing at Harvard St. / Thorndike St.",
                    "Porter Square Station",
                    "Mass Ave / Linear Park",
                    "359 Broadway - Broadway at Fayette Street",
                    "Somerville Hospital at Highland Ave / Crocker St",
                    "Packard Ave / Powderhouse Blvd",
                    "Teele Square at 239 Holland St",
                    "Biogen Idec - Binney St / Sixth St",
                    "Charles St at Beacon St",
                    "BIDMC - Brookline at Burlington St",
                    "West Broadway at Dorchester St",
                    "Egleston Square at Columbus Ave",
                    "Hyde Square at Barbara St",
                    "JP Centre - Centre Street at Myrtle Street",
                    "Milk St at India St",
                    "JP Monument - South St at Centre St",
                    "Hayes Square at Vine St.",
                    "South Boston Library - 646 East Broadway",
                    "E. Cottage St at Columbia Rd",
                    "Upham's Corner - Ramsey St at Dudley St",
                    "Summer St at Cutter St",
                    "Green St T",
                    "Jackson Square T at Centre St",
                    "New Balance Store - Boylston at Dartmouth"
                ],
                "description": "station",
                "index": 0,
                "layout": "IPY_MODEL_dabf33cc57d94cf2be636096cd3fac3a",
                "style": "IPY_MODEL_e0d9427c351f49a0867501fc22534e1d"
            }
        },
        "c456cf64c943431aa15f3ed707ea7c53": {
            "model_name": "LayoutModel",
            "model_module": "@jupyter-widgets/base",
            "model_module_version": "1.1.0",
            "state": {}
        },
        "ebb8f27481964c4fbd51ec3f44f2df2a": {
            "model_name": "OutputModel",
            "model_module": "@jupyter-widgets/output",
            "model_module_version": "1.0.0",
            "state": {
                "layout": "IPY_MODEL_c456cf64c943431aa15f3ed707ea7c53",
                "outputs": [
                    {
                        "output_type": "display_data",
                        "data": {
                            "text/plain": "<Figure size 360x432 with 1 Axes>",
                            "image/png": "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\n"
                        },
                        "metadata": {
                            "needs_background": "light"
                        }
                    }
                ]
            }
        },
        "259f27d4e80a48c894404b16c81c8db3": {
            "model_name": "LayoutModel",
            "model_module": "@jupyter-widgets/base",
            "model_module_version": "1.1.0",
            "state": {}
        },
        "4c18bfc755d54fc8a7b55ecd51185dad": {
            "model_name": "VBoxModel",
            "model_module": "@jupyter-widgets/controls",
            "model_module_version": "1.4.0",
            "state": {
                "_dom_classes": [
                    "widget-interact"
                ],
                "children": [
                    "IPY_MODEL_eef032b8dd93481588b7a9adccacec75",
                    "IPY_MODEL_6bb00aba74da4def87eed566dda99c56"
                ],
                "layout": "IPY_MODEL_259f27d4e80a48c894404b16c81c8db3"
            }
        },
        "0f5e7e3c502a4e6cac8086c51dc0b1f0": {
            "model_name": "LayoutModel",
            "model_module": "@jupyter-widgets/base",
            "model_module_version": "1.1.0",
            "state": {}
        },
        "b2704c2a1aaf4ab2b01e3c223040a08a": {
            "model_name": "DescriptionStyleModel",
            "model_module": "@jupyter-widgets/controls",
            "model_module_version": "1.4.0",
            "state": {
                "description_width": ""
            }
        },
        "eef032b8dd93481588b7a9adccacec75": {
            "model_name": "DropdownModel",
            "model_module": "@jupyter-widgets/controls",
            "model_module_version": "1.4.0",
            "state": {
                "_options_labels": [
                    "W 11 St & 6 Ave",
                    "Cleveland Pl & Spring St",
                    "W 56 St & 6 Ave",
                    "8 Ave & W 33 St",
                    "St Marks Pl & 2 Ave",
                    "Front St & Washington St",
                    "Broadway & W 39 St",
                    "E 2 St & Avenue B",
                    "Clermont Ave & Park Ave",
                    "Harrison St & Hudson St",
                    "Wythe Ave & Metropolitan Ave",
                    "Pearl St & Hanover Square",
                    "W 25 St & 6 Ave",
                    "W 26 St & 8 Ave",
                    "Fulton St & Waverly Ave",
                    "Broadway & W 58 St",
                    "2 Ave & E 58 St",
                    "Cliff St & Fulton St",
                    "6 Ave & W 33 St",
                    "Front St & Maiden Ln",
                    "W 20 St & 7 Ave",
                    "University Pl & E 14 St",
                    "E 16 St & 5 Ave",
                    "E 15 St & 3 Ave",
                    "E 53 St & Lexington Ave",
                    "Vesey Pl & River Terrace",
                    "Spruce St & Nassau St",
                    "E 3 St & 1 Ave",
                    "St Marks Pl & 1 Ave",
                    "E 55 St & 2 Ave",
                    "E 43 St & 2 Ave",
                    "W 51 St & 6 Ave",
                    "E 11 St & 1 Ave",
                    "E 7 St & Avenue A",
                    "Park Pl & Church St",
                    "W 18 St & 6 Ave",
                    "9 Ave & W 22 St",
                    "Watts St & Greenwich St",
                    "Broadway & W 53 St",
                    "9 Ave & W 45 St",
                    "Broadway & Berry St",
                    "Henry St & Atlantic Ave",
                    "Broadway & E 22 St",
                    "Perry St & Bleecker St",
                    "Lefferts Pl & Franklin Ave",
                    "Centre St & Chambers St",
                    "W 17 St & 8 Ave",
                    "FDR Drive & E 35 St",
                    "Greenwich Ave & 8 Ave",
                    "Broadway & E 14 St",
                    "W 52 St & 5 Ave",
                    "Henry St & Grand St",
                    "W 16 St & The High Line",
                    "S 4 St & Wythe Ave",
                    "Washington St & Gansevoort St",
                    "W 4 St & 7 Ave S",
                    "W 52 St & 9 Ave",
                    "E 11 St & 2 Ave",
                    "1 Ave & E 15 St",
                    "W 31 St & 7 Ave",
                    "W 34 St & 11 Ave",
                    "W 41 St & 8 Ave",
                    "Broad St & Bridge St",
                    "Washington Pl & 6 Ave",
                    "Pershing Square S",
                    "Suffolk St & Stanton St",
                    "West St & Chambers St",
                    "W 20 St & 8 Ave",
                    "Allen St & E Houston St",
                    "Columbia St & Rivington St",
                    "W Houston St & Hudson St",
                    "W 37 St & 10 Ave",
                    "Broadway & W 55 St",
                    "Lexington Ave & E 26 St",
                    "W 20 St & 11 Ave",
                    "W 22 St & 8 Ave",
                    "MacDougal St & Washington Sq",
                    "Dean St & 4 Ave",
                    "1 Ave & E 30 St",
                    "2 Ave & E 31 St",
                    "Franklin Ave & Myrtle Ave",
                    "Bank St & Hudson St",
                    "W 13 St & 5 Ave",
                    "E 10 St & 5 Ave",
                    "Centre St & Worth St",
                    "W 53 St & 10 Ave",
                    "E 52 St & 2 Ave",
                    "W 14 St & The High Line",
                    "W 33 St & 7 Ave",
                    "1 Ave & E 18 St",
                    "Central Park S & 6 Ave",
                    "Broadway & W 24 St",
                    "Clinton Ave & Flushing Ave",
                    "9 Ave & W 18 St",
                    "E 59 St & Sutton Pl",
                    "W 24 St & 7 Ave",
                    "Front St & Gold St",
                    "W 56 St & 10 Ave",
                    "E 47 St & 1 Ave",
                    "Broadway & Battery Pl",
                    "S 3 St & Bedford Ave",
                    "Franklin St & W Broadway",
                    "E 4 St & 2 Ave",
                    "Lispenard St & Broadway",
                    "Allen St & Hester St",
                    "Lafayette St & E 8 St",
                    "Mott St & Prince St",
                    "W 38 St & 8 Ave",
                    "LaGuardia Pl & W 3 St",
                    "Broadway & W 29 St",
                    "E 17 St & Broadway",
                    "Reade St & Broadway",
                    "E 12 St & 3 Ave",
                    "9 Ave & W 14 St",
                    "Broadway & W 41 St",
                    "Rivington St & Chrystie St",
                    "W 13 St & 6 Ave",
                    "Great Jones St",
                    "Grand Army Plaza & Central Park S",
                    "Christopher St & Greenwich St",
                    "Rivington St & Ridge St",
                    "E 9 St & Avenue C",
                    "W 49 St & 8 Ave",
                    "W 15 St & 7 Ave",
                    "Duffield St & Willoughby St",
                    "E 55 St & Lexington Ave",
                    "Hudson St & Reade St",
                    "E 48 St & 3 Ave",
                    "Duane St & Greenwich St",
                    "Howard St & Centre St",
                    "W 47 St & 10 Ave",
                    "MacDougal St & Prince St",
                    "Broadway & W 51 St",
                    "E 16 St & Irving Pl",
                    "E 47 St & Park Ave",
                    "Lawrence St & Willoughby St",
                    "6 Ave & Broome St",
                    "E 47 St & 2 Ave",
                    "Mercer St & Spring St",
                    "W 39 St & 9 Ave",
                    "E 19 St & 3 Ave",
                    "Emerson Pl & Myrtle Ave",
                    "Metropolitan Ave & Bedford Ave",
                    "W 54 St & 9 Ave",
                    "Stanton St & Chrystie St",
                    "S 5 Pl & S 4 St",
                    "Pershing Square N",
                    "Grand St & Greene St",
                    "Bank St & Washington St",
                    "W 45 St & 8 Ave",
                    "Broadway & W 36 St",
                    "Greenwich St & N Moore St",
                    "Clinton Ave & Myrtle Ave",
                    "Broadway & W 49 St",
                    "Cumberland St & Lafayette Ave",
                    "Grand St & Havemeyer St",
                    "Fulton St & Rockwell Pl",
                    "8 Ave & W 31 St",
                    "Ashland Pl & Hanson Pl",
                    "E 53 St & Madison Ave",
                    "Old Fulton St",
                    "E 20 St & 2 Ave",
                    "Atlantic Ave & Fort Greene Pl",
                    "Mercer St & Bleecker St",
                    "E 39 St & 2 Ave",
                    "Liberty St & Broadway",
                    "Madison St & Montgomery St",
                    "Broadway & W 60 St",
                    "W 21 St & 6 Ave",
                    "Canal St & Rutgers St",
                    "W 42 St & 8 Ave",
                    "E 40 St & 5 Ave",
                    "E 45 St & 3 Ave",
                    "Lexington Ave & E 24 St",
                    "W Broadway & Spring St",
                    "Cadman Plaza E & Tillary St",
                    "W 22 St & 10 Ave",
                    "E 51 St & 1 Ave",
                    "Clinton St & Grand St",
                    "W 59 St & 10 Ave",
                    "E 39 St & 3 Ave",
                    "Church St & Leonard St",
                    "Stanton St & Mangin St",
                    "Allen St & Rivington St",
                    "W 27 St & 7 Ave",
                    "West Thames St",
                    "Washington Square E",
                    "Washington Pl & Broadway",
                    "10 Ave & W 28 St",
                    "Carmine St & 6 Ave",
                    "W 43 St & 10 Ave",
                    "E 10 St & Avenue A",
                    "W 43 St & 6 Ave",
                    "12 Ave & W 40 St",
                    "W 37 St & 5 Ave",
                    "Hancock St & Bedford Ave",
                    "E 56 St & Madison Ave",
                    "9 Ave & W 16 St",
                    "Barrow St & Hudson St",
                    "Lexington Ave & Classon Ave",
                    "E 6 St & Avenue B",
                    "Jay St & Tech Pl",
                    "E 32 St & Park Ave",
                    "State St & Smith St",
                    "E 31 St & 3 Ave",
                    "E 58 St & 3 Ave",
                    "W 45 St & 6 Ave",
                    "Sullivan St & Washington Sq",
                    "Washington Ave & Greene Ave",
                    "Murray St & West St",
                    "Bayard St & Baxter St",
                    "E 13 St & Avenue A",
                    "Elizabeth St & Hester St",
                    "E 33 St & 5 Ave",
                    "E 5 St & Avenue C",
                    "8 Ave & W 52 St",
                    "Division St & Bowery",
                    "Washington Ave & Park Ave",
                    "St James Pl & Oliver St",
                    "W 52 St & 11 Ave",
                    "Market St & Cherry St",
                    "Joralemon St & Adams St",
                    "E 27 St & 1 Ave",
                    "11 Ave & W 41 St",
                    "11 Ave & W 27 St",
                    "Forsyth St & Broome St",
                    "Willoughby St & Fleet St",
                    "South End Ave & Liberty St",
                    "DeKalb Ave & S Portland Ave",
                    "W 49 St & 5 Ave",
                    "E 25 St & 2 Ave",
                    "5 Ave & E 29 St",
                    "Sands St & Gold St",
                    "W 29 St & 9 Ave",
                    "Broadway & W 32 St",
                    "E 14 St & Avenue B",
                    "Lafayette St & Jersey St",
                    "Lafayette Ave & St James Pl",
                    "Norfolk St & Broome St",
                    "York St & Jay St",
                    "W 26 St & 10 Ave",
                    "Broadway & W 37 St",
                    "E 56 St & 3 Ave",
                    "E 43 St & Vanderbilt Ave",
                    "DeKalb Ave & Vanderbilt Ave",
                    "W 46 St & 11 Ave",
                    "E 33 St & 1 Ave",
                    "Bialystoker Pl & Delancey St",
                    "Forsyth St & Canal St",
                    "W 13 St & 7 Ave",
                    "Warren St & Church St",
                    "Greenwich St & Warren St",
                    "Gallatin Pl & Livingston St",
                    "6 Ave & Canal St",
                    "Avenue D & E 8 St",
                    "E 30 St & Park Ave S",
                    "John St & William St",
                    "E 11 St & Broadway",
                    "Lafayette Ave & Classon Ave",
                    "Clark St & Henry St",
                    "Bond St & Schermerhorn St",
                    "Little West St & 1 Pl",
                    "South St & Whitehall St",
                    "Pike St & E Broadway",
                    "State St",
                    "Pitt St & Stanton St",
                    "E 6 St & Avenue D",
                    "Avenue D & E 3 St",
                    "Carlton Ave & Park Ave",
                    "Avenue D & E 12 St",
                    "E 20 St & FDR Drive",
                    "E 25 St & 1 Ave",
                    "E 23 St & 1 Ave",
                    "Pike St & Monroe St",
                    "Madison St & Clinton St",
                    "1 Ave & E 44 St",
                    "Barclay St & Church St",
                    "Catherine St & Monroe St",
                    "Park Ave & St Edwards St",
                    "Willoughby Ave & Walworth St",
                    "Montague St & Clinton St",
                    "Cherry St",
                    "E 51 St & Lexington Ave",
                    "E 20 St & Park Ave",
                    "W 44 St & 5 Ave",
                    "Old Slip & Front St",
                    "E 37 St & Lexington Ave",
                    "Kent Ave & S 11 St",
                    "Hicks St & Montague St",
                    "Henry St & Poplar St",
                    "South St & Gouverneur Ln",
                    "Laight St & Hudson St",
                    "Washington Park",
                    "Concord St & Bridge St",
                    "E 2 St & 2 Ave",
                    "Cadman Plaza E & Red Cross Pl",
                    "Adelphi St & Myrtle Ave",
                    "Monroe St & Bedford Ave",
                    "E 2 St & Avenue C",
                    "Pearl St & Anchorage Pl",
                    "Fulton St & Clermont Ave",
                    "Clinton St & Joralemon St",
                    "Johnson St & Gold St",
                    "Columbia Heights & Cranberry St",
                    "Monroe St & Classon Ave",
                    "Myrtle Ave & St Edwards St",
                    "Willoughby Ave & Hall St",
                    "3 Ave & Schermerhorn St",
                    "Lafayette Ave & Fort Greene Pl",
                    "S Portland Ave & Hanson Pl",
                    "Clinton St & Tillary St",
                    "Atlantic Ave & Furman St",
                    "William St & Pine St",
                    "Bedford Ave & S 9th St",
                    "Macon St & Nostrand Ave",
                    "DeKalb Ave & Skillman St",
                    "Clermont Ave & Lafayette Ave",
                    "Maiden Ln & Pearl St",
                    "Water - Whitehall Plaza",
                    "Fulton St & Grand Ave",
                    "Hanover Pl & Livingston St",
                    "Greenwich Ave & Charles St",
                    "St James Pl & Pearl St",
                    "Nassau St & Navy St",
                    "Railroad Ave & Kay Ave",
                    "7 Ave & Farragut St",
                    "Flushing Ave & Carlton Ave",
                    "DeKalb Ave & Hudson Ave",
                    "Fulton St & William St",
                    "Shevchenko Pl & E 6 St"
                ],
                "description": "station",
                "index": 17,
                "layout": "IPY_MODEL_0f5e7e3c502a4e6cac8086c51dc0b1f0",
                "style": "IPY_MODEL_b2704c2a1aaf4ab2b01e3c223040a08a"
            }
        },
        "fe81d23be3794cfda23bb73c74beb730": {
            "model_name": "LayoutModel",
            "model_module": "@jupyter-widgets/base",
            "model_module_version": "1.1.0",
            "state": {}
        },
        "6bb00aba74da4def87eed566dda99c56": {
            "model_name": "OutputModel",
            "model_module": "@jupyter-widgets/output",
            "model_module_version": "1.0.0",
            "state": {
                "layout": "IPY_MODEL_fe81d23be3794cfda23bb73c74beb730",
                "outputs": [
                    {
                        "output_type": "display_data",
                        "data": {
                            "text/plain": "<Figure size 360x432 with 1 Axes>",
                            "image/png": "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\n"
                        },
                        "metadata": {
                            "needs_background": "light"
                        }
                    }
                ]
            }
        },
        "f72199782ec04aeeabb91a6659ee3c92": {
            "model_name": "LayoutModel",
            "model_module": "@jupyter-widgets/base",
            "model_module_version": "1.1.0",
            "state": {}
        },
        "4a727d12332a453b87a358225a58adab": {
            "model_name": "VBoxModel",
            "model_module": "@jupyter-widgets/controls",
            "model_module_version": "1.4.0",
            "state": {
                "_dom_classes": [
                    "widget-interact"
                ],
                "children": [
                    "IPY_MODEL_c1531ee8d22247159946710d0440b3a1",
                    "IPY_MODEL_4e18a8afe61d4a54b05994a9a429f401"
                ],
                "layout": "IPY_MODEL_f72199782ec04aeeabb91a6659ee3c92"
            }
        },
        "76e3e01125c541fc9c954587dc573228": {
            "model_name": "LayoutModel",
            "model_module": "@jupyter-widgets/base",
            "model_module_version": "1.1.0",
            "state": {}
        },
        "4c9255a4260c4da783718b61af84cfe2": {
            "model_name": "DescriptionStyleModel",
            "model_module": "@jupyter-widgets/controls",
            "model_module_version": "1.4.0",
            "state": {
                "description_width": ""
            }
        },
        "c1531ee8d22247159946710d0440b3a1": {
            "model_name": "DropdownModel",
            "model_module": "@jupyter-widgets/controls",
            "model_module_version": "1.4.0",
            "state": {
                "_options_labels": [
                    "Cross St. at Hanover St.",
                    "Lewis Wharf - Atlantic Ave.",
                    "South Station - 700 Atlantic Ave.",
                    "TD Garden - Legends Way",
                    "Boston Public Library - 700 Boylston St.",
                    "Yawkey Way at Boylston St.",
                    "Northeastern U / North Parking Lot",
                    "Overland St at Brookline Ave",
                    "Mayor Thomas M. Menino - Government Center",
                    "B.U. Central - 725 Comm. Ave.",
                    "Boylston St. at Arlington St.",
                    "Back Bay / South End Station",
                    "Aquarium Station - 200 Atlantic Ave.",
                    "Tremont St / W Newton St",
                    "Seaport Hotel",
                    "Washington St. at Rutland St.",
                    "Packard's Corner - Comm. Ave. at Brighton Ave.",
                    "Christian Science Plaza",
                    "HMS / HSPH - Ave. Louis Pasteur at Longwood Ave.",
                    "Rowes Wharf - Atlantic Ave",
                    "Stuart St. at Charles St.",
                    "Washington St. at Waltham St.",
                    "Roxbury Crossing Station",
                    "Union Square - Brighton Ave. at Cambridge St.",
                    "Kenmore Sq / Comm Ave",
                    "Seaport Square - Seaport Blvd. at Boston Wharf",
                    "Summer St. / Arch St.",
                    "Colleges of the Fenway",
                    "Faneuil Hall - Union St. at North St.",
                    "Post Office Square",
                    "Prudential Center / Belvidere",
                    "Cambridge St. at Joy St.",
                    "Landmark Centre",
                    "Boston Medical Center - 721 Mass. Ave.",
                    "Agganis Arena - 925 Comm Ave.",
                    "Harvard Real Estate - Brighton Mills - 370 Western Ave",
                    "Brigham Cir / Huntington Ave",
                    "Ruggles Station / Columbus Ave.",
                    "Harvard Real Estate - 219 Western Ave. at North Harvard St.",
                    "Longwood Ave / Binney St",
                    "Newbury St / Hereford St",
                    "New Balance - 38 Guest St.",
                    "Harvard University Housing - 111 Western Ave. at Soldiers Field Park",
                    "Boylston St / Berkeley St",
                    "Beacon St / Mass Ave",
                    "Washington St. at Lenox St.",
                    "Columbus Ave. at Mass. Ave.",
                    "Dudley Square",
                    "Boylston / Mass Ave",
                    "Tremont St. at Berkeley St.",
                    "Innovation Lab - 125 Western Ave. at Batten Way",
                    "Chinatown Gate Plaza - Surface Rd. at Beach St.",
                    "Tremont St / West St",
                    "Charles Circle - Charles St. at Cambridge St.",
                    "Fan Pier",
                    "The Esplanade - Beacon St. at Arlington St.",
                    "Boylston at Fairfield",
                    "Longwood Ave/Riverway",
                    "Dorchester Ave. at Gillette Park",
                    "Congress / Sleeper",
                    "Boston Convention & Exhibition Center",
                    "Harvard Square at Brattle St / Eliot St",
                    "Central Sq Post Office / Cambridge City Hall at Mass Ave / Pleasant St",
                    "Harvard Square at Mass Ave/ Dunster",
                    "Lafayette Square at Mass Ave / Main St / Columbia St",
                    "Central Square at Mass Ave / Essex St",
                    "Harvard Kennedy School at Bennett St / Eliot St",
                    "Union Square - Somerville",
                    "Somerville City Hall",
                    "Beacon St at Washington / Kirkland",
                    "Coolidge Corner - Beacon St @ Centre St",
                    "MIT at Mass Ave / Amherst St",
                    "Boylston St / Washington St",
                    "Allston Green District - Commonwealth Ave & Griggs St",
                    "Brookline Town Hall / Library Washington St",
                    "MIT Stata Center at Vassar St / Main St",
                    "South Bay Plaza",
                    "CambridgeSide Galleria - CambridgeSide PL at Land Blvd",
                    "Buswell Park",
                    "Andrew Station - Dorchester Ave at Humboldt Pl",
                    "Conway Park - Somerville Avenue",
                    "One Broadway / Kendall Sq at Main St / 3rd St",
                    "Brookline Village - Station Street @ MBTA",
                    "One Kendall Square at Hampshire St / Portland St",
                    "Lechmere Station at Cambridge St / First St",
                    "Inman Square at Vellucci Plaza / Hampshire St",
                    "nan",
                    "Harvard Law School at Mass Ave / Jarvis St",
                    "Harvard University Housing - 115 Putnam Ave at Peabody Terrace",
                    "JFK / UMASS Station",
                    "University of Massachusetts Boston",
                    "Charlestown - Warren St at Chelsea St",
                    "Charlestown - Main St at Austin St",
                    "Harvard  University River Houses at DeWolfe St / Cowperthwaite St",
                    "Cambridge Main Library at Broadway / Trowbridge St",
                    "Cambridge St - at Columbia St / Webster Ave",
                    "TD Garden - Causeway at Portal Park #2",
                    "Spaulding Rehabilitation Hospital - Charlestown Navy Yard",
                    "Boston Medical Center -  East Concord at Harrison Ave",
                    "Franklin St. / Arch St.",
                    "Harvard University River Houses / Plympton St at Memorial Drive",
                    "Washington Square at Washington St. / Beacon St.",
                    "New Balance - Guest St. at Life St.",
                    "Davis Square",
                    "Wilson Square",
                    "Ball Square",
                    "Powder House Circle",
                    "Harvard University Radcliffe Quadrangle at Shepard St / Garden St",
                    "Lower Cambridgeport at Magazine St/Riverside Rd",
                    "Kendall T at Main St",
                    "Mt Pleasant Ave / Dudley Town Common",
                    "Harvard University / SEAS Cruft-Pierce Halls at 29 Oxford St",
                    "TD Garden - Causeway at Portal Park #1",
                    "Harvard University Gund Hall at Quincy St / Kirkland S",
                    "JFK Crossing at Harvard St. / Thorndike St.",
                    "Porter Square Station",
                    "Mass Ave / Linear Park",
                    "359 Broadway - Broadway at Fayette Street",
                    "Somerville Hospital at Highland Ave / Crocker St",
                    "Packard Ave / Powderhouse Blvd",
                    "Teele Square at 239 Holland St",
                    "Biogen Idec - Binney St / Sixth St",
                    "Charles St at Beacon St",
                    "BIDMC - Brookline at Burlington St",
                    "West Broadway at Dorchester St",
                    "Egleston Square at Columbus Ave",
                    "Hyde Square at Barbara St",
                    "JP Centre - Centre Street at Myrtle Street",
                    "Milk St at India St",
                    "JP Monument - South St at Centre St",
                    "Hayes Square at Vine St.",
                    "South Boston Library - 646 East Broadway",
                    "E. Cottage St at Columbia Rd",
                    "Upham's Corner - Ramsey St at Dudley St",
                    "Summer St at Cutter St",
                    "Green St T",
                    "Jackson Square T at Centre St",
                    "New Balance Store - Boylston at Dartmouth"
                ],
                "description": "station",
                "index": 0,
                "layout": "IPY_MODEL_76e3e01125c541fc9c954587dc573228",
                "style": "IPY_MODEL_4c9255a4260c4da783718b61af84cfe2"
            }
        },
        "81d52f1a222a47069d12e6a977bd1f8b": {
            "model_name": "LayoutModel",
            "model_module": "@jupyter-widgets/base",
            "model_module_version": "1.1.0",
            "state": {}
        },
        "4e18a8afe61d4a54b05994a9a429f401": {
            "model_name": "OutputModel",
            "model_module": "@jupyter-widgets/output",
            "model_module_version": "1.0.0",
            "state": {
                "layout": "IPY_MODEL_81d52f1a222a47069d12e6a977bd1f8b",
                "outputs": [
                    {
                        "output_type": "display_data",
                        "data": {
                            "text/plain": "<Figure size 360x432 with 1 Axes>",
                            "image/png": "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\n"
                        },
                        "metadata": {
                            "needs_background": "light"
                        }
                    }
                ]
            }
        }
    }
}
</script>
</head>
<body>

<script type="application/vnd.jupyter.widget-view+json">
{
    "version_major": 2,
    "version_minor": 0,
    "model_id": "4c18bfc755d54fc8a7b55ecd51185dad"
}
</script>

<script type="application/vnd.jupyter.widget-view+json">
{
    "version_major": 2,
    "version_minor": 0,
    "model_id": "4a727d12332a453b87a358225a58adab"
}
</script>

</body>
</html>

## Conclusion

How did we setup the datasets like we did. Before we setup the data,
firstly let's setup the data like we did.

Firstly, in a terminal window clone the git repository. Lorem ipsum
dolor sit amet, consectetur adipiscing elit. Nam dictum venenatis eros
sed dignissim. Vestibulum nisi lorem, bibendum ut est ut, pharetra
mattis enim. Aenean blandit ut nulla vehicula blandit. Duis non lectus
laoreet, ornare velit sit amet, vestibulum odio. Nullam fringilla
sodales justo. Morbi quis turpis maximus, vehicula massa sed, commodo
tortor. Interdum et malesuada fames ac ante ipsum primis in faucibus.
Suspendisse sed est a velit cursus imperdiet. Ut est diam, dignissim
eget metus eu, semper tincidunt nulla.

Duis volutpat in lorem et vehicula. Fusce fringilla, est in pulvinar
accumsan, diam ligula auctor lorem, vitae ultrices ante ex in urna.
Pellentesque pellentesque ultricies ligula, eu posuere risus eleifend
nec. Sed vulputate sollicitudin magna, pulvinar fringilla magna cursus
id. Cras ut ex sit amet nulla aliquet eleifend vel sed arcu. Suspendisse
quis convallis arcu. Nunc gravida quis tellus sed placerat. Nunc
facilisis suscipit augue, ut tincidunt mi vulputate sed.

Maecenas efficitur magna sed fermentum pretium. Aliquam mattis ante et
vestibulum fermentum. Phasellus efficitur maximus eros. Quisque vitae
tortor erat. Phasellus id iaculis massa, imperdiet sollicitudin ante.
Aenean ultricies ex erat. Proin vehicula nunc eu nulla scelerisque, non
porta metus laoreet. Mauris tincidunt ante elit, et cursus justo
pellentesque vel. Morbi ut pulvinar est. Maecenas arcu quam, mattis
vitae quam et, sodales porta ante. Orci varius natoque penatibus et
magnis dis parturient montes, nascetur ridiculus mus. Aliquam erat
volutpat. Pellentesque a tempor lorem, non fermentum nulla. Suspendisse
potenti.

Donec efficitur faucibus tellus ac rhoncus. Nam condimentum interdum
lorem nec hendrerit. Sed id nunc lectus. Integer cursus mauris suscipit
arcu bibendum, non ullamcorper turpis vestibulum. Sed aliquet, dui sit
amet feugiat condimentum, ex ipsum faucibus magna, sit amet lacinia
lorem nisl a velit. Nam facilisis ullamcorper porttitor. Donec finibus,
diam a finibus volutpat, lacus
