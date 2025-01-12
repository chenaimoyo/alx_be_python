from datetime import datetime, timedelta





def display_current_datetime():

    current_date = datetime.now()

    format_date = current_date.strftime("%Y-%m-%d %H:%M:%S                                       ")

    print(f"Current date and time: {format_date}")





def calculate_future_date():

    current_date = datetime.now()

    days_to_add = int(input("Enter the number of days to add to the current date: "))



    future_date = current_date + timedelta(days=days_to_add)

    format_future_date = future_date.strftime("%Y-%m-%d")



    print(f"Future Date: {format_future_date}")





def main():

    display_current_datetime()

    

    calculate_future_date()



if __name__ == "__main__":

    main()
