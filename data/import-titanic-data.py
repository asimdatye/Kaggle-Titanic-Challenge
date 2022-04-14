import kaggle
import pandas

from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

# downloading from kaggle.com/c/sentiment-analysis-on-movie-reviews
# there are two files, train.tsv.zip and test.tsv.zip
# we write to the current directory with './'
api.competition_download_file('titanic',
                              'gender_submission.csv', path='./')
api.competition_download_file('titanic',
                              'train.csv', path='./')
api.competition_download_file('titanic',
                              'test.csv', path='./')
