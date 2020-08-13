''' Github 
    Userid
    Checker'''

import os
import requests
import re
from bs4 import BeautifulSoup

headers = requests.utils.default_headers()
headers.update(
    {
        'User-Agent': 'Safal',
        'From': 'none'
    }
)

print(F'''
              _   _                 
             | | | |                
  _ __  _   _| |_| |__   ___  _ __  
 | '_ \| | | | __| '_ \ / _ \| '_ \ 
 | |_) | |_| | |_| | | | (_) | | | |
 | .__/ \__, |\__|_| |_|\___/|_| |_|
 | |     __/ |                      
 |_|    |___/         
 -safal30
''')

userid = input("Github Id: ")

#fetch website
url = "https://github.com/"
url_id = url + userid
print(f"\nUrl: ",url_id,"\n")

#page response function
def response(urlx):
    url_res = requests.get(url_id, headers=headers)
    url_status = url_res.status_code

    if url_status == 400 or url_status == 404:
        print("Use ID not found / Please recheck and enter ID again")
        GithubID = False
    elif url_status == 503:
        print("Website down or couldn't be fetched")
        GithubID = False
    elif url_status == 200:
        print("User ID found >> fetching details...")
        GithubID = True

        #followers - following - repos - contribs
        def stats(urlx):
            url_text = url_res.text
            follow_bs = BeautifulSoup(url_text, "html.parser")

            try:
                text_followers = follow_bs.select_one("span.text-bold.text-gray-dark").text.strip()
                print("\nFollowers:",text_followers)

                text_following = follow_bs.select("span.text-bold.text-gray-dark")[1].text.strip()
                print("Following:",text_following)
            except:
                print("\nPrivate profile or no followers / following")

            try:
                text_repos = follow_bs.select_one("span.Counter").text.strip()
                print("Public Repositories:",text_repos)
            except:
                print("No public repositories found")

            try:
                text_contrib = follow_bs.select("h2.f4.text-normal.mb-2")[1].text.strip()
                print(text_contrib[:-25], "recorded")               
            except:
                print("No contributions found")
            
            #popular repos - customised pins
            try:
                print("\nPopular / Pinned Repositories:")
                text_popular_repos = follow_bs.select("span.repo")

                for i in text_popular_repos:
                    name = i.text.strip()
                    print(name)
                else:
                    return                
            except:
                print("No popular / pinned repos found")
                

        stats(url_id)

    else:
        print("Error")
    return GithubID



if __name__ == "__main__":
    response(url_id)
