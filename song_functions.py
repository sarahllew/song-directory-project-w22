#11.2 
def print_main_menu(menu):
    """
    Given a dictionary with the menu,
    prints the keys and values as the
    formatted options.
    Adds additional prints for decoration
    and outputs a question
    "What would you like to do?"
    """
    print("==========================")
    print("What would you like to do?")
    for key, option in menu.items():
        print(f'{key} - {option}')
    print("==========================")
    
def get_written_date(date_list):
    """
    The function takes a parameter a list of strings in [MM,DD,YYYY] format 
    returns the resulting date as a string
    """
    month_names = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }
    
    num = int(date_list[0])
    month = str(month_names[num])
    date = str(int(date_list[1]))
    year = str(date_list[2])
    
    written_date = month + " "+ date + "," + " " + year
    return written_date

######## LIST OPTION ######## 11.3 

def get_selection(action, suboptions, to_upper = True, go_back = False):
    """
    param: action (string) - the action that the user
            would like to perform; printed as part of
            the function prompt
    param: suboptions (dictionary) - contains suboptions
            that are listed underneath the function prompt.
    param: to_upper (Boolean) - by default, set to True, so
            the user selection is converted to upper-case.
            If set to False, then the user input is used
            as-is.
    param: go_back (Boolean) - by default, set to False.
            If set to True, then allows the user to select the
            option M to return back to the main menu

    The function displays a submenu for the user to choose from. 
    Asks the user to select an option using the input() function. 
    Re-prints the submenu if an invalid option is given.
    Prints the confirmation of the selection by retrieving the
    description of the option from the suboptions dictionary.

    returns: the option selection (by default, an upper-case string).
            The selection be a valid key in the suboptions
            or a letter M, if go_back is True.
    """
    selection = None
    if go_back:
        if 'm' in suboptions or 'M' in suboptions:
            print("Invalid submenu, which contains M as a key.")
            return None

    while selection not in suboptions:
        print(f"::: What would you like to {action.lower()}?")
        for key in suboptions:
            print(f"{key} - {suboptions[key]}")
        if go_back == True:
            selection = input(f"::: Enter your selection "
                              f"or press 'm' to return to the main menu\n> ")
        else:
            selection = input("::: Enter your selection\n> ")
        if to_upper:
            selection = selection.upper() # to allow us to input lower- or upper-case letters
        if go_back and selection.upper() == 'M':
            return 'M'

    if to_upper:    
        print(f"You selected |{selection}| to",
              f"{action.lower()} |{suboptions[selection].lower()}|.")
    else:
        print(f"You selected |{selection}| to",
          f"{action.lower()} |{suboptions[selection]}|.")
    return selection

