#redirect_checker


Python tool that checks status codes for a site

At this time it also requires an external file with a list of directories or files to check the status of.

To run:
-
From the command line run:
>python redirect _ checker.py inputfile.txt outputfile.txt

The txt file should be in the format of: 
>/path

Example.
If you want to check www.example.com

Change the base _ url variable to the domain you are checking.

>base_url = #"URL"

to

>base_url = "example.com"
