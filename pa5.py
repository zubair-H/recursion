

def update_user_info(users = {},upd = {}): # I added empty squiggly brackets because if one of parameters is empty the function won't be empty.
    my_dict = {} # this for the new dictionary
    if upd == {}: # this is for the base case, if upd is empty then don't do anything.
        return users # don't do anything, and simply return users, without doing anything.
    if users == {}: # this base case is for when the input for user is empty but the input for upd is not empty. I want to add everything from upd into a new dictionary.
        for i in range(len(upd)): # this is to iterate through upd. this is also to create a dictionary from the given input inside of upd.
            key = upd[i][0]  # this will take the first element and create a key from it
            my_dict[key] = [upd[i][1],upd[i][2]] # this line creates the value from the given list through upd.
        return my_dict # simply come to a stop and display the newly created dictionary.
    for i in upd: # this base case is when users have elements and needs to be updated. I need to iterate through upd so then im able to compare elements from upd against elements in users.
        if (i[0]) in users: # first, I want to check if the name from users are in upd.
            users[i[0]][0] += i[1] # if they are, then add elements at the index position of 1 from upd into users.
            for items in (i[2]): # this will iterate through the items that match elements that are inside of users with elements that inside of upd.
                (users[i[0]][1]).append(items) # then I want to add all of those items in users.
        else: # if the names from users are not in upd, then I wand to add that whole element into users.
            users[i[0]] = [[i][0][1],[i][0][2]] # this will add the users from upd that are not in users. This is when no current readers have updated their progress, instead there have been only new users. its for the case.
    return users # simply return the users after all the changes have been made.


def update_progress(users_books, new_books_read= {}): # for this one I only made new_books_read= {} because in case there are no new readers.
   new_2d = [] # this is 2d list ill be using the convert the given dictionary into a 2d list so that it can match the input of the first function so that I can call the first function.
   for (key2, value2) in new_books_read.items(): # I used .items built in because I want both the keys and values from new_books_read.
       new_2d.append([key2,value2]) # this is where im converting the dictionary into a 2d list.
   for (key,value) in users_books.items(): # another for loop so that I can iterate through users_books, because I want to change their reading scores by how many books a user has read.
       users_books[key] = [len(value)*10, value] # this is where i'm multiplying the number of books times by 10, using the len built in.
   for i in range(len(new_2d)): # I need to iterate through new_2d so that I can add the number of books times by 10 in the correct spot.
       new_2d[i].insert(1,len(new_2d[i][1])*10) # using the .insert built in allows me to insert the number of books times by 10 at the index location of 1.
   return (update_user_info(users_books,new_2d)) # this is where i'm calling the first function to inset the input of the second function.



def users(names, books, new_books = ()): # what is that called
    key = [] # this to create a dictionary and it's key of the dictionary that i'm creating.
    value = [] # this is value of the dictionary.
    new_dict1 = {} # this is the first dictionary, key and value will be stored in this one.
    key2 = [] # keys of the second dictionary.
    value2 = [] # values of the second dictionary.
    new_dict2 = {} # this is the second dictionary.
    for i in range(len(names)): # im using this for loop to iterate through names, so that I can create dictionary 1.
        key = names[i] # this is where im creating the keys for the first dictionary.
        value = books[i] # this is where im creating the values for the first dictionary.
        new_dict1[key] = value
    for j in range(len(new_books)):
        key2 = names[j]
        value2 = new_books[j]
        new_dict2[key2] = value2
    return(update_progress(new_dict1,new_dict2))



def string_difference(s = None, t = None): # I added None for both s and t because if one of the parameters is empty, my program will still run and won't crash.
    new_list = [] # this to store all the values from s that are not in t.
    if len(s) == 0 or len(t) == 0: # this is the base case, in case of the parameters reach 0, I want the function to stop.
        return new_list # give me the list that store all the values from s that are not in t.
    if s[0] not in t: # this is to check if any of the values from s are not in t. it does that by checking every 1st element in s.
        new_list.append(s[0]) # if the condition is met, then I want that value to be stored in new_list.
    return new_list + string_difference(s[1:],t) # I added new_list and t in the call function because I dont want the values inside of them to reset.
    # Also, this is where recursion comes in and restarts the function, keep on going until it meets once of the base cases.

def count_consecutive_chars(some_str=None, counter = 0):# I added counter to a track of how many times a character has been repeated. there was no other to do this.
    my_tuple = [] # this the list that i'm using to append the all values that are repeating the number of times it's going to repeat.
    if len(some_str) == 0: # this first base case, I want the loop to end if the length of the some_str equals 0
        return my_tuple # end it here and return my_tuple.
    elif len(some_str) == 1:
        my_tuple.append((some_str[0], counter))
        return my_tuple
    else:
        if some_str[0] == some_str[1]:
            counter += 1
            #my_tuple.append(some_str[0])
            return my_tuple + count_consecutive_chars(some_str[1:],counter)
        else:
            counter += 1
            return my_tuple + count_consecutive_chars(some_str[1:],counter)
print(count_consecutive_chars("AABBBCCCC"))