def print_song(song, rating_map, title_only=False , showid=False):
    """
    param: song (dict) - a single song dictionary
    param: rating_map (dict) - a dictionary object that is expected
            to have the string keys that correspond to the "rating"
            integer values stored in the song; the stored value is displayed for the
            rating field, instead of the numeric value.
    param: title_only (Boolean) - by default, set to False.
            If True, then only the name of the song is printed.
            Otherwise, displays the formatted song fields.
    param: show_id (Boolean) - by default, set to False.
            If False, then the id number of the song is not displayed.
            Otherwise, displays the id number.

    returns: None; only prints the song values

    Helper functions:
    - get_written_date() to display the 'duedate' field
        You created a similar function in a previous lab.
    """
    
    if title_only == True and showid == False: # checks if Title_only, show_id = T, F
        title2 = song["title"]
        print(f"{'TITLE:':>9} {title2}")
        
    elif title_only == True and showid == True: #checks if title_only, show_id = T,T
        title2 = song["title"]
        ID = song["uid"]
        print(f"{'ID:':>9} {ID} |   TITLE: {title2}")
        
    elif title_only == False: 
        if showid == False: # checks if title_only = F, show_id = T
    
            print(f"{'TITLE:':>9} {song['title']}")
            artist = song["artist"]
            print(f"{'ARTIST:':>9} {artist}")
            if len(song["length"]) == 0:
                pass
            else: 
                length = song["length"]
                print(f"{'LENGTH:':>9} {length}")
            if len(song["album"]) == 0:
                pass
            else:
                album = song["album"]
                print(f"{'ALBUM:':>9} {album}")
            if len(song["genre"]) == 0:
                pass
            else: 
                genre = song["genre"]
                new_list_of_genres = []
                for each_genre in genre:
                    str_genre = str(each_genre)
                    cap_genre = str_genre.title()
                    new_list_of_genres.append(cap_genre)
                final_genre = ", ".join(new_list_of_genres)
                print(f"{'GENRE:':>9} {final_genre}")
            if len(str(song["rating"])) == 0:
                pass
            else:
                rating_num = str(song["rating"])
                rating = rating_map[rating_num]
                print(f"{'RATING:':>9} {rating}")
            if len(song["released"]) == 0:
                pass
            else: 
                released_date = song["released"]
                released_date_list = released_date.split("/")
                released = get_written_date(released_date_list)
                print(f"{'RELEASED:':>9} {released}")
            favorite = song["favorite"]
            print(f"{'FAVORITE:':>9} {favorite}")
            print("*"*42)
           
        else: #checks if title_only = F, show_id = T
            
            if len(song["title"]) == 0:
                pass
            else: 
                title = song["title"]
                ID = song["uid"]
                print(f"{'ID:':>9} {ID} |   TITLE: {title}")
            artist = song["artist"]
            print(f"{'ARTIST:':>9} {artist}")
            if len(song["length"]) == 0:
                pass
            else: 
                length = song["length"]
                print(f"{'LENGTH:':>9} {length}")
            if len(song["album"]) == 0:
                pass
            else:
                album = song["album"]
                print(f"{'ALBUM:':>9} {album}")
            if len(song["genre"]) == 0:
                pass
            else:
                genre = song["genre"]
                new_list_of_genres = []
                for each_genre in genre:
                    str_genre = str(each_genre)
                    cap_genre = str_genre.title()
                    new_list_of_genres.append(cap_genre)
                final_genre = ", ".join(new_list_of_genres)
                print(f"{'GENRE:':>9} {final_genre}")
            if len(str(song["rating"])) == 0:
                pass
            else:
                rating_num = str(song["rating"])
                rating = rating_map[rating_num]
                print(f"{'RATING:':>9} {rating}")
            if len(song["released"]) == 0:
                pass
            else: 
                released_date = song["released"]
                released_date_list = released_date.split("/")
                released = get_written_date(released_date_list)
                print(f"{'RELEASED:':>9} {released}")
            favorite = song["favorite"]
            print(f"{'FAVORITE:':>9} {favorite}")
            print("*"*42)



def print_songs(song_dict, rating_map, title_only = False, showid = False, fave = False, get_genre = False):
    """
    param: song_dict (dict) - a dictionary containing dictionaries with
            the song data
    param: rating_map (dict) - a dictionary object that is expected
            to have the integer keys that correspond to the "rating"
            integer values stored in the song; the stored value is displayed 
            for the rating field, instead of the numeric value.
    param: title_only (Boolean) - by default, set to False.
            If True, then only the title of the song is printed.
            Otherwise, displays the formatted song fields.
    param: show_id (Boolean) - by default, set to False.
            If False, then the key (unique ID number) of the song is not displayed.
            Otherwise, displays the id number.
    param: fave (Boolean) - by default, set to False, and prints all songs.
            Otherwise, if it is set to True, prints only the songs marked as favorite.
            This parameter is meant to be used exclusive of get_genre
            (i.e. if fave=True, then get_genre should be False, and vice versa).
    param: get_genre (Boolean) - by default, set to False, and prints all songs.
            If set to True, then the function should ask the user for a
            genre keyword (string) and print only those songs that contain that string in its genre value.
            This parameter is meant to be used exclusive of fave (i.e. if fave=True, then get_genre should be False, and vice versa).
            NOTE: If a song has multiple instances of that genre keyword, you should only print the song once.

    returns: None; only prints the song values from the song_list

    Helper functions:
    - print_song() to print individual songs
    """

    print("*"*42)
    
   # Check to see if get_genre is True, so that you can ask for the genre keyword
   # Go through all the songs in the song dictionary:
    if get_genre == True:
        keyword = str(input("Enter genre:: "))
        for song in song_dict.values():
            for genres in song["genre"]:
                if keyword in genres:
                    print_song(song, rating_map, title_only = False, showid=False)
    else:             
        for info, song in song_dict.items():
            # if not asking for favorites or specific genres: print everything ## OPTION A and OPTION B
            if fave == False and get_genre == False:
                if title_only == True:
                    if showid == False:
                        print_song(song, rating_map, title_only = True, showid = False)
                    else:
                        print_song(song, rating_map, title_only = True, showid = True)
                else:
                    if showid == True:
                        print_song(song, rating_map, title_only = False, showid = True)
                    else:
                        print_song(song, rating_map, title_only = False, showid = False)
        # otherwise: if asking for favorites, print just those:## OPTION F 
            elif fave == True:
                if song_dict[info]["favorite"] == True:
                    print_song(song, rating_map, title_only = False, showid=False)
                
