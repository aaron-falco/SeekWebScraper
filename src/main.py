from urllib.request import urlopen
from pathlib import Path
import os
import re
import csv
import sys

def hasMultiplePages(pageHtml: str) -> bool:
    if( pageHtml.find("y735df0 y735df3 _1iz8dgs5a _1iz8dgsfq") == -1 ):
        return False
    return True

def hasNextPage(pageHtml: str) -> bool:
    anchorTagStartIndex = pageHtml.find('<', pageHtml.find("y735df0 _1iz8dgsa6 _1iz8dgs9v _1iz8dgsw"))
    anchorTagEndIndex = pageHtml.find('>', anchorTagStartIndex)
    if( pageHtml.find('hidden="false"', anchorTagStartIndex, anchorTagEndIndex) == -1 ):
        return False
    return True

def seachPage(pageHtml: str, pattern: str):
    rtrn = re.findall(pattern, pageHtml)
    rtrn.pop()
    return rtrn

def main() -> int:
    programmingLanguages = ['C#', 'C++', 'Java', 'JavaScript', 'PHP', 'SQL', 'React', 'F#', 'Python', 'HTML', 'CSS', 'JSON'] # Programming languages to search for.
    progLangInstances = [0,0,0,0,0,0,0,0,0,0,0,0] # Number of times each programming language was found, in the same order as 
    jobListingPattern = '<h3.*?/a>' # Pattern to search job listings. (Header 3 is used by Seek for Job Listings on the search page). End pattern with close tag for link (/a>).

    searchUrl = 'https://www.seek.com.au/jobs-in-information-communication-technology/engineering-software/in-North-Shore-&-Northern-Beaches-Sydney-NSW?'
    #'https://www.seek.com.au/jobs-in-information-communication-technology/engineering-software/in-St-Leonards-NSW-2065?distance=0'
    # https://www.seek.com.au/jobs-in-information-communication-technology/engineering-software/in-St-Leonards-NSW-2065?distance=0&jobId=75737782&type=standard
    #'https://www.seek.com.au/jobs-in-information-communication-technology/developers-programmers/in-North-Shore-&-Northern-Beaches-Sydney-NSW'

    page = urlopen(searchUrl)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")

    results = []

    if (hasMultiplePages(html) == False):
        results.extend(re.findall(jobListingPattern, html))
        results.pop()

    else:
        changeableUrl = searchUrl
        insertIndex = searchUrl.find('?') + 1
        pageNum = 1
        nextPageExists = True
        while nextPageExists:
            page = urlopen(changeableUrl)
            html_bytes = page.read()
            html = html_bytes.decode("utf-8")
            pageNum += 1
            results.extend(seachPage(html, jobListingPattern))
            changeableUrl = searchUrl[:insertIndex] + 'page=' + str(pageNum) + '&' + searchUrl[insertIndex:]
            nextPageExists = hasNextPage(html)
        
    
    

    jobsLinks = []
    baseLink = "https://www.seek.com.au"

    i = 0

    while i < len(results):
        temp = str(results[i])
        linkstartindex = temp.find('<a href="') + 9
        linkendindex = temp.find('" class')
        jobsLinks.append(baseLink + temp[linkstartindex:linkendindex])
        i += 1



    i = 0
    while i < len(jobsLinks):
        
        page = urlopen(jobsLinks[i])
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")

        j = 0

        while j < len(programmingLanguages):
                if html.find(programmingLanguages[j]) != -1:
                    progLangInstances[j] += 1
                j += 1
        i += 1
    
    progLangInstances[2] -= progLangInstances[3]

    
    path = Path(__file__).parent / "Output"
    if (not os.path.exists(path)):
        os.mkdir(path)
    f = open(path / 'ProgLangCount.csv', 'w')
    fWriter = csv.writer(f)
    fWriter.writerow(programmingLanguages)
    fWriter.writerow(progLangInstances)
    f.close()
    
    return 0

if __name__ == '__main__':
    sys.exit(main())