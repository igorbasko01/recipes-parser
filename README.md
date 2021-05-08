# Youtube Recipes Downloader Parser and Loader
## Overview
The basic idea of this project is to automatically download the 
descriptions of youtube recipe videos, parse them into recipes and
separate ingredients using a CRF model from [mtlynch/ingredient-phrase-tagger](https://github.com/mtlynch/ingredient-phrase-tagger),
and load it into `neo4j`.

## Preparations
Before running the python app in this repo, we need to prepare the
environment:
1. Clone this repository.
1. Create a Google API key for downloading descriptions from youtube.
1. Install and Run a neo4j database.
1. Fill out the `settings.json` file.

### Create Google API key
A short explanation for creating an API key could be found in this
blog [post](https://igorbasko01.github.io/youtube/google/python/2021/03/22/youtube-video-desc-api.html)
under the `API` section.

### Install and Run a neo4j database
Download `neo4j` from the [Download Center](https://neo4j.com/download-center)
After installation, create a local database and run it.
The easiest way is to download a Neo4j Desktop and create a
database through it.

### Fill the settings file
Make the following changes:
1. Using the `settings-template.json` file, create a `settings.json`file.
1. Fill out the `google-api-key` setting.
1. Fill out the `neo4j.password` setting.
1. Replace the `youtube-channel` setting, with the channel id that you want to parse.

## Running the parser
The python app is separated into 3 sections.
1. Extractor - Downloads the descriptions and breaks them down to two sections: Recipe, Ingredients.
1. Transformer - Extracts the single ingredients from the ingredients section, with amount and extra information.
1. Load - Load the recipes and ingredients into neo4j. 

There are some `make` commands for easier execution.
1. `make run` - Runs all the sections in order.
1. `make run-extract` - Runs only the extract section.
1. `make run-transform` - Runs only the transform section.
1. `make run-load` - Runs only the load section.