######## DELETE FUNCTION ######## 11.6
                
def delete_song(song_dict, songid):
    """
    param: song_dict - a dictionary of songs (dict of dict)
    param: songid (str) - a string that is expected to
            contain the key to a song dictionary (i.e. same as its unique ID)

    The function first checks if the dictionary of songs is empty.
    The function then validates the song ID to verify
    that the provided ID key can access an element from song_dict
    On success, the function saves the item's "title" from song_dict
    and returns that string ("title" value)
    after the item is deleted from song_dict.

    returns:
    If the input list is empty, return 0.
    If the ID is not valid (i.e. not found in the song_dict), return -1.
    Otherwise, on success, the entire song is removed from song_dict
    and the function returns the title of the deleted song.
    """
    if song_dict == {}: ## checks if song_dict is an empty dictionary and returns 0 
        return 0
    else: 
        if songid in song_dict: #checks if the songid in song_dict,deletes it/returns it
            temp = song_dict[songid]["title"]
            del song_dict[songid]
            return temp
        else:                   ##if songid is not in song_dict 
            return -1

######## "ADD" ######## 11.4:

def is_valid_addlist(str_info_list):
    """
    param: str_info_list = a list of strings with inputed information
    
    The function checks if the entire input list is made up of strings.
    returns:
    A Boolean value.
    """
    if len(str_info_list) != 9: #checks if the length of the list consists of 9 
        return False
    for item in str_info_list: # checks if the items in the list are all strings
        if type(item) != str:
            return False
    return True

def is_valid_title(title):
    """
    param: title - a string value passed from the user input of the title value
    
    The function checks if the title value is a string that's at least 2 characters
    long and at most 40 characters long.
    returns:
    A Boolean value.
    """
    if 2 <= len(title) <= 40: #checks that the title is between 2 and 40 characters
        return True
    else:
        return False
    
def is_valid_time(length):  
    """
    param: length - the string value from user input for "length" value input
    
    The function checks if the length value is a string that has 2 digits,
    followed by a colon, followed by 2 digits. "04:33"
    returns:
    A Boolean value.
    """
    if len(length) != 5:
        return False
    elif length.count(":") != 1: #checks how many ":" are in the input
        return False
    elif length[0].isdigit() == False: #checks for the values as digits 
        return False
    elif length[1].isdigit() == False:
        return False
    elif length[2] != ":": #checks that the ":" is in the right place
        return False
    elif length[3].isdigit() == False: #checks if values are digits 
        return False
    elif length[4].isdigit() == False:
        return False
    else:
        return True
    
