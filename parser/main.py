import pandas
import time


def create_new_dataframe():
    start_time = time.perf_counter()
    data = pandas.read_csv('data.csv')
    end_time = time.perf_counter()

    elapsed_time = end_time - start_time
    print(f"Reading CSV took {elapsed_time:.6f} seconds.")

    countries = ['United States', 'United Kingdom', 'Brazil', 'Germany', 'Italy']

    start_time = time.perf_counter()
    filtered_data = data[data['region'].isin(countries)]
    end_time = time.perf_counter()

    elapsed_time = end_time - start_time
    print(f"Filtering CSV took {elapsed_time:.6f} seconds.")

    filtered_data.to_csv('filtered_data.csv', index=False)


def test():
    start_time = time.perf_counter()
    data = pandas.read_csv('filtered_data.csv')
    end_time = time.perf_counter()

    elapsed_time = end_time - start_time
    print(f"Reading filtered CSV took {elapsed_time:.6f} seconds.")


if __name__ == '__main__':
    test()
