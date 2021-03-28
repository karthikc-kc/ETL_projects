# ETL_projects
sparkify project and pipelines

This Projects aims to deliver a seamless data pipelines to extract data from sparkfiy app and Load it into sparkify database. 
The dataset created will serve the Analytics team to understand the users and choices in order to create good playlist. 

> Tech Details:

1. Used Pyspark frame to load data from the JSON files into the PostgreSQL. 
2. Created Tables in PostgreSQL. 

> Data Modeling:
1. Created four Dimension Tables to store information related USers, Song, Artist and Time.
2. Created One fact Transaction table which holds information on User's activity. 
3. Star Schema Model to answer the questions or gain insights like Users Interest, Trending Albums. 

![image](https://user-images.githubusercontent.com/80103842/112745768-6c693f00-8fc8-11eb-8c93-8f79a0032bf7.png)




