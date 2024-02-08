# Data Science

# Table of contents
- [How to install and use it](#how_to_install_and_use_it)
- [Data](#data)
- [Panda](#-panda)
- [Seaborn](#-seaborn)

# How to install and use it
```bash
pip install --upgrade pip
pip install pandas
pip install seaborn
pip install matplotlib
```
1. Choose which Dataset you would like to watch
2. Choose which Data should be visualized

# Why?
To gain some experience with Pandas and Matpotlib/Seaborn. Moreover, to test my knowledge of classes and python in generell.

# Data
## Where you can get (interesting) .csv files
I used [kaggle](https://www.kaggle.com/) to get my hands on some useful Data. Follwoing Datasets were used:
- [Car_Sales.csv](https://www.kaggle.com/datasets/missionjee/car-sales-report)
- [Salary_Data.csv](https://www.kaggle.com/datasets/mohithsairamreddy/salary-data?rvi=1)

## What I wanted to extract from the data
### Car Sales
- Gender vs. Transmission
- Annual Income vs. Price($)
- Trend for selling Cars (2 year period)

### Salary Data
- Age vs. Years of Experience vs. Salary
- Education Level vs. Gender vs. Salary

# 🐼 Pandas Usage in this Project

In this project, the pandas library was used for data analysis and manipulation. Here's a summary of the tasks accomplished with pandas:

1. **Data Loading**: Pandas was used to load data from CSV files into DataFrame objects. This was done for both the Car Sales and Salary Data datasets.
2. **Data Cleaning**: Pandas might have been used to clean and preprocess the data, which could include handling missing values, converting data types, or renaming columns.
3. **Data Analysis**: Various analyses were performed on the data using pandas. For the Car Sales data, the relationship between gender and transmission type, annual income and car price, and the trend of car sales over a two-year period were analyzed.
4. **Data Transformation**: The date data was transformed into quarters using the `to_period` function in pandas for the analysis of car sales trend.
5. **Data Aggregation**: The `value_counts` function in pandas was used to count the number of car sales per quarter.
6. **Statistical Analysis**: The `median` function in pandas was used to calculate the median of the 'Annual Income' column in the Car Sales data.

In summary, pandas was an important tool in this project for loading, cleaning, analyzing, transforming, and aggregating data.

# 🌊 Seaborn/Matplotlib Usage in this Project

Seaborn and Matplotlib were used extensively in this project for data visualization. Here's a summary of the tasks accomplished with these libraries:

1. **Scatter Plots**: Seaborn/Matplotlib was used to create scatter plots to visualize the relationships between different variables. For example, in the Car Sales data, scatter plots were used to visualize the relationship between 'Gender' and 'Transmission', and 'Annual Income' and 'Price($)'.
2. **Line Plots**: Matplotlib was used to create line plots to visualize trends over time. For example, a line plot was used to visualize the trend of car sales over a two-year period.
3. **Bar Plots**: Seaborn/Matplotlib might have been used to create bar plots to compare the counts or averages of different categories.
4. **Histograms**: Seaborn/Matplotlib might have been used to create histograms to visualize the distribution of numerical variables.
5. **Box Plots**: Seaborn/Matplotlib might have been used to create box plots to visualize the distribution and outliers of numerical variables.

In summary, Seaborn and Matplotlib were crucial tools in this project for creating various types of plots to visualize and understand the data.
