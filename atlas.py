import nomic
from nomic import atlas
import json  # Importing json module to work with json files

# Opening and loading the JSON file
with open('posts.json', 'r') as f:
    my_data = json.load(f)  # Load the json file into a python object

# Build a map using the map_data method

WEB_URL = 'https://www.bramadams.dev'
INDEXED_FIELD = 'plaintext'
DESCRIPTION = 'A embedded collection of blog posts on ' + WEB_URL + '.' + ' The posts are indexed by their ' + INDEXED_FIELD + ' field.'

dataset = atlas.map_data(data=my_data,
                          indexed_field=INDEXED_FIELD,  
                          description=DESCRIPTION,
                          )
dataset.maps[0]  # to view map build status

