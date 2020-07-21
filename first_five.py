import sys
from pathlib import Path
from nltk.tokenize import sent_tokenize

podcast = sys.argv[1]
first_five = None
with open(podcast) as podcast_content:
    content = podcast_content.read()
    first_five = sent_tokenize(content)[0:5]

first_five = ' '.join(first_five)
with open('summaries/first_five_summaries/'+ Path(podcast).stem + '_summary.txt', 'a') as summary:
    summary.write(first_five)