from song_functions import * 


#11.2
assert get_written_date(["01", "02", "2022"]) == 'January 2, 2022'
assert get_written_date(["01", "12", "1970"]) == 'January 12, 1970'
assert get_written_date(["04", "14", "2020"]) == 'April 14, 2020'
assert get_written_date(["06", "19", "2000"]) == 'June 19, 2000'  

# 11.4 
addlist1 = ["Cardigan - Extended Version", "Taylor Swift", "07:66", "Folklore", "folk,indie rock", "3", "07/27/2020", "True", "12333"]
addlist2 = ["Cardigan - Extended Version", "Taylor Swift", "17:30", "Folklore", "folk,indie rock", 3, "07/27/222222", True, "12332"]
addlist3 = ["Cardigan - Extended Version", "Taylor Swift", "H7:59", "Folklore"]
addlist5 = ["H", "Taylor Swift", "07:59:", "Folklore", "folk,indie rock", "3", "-22/27/2020", "T", "12"]
addlist12 = ["RATE", "Taylor Swift", "07:66", "Folklore", "folk,indie rock", "9", "07/27/2020", "True", "12333"]

rating_map = {
    "1": "Hate",
    "2": "Dislike",
    "3": "Neutral",
    "4": "Like",
    "5": "Love!"
}

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

list_keys = ['12332', '14567', '14568', '78210', '78211', '99105']
uid1 = "12333"
uid2 = "12332"
uid5 = "12"
uid6 = "00000"
date1 = "07/27/2020"
date2 = "07/27/222222"
date5 = "-22/27/2020"
title1 = "Cardigan"
title2 = "C"
title3 = "Cardigan - Extended Version featuring Lana del Rey, Post Malone, ASAP Rocky, Lorde, Phoebe Bridgers"
length1 = "H6:59"
length2 = "22:AA"
length3 = "2::3"
length4 = "02:20"

    ## check is_valid_addlist
assert is_valid_addlist(addlist1) == True
assert is_valid_addlist(addlist2) == False
assert is_valid_addlist(addlist3) == False


    ## check is_valid_title()
assert is_valid_title(title1) == True
assert is_valid_title(title2) == False
assert is_valid_title(title3) == False

    ## check is_valid_time()
assert is_valid_time(length1) == False
assert is_valid_time(length2) == False
assert is_valid_time(length3) == False
assert is_valid_time(length4) == True

    ## check is_valid_date()

assert is_valid_date(date1) == True
assert is_valid_date(date2) == False
assert is_valid_date(date5) == False


    ## check is_valid_uid() 
assert is_valid_uid(uid1,list_keys) == True
assert is_valid_uid(uid2,list_keys) == False
assert is_valid_uid(uid5,list_keys) == False
assert is_valid_uid(uid6,list_keys) == False


    ## check get_new_song()
assert get_new_song(addlist3, rating_map, list_keys) == ("Bad list. Found non-string, or bad length", 0)
assert get_new_song(addlist12, rating_map, list_keys) == ("Invalid Rating value", -3)
assert get_new_song(addlist1, rating_map, list_keys) == {
      "title": "Cardigan - Extended Version",
      "artist": "Taylor Swift",
      "length": "07:66",
      "album": "Folklore",
      "genre": ["folk", "indie rock"],
      "rating": 3,
      "released": "07/27/2020",
      "favorite": True,
      "uid" : 12333
   }

filename1 = "xxx"
filename2 = "xxx.csv"
filename3 = "csv"
filename4 = "good.csv"
filename5 = "nonexist.csv"
## check 11.8 save_to_csv()
assert save_to_csv(all_songs, filename1) == -1
assert save_to_csv(all_songs, filename2) == None
assert save_to_csv(all_songs, filename3) == -1
assert save_to_csv(all_songs, filename4) == None

## check 11.9 load_from_csv()
assert load_from_csv(filename1, all_songs, rating_map, list_keys) == -1
assert load_from_csv(filename5, all_songs, rating_map, list_keys) == None

songuid1 = "12332"
songuid2 = "234AA"
empty_dict = {}
## check delete_song()
assert delete_song(all_songs, songuid1) == "Cardigan"
assert delete_song(all_songs, songuid2) == -1
assert delete_song(empty_dict, songuid2) == 0 

## 11.5 check edit_song()
key_info = "The Louvre"
key_field = "title"
user_opt = "12332"
key_info2 = "14567"
key_field2 = "uid"
empty_dict = {}
title_not = 3
assert edit_song(empty_dict, "12332", rating_map, "title", "Cardigan", list_keys) == 0
assert edit_song(all_songs, "12332", rating_map, title_not, "Cardigan", list_keys) == -1
assert edit_song(all_songs, "12332", rating_map, key_field2, key_info2, list_keys) == "uid"

## test practice
good = "test1.csv"
print(load_from_csv(good, all_songs, rating_map, list_keys))
