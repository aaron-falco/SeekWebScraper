import csv
from urllib.request import urlopen
import os
from pathlib import Path
import re
import urllib

# searchUrl = 'https://www.seek.com.au/jobs-in-information-communication-technology/in-All-Sydney-NSW?&subclassification=6287%2C6290'
# changeableUrl = searchUrl
# insertIndex = searchUrl.find('?') + 1

# jobListingPattern = '<h3.*?/a>' # Pattern to search job listings. (Header 3 is used by Seek for Job Listings). End pattern with close tag for link (/a>).

# results = []

# i = 1
# while i > 0:
#     page = urlopen(changeableUrl)

#     html_bytes = page.read()
#     html = html_bytes.decode("utf-8")

#     length = len(re.findall(jobListingPattern, html))

#     if length < 2:
#         break
    
#     temp = re.findall(jobListingPattern, html)

#     results.extend(temp)
    
#     i += 1

#     newSearchUrl = searchUrl[:insertIndex] + 'page=' + str(i) + '&' + searchUrl[insertIndex:]
#     changeableUrl = newSearchUrl


# jobsLinks = []
# baseLink = "https://www.seek.com.au"

# for x in results:
#     temp = str(x)
#     linkstartindex = temp.find('<a href="') + len('<a href="')
#     linkendindex = temp.find('" class')
#     newLink = baseLink + temp[linkstartindex:linkendindex]
#     jobsLinks.append(newLink)

# temppage = urlopen('https://www.seek.com.au/job/73213698?ref=search-standalone&type=standard#sol=726693aeec4f665c471646fb6927a2d15917be6b')
# html_bytes = temppage.read()
# html = html_bytes.decode("utf-8")

# print(html)

# xyz = html.find("C#")

# path = Path(__file__).parent / "Output"
# if (not os.path.exists(path)):
#     os.mkdir(path)