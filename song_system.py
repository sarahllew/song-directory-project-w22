from song_functions import * 

#11.2
the_menu = {
    "L" : "List",
    "A" : "Add",
    "E" : "Edit",
    "D" : "Delete",
    "M" : "Show statistical data on",
    "S" : "Save the data to file",
    "R" : "Restore data from file",
    "Q" : "Quit this program"
             } 
opt = None

#11.3 
all_songs = {
   "12332": {
      "title": "Cardigan",
      "artist": "Taylor Swift",
      "length": "03:59",
      "album": "Folklore",
      "genre": ["folk", "indie rock"],
      "rating": 4,
      "released": "07/27/2020",
      "favorite": True,
      "uid" : 12332
   },
   "14567": {
      "title": "Soul Meets Body",
      "artist": "Death Cab for Cutie",
      "length": "",
      "album": "Plans",
      "genre": ["indie pop", "indie rock"],
      "rating": 5,
      "released": "07/16/2005",
      "favorite": True,
      "uid":14567
      },
   "78210": {
      "title": "Fake Love",
      "artist": "BTS",
      "length": "04:02",
      "album": "",
      "genre": ["hip hop", "electro pop", "Korean pop"],
      "rating": 3,
      "released": "05/18/2018",
      "favorite": False,
      "uid":78210
      },
    "99105": {
      "title": "Foil",
      "artist": "'Weird Al' Yankovic",
      "length": "02:22",
      "album": "Mandatory Fun",
      "genre": ["pop", "parody"],
      "rating": 5,
      "released": "07/15/2014",
      "favorite": True,
      "uid": 99105
      }
}

list_menu = {
    "A": "all songs - full",
    "B": "all songs - titles only",
    "F": "favorite songs",
    "G": "songs of a specific genre"
}


rating_map = {
    "1": "Hate",
    "2": "Dislike",
    "3": "Neutral",
    "4": "Like",
    "5": "Love!"
}

#11.2 -------------------------------------------------------------------------
while True:
    print_main_menu(the_menu)
    opt = input("::: Enter a menu option\n> ")
    opt = opt.upper() # to allow us to input lower- or upper-case letters

    if opt not in the_menu: 
        print(f"WARNING: {opt} is an invalid menu option.\n")
        continue

    print(f"You selected option {opt} to > {the_menu[opt]}.")

    if opt == "Q": 
        print("Goodbye!\n")
        break # exit the main `while` loop
    
# 11.3 "List" menu option ---------------------------------------------------------
    elif opt == 'L':
        if all_songs == {}:
            print("WARNING: There is nothing to display!")
            # Pause before going back to the main menu
            input("::: Press Enter to continue")
            continue

        subopt = get_selection(the_menu[opt], list_menu)
        if subopt == 'A':
            print_songs(all_songs, rating_map, showid = True)
        elif subopt == 'B':
            print_songs(all_songs, rating_map, title_only = True)
        elif subopt == 'F':
            print_songs(all_songs, rating_map, fave = True)
        elif subopt == 'G':
            print_songs(all_songs, rating_map, get_genre = True)

# 11.4 "Add" Menu Option ----------------------------------------------------------------
    elif opt == 'A':
        continue_action = 'y'
        while continue_action == 'y':
            song_info = []
            print("::: Enter each required field:")
            # TODO: Get user inputs for all 9 song info fields (i.e. keys). 
            # Get *all* inputs as strings.
            title = str(input("Title: "))
            artist = str(input("Artist: ")) 
            length = str(input("Length (00:00 format): "))
            album = str(input("Album: "))
            genres = str(input("Genres (separate them with commas): "))
            rating = str(input("Rating (1-5): "))
            release = str(input("Release Date (MM/DD/YYYY format): "))
            favorite = str(input("Favorite (T/F): "))
            uid = str(input("Unique ID: "))
            song_info.extend([title,artist,length,album,genres,rating,release,favorite,uid])
            key_list = all_songs.keys()
            result = get_new_song(song_info,rating_map,key_list)  
            if type(result) == dict:
                all_songs.update({"uid":result}) 
                print(f"Successfully added a new song!")
                print_song(result, rating_map, title_only = False, showid = False) # TODO 
            elif type(result) == tuple:
                print(f"WARNING: invalid data!")
                print(f"Error: {result[0]}")

            print("::: Would you like to add another song?", end=" ")
            continue_action = input("Enter 'y' to continue.\n> ")
            continue_action = continue_action.lower() 
            # ----------------------------------------------------------------
# 11.6 "Delete" Menu option-------------------------------------------------------
    elif opt == 'D':
      if all_songs == {}: #checks to see if there is anything left in the dict to delete
       print("WARNING: There is nothing to delete!") 
      else:
       continue_action = 'y'
       while continue_action == 'y': #if 'y' is the input, then it calls print_songs()
           print_songs(all_songs, rating_map, title_only = True, showid = True)
           print("Which song would you like to delete?")
           print("X - Delete all songs at once") 
           print("::: OR Enter the number corresponding to the song ID")
           print("::: OR press 'M' to cancel and return to the main menu.")
           user_option = input(">")
           if user_option == "X": #checks whether to delete ALL songs 
               print("::: WARNING! Are you sure you want to delete ALL songs?")
               print("::: Type Yes to continue the deletion.")
               user_option2 = input(">")
               if user_option2 == "Yes": 
                   all_songs.clear()
                   print("Deleted all songs.")
                   break # exit the loop 
           elif user_option == "M":
               break #exit the loop to main menu 
           else: #deletes song based on if the uid is valid or not 
                if user_option in all_songs:
                  deleted_song = delete_song(all_songs, user_option)
                  print("Success!")
                  print(f"Deleted the song |{deleted_song}|")
                  print(f"::: Would you like to delete another song? Enter 'y' to continue.")
                  continue_action = input(">")
                  
                elif user_option not in all_songs:
                  print(f"WARNING: |{user_option}| is an invalid song ID!")
                  print(f"::: Would you like to delete another song? Enter 'y' to continue.")
                  continue_action = input(">")

