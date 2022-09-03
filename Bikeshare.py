import time
import pandas as pd
import numpy as np
import os

CITY_DATA = { 'chicago': '/root/udecity/chicago.csv',
              'new york city': '/root/udecity/new_york_city.csv',
              'washington': '/root/udecity/washington.csv' }
MONTH_DATA = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

DAY_DATA = ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_name = ''
    while city_name.lower() not in CITY_DATA:
        city_name = input("\nchoose city  to analyze data? (E.g. Input either chicago, new york city, washington)\n")
        if city_name.lower() in CITY_DATA:
            city = CITY_DATA[city_name.lower()]
        else:
            print("The City you've entered isnt valid \n")

    # TO DO: get user input for month (all, january, february, ... , june)
    month = ''
    while(True):
        if(month == 'january' or month == 'february' or month == 'march' or month == 'april' or month == 'may' or month == 'june' or month == 'all'):
            break
        else:
            month = input('Enter a valid month : \n').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ''
    while(True):
        if(day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday' or day == 'saturday' or day == 'sunday' or day == 'all'):
            break
        else:
            day = input('Enter a valid day: \n').lower()

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
    df = pd.read_csv(city)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['month'] = df['Start Time'].dt.month_name()    
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        allmonths = ['january', 'february', 'march', 'april', 'may', 'june']
        month = allmonths.index(month) + 1
        df = df[df['Start Time'].dt.month == month]
        
    if day != 'all':
        df = df.loc[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].value_counts().idxmax()  
    print("The most common month : " + common_month)

    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].value_counts().idxmax()
    print("The most common day of week  :  " + common_day_of_week)

    # TO DO: display the most common start hour
    common_start_hour = df['hour'].value_counts().idxmax()
    print("The most common start hour : " + str(common_start_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The most common used start station is:", df['Start Station'].value_counts().idxmax(), '\n')

    # display most commonly used end station
    print("The most common used end station is:", df['End Station'].value_counts().idxmax(), '\n')

    # display most frequent combination of start station and end station trip
    df['start_end_station'] = df['Start Station'] + df['End Station']
    print("The most frequent combination trip is:", df['start_end_station'].value_counts().idxmax(), '\n')



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time is: " + str(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time is: " + str(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
        # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("count of differnt user:",user_types.to_frame())
    user_types = df['User Type'].value_counts()


    # Display counts of gender

    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print("counts of gender:",gender.to_frame())
    else:
        print("There is no Gender information")


    # Display earliest, most recent, and most common year of birth
    if 'Gender' in df.columns:
        early = df['Birth Year'].min()
        print("early birth:",int(early))
        recent = df['Birth Year'].max()
        print("recent birth:",int(recent))
        common_birth = df['Birth Year'].mode()
        print("common year:",int(common_birth))
    else:
        print("\n there is no gender information\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    data = 0
    while True:
       display = input('Would you like to see the first 5 lines of raw data? Choose Yes or No.\n').lower()
       if display == 'no':
            return
       elif display == 'yes':
        data += 5
        print(df.iloc[data:data+5])
       else:
        print('Choose Yes or No.\n') 

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
