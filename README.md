![YouTube_API_CoverImage](https://github.com/sebasquirarte/YouTube-API-Project/assets/39809366/70391465-7cad-4cfc-9b49-3f706c89b82c)

Sebastian Quirarte | sebastianquirajus@gmail.<nolink>com | in/sebastianquirarte | Last Updated: Nov 29 2023

# Objective

The aim of this project is to extract, transform, and visualize data from any YouTube channel and all its videos using the YouTube API using Python and PowerBI. In this case I wanted to analyze one of my favorite channels: *[Kurzgesagt – In a Nutshell](https://www.youtube.com/channel/UCsXVk37bltHxD1rDPwtNM8Q)*. 

# Overview

1. _**Data Extraction and Transformation**_: Extracting data directly from YouTube through their API and storing this data into dataframes.

2. _**Data Preprocesing**_: Converting data types, creating new columns and cleaning dataframes.

3. _**Visualization and Analysis**_ Visualizing and analyzing the data obtained from all the videos uploaded by the channel of interest.

4. _**Dashboard**_: Creating a dashboard in PowerBI of the data collected to display the project results in a concise manner.

# Libraries Used

- _**googleapiclient**_: The official Python client library for Google's discovery based APIs.
- _**pandas**_: data manipulation, analysis, and data structures and operations for manipulating numerical tables and time series.
- _**IPython**_: interactive command-line terminal for Python. Used in this case for JSON formatting.
- _**dateutil**_: helps you manipulate and work with dates and time stamps.
- _**isodate**_: implements ISO 8601 date, time and duration parsing.
- _**youtubeAPI**_: functions written specifically for this project, available in file *'youtubeAPI.py'*
- _**seaborn**_: data visualization library based on matplotlib.
- _**matplotlib**_: comprehensive library for creating static, animated, and interactive visualizations in Python.
- _**nltk**_: symbolic and statistical natural language processing (NLP) for English written in Python.
- _**wordcloud**_: word cloud generator in Python.  

# Results

### Plots Using Python
<img width="2000" alt="Plots1" src="https://github.com/sebasquirarte/YouTube-API-Project/assets/39809366/c40fa5c8-312b-4e86-9c29-06b34d85ba00">
<img width="1900" alt="Plots2" src="https://github.com/sebasquirarte/YouTube-API-Project/assets/39809366/77a01f76-c90a-49fa-8a0f-e11f2cbe0385">
<img width="1750" alt="Plots3" src="https://github.com/sebasquirarte/YouTube-API-Project/assets/39809366/3225289a-744b-4aa9-92e2-8a8dae720fe4">

### Dashboard PowerBI ([LINK](https://www.novypro.com/project/youtube-api-project-power-bi))
<img width="959" alt="YoutubeAPI Dashboard" src="https://github.com/sebasquirarte/YouTube-API-Project/assets/39809366/6c425d3d-0ca5-4669-a074-0b506ac0964b">

# Full project in Jupyter Notebook
- [Jupyter Notebook](https://github.com/sebasquirarte/YouTube-API-Project/blob/main/Youtube-API.ipynb)