##----------------------------------------------------------------------------           

# 11.8 "Save" Menu Option 
    elif opt == 'S':
        continue_action = 'y'
        while continue_action == 'y':
            print("::: Enter the filename ending with '.csv'.")
            filename = input("> ")
            output = save_to_csv(all_songs,filename) # TODO: Call the function with appropriate inputs and capture the output
            if output == -1: # TODO
                print(f"WARNING: |{filename}| is an invalid file name!") # TODO
                print("::: Would you like to try again?", end=" ")
                continue_action = input("Enter 'y' to try again.\n> ")
            else:
                print(f"Successfully stored all the songs to |{filename}|")
                continue_action = 'n'
    #--------------------------------------------------------------------------

# 11.9 "Restore" Menu Option
    #attemps: 1) bad file name
    #2) uses bad file name... the file doesn't exist!
    #3) successful
    elif opt == "R":
        continue_action = 'y'
        while continue_action == 'y':
            print("::: Enter the filename ending with '.csv'.")
            filename = input("> ")
            key_list = all_songs.keys()
            output = load_from_csv(filename, all_songs, rating_map, key_list)
            if output == -1: #filename is not valid 
                print("WARNING: invalid input - must end with '.csv'")
                print("::: Would you like to try again?", end=" ")
                continue_action = input("Enter 'y' to try again.\n> ")
            elif output == None: ##filename doesn't exist
                print(f"WARNING: |{filename}| was not found!")
                print("::: Would you like to try again?", end=" ")
                continue_action = input("Enter 'y' to try again.\n> ")
            else:
                if len(output) != 0: ## has invalid data
                    print(f"WARNING: |{filename}| contains invalid data!")
                    print("The following rows from the file were not loaded:")
                    print(output)
                    print("::: Would you like to try again?", end=" ")
                    continue_action = input("Enter 'y' to try again.\n> ")
                else: ## no invalid data
                    print(f"Successfully restored all songs from |{filename}|")
                    print("::: Would you like to try again?", end=" ")
                    continue_action = input("Enter 'y' to try again.\n> ")
#--------------------------------------------------------------------------
#11.5 "Edit" menu option
    elif opt == 'E':
        continue_action = 'y'
        while continue_action == 'y':
            if all_songs == {}: 
                print("WARNING: There is nothing to edit!")
                break
            print("::: Song list:")
            print_songs(all_songs, rating_map, title_only = True, showid = True)
            print("::: Enter the song ID you wish to edit.")
            user_option = input("> ")
            if user_option in all_songs: 
                subopt = get_selection("edit", all_songs[user_option], to_upper = False, go_back = True)
                if subopt == 'M': # if the user changed their mind
                    break
                print(f"::: Enter a new value for the field |{subopt}|") 
                field_info = input("> ")
                key_list = all_songs.keys()
                result = edit_song(all_songs, user_option, rating_map, subopt, field_info, key_list) 
                if type(result) == dict:
                    print(f"Successfully updated the field |{field_info}|:")  
                    print_song(result, rating_map, title_only = False, showid =False )  
                else: # edit_song() returned an error
                    print(f"WARNING: invalid information for the field |{subopt}|!")  
                    print(f"The song was not updated.")
            else: # song ID is incorrect/invalid
                print(f"WARNING: |{user_option}| is an invalid song ID!")  

            print("::: Would you like to edit another song?", end=" ")
            continue_action = input("Enter 'y' to continue.\n> ")
            continue_action = continue_action.lower()      

            # ----------------------------------------------------------------
##11.7 "Show Statistical Data" menu option
    elif opt == "M":
        continue_action = 'y'
        while continue_action == 'y':
            print("::: What would you like to show statistical data on?")
            print("A - Mean value of all song ratings")
            print("B - Median value of all song ratings")
            print("C - Standard Deviation value of all song ratings")
            print("D - Histogram of all song ratings")
            print("::: Enter your selection")
            subopt = input("> ")
            if subopt == 'A' or subopt == 'a':
                print("You selected |A| to show statistical data on |mean value of all song ratings|.")
                do_stats(all_songs, "A")
            if subopt == "B" or subopt == 'b':
                print("You selected |B| to show statistical data on |median value of all song ratings|.")
                do_stats(all_songs, "B")
            if subopt == "C" or subopt == 'c':
                print("You selected |C| to show statistical data on |standard deviation value of all song ratings|.")
                do_stats(all_songs, "C")
            if subopt == "D" or subopt == 'd':
                print("You selected |D| to show statistical data on |histogram of all song ratings|.")
                do_stats(all_songs, "D")
            print("::: Would you like to get different statistics?", end =" ")
            continue_action = input("Enter 'y' to continue.\n> ")
            
    input("::: Press Enter to continue")

print("Have a nice day!")
