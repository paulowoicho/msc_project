"""
Since json files contain fragemented sentences, combine each fragment to form a
continuous document.

"""
import json
from pathlib import Path
import sys


# podcast = sys.argv[1]

def reformat(podcast):
    transcript = ''
    with open(str(podcast)) as json_file:
        data = json.load(json_file)
        for item in data['results']:
            try:
                transcript += ' ' + item['alternatives'][0]['transcript']
            except:
                pass #not all item with 'alternatives' key contain a 'transcript' key
    
    f = open('concatenated/'+ Path(podcast).stem + '.txt', "a")
    f.write(transcript)
    f.close()


rootdir = Path('C:\\Users\\Owoicho\\Desktop\\testes\\spotify-podcasts-2020')
# Return a list of regular files only, not directories
file_list = [f for f in rootdir.glob('**/*') if f.is_file()]

for file in file_list:
    reformat(file)