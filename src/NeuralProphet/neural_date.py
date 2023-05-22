
import datetime
def get_current_date():
    """This function does the following: It gets the current date and returns it in the format YYYY-MM-DD

    Args: None
    
    Returns: The current date (str) in the format YYYY-MM-DD
    """
        
    return datetime.date.today().strftime('%Y-%m-%d')


def subtract_years(date_str : str, years: int):
    
    """This function does the following: It subtracts a number of years from a given date and returns the new date in the format YYYY-MM-DD
    
    Args: date_str (str): The date to be subtracted from in the format YYYY-MM-DD
          years (int): The number of years to be subtracted from the date
    
    Returns: The new date (str) in the format YYYY-MM-DD
    """
    
    date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
    
    new_date_obj = date_obj - datetime.timedelta(days=365*years)
    
    
    return new_date_obj.strftime('%Y-%m-%d')
