# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 14:45:05 2021

@author: HaNin4Com
"""


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:        
        city = str( input("Please enter one of these cities to analyze (chicago, new york city, washington):"))
        city = city.lower()
        print("you chose {}".format(city))
        if city not in ['chicago', 'new york city', 'washington']:
            print("please choose from the city list")
            continue
    # get user input for month (all, january, february, ... , june)
        month = str(input("enter a month from this list to analyze (all, january, february, ... , june):"))
        month = month.lower()
        print("you chose {}".format(month))
        if month not in ['all', 'january', 'february','march', 'april' ,'may', 'june']:
            print("please choose from the month list")
            continue
    # get user input for day of week (all, monday, tuesday, ... sunday)
        day = str(input("enter a day to analyze (all, monday, tuesday, ... sunday):"))
        day = day.lower()
        print("you chose {}".format(day))
        if day  not in  ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
            print("please choose from the day list")
            continue
       
        else:
            break
         
        
           
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df
    
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].mode()[0]
    print("Most common month is:",most_common_month)
    # display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print("Most common day is ",most_common_day)
    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode()[0]
    print("Most common start hour is:",most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("Most common start station is:\n",most_common_start_station)
    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("\nMost common end station is:\n",most_common_end_station)
    # display most frequent combination of start station and end station trip
    
    df["From To Trip"] = 'From '+ df["Start Station"]+' to ' + df["End Station"] 
    most_frequent_Trip = df["From To Trip"].mode()[0]
    print("\nMost frequent trip is:\n",most_frequent_Trip)
    #most_frequent_Trip = df['Start Station','End Station'].mode()[0]
    #print("Most frequent Trip is:",most_frequent_Trip)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    df['Trip Duration'] = df['End Time'] - df['Start Time']
    total_travel_time = df['Trip Duration'].sum()
    trips_count = df['Trip Duration'].count()
    print("Total travel time is:", total_travel_time)
    # display mean travel time
    mean_travel_time = total_travel_time / trips_count
    print("\nAverage travel time is:", mean_travel_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print("\nUser type count is:\n",user_type_count)
    # Display counts of gender
    if 'Gender'and'Birth Year' in df.columns:
    
        gender_count =  df['Gender'].value_counts()
        print("\nGender count is:\n",gender_count)
         
        most_common_birth_year = df['Birth Year'].mode()[0]
        print("\nMost common birth year is:",most_common_birth_year )
        
        earliest_year_of_birth = df['Birth Year'].min()
        print("\nEarliest year of birth:",earliest_year_of_birth)
        
        most_recent_year_of_birth = df['Birth Year'].max()
        print("\nMost recent year of birth:",most_recent_year_of_birth)
    else:
        print("\nThis city has no information about gender or birth year!")
    # Display earliest, most recent, and most common year of birth
    #earliest_year_of_birth = df['Birth Year'].min()
    #print("Earliest year of birth:",earliest_year_of_birth)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
    
#def view_data(df):
    #start_loc = 0
    #while True:
        #view_data = input('\nWould you like to view (another) 5 rows of individual trip data? Enter yes or no\n')
        #print(df.iloc[start_loc:start_loc+5])
        #start_loc += 5
        
        #if view_data.lower() != 'yes':
            #break
        
def view_data(df):           
    start_loc = 0
    view_data = input('\nWould you like to view  5 rows of individual trip data? Enter yes or no\n')    
    if view_data.lower() != 'no':
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
       
        while True:
        
            view_data = input('\nWould you like to view (another) 5 rows of individual trip data? Enter yes or no\n')    
            print(df.iloc[start_loc:start_loc+5])
            start_loc += 5
        
            if view_data.lower() != 'yes':
                break
    
                       

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
