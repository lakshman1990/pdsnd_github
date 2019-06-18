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
        try:
            city = input("Enter the name of the city (chicago, new york city, washington) to analyze: ").lower()
        except:
            print('\nNot a valid city, please try again!')
            continue
        
        if city not in ('chicago','new york city','washington'):
            print('\nNot a valid city, try again')
            continue
        else:
            break
    
    # get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input("Enter the name of the month to filter by, or 'all' to apply no month filter: ").lower()
        except:
            print('\nNot a valid month, please try again!')
            continue
        
        if month not in ('all','january','february','march','april','may','june'):
            print('\nNot a valid month, try again')
            continue
        else:
            break
    
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input("Enter the name of the day of week to filter by, or 'all' to apply no month filter: ").lower()
        except:
            print('\nNot a valid day of week, please try again!')
            continue
        
        if day not in ('all','monday','tuesday','wednesday','thursday','friday','saturday','sunday'):
            print('\nNot a valid day of week input, try again')
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
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        months = ['january','february','march','april','may','june']
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
    monthCount = df['month'].mode()[0]
    print('Most Common Month:',monthCount)
    # display the most common day of week
    dayOfWeek = df['day_of_week'].mode()[0]
    print('Most Common Day of Week:',dayOfWeek)
    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    startHour = df['hour'].mode()[0]
    print('Most Common Start Hour:',startHour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    startStation = df['Start Station'].mode()[0]
    print('Most Common Start Station:',startStation)
    # display most commonly used end station
    endStation = df['End Station'].mode()[0]
    print('Most Common End Station:',endStation)

    # display most frequent combination of start station and end station trip
    df['Combination Station'] = df['Start Station'] + '/' + df['End Station']
    print('Frequent Trip Station Combination:',df['Combination Station'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    totalTime = df['Trip Duration'].sum()
    print('Total Travel Time:',totalTime)
    # display mean travel time
    meanTime = df['Trip Duration'].mean()
    print('Mean Travel Time:',meanTime)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    userTypeCounts = df['User Type'].value_counts()
    print('Counts of User Types:\n',userTypeCounts)
    print('\n')
    # Display counts of gender
    if 'Gender' in df.columns:
        genderCounts = df['Gender'].value_counts()
        print('Counts of Gender:\n',genderCounts)
    else:
        print('\nGender column not available in the city you entered to provide the data')
    print('\n')
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliestYear = int(df['Birth Year'].min())
        recentYear = int(df['Birth Year'].max())
        commonYear = int(df['Birth Year'].mode()[0])
    
        print('Earliest: {}, most recent: {}, and most common year of birth: {}'.format(earliestYear,recentYear,commonYear))
    else:
        print('\nBirth Year column not available in the city you entered to provide the data')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# Shows raw data to the users
def showRawData(cityName):
    raw_data = pd.read_csv(CITY_DATA[city])
    row_count = 5
    while True:
        try:
            print(raw_data.iloc[:row_count,:raw_data.shape[1]])
            requestData = input('\nDo you want to see more raw data for the city you selected?\n')
        except:
            continue
        
        if requestData.lower() == 'yes':
            row_count = row_count + 5
            continue
        else:
            break
       

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        rawData = input('\nWould you like to view the raw data of the city you selected?\n')
        if rawData.lower() != 'yes':
            break
        else:
            showRawData(cityName)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