def is_valid_date(num): 
        
    """
    param: num - the released date from the user input from the list of strings
    The function checks if the released date is in a MM/DD/YYYY format.
    returns:
    A Boolean value.
    """
    num_days = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    
    split_date = num.split("/")
    if len(num) != 10: #checks the length to make sure it is correct format
        return False
    elif len(split_date[0]) and len(split_date[1]) != 2: #checks that the days/month are 2 chars 
        return False
    elif len(split_date[2]) != 4: #checks if the year is 4 chars
        return False
    elif num.count("/") !=2:
        return False
    elif num[2] != "/" and date[5] != "/": #checks that the "/" is in the right place
        return False
    else:
        month = split_date[0]
        day = split_date[1]
        year = split_date[2]
        if month.isdigit(): ### check if it is a valid month
            if int(month) >= 1 and int(month) <= 12:
                if day.isdigit(): ### if this is true, then check if it is a valid day
                    if 1 <= int(day) <= num_days[int(month)]: ### if this is true, then check if it is a vaild year
                        if int(year) > 1000:
                            return True
                        else:
                            return False 
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False


def is_valid_uid(num, key_list): 
    """
    param: num - the uid from the inputted list of str 
    param: key_list - a list of all keys in the song dictionary (use.key())
    
    The function checks if uid value is a string with exactly 5 digits.
    The range of these digits can only be "10000" to "99999",
    The value has to be unique to any other uid in the current dict (all_songs).
    returns:
    A Boolean value if the uid is valid or not.
    """
    if type(num) != str:
        return False
    elif len(num) != 5: #checks if the length is 5
        return False
    elif num.isdigit() == False: #checks if the string is all digits 
        return False
    elif 10000 <= int(num) <= 99999: #makes sure that it is between the right numbers and is unique
        if num not in key_list:
            return True
        else:
            return False
    else:
        return False

def get_new_song(str_info_list, rating_map, key_list):
    """
    param: str_info_list = a list of strings
    param: rating_map (dict)
    param: key_list = list of keys for a dictionary

    The function returns different types of values, checks if it succeeds/fails.
    The function calls helper functions to determine if these are valid, and returns values
    depending on this.
    The function checks if the "rating" value is a string that is a digit between 1 and 5 (inclusive)
    The function checks if the "favorite" value is valid, can be "True, T, t..."
        The value must start with T,t,F, or f.
    Once the validation is done, values are passed into get_new_song() through the list parameter,
        must be added as values to a NEW dict with the 9 song keys 

    returns:
    If the input list is not made up of strings and the value is invalid, return a tuple
      containing the message string "Bad list. Found non-string, or bad length" and the integer 0.
    If the title value is invalid, return a tuple containing the message str "Bad Title length" and -1.
    If the length value is invalid, return a tuple containing the message
      string "Invalid time format for Length" and the integer -2.
    If the rating value is invalid (no helper function), return a tuple containing "Invalid Rating value"
      and the integer -3.
    If the released value is invalid, then return a tuple containing
      "Invalid date format for Release Date" and the integer -4.
    If the favorite value is invalid, then return a tuple containing "Invalid value for Favorite" and -5.
    If the uid value is invalid, then return a tuple containing a message
        "Unique ID is invalid or non-unique" and the integer -6.
    return the new dictionary 
    
    Helper functions:
    - is_valid_addlist() checks if the list is made of strings
    - is_valid_title() checks if the title is a string at least 2 char long and at most 40 char
    - is_valid_time() checks to see if the lngth is 00:00 format
    - is_valid_date() checks if the released value is the right format
    - is_valid_uid() checks if the uid is unique
    """

    list_of_TF_values = ["T","f","F","t"]

    new_dict = {}

    if is_valid_addlist(str_info_list)== False: #checks if the list of strings is valid
        return ("Bad list. Found non-string, or bad length", 0)
    elif is_valid_time(str_info_list[2]) == False: #checks if the length is valid
        return ("Invalid time format for Length", -2)
    elif str_info_list[5] not in "12345": #checks if the rating is within the limits 
        return ("Invalid Rating value", -3)
    elif is_valid_date(str_info_list[6]) == False: #checks if the date is valid
        return ("Invalid date format for Release Date", -4)
    elif str_info_list[7][0] not in list_of_TF_values: #checks if fave starts with "T","t","F","f"
        return ("Invalid value for Favorite", -5)
    elif is_valid_uid(str_info_list[8], key_list) == False: #checks if uid is unique
        return ("Unique ID is invalid or non-unique", -6)
    elif is_valid_title(str_info_list[0]) == False: #checks if the title length is correct
        return ("Bad Title length", -1)
    else:
        genre_val_list = []
        split_genres = str_info_list[4].split(",") #appends the genre inputs into a list 
        for genres in split_genres:
            genre_val_list.append(genres)

        rating = int(str_info_list[5]) # converts the rating and id to an integer
        id_val = int(str_info_list[8])
        if str_info_list[7][0] == "T" or str_info_list[7][0] == "t": #returns True or False based on input
            fave = True
        else:
            fave = False

        new_dict = {"title": str_info_list[0], #creates new dictionary of inputted values 
                    "artist": str_info_list[1],
                    "length": str_info_list[2],
                    "album": str_info_list[3],
                    "genre": genre_val_list,
                    "rating": rating,
                    "released": str_info_list[6],
                    "favorite": fave,
                    "uid": id_val
                    }
        return new_dict
    
