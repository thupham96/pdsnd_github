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
    while True:
        city = input('Would you like to see results for Chicago, New York City, or Washington?\n')
        if city.lower() not in ("chicago","new york city","washington"):
            print("Invalid input. Please try again.")
            continue
        else:
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Which month? January, February, March, April, May, June, or all? Please type out the full month name.\n')
        if month.lower() not in ("january","february","march","april","may","june","all"):
            print("Invalid input. Please try again.")
            continue
        else:
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Which day? Please type your response as an integer (e.g., 1=Sunday) or all for no filter.\n')
        if str(day) not in ('1','2','3','4','5','6','7','all'):
            print("Invalid input. Please try again.")
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
    filename = CITY_DATA[city.lower()]

    if day == 'all':
        df = pd.read_csv(filename)
        if month != 'all':
            df['Start Time'] = pd.to_datetime(df['Start Time'])
            df = df[df['Start Time'].dt.strftime('%B') == month.capitalize()]
    else:
        df = pd.read_csv(filename)
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df = df[df['Start Time'].dt.dayofweek == int(day)]
        if month != 'all':
            df = df[df['Start Time'].dt.strftime('%B') == month.capitalize()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    most_common_month = df['month'].mode()[0]
    print("Most common month: {}".format(most_common_month))

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    most_common_day = df['day_of_week'].mode()[0]
    print("Most common day of week: {}".format(most_common_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print("Most common start hour: {}".format(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("Most commonly used start station: {}".format(popular_start_station))
    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("Most commonly used end station: {}".format(popular_end_station))
    # TO DO: display most frequent combination of start station and end station trip
    popular_combination = df.groupby(['Start Station','End Station']).size().sort_values().index[0]
    print('Most frequent combination of start station and end station trip: {}'.format(popular_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time: {}".format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time: {}".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(city, df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print("Counts of user types: {}".format(user_type_count))

    # TO DO: Display counts of gender
    if city.lower() in ('new york city','chicago'):
        gender = df['Gender'].value_counts()
        print("Counts of gender: {}".format(gender))
    else:
        print("No data for gender is available.")

    # TO DO: Display earliest, most recent, and most common year of birth
    if city.lower() in ("new york city","chicago"):
        earliest_birth_year = df['Birth Year'].min()
        print("Earliest birth year: {}".format(earliest_birth_year))
        most_recent_birth_year = df['Birth Year'].max()
        print("Most recent birth year: {}".format(most_recent_birth_year))
        most_common_birth_year = df['Birth Year'].mode()[0]
        print("Most common birth year: {}".format(most_common_birth_year))
    else:
        print("No data for birth year is available.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(city, df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
