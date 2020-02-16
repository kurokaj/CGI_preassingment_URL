import time
import sys
import logging
import re
import threading
import urllib.request
import urllib
from datetime import datetime

"""
The main goes through list of URLs from txt-file, checks if Regular Expressions (RE's) are found
    and writes results to a log file

User can choose the used RE's from different groups that are read from txt-file, by inputting the right group
    name to the terminal
"""


"""
Checks is the URL- list matches with the given RE-group
"""
def checker(RE_value, re_map):
    # Sum of matces found on single sweep
    ssum = 0


    RE_list = re_map[RE_value]

    print("Reading url's from txt file to list...")
    # Read list of URLs
    with open('url_list_final.txt') as f:
        lines = f.read().splitlines()

    url_list = lines

    for count,url in enumerate(url_list):

        try:
            # Open the URL
            fd = urllib.request.urlopen(url)
            # Read lines from URL
            data_t = fd.read()
        except(urllib.error.URLError):
            print("ERROR: cannot find "+str(count)+" url")
            logging.critical("["+str(datetime.now())+"] Could not find url: "+url)
            data_t = []

        for line in data_t:
            RE_result = re.search(RE_list,str(line))
            if RE_result:
                    print("Match found with "+ RE_value)
                    logging.critical("["+str(datetime.now())+"] Found match in URL: "+url+" and RE: " + RE_value)
                    ssum +=1
                    break

    return ssum

"""
Takes user input and changes the RE-group accordingly.
"""
def in_put(re_map):
    # Takes input from user
    global RE_val
    global bol

    while(bol):
        temp_RE_val2 = input("Choose the RE's that are used...")
        if(temp_RE_val2 in re_map):
            RE_val = temp_RE_val2
            temp_RE_val2 = '0'
            print("You chose to track for:  ", RE_val)
            print("New RE-group will be effective next round...")

        else:
            print("Input key did not match any RE-group.")

            print("Shutting down input- thread...")
            bol = False

"""
Calls the checker- function once in every 60 seconds. Creates and writes info to log-file.
The user contact is ran in another thread, so it does not intervene with the main or checker.
Exits and shuts down the rest as user presses CTRL-C
"""
def main():
    # Global varialbes
    global bol
    bol = True

    # The default ER key (can be changed by user any time)
    global RE_val
    RE_val = "Business"

    # Create log-file
    print("Creating log-file...")
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    logging.basicConfig(filename="log_url.log", level=logging.INFO)

    # Dictionary of RE's for different domains
    # Read keys/values from txt-file
    print("Reading regular expression values from txt-file to dictionary...")
    re_map = {}
    with open("ER_dict_final.txt") as f:
        for line in f:
            (key, value) = line.split()
            re_map[str(key)] = value

    logging.info("["+str(datetime.now())+"] Starting the main- program.")
    logging.info("["+str(datetime.now())+"] Starting thread for the user-input.")

    th = threading.Thread(target=in_put, args=(re_map,))
    try:
        th.start()
    except (KeyboardInterrupt, SystemExit):
        bol = False

    t0 = time.time()
    flag = 1
    summm = 0
    try:
        while bol:
            # Run checker in 60s intervals
            if((time.time()-t0)/60 >= 1):
                flag = 1

            if(flag == 1):
                summm +=1

                temp_RE_val = RE_val
                logging.info("Starting the "+ str(summm)+ " round, with RE-group "+temp_RE_val)
                ret_sum = checker(temp_RE_val, re_map)

                print("\nThe sum of found matches on ER-group '"+temp_RE_val+"': " + str(ret_sum))
                logging.critical("["+str(datetime.now())+"] The sum of found matches on ER-group '"+temp_RE_val+"': " + str(ret_sum))

                flag = 0
                t0 = time.time()
                print("Waiting to run URL-list again...")

    except(KeyboardInterrupt, SystemExit):
        bol = False
        print("\nPress enter to end user-input.")
        print("\nExiting the main...")



if __name__== "__main__":
  main()