### 11.8 "Save" -----------------------------------------------------------------
    
def save_to_csv(song_dict, filename):
    """
    param: song_dict(dict of dict) - The dictionary of songs stored 
    param: filename (str) - A string that ends with '.csv' which represents
               the name of the file to which to save the songs. This file will
               be created if it is not present, otherwise, it will be overwritten.

    The function ensures that the last 4 characters of the filename are '.csv'.
    The function requires the `import csv` as well as `import os`.

    The function will use the `with` statement to open the file `filename`.
    After creating a csv writer object, the function uses a `for` loop
    to loop over every song in the dictionary and creates a new list
    containing only strings - this list is saved into the file by the csv writer
    object. The order of the elements in the dictionary is:

    * title
    * artist
    * length
    * album
    * genre (all element in the original list are converted to string
        joined with commas separating)
    * rating (converted to string)
    * released (written as string, i.e, "06/06/2022", NOT "June 6, 2022")
    * favorite (converted to string)
    * uid

    returns:
    -1 if the last 4 characters in `filename` are not '.csv'
    None if we are able to successfully write into `filename`
    """
    import csv
    import os
    song_list = []
    str_last_4 = filename[-4:] #checks if the last four of the filename are '.csv'
    
    if str_last_4 != ".csv" or len(filename) < 4:
        return -1
    else:
        with open(filename, 'w', newline ='') as myfile: 
            writer = csv.writer(myfile)
            for dictionary, categories in song_dict.items():
                fixed_genre = ",".join(categories["genre"]) #joins the genres to a string separated by ","
                song_dict[dictionary]["genre"] = fixed_genre #assigns the genre to the dictionary value
                fixed_rating = str(categories["rating"]) #converts the rating to a string
                song_dict[dictionary]["rating"] = fixed_rating #assigns the rating to the dictionary value
                fixed_released = str(categories["released"]) #converts the date to a string 
                song_dict[dictionary]["released"] = fixed_released #assigns the date to the dictionary value
                fixed_uid = str(categories["uid"]) #converts the uid to a string
                song_dict[dictionary]["uid"] = fixed_uid #assigns the uid to the dictionary value
                fixed_fave = str(categories["favorite"])#converts the fave to a string
                song_dict[dictionary]["favorite"] = fixed_fave #assigns the fave to the dictionary value
                song_list = []
                for item in song_dict[dictionary].values(): #appends the values to the list of strings
                    song_list.append(item)
                writer.writerow(song_list) #writes the list of strings into csv file

### 11.9 "Restore" menu option-----------------------------------------
    
