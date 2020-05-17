# --------------
import numpy as np 
import pandas as pd 
import seaborn as sns
import calendar
import warnings
from matplotlib import pyplot as plt
warnings.filterwarnings('ignore')

def line_chart(df, period, col):
    if period == "Month":
        data = df.groupby(df.index.month).mean()
    elif period == "Day":
        data = df.groupby(df.index.day).mean()
    elif period == "Year":
        data = df.groupby(df.index.year).mean()
    
    calendar_months = calendar.month_name[1:]
    x_series = calendar_months
    y_series = data[col]

    plt.plot(x_series, y_series)
    plt.title('Temperature Trend, 2012')
    plt.xlabel(period)
    plt.xticks(rotation=90)
    plt.ylabel(col)
    plt.show()

def plot_categorical_columns(df):
    categorical_columns = df.select_dtypes(include=['object']).categorical_columns

    for i in range (0,len(categorical_columns),2):
        if len(categorical_columns) > i+1:

            plt.figure(figsize=(10,4))
            plt.subplot(121)
            df[categorical_columns[i]].value_counts(normalize=True).plot(kind='bar')
            plt.title(categorical_columns[i])
            plt.subplot(122)
            df[categorical_columns[i+1]].value_counts(normalize=True).plot(kind='bar')
            plt.title(categorical_columns[i+1])
            plt.tight_layout()
            plt.show()

        else:
            df[categorical_columns[i]].value_counts(normalize=True).plot(kind='bar')
            plt.title(categorical_columns[i])
            plt.show()


def plot_categorical_columns(df):
    categorical_columns = df.select_dtypes(include=['object']).columns

    for i in range(0,len(categorical_columns),2):
        if len (categorical_columns) > i+1:

            plt.figure(figsize=(10,4))
            plt.subplot(121)
            df[categorical_columns[i]].value_counts(normalize=True).plot(kind='bar')
            plt.title(categorical_columns[i])
            plt.subplot(122)
            df[categorical_columns[i+1]].value_counts(normalize=True).plot(kind='bar')
            plt.title(categorical_columns[i+1])
            plt.tight_layout()
            plt.show()

        else:
            df[categorical_columns[i]].value_counts(normalize=True).plot(kind='bar')
            plt.title(categorical_columns[i])
            plt.show()

def plot_cont(df,plt_typ):
    numeric_columns = df.select_dtypes(include=['number']).columns.tolist()
    df=df[numeric_columns]

    for i in range(0,len(numeric_columns),2):
        if len(numeric_columns) > i+1:
            plt.figure(figsize=(10,4))
            plt.subplot(121)

            if plt_typ == 'boxplot':
                sns.boxplot(df[numeric_columns[i]])
                plt.subplot(122)
                sns.boxplot(df[numeric_columns[i+1]])
            elif plt_typ == 'displot':
                sns.boxplot(df[numeric_columns[i]])
                plt.subplot(122)
                sns.displot(df[numeric_columns[i+1]])
            else:
                print('Pass either distplot/boxplot')

        plt.tight_layout()
        plt.show()


def group_values(df,col1,agg1,col2):
    aggregate = {'mean':np.mean, 'max':np.max, 'min':np.min}
    grouping = df.groupby(col1).agg(aggregate[agg1])
    plt.figure(figsize=(10,4))
    plt.ylabel(col2)
    grouping[col2].plot(kind='bar')
    plt.show()


weather_df=pd.read_csv(path, parse_dates=True, index_col='Date/Time')
print(weather_df.head(5))
print(weather_df.shape)

line_chart(weather_df,'Month','Temp (C)')

plot_categorical_columns(weather_df)

plot_cont(weather_df, 'distplot')

plot_cont(weather_df, 'boxplot')

group_values(weather_df, 'Weather','mean','Visibility (km)')









