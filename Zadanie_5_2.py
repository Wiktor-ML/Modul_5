# Punkt 1 Zdania
class movie:
    def __init__(self, title, release_date, gender, number_of_views):
        self.title = title
        self.release_date = release_date
        self.gender = gender
        self.number_of_views = number_of_views
        # Punkt 5 Zadania 
        self.name_for_output = title + " " + "(" + str(release_date) + ")"

# Punkt 3 Zadania    
    def play(self, step=1):
       self.number_of_views += step
     
    def __str__(self):
        return f"{self.name_for_output}"

# Punkt 2 Zdania
class serial(movie):
   def __init__(self, number_of_season, number_of_episode, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.number_of_season = number_of_season
       self.number_of_episode = number_of_episode
       # Punkt 4 Zadania 
       self.name_for_output = self.title + " " + "S" + str(self.number_of_season).zfill(2) + "E" + str(self.number_of_episode).zfill(2)
    
   def __str__(self):
        return f"{self.name_for_output}"    

# Punkt 6 Zadania    
list_of_movies_and_series = []
    
titanic = movie("Titanic", "1997", "drama", 1000000)
list_of_movies_and_series.append(titanic)


simpson = serial(32,12, "Simpson", "2003", "comedy", 2000000)
list_of_movies_and_series.append(simpson)

blade_runner = movie("Blade Runner", "1982", "sci-fi", 3000000)
list_of_movies_and_series.append(blade_runner)

shogun_nx = serial(1, 9, "Shogun", "2024", "history", 9000000)
list_of_movies_and_series.append(shogun_nx)

# Punkt 7 Zadania    
def get_movies(list_of_movies_and_series):
    all_movies = [item for item in list_of_movies_and_series if isinstance(item, movie) and not isinstance(item, serial)]   
    return all_movies

def get_series(list_of_movies_and_series):
    all_series = [item for item in list_of_movies_and_series if isinstance(item, serial)]
    return all_series


# Punkt 8 Zadania    
def search(list_of_movies_and_series, title):  
    for item in list_of_movies_and_series:
        if item.title.lower() == title.lower():
            print(item)


# Punkt 9 Zadania    
import random

def generate_views(list_of_movies_and_series):
    random_number = random.randint(0, len(list_of_movies_and_series)-1)
    logging.debug(f" Choose index {random_number}")
    logging.debug(f" Chosen item: {list_of_movies_and_series[random_number]}")
    logging.debug(f" Number of views before: {list_of_movies_and_series[random_number].number_of_views}")
    random_added_views = random.randint(1, 100)
    logging.debug(f" Random added views: {random_added_views}")
    list_of_movies_and_series[random_number].number_of_views += random_added_views       
    logging.debug(f" Number of views after: {list_of_movies_and_series[random_number].number_of_views}")
    return(list_of_movies_and_series)

# Punkt 10 Zadania    
def generate_views_10_times():
    for _ in range(10):
        generate_views(list_of_movies_and_series)

# Punkt 11 Zadania    
import logging
logging.basicConfig(level=logging.DEBUG)

def top_titles(list_of_movies_and_series, number_of_movies_to_display, content_type):
    if content_type == movie:
        list_of_items = get_movies(list_of_movies_and_series)
        
    elif content_type == serial:
        list_of_items = get_series(list_of_movies_and_series)
        
    elif content_type == " ":
        list_of_items = list_of_movies_and_series
    else:    
        logging.error("Invalid content type, please try again")
        exit(1)

    
           
    sorted_list = sorted(list_of_items, key=lambda x: x.number_of_views, reverse=True)

    return_items = []
    
    for item in sorted_list[:number_of_movies_to_display]:
        if number_of_movies_to_display > len(sorted_list):
            logging.error(f"Number of items to display is greater than number of movies/series in the list, please try again with smaller number. "
                         f"There are only {len(sorted_list)} {content_type.__name__}s in the library")
            exit(1)
        else:
            return_items.append(item)
    return(return_items)
       

 # Zadanie dla chetnych: punkt 1
 
def put_series_to_library(library_name, series_name, release_date, gender, number_of_seasons, number_of_episodes):
    for number_of_season in range(1, number_of_seasons + 1):
        for number_of_episode in range(1, number_of_episodes + 1):
            new_series = serial(number_of_season, number_of_episode, series_name, release_date, gender, number_of_views=0)
            library_name.append(new_series)
    return library_name

#To test if the function works uncommend the line below:
#put_series_to_library(list_of_movies_and_series,"Last dance", "2021", "documentary", 2, 10)


# Zadanie dla chetnych: punkt 2

def count_total_number_of_episodes(library, series_name):
    count = 0
    for item in library:
         if isinstance(item, Serial) and item.title == series_name:
             count += 1
    return(count)

print("Biblioteka filmow")

generate_views(list_of_movies_and_series)

from datetime import datetime

current_date = datetime.now()

formatted_date = current_date.strftime("%d.%m.%Y")


print(f"Najpopularniejsze trzy filmy i seriale dnia {formatted_date} to: ")

three_top_titles_of_movies_and_series = top_titles(list_of_movies_and_series, 3, " ")
for item in three_top_titles_of_movies_and_series:
    print(item)
