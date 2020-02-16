Pre-assginment CGI ML team

I created a Python script that takes in a list of urls and checks if it finds certain regular expressions in those urls. The user can change the RE's mid-run by typing certain RE-groups to the terminal. These RE-groups are stored in a txt-file and read prior the url checking. 

Functions:
	- Checker
	Checks if any of the URL- list matches with the given RE-group
		- in 
			-value that determines RE-group
			-dictionary of the RE's
		- out
			-Sum of the found matches in the URL list
	- In_put
	Takes user input and changes the RE-group accordingly.
		- in
			-dictionary of the RE's
		- out
			-None
	- Main 
	Calls the checker- function once in every 60 seconds. Creates and writes info to log-file. The user contact is ran in another thread, so it does not intervene with the main or checker. Exits and shuts down everythin if user presses CTRL-C

The program can be run by command "python3 main.py". All the libraries are Python Standard Libraries, so no "extra" content was used. The files "ER_dict_final" and "url_list_final" hold RE's and URL-list for the final implementation. URL's were collected online randomly.  

As mentioned the results are stored in log- file with time stamps for later use. 
The script could be used to find certain URL's that are fitted for a certain ML/AI task or in more practical application, as a possible threat implicator. 

For future development the script could be tuned to be more robust and the RE's to be more precise (in certain field). The user interface is not the best possible but something I wanted to add so that the user can change the RE's mid-process. The termination might have been better to implement with own signal handler.  

I found that the assignment was a little too vague, although I know that the intention was to leave room for thinking. I hope that my implementation is to the same direction that was expected.  
