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

Instructions to Install:
1. clone the Repo.
2. Download the files from http://millionsongdataset.com/
3. Install required packages, python version 3 and above, PySparkAPI, Postgreclient API.
4. Install Jupyter notebook for testing.

For ETL:
Step 1: Ensure to download the required source file. 
Step 2: Run the Create_table.py.
Step 3: Run the test.ipynb to check whether the table has been created or not.
Step 4: Run the etl.py. 


Note* Before running the etl.py, please test your ETL by using etl.ipynp as per the above mentioned steps. 


![image](https://user-images.githubusercontent.com/80103842/112745768-6c693f00-8fc8-11eb-8c93-8f79a0032bf7.png)