def load_from_csv(filename, in_dict, rating_map, allkeys):
    """
    param: filename (str) - A string variable which represents the
            name of the file from which to read the contents.
    param: in_dict (dict of dict) - A dictionary of songs (dictionary objects) to which
            the songs read from the provided filename are added.
            If in_dict is not empty, the existing songs are not dropped.
    param: rating_map (dict) - a dictionary object that is expected
            to have the integer keys that correspond to the "rating"
            integer values stored in the song; the stored value is displayed 
            for the rating field, instead of the numeric value.
    param: allkeys (key_list) - a key_list of all keys in the song dictionary

    The function ensures that the last 4 characters of the filename are '.csv'.
    The function requires the `import csv` and `import os`.

    If the file exists, the function will use the `with` statement to open the
    `filename` in read mode. For each row in the csv file, the function will
    proceed to create a new song using the `get_new_song()` function.
    - If the function `get_new_song()` returns a valid song object,
    it gets added to `in_dict`.
    - If the `get_new_song()` function returns an error, the 1-based
    row index gets recorded and added to the NEW list that is returned.
    E.g., if the file has a single row, and that row has invalid song data,
    the function would return [1] to indicate that the first row caused an
    error; in this case, the `in_dict` would not be modified.
    If there is more than one invalid row, they get excluded from the
    in_dict and their indices will be appended to the new list that's
    returned.

    returns:
    * -1, if the last 4 characters in `filename` are not '.csv'
    * None, if `filename` does not exist.
    * A new empty list, if the entire file is successfully read from `in_dict`.
    * A list that records the 1-based index of invalid rows detected when
      calling get_new_song().

    Helper functions:
    - get_new_song()
    """        
    import csv
    import os
    new_list = []
    p = os.path.join(filename)
    str_last_4 = filename[-4:]
    if str_last_4 != ".csv" or len(filename) < 4: #checks if the filename is correct
        return -1
    
    elif os.path.exists(p): #checks if the filename exists 
        with open(filename, 'r') as csvfile:
            readerObj = csv.reader(csvfile, delimiter=",")
            row_num = 1 
            for row in readerObj:
                returned = get_new_song(row, rating_map, allkeys) # gets a new song for the row of the file

                if type(returned) == dict:
                    if returned not in in_dict.items():
                        uid_key = str(returned["uid"]) #assigns the key to a string
                        in_dict[uid_key] = returned #adds the song as a value and the uid as a key in the dictionary
                else:
                    new_list.append(row_num) #appends index of the invalid row to a list
                    row_num += 1
                return new_list #returns the list 
    else:
        return None

## 11.5 "EDIT SONG" ----------
def edit_song(song_dict, songid, rating_map, field_key, field_info, allkeys):
    """
    param: song_dict (dict) - dictionary of all songs
    param: songid (str) - a string that is expected to contain the key of
            a song dictionary (same value as its unique id)
    param: rating_map (dict) - a dictionary object that is expected
            to have the integer keys that correspond to the "rating"
            integer values stored in the song; the stored value is displayed 
            for the rating field, instead of the numeric value.
    param: field_key (string) - a text expected to contain the name
            of a key in the song dictionary whose value needs to 
            be updated with the value from field_info  " LIKE TITLE ETC"
    param: field_info (string) - a text expected to contain the value
            to validate and with which to update the dictionary field
            song_dict[field_key]. The string gets stripped of the
            whitespace and gets converted to the correct type, depending
            on the expected type of the field_key. "VALUE OF FIELD" 
    param: allkeys (key_list) - a key_list of all keys in the song dictionary.

    The function first calls some of its helper functions
    to validate the provided field.
    If validation succeeds, the function proceeds with the edit.

    return:
    If song_dict is empty, return 0.
    If the field_key is not a string, return -1.
    If the remainder of the validation passes, return the dictionary song_dict[songid].
    Otherwise, return the field_key.

    Helper functions:
    The function calls the following helper functions depending on the field_key:
    - is_valid_title()
    - is_valid_time()
    - is_valid_date()
    - is_valid_uid()
    """
    
    if song_dict == {}:
        return 0
    if type(field_key) != str: #checks if the field_key is a string
        return -1
    if field_key == "title": #checks if the title is valid, then returns either key or new dict
        if is_valid_title(field_info) == True:
            song_dict[songid]["title"] = field_info
            return song_dict[songid]
        else:
            return field_key
    if field_key == "artist": #checks if the artist input is valid, then returns either the key or new dict
        song_dict[songid]["artist"] = field_info
        return song_dict[songid]
    if field_key == "length": 
        if is_valid_time(field_info) == True: #checks if the length input is valid, returns either key or new dict
            song_dict[songid]["length"] = field_info
            return song_dict[songid]
        else:
            return field_key
    if field_key == "rating": #checks if the rating is valid, then returns either key or new dict
        if field_info in "12345":
            song_dict[songid]["rating"] = field_info
            return song_dict[songid]
        else:
            return field_key
    if field_key == "released":  #checks if the released date is valid, then returns either key or new dict
        if is_valid_date(field_info) == True:
            song_dict[songid]["released"] = field_info
            return song_dict[songid]
        else:
            return song_dict[songid]
    if field_key == "favorite":
        list_TF_val = ["T","t","F","f"]  #checks if favorite is valid 
        if field_key[0] in list_TF_val:
            if field_key[0] == "T" or field_key[0] == "t":
                song_dict[songid]["favorite"] = True
                return song_dict[songid]
            elif field_key[0] == "F" or field_key[0] == "f":
                song_dict[songid]["favorite"] = False
                return song_dict[songid]
        else:
            return field_key #returns field key instead of edited dict if it is not valid 
    if field_key == "uid": 
        if is_valid_uid(field_info, allkeys) == True: #checks if the field key inputed is correct
            song_dict[songid]["uid"] = field_info
            return song_dict[songid]
        else:
            return field_key #returns field key instead of dict if the field_key is not valid
    
    
