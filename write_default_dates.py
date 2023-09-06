import os
import pickle
from dotenv import load_dotenv
from typing import Final

from clean_wiki_data import get_cleaned_dates

# Load .env
load_dotenv()

# Constants
SAVED_DATES_FILEPATH: Final = os.getenv("SAVED_DATES_FILEPATH")

def __load_saved_dates():
    try:
        with open(SAVED_DATES_FILEPATH, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []

def __save_dates(saved_dates):
    with open(SAVED_DATES_FILEPATH, "wb") as file:
        pickle.dump(saved_dates, file)

def write_default_dates():
    # Load the existing saved_dates or initialize an empty list
    saved_dates = __load_saved_dates()

    # Get the default dates from the external script
    default_dates = get_cleaned_dates()

    # Append default dates to the saved_dates list
    saved_dates.extend([(0, date) for date in default_dates])

    # Save the updated saved_dates list to the file
    __save_dates(saved_dates)

    print("[DEFAULT_DATE][FILE_UPDATE] Default dates added to saved_dates.")

if __name__ == "__main__":
    write_default_dates()