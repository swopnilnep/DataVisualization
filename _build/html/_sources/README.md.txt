# US Bikeshare Data Visualization

In this project, we aim to analyze and create visualizations based on 2 of the US's most popular bikeshare service providers: CitiBike in NYC and BlueBikes in Boston. Based on the data we will compare several stories that underly within the data. 

## Setup Instructions
Firstly, in a terminal window clone the git repository: 
```
$ git clone https://github.com/swopnilnep/DataVisualization
$ cd /data/bikeshare/
```

If the directory does not exist, make a directory in the location
```
$ mkdir data`
$ cd data`
$ mkdir nyc unified boston
```


Get the NYC data from here: 
* [Stations](https://feeds.citibikenyc.com/stations/stations.json) - Save to `/data/bikeshare/data/nyc/stations.json`
* [Data](https://s3.amazonaws.com/tripdata/index.html) - Save to `/data/bikeshare/data/nyc/nyc.csv`

Get the Boston data from here: 
* Stations - Included in trip history download
* [Data](http://files.hubwaydatachallenge.org/hubway_2011_07_through_2013_11.zip) -  Save to `/data/bikeshare/data/boston/boston.csv`

In your repository, navigate to `./scripts` and run all three scripts in this particular order.
```
$ python3 nyc_normalize.py
$ python3 boston_normalize.py
$ python3 merge_datasets.py
```
Make sure you have pandas and numpy installed through either pip or Anaconda

## Sources
* BuzzFeed Bikeshare Data Visualization
* Citibike - NYC Bikeshare Data
* Hubway - Boston
