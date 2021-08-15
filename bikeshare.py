import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
city_name = ['chicago', 'new york city', 'washington']
months = ['january', 'feburary', 'march', 'april', 'may', 'june', 'all']
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']


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
    try:
        city = input ('Would you like to see data for Chicago, New York City or Washington?\n').lower()   
        while city not in city_name:
            print("You entered a invalid ", city, " please try again.")
            city= input ("Please select either Chicago, New York City or Washington\n").lower()
            if city in city_name:
                break
        print("You select ", city, " thank you.")
    except:
        print('Error Occured')

    # TO DO: get user input for month (all, january, february, ... , june)
    try:
        month =  input('Please enter one of the following months: All, January, February, March, April, May, or June.\n').lower()
        while month not in months:
           print("You entered a invalid ", month, " please try again") 
           month = input ("Please select either one of the following: All, January, February, March, April, May, or June. \n").lower()
           if month in months:
                break
        print("You select ", month, " thank you.")
    except:
        print('Error Occured')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    try:
        day =  input('Please enter one of the following months: All, Monday, Tuesday, Wednesday, Thursday, Friday, or Saturday.\n').lower()
        while day not in days:
           print("You entered a invalid ", day, " please try again") 
           day = input ("Please select either one of the following: All, Monday, Tuesday, Wednesday, Thursday, Friday, or Saturday.\n").lower()
           if day in days:
                break
        print("You select ", day, " thank you.")
    except:
        print('Error Occured')    


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
    
    df = pd.read_csv(CITY_DATA [city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['days_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        months = ['january', 'feburary', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
        
    if day != 'all':
        df = df[df['days_of_week'] == day.title()]
    
    return df

def time_stats(df, month):
    """Displays statistics on the most frequent times of travel."""
        
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
  
    # TO DO: display the most common month
    if df['month'].to_string() != month:
        popular_month = df['month'].mode()[0]
        print('Most common month:', popular_month)
    else:
        print('Most common month: not available since you have selected a specific month.')

    # TO DO: display the most common day of week
    popular_weekday = df['days_of_week'].mode()[0]
    print('Most common day of week:', popular_weekday)

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most common hour of day:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    print('Most commonly used start station:', popular_start) 

    # TO DO: display most commonly used end station
    popular_start = df['Start Station'].mode()[0]
    print('Most commonly used start station:', popular_start)

    # TO DO: display most frequent combination of start station and end station trip
    df['station_combination']= df['Start Station'] + ':' + df['End Station']
    popular_station_combination = df['station_combination'].mode()[0]
    print('Most commonly used combination of stations:', popular_station_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    sum_travel_time = df['Trip Duration'].sum() / 60 / 60
    print('total travel time:', sum_travel_time, 'hours')

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean() / 60
    print('mean travel time:', mean_travel_time, 'minutes')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts().to_frame()
    print('Distribution of user types:', user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
       gender_count = df['Gender'].value_counts().to_frame()
       print('Distribution of gender:', gender_count)
    else:
       print("No gender data to share.")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        most_recent_birthyear = df['Birth Year'].max()
        print('Most recent birth year:', int(most_recent_birthyear))
        earliest_birthyear = df['Birth Year'].min()
        print('Earliest birth year:', int(earliest_birthyear))
        most_common_birthyear = df['Birth Year'].mode()[0]
        print('Most common birth year:', int(most_common_birthyear))
    else:
        print("No birth year data to share.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?\n").lower()
    start_loc = 0
    end_loc = 5
    while True:
        if view_data != 'no':
           print(df.iloc[start_loc:end_loc])
           start_loc += 5
           end_loc += 5
        if view_data != 'yes':
            break
        view_display = input("Do you wish to continue?: ").lower()
        if view_display != 'yes':
            break
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break



if __name__ == "__main__":
    main()