##11.7 "Show Statistical Data On" Menu Option
def do_stats(song_dict, opt):
    """
    param: song_dict - a dictionary of songs (dict of dict)
    param: opt (str) - an option from the menu
    to do one of the following statistical calculations:
        "A" - find the mean (average) of all song ratings values
        "B" - find the median of all song ratings values
        "C" - find the standard deviation of all song ratings values
        "D" - print out a histogram of all song ratings values

    Helpful hint: see example on top of page in
    zyBook Ch. 8.4 to see how to do mean and stddev calculations.

    returns: Nothing! This function only PRINTS out results.    
    """

    rates = []
    for song in song_dict.values():
        if song["rating"] != '':
            rates.append(song["rating"]) #appends the ratings if it is not empty 

    if opt == "A":
        mean = sum(rates)/len(rates) #finds the mean of all ratings
        print(f'The mean value of all ratings is: {mean:.2f}')

    elif opt == "B":
        rates.sort()
        remainder = len(rates) %2
        if remainder == 0:
            num1 = int((len(rates)/2))
            num2 = int((len(rates)/2)-1)
            median = (rates[num1] + rates[num2]) / 2 #finds the median for an even number
            print(f'The median value of all ratings is: {median:.2f}')
        else:
            num = len(rates) / 2
            median = int(num) #finds the median (middle number of list) if an odd number of ratings
            print(f'The median value of all ratings is: {median:.2f}')
        
    elif opt == "C":
        val = 0
        mean = sum(rates)/len(rates)
        for rate in rates:
            val += (rate - mean)**2
        std_dev = (val/len(rates))**0.5 #finds the standard deviation for ratings
        print(f'The standard deviation value of all ratings is: {std_dev:.2f}')

    elif opt == "D":
        str_items = []
        for item in rates:
            str_item = str(item)
            str_items.append(str_item)
        " ".join(str_items) #joins the items of ratings into a string
        once = str_items.count("1") #counts how many times "1" appears
        twice = str_items.count("2") #counts how many times "2" appears
        threetimes = str_items.count("3") #counts how many times "3" appears
        fourtimes = str_items.count("4") #counts how many times "4" appears
        fivetimes = str_items.count("5") #counts how many times "5" appears
        
        if once != 0:
            print("1 ", end ="")
            print("*" * once)
        else: 
            print("1 ")
        if twice !=0:
            print("2 ", end ="")
            print("*" * twice)
        else:
            print("2 ")

        if threetimes != 0:
            print("3 ", end ="")
            print("*" * threetimes)
        else:
            print("3 ")

        if fourtimes !=0:
            print("4 ", end ="")
            print("*" * fourtimes)
        else:
            print("4 ")

        if fivetimes !=0:
            print("5 ", end ="")
            print("*" * fivetimes)
        else:
            print("5 ")
        #for the if and else statements, the count of how many times
            #each rating appears is checked to see if it is 0.
            # if the count is 0, it only prints the rating ex 1,2,3 but does
            #not print the number of asterisks according to the value.
          
        
            

        
