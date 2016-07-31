from bs4 import BeautifulSoup
import urllib2
import random
from time import sleep

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Trustnet doesn't like it when you use python to retrieve pages so we
# need to impersonate chrome
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36"
}

urls = [
    # AXA Framlington Global Technology Z Acc
    "https://www.trustnet.com/Factsheets/Factsheet.aspx?fundCode=FRMNFI&univ=O&typeCode=F03TL",
    # FUNDSMITH LLP EQTY FD T CL ACC STERL DIRE
    "https://www.trustnet.com/Factsheets/Factsheet.aspx?fundCode=LSFX1&univ=O&typeCode=FLSX3",
    # MAJEDIE ASSET MGT UK INCOME X ACC NAV
    "https://www.trustnet.com/Factsheets/Factsheet.aspx?fundCode=GGFQH&univ=U&typeCode=FGRHG",
    # PREMIER PORTFOLIO PAN EURP PROP C DIS NAV
    "https://www.trustnet.com/Factsheets/Factsheet.aspx?fundCode=BDF01&univ=O&typeCode=FEZB6",
    # THREADNEEDLE INV SPECIALIST CHINA OPPS ZNA
    "https://www.trustnet.com/Factsheets/Factsheet.aspx?fundCode=T1F54&univ=O&typeCode=FG7DP",
    # RIVER & MERCANTILE FUNDS ICVC - UK EQUITY SMALLER COMPANIES B ACC
    "https://www.trustnet.com/Factsheets/Factsheet.aspx?fundCode=R2F96&univ=O&typeCode=FRMUS",
    # AXA FRAMLINGTON UN BIOTECH Z ACC
    "https://www.trustnet.com/Factsheets/Factsheet.aspx?fundCode=FRBIOI&univ=O&typeCode=F11VD",
    # GLG PARTNERS INV CONTINENTAL EURP PROF C
    "https://www.trustnet.com/Factsheets/Factsheet.aspx?fundCode=4SEGA&univ=O&typeCode=FZJ54",
    # GOLDMAN SACHS INDIA EQUITY PTF R GBP
    "https://www.trustnet.com/Factsheets/Factsheet.aspx?fundCode=CAFH8&univ=B&typeCode=FF4KZ",
    # CITI FINANCIAL ABSOLUTE EQUITY I ACC
    "https://www.trustnet.com/Factsheets/Factsheet.aspx?fundCode=BEFF0&univ=O&typeCode=FBEF2"
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
    price_info_row = soup.find("div", class_="panel_widget price").find_all("tr")[1]
    price_info_row_children = price_info_row.findChildren()

    fund_name = price_info_row_children[0].getText().strip()
    unit_type = price_info_row_children[1].getText().strip()
    currency = price_info_row_children[2].getText().strip()
    price = price_info_row_children[3].getText().strip()
    date = price_info_row_children[4].getText().strip()
    citicode = price_info_row_children[6].getText().strip()
    sedol = price_info_row_children[7].getText().strip()
    isin = price_info_row_children[8].getText().strip()

    print fund_name
    print unit_type
    print currency
    print price
    print date
    print citicode
    print sedol
    print isin
