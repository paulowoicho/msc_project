"""
This script takes in the Spotify Dataset and reformats it into a .db file which can easily
be exported as a .csv file. This is so that the data can be worked with easily using Pandas.


***Few Notes****
- Ran out of memory trying to write data to a dataframe and to a csv file (could have used a VM)
- Wrote it out to a db file instead and exported it to a csv
- should be able to import the data into colab as a dataframe straight away

"""
import json
from pathlib import Path
import sys
import sqlite3 


connection = sqlite3.connect("podcast_testset.db") #instantiate a database to write the table to
crsr = connection.cursor()

# SQL command to create a table in the database 
sql_command = """CREATE TABLE dataset ( 
episode_id TEXT PRIMARY KEY, 
transcript TEXT 
);"""

# execute the statement 
crsr.execute(sql_command)

def add_to_sql(podcast):
    """
    This function takes in the podcast's json transcript file and concatentates all the transcript
    segments to form a long running transcript. Information regarding when each word is uttered is 
    discarded. It builds an sql table that is then written to a .db file.
    """
    transcript = ""
    with open(str(podcast)) as json_file:
        data = json.load(json_file)
        for item in data['results']:
            try:
                transcript += ' ' + item['alternatives'][0]['transcript']
            except:
                pass #not all item with 'alternatives' key contain a 'transcript' key
    
    episode_id = "spotify:episode:" + Path(podcast).stem #This is the format of the episode_uri in the metadata.csv file
    

    sql_command = "INSERT INTO dataset (episode_id, transcript) VALUES (?, ?);"
    vals = (episode_id, transcript)
    crsr.execute(sql_command, vals)


def podcasts_to_df(directory_path):
    """
    This function takes in the folder where the dataset is located and builds a table for each
    podcast transcript file in the folder.
    """
    rootdir = Path(directory_path)
    file_list = [f for f in rootdir.glob('**/*') if f.is_file()]
    
    for file in file_list:
        add_to_sql(file)

podcasts_to_df('spotify-podcasts-2020-test')
connection.commit()
connection.close()
