# Automatic Podcasts Summarisation using the Spotify Podcasts Dataset (MSc Project)

This project explores automatic podast summarisation using the [Spotify Podcasts Dataset](https://arxiv.org/abs/2004.04270) and several extractive and extractive models. This project was done in the context of the [TREC 2020 Podcasts Track](https://podcastsdataset.byspotify.com/). This repo contains the helper scripts and notebooks used to conduct the experiments. 

The code for fine-tuning the abstractive models are based on [Fine-tune T5 for Summarization](https://github.com/abhimishra91/transformers-tutorials/blob/master/transformers_summarization_wandb.ipynb) by [Abhishek Kumar Mishra](https://github.com/abhimishra91) and from Blurr's official [documentation](https://ohmeow.github.io/blurr/modeling-summarization/) 

The code for the Keyword Extraction technique used to filter the original dataset is based on code from [Understand TextRank for Keyword Extraction by Python](https://towardsdatascience.com/textrank-for-keyword-extraction-by-python-c0bae21bcec0) by [Xu Liang](https://towardsdatascience.com/@bramblexu)

## Project Contents

    /experiments
This directory contains all the notebooks used to run the experiments for this project. It contains code
used to explore the data, train the abstractive models, generate results, and upload the model to the HuggingFace
Library.

    /summariser-package

This directory contains the code used to make the Python Package that leverages the fine-tuned T5 model

`reformat.py` and `data_extraction.py`

These files contain the code used to extract the json transcripts from the compressed tar file they were 
distributed in and reformat them for easy use with Pandas.

`podcast-testset.db`

This file is a sample of the end result of extracting and reformating the distributed data.

## Results

### Quantitative

For the quantitative evaluation, models are scored by the ROUGE metric using creator descriptions as gold summaries.
Since the summaries vary in quality, and there are many ways to summarise a podcast, these results only show what model best
approximates the creator summaries.

| Model | ROUGE 1-F  | ROUGE 2-F  | ROUGE L-F |
| :-----: | :-: | :-: |:-: |
| Supervised BART | 18.4 | **4.8** | 15.7 |
| First Five Sentences | 13.7 | 2.0 | 11.8 |
| Extractive Pipeline with BERT | 13.6 | 1.6 | 10.9 |
| Extractive Pipeline with SpanBERT | 15.2 | 1.7| 12.3 |
| Extractive Pipeline with BERT and Coreference Resolution | 14.9 | 1.6 | 11.7 |
| T5 | **18.5** | 4.3 | **16.6** |
| PEGASUS | 17.2 | 3.9 | 15.5 |
| Extractive Pipeline with SpanBERT + T5 | 16.9 | 3.5 | 15.1 |

### Qualitative

For the qualitative evaluation, volunteer evaluators are asked to evaluate the models summaries on an EGFB scale.
Overall, the assessors preferred the summaries generated by T5 the most.

| Grade | T5(Fine-Tuned) | PEGASUS(Fine-Tuned) | Extractive w/ Span-BERT | SpanBERT(Top-15) +T5 | First-15 Sentences +T5| 
| :-----: | :-: | :-: |:-: | :-: |:-: |
E: Excellent | 33 | 23 | 0 | 25 | **36**
G: Good |**80** | 53 | 38 | 55| 57
F: Fair | 22 | 37 | 67 | 40 |40
B: Bad |15 | 37 | 45 | 30 |17

Quantitatively and qualitatively, T5 model performs best overall. Summaries generated by all models can be found [here](https://docs.google.com/spreadsheets/d/1sVvH8Mrw0cGDgtG6Wqf--azpRp9E9D-FcMEA5qaMMmU/edit?usp=sharing)

## Other Outputs
Asides the submission to TREC with summaries generated on the official testset, other outputs of this project include: 

 - A python package hosted on the Python Package Index that leverages the fine-tuned T5 model to generate summaries. This package is available here https://pypi.org/project/t5-podcast-summariser/
 - The fine-tuned T5 model made available on the huggingface library. The model is available here: https://huggingface.co/paulowoicho/t5-podcast-summarisation
