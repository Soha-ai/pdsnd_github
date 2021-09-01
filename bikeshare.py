#Hi GitHub community
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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city= input("Which city you want to show it's data (chicago, new york city or washington): ").lower()
    while city not in CITY_DATA:
        print("Sorry, you wtite a non exist chocie could you pleas reinsert a right one")
        city= input("Which city you want to show it's data (chicago, new york city or washington): ").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = 'all'
    months=['january', 'february', 'march', 'april', 'may', 'june']
    print("Do you want to show data of 'all month' or data for 'specifc month' from {}? ".format(months))
    m= input("write 'all' for all month or 'sm' for specifc month ").lower()
    while m != 'all' and m!='sm':
        print("Sorry, you wtite a non exist chocie could you pleas reinsert a right one")
        m= input("write 'all' for all month or 'sm' for specifc month ").lower()
    if m == 'sm':
        month = input("write month from list {} ".format(months))
        while month not in months:
            print("Sorry, you wtite a non exist chocie could you pleasr reinsert a right one")
            month = input("write month from list {} ".format(months)).lower()
    elif m == 'all':
        month = 'all'



    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = 'all'
    days=['monday','tuesday','wednesday','thursday','friday','saturday']
    print("Do you want to show data of 'all week' or data for 'one day of week' from {}? ".format(days))
    d= input("write 'all' for all week or 'sd' for specifc day ").lower()
    while d != 'all' and d!='sd':
        print("Sorry, you wtite a non exist chocie could you pleas reinsert a right one")
        d= input("write 'all' for all week or 'sd' for specifc day ").lower()

    if d == 'sd':
        day = input("write day from list {} ".format(days)).lower()
        while day not in days:
            print("Sorry, you wtite a non exist chocie could you pleas reinsert a right one")
            day = input("write day from list {} ".format(days)).lower()
    else:
        day = 'all'


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
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = pd.DatetimeIndex(df['Start Time']).month
    df['day'] = pd.DatetimeIndex(df['Start Time']).weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month
    df['month']=pd.DatetimeIndex(df['Start Time']).month
    m=df['month'].mode()[0]


    # TO DO: display the most common day of week
    df['day']=pd.DatetimeIndex(df['Start Time']).weekday_name
    d=df['day'].mode()[0]


    # TO DO: display the most common start hour
    df['hour']=pd.DatetimeIndex(df['Start Time']).hour
    h=df['hour'].mode()[0]

    print("The Most common month: {} ,\n The most common day: {},\n The most common hour: {}".format(m,d,h))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    start= df['Start Station']
    # TO DO: display most commonly used start station
    most_start= start.mode()[0]


    end= df['End Station']
    # TO DO: display most commonly used end station
    most_end= end.mode()[0]


    # TO DO: display most frequent combination of start station and end station trip
    frequent= start + end
    most_frequent= frequent.mode()[0]

    print("The Most common used start station: {} ,\nThe most common used end station: {},\nThe most common frequent trip: {}".format(most_start,most_end,most_frequent))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    trip= df['Trip Duration']
    # TO DO: display total travel time
    total= trip.sum()


    # TO DO: display mean travel time
    average= trip.mean()

    print("The total of travel time: {} ,\nThe average of travel time: {}".format(total,average))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user= df['User Type']
    # TO DO: Display counts of user types
    user_type = user.value_counts()

    print("The number of user type is:\n{} ,".format(user_type))


    if 'Gender' not in df.columns:
        print("there is no gender and birth columns in washington data")
    else:
        gender=df['Gender']
        # TO DO: Display counts of gender
        gender_count= gender.value_counts()

        birth=df['Birth Year']
        # TO DO: Display earliest, most recent, and most common year of birth
        earliest = min(birth)
        recent= max(birth)
        most_bith_year= birth.mode()[0]

        print("\nThe number count gender is:\n{},\nThe earliest year of birth of user is: {} ,\n".format(gender_count,earliest))
        print("The recent year of birth of user is: {} ,\nThe most year of birth of users is: {}".format(recent,most_bith_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart.lower() != 'yes':
            print("this is some row of file you display data from")
            show = 'y'
            i=0
            while show == 'y':
                print(df.iloc[i:i+5,:])
                i+=5
                print("Do you want to show more?")
                show= input("type 'y' for Yes or 'n' for No: ").lower()
                if show != 'y':
                    exit()


if __name__ == "__main__":
	main()
