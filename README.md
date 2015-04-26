#redirect_checker

Python tool that checks status codes for a site

At this time it also requires an external file with a list of directories or files to check the status of.

The input file should be in the format of: 
>/path

For example. If you want to check www.example.com/about and www.example.contact the text file should look like:

```
/about
/contact
```

To run:
-
From the command line run:
>python redirect_checker.py inputfile.txt outputfile.txt

The script now prompts the user asking what domain they want to check.

For example:
>What is the domain you want to check?

>http://example.com

**Be sure to include `http://` in front of the url.**