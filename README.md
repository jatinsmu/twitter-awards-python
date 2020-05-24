# Award Winner Names from Twitter in Real-Time

# Description
This project extracts the names of people winning awards from twitter live feeds in real-time. You can modify the search strings to extract
names for people associated with any event. 
The data is unstructured in nature and hence we use Text Mining techniques to extract useful information.

# Installation
``` Python 3+ ```

# Libraries required
``` NLTK ```
``` names_dataset ```
``` word_tokenize ```
``` stopwords ```

You can install these libraries by using pip. eg. ```pip install names_dataset```

# Usage
You need to have Twiter Developer API credentials in order to use this project.
Enter your credentials as required at line 19-22. Set the ```count``` to any number of results that you want to search from the twitter live feed.
Run the script, and you would see a list containing names of all the award winners.
