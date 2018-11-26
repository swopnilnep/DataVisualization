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

## IPython Notebooks 
 Title  | Description | Link |
|---|---|---| 
|Preliminary Analysis | Looking at the ridership of the NYC and Boston Bicycles and various other variables that add to it like gender and membership.| [![img](./images/link.png)](ipython/analysis_giang.ipynb) |
| 2D Data Analysis | Some other stages of the data analysis including 2 dimensional data as well as grouping the data by various variables |[![img](./images/link.png)](ipython/analysis_swopnil.ipynb) |
| Geographical Analysis | Looking at latitudes and longitudes and plotting them in heatmaps and animations in a geographical plane | [![img](./images/link.png)](ipython/gmaps_visualizations.ipynb.ipynb) |

## Journals
| Date  | Title  | Author | Link |
|---|---|---|---|
| `2018-11-06`  | Selecting the Dataset: Motivations, Goals, Initial Ideas  | Swopnil | [![img](./images/link.png)](journals/20181106_swopnil.md) |
| `2018-11-09`  | Selecting the Modules and Languages: Which languages we are using and why?  | Swopnil | [![img](./images/link.png)](journals/20181109_swopnil.md) |
| `2018-11-10`  | Git Commands | Giang | [![img](./images/link.png)](journals/20181110_giang.md) |
| `2018-11-10`  | Data Visualization Project Management Schedule | Swopnil | [![img](./images/link.png)](journals/20181115_swopnil.md) |
| `2018-11-11`  | Markdown Lesson | Giang | [![img](./images/link.png)](journals/20181111_giang.md) |
| `2018-11-12`  | Transcription and Unification of the datasets | Giang | [![img](./images/link.png)](journals/20181122_giang.md) |

## Sources
* BuzzFeed Bikeshare Data Visualization
* Citibike - NYC Bikeshare Data
* Hubway - Boston
