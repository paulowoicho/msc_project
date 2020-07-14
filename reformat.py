"""
Since json files contain fragemented sentences, combine each fragment to form a
continuous document.

"""
import json

transcript = ''

with open('399kdfMnjw0KYANZU7CQJ0.json') as json_file:
    data = json.load(json_file)
    for item in data['results']:
        try:
            transcript += ' ' + item['alternatives'][0]['transcript']
        except:
            pass #not all item with 'alternatives' key contain a 'transcript' key

f = open("concat.txt", "a")
f.write(transcript)
f.close()