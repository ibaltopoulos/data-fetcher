from bs4 import BeautifulSoup
import urllib2
import random
from time import sleep


# Trustnet doesn't like it when you use python to retrieve pages so we
# need to impersonate chrome
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36"
}

urls = [
    # CF Lindsell Train UK Equity Class D - Accumulation (GBP)
    "http://www.hl.co.uk/funds/fund-discounts,-prices--and--factsheets/\
search-results/c/cf-lindsell-train-uk-equity-class-d-accumulation"
]


def wait_random(max_duration_sec):
    random_duration_sec = random.uniform(0, max_duration_sec)
    print "Wait (sec): %s" % random_duration_sec
    sleep(random_duration_sec)

for url in urls:
    wait_random(8)
    req = urllib2.Request(url, headers=headers)
    fileHandle = urllib2.urlopen(req)
    page = fileHandle.read()
    fileHandle.close()

    soup = BeautifulSoup(page, "lxml")
    fund_name = soup.find("div", id="security-title").find("h1").getText().strip()
    price = soup.find("span", class_="bid price-divide").getText().strip()
    date = soup.find("div", class_="price-unavailable").getText().strip()

    print fund_name
    print price
    print date
