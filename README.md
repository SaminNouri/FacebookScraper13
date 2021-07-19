# FacebookScraper:

requirements:<br />
1- pip install pymongo<br />
2- pip install facebook-scraper

The JSON file named "post.json" contains the features of the posts that the scraper gathers. If the value of the feature is True then the scraper will get that feature of the users and if the value is False the scraper won't scrape that feature

The JSON file named "prof.json" contains the features of the profiles that the scraper gathers. If the value of the feature is True then the scraper will get that feature of the users and if the value is False the scraper won't scrape that feature

The JSON file named "Output.json" contains the three fields:<br />
-cluster: the URL of the MongoDB database to save to<br />
-database: the name of the database in Mongodb<br />
-collection: the name of the collection in the database that the data will be stored in it.<br />

The file named "users.txt" contains the names of the users.<br />
In this file there should be a symbol that splits the usernames.<br />
The default symbol is '\n'.<br />
It is possible to change this symbol with something such as ',' by using the following code:
```
python cli.py --cookies cookies.txt --Users users.txt --splitter , --postPath post.json --profilePath prof.json --outputPath Output.json
```
It is necessary to get the cookies of the browser in a txt file as argument.

It is also possible to only scrape the profile of the users:
```
python cli.py --cookies cookies.txt --Users users.txt --profilePath prof.json --outputPath Output.json
```
It is also possible to only scrape the posts of the users:
```
python cli.py --cookies cookies.txt --Users users.txt --postPath post.json --outputPath Output.json
```

