from pytrends.pyGTrends import pyGTrends
import time
from random import randint



google_username = input('Enter your googleaccount username')
google_password = input('Enter password:')
path = ""
subject = input('In what trend are you interested?')
# connect to Google
connector = pyGTrends(google_username, google_password)
# make request
connector.request_report(subject)
# wait a random amount of time between requests to avoid bot detection
time.sleep(randint(5, 10))
# download file
connector.save_csv(path, subject)
# get suggestions for keywords
#keyword = "milk substitute"
#data = connector.get_suggestions(keyword)
#print(data)
