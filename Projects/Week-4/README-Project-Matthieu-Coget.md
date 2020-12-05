![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Project: Visualization on the Terrorism attacks between 1970 and 2017 


## Content
- [Presentation of the project](https://docs.google.com/presentation/d/1Ai-mZfTvXBwPrxQzoZmWBExR1j0E8oJikONONBjCgnA/)
- [Project Description](#project-description)
- [Datas Approach](#datas-approach)
- [Code Approach](#code-approach)
- [Challenges](#challenges)
- [Lessons Learnt](#lessons_learnt)
- [Files](#files)

## Project Description

The goal of this project was visualize datas with Python. I searched datasets on different websites and choose one available on [Kaggle about Global Terrorism Attacks](https://www.kaggle.com/START-UMD/gtd) and after that I clean the dataset to analyse datas on it (the shape was at first 181691 rows per 135 columns) and after create visualizations to support this analysis.

As french citizens, we always think that the terrorism is a phenomenon only western countries. And when it's happening in another country, we only hear about Frenchs, Europeans or even North-Americans. The analysis and its visualization will show something really different.

### Datas Approach

At first, the challenge was to select a dataset already created with the objective of creating for datavisulations. After going through 5 datasets, the one on Global Terrorism Attacks seems to be interesting with a lot of values (more than 24.5 millions values in the dataset).

The point was to clean the dataset in a way it will be useful in a way to show the number of victims (killed and wounded), which are the most attacked countries by terrorists, evolution during time and if there is a clear evolution between decades and even if there is a tipping point during this period.

For that, the number of columns has been reduced to 45, even if some of them can have been dropped. Some of the columns contain only 1% of non-null datas.

### Code Approach

Before any visualization, the data have been reordered with two goals : the evolution through years and the most attacked countries. So pivot tables have been created to count those elements. Even if they won't always be used in a visualization, it could be handy during the presentation.

To create the different visualizations, it was necessary to use Matplotlib and Seaborn librairies to show histograms, bar graphs that show the different points. 
The map creation has been done with Geopandas library to show the number of terrorist attacks by country and after look at the evolution for every year. 


## Challenges

The first challenge was to find a dataset with enough data to analyse it and construct visualizations. After that, the dataset had to be cleaned to make it useful by reducing the number of columns and avoid data that would distort the analysis.

The second was to create pivot tables that are meaningful and can be used in the dataviz.

The visualization construction was a real challenge : even if the kind of graph seems to be clear, the data selection for each can be tricky. And after creating a visualization, it must be beautify with legend, title, color, scale, scale labels.

The maps creation have been a real challenge: first it was difficult to install Geopandas (8 libraries must be installed before accessing to this one). To avoid those installations and have a visualization more interactive, the folium library was tested to create a map with the 50 terrorist attacks that caused the most victims and the goal was to create a bubble map. But the use of this library need too much time to understand every point.
So it was decided to use the Geopandas library to create the different maps.


##  Lessons learned

* Prepare a DataFrame to make it useful for the analysis and the visualization.
* Use pivot tables to analyse datas.
* Merge DataFrames.
* Create beautiful visualizations and choose the right one for every case.
* Create a map with different libraries, choose the right library for the specific case.


## Files
* [Presentation of the project]()
* [Jupyter Notebook with the code]()
* [Data Folder]()
