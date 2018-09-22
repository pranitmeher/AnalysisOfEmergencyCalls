Read ME
=================================================================================================
Files :

clustering_location.py
dataCheckBaltimore.py
DataCleaningBaltimore.py
Google_map_plotter-3.py
Google_map_plotter-4.py
heatmap-6.py
heatmap-8.py
text to csv.py
time_graph.py

-------------------------------------------------------------------------------------------------
Database URL : https://data.baltimorecity.gov/Public-Safety/911-Calls-for-Service/xviu-ezkt

-------------------------------------------------------------------------------------------------
Database Cleaning: 

****You will have to change the folder path and the name for your database****

1) Run dataCheckBaltimore.py to check the data for row count and column values 
2) Run csv_writer.py to convert the data files into CSV format for the Weka to read
3) Run DataCleaningBaltimore.py to clean the NULL rows and zero figure values
4) Run LOC_filter.py to filter all the invalid locations and limit the dataset to Baltimore
5) Run clustering_location.py to separate the location information to run on WEKA

Data Analysis :

****You will have to change the folder path and the name for your database****

1) Run heatmap-6.py to generate a overall database heatmap with large bin values and detailed analysis
2) Run heatmap-8.py to generate Heatmaps for specific priority with detailed view and high bin count
3) Run Time-Graph.py to seperate the hour for each entry and Run the CSV file in the WEKA to get the analysis
4) Run Google_map_plotter-3.py to generate the Google Map output for the cluster size 10
5) Run Google_map_plotter-4.py to generate the Google Map output for the cluster size 50
6) Run the CSV files on the WEKA and select clustering as K-Means and respective K.

=================================================================================================