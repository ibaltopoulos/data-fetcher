import csv
import dateutil.parser
import ctypes
import os
import platform
import pyodbc
import random
from time import sleep


def get_db_data():
    connection = pyodbc.connect('Driver={SQL Server};Server=quantdb;')
    cursor = connection.cursor()
    cursor.execute("select top 100 * from QuantAnalyst.dbo.IP_zscores")
    rows = cursor.fetchall()
    for row in rows:
        print row.sec_id, row.zscore_4yrs

# - Check if we have enough storage to download one more file. We should have about 100 MB left
# before we start the whole process


def get_free_space_mb(dirname):
    """Return folder/drive free space (in megabytes)."""
    if platform.system() == 'Windows':
        free_bytes = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(dirname), None, None, ctypes.pointer(free_bytes))
        return free_bytes.value / 1024 / 1024
    else:
        st = os.statvfs(dirname)
        return st.f_bavail * st.f_frsize / 1024 / 1024


# - check if the file exists before starting to download
# if the file exists read the top 10 lines and the bottom 10 lines
# find the earliest (is it sorted in asc or desc order?
# if the last data date is before today (or yesterday) then we want to download
# the latest data
# download the latest data and append (?) to the CSV file? What about price close adjustments?
# The files should be written out in a sensible way
#   - One directory per country?
#   - One file per company, this is for the prices. What about the fundamentals?
#   -


def op():
    with open('file.csv') as f:
        reader = csv.reader(f)
        first = dateutil.parser.parse(reader.next()[3])
        for row in reader:
            pass
    last = dateutil.parser.parse(row[3])

    print('%s - %s' % (first, last))
    # OUTPUTS:
    # 2015-10-25T18:02:30.798426Z - 2015-10-25T18:02:30.862365Z
    # If you then want to get first and last back into a datetime object (from isoformat), you can


# For every request we make to either bloomberg or yahoo finance, we wait a random amount
# of time between 0 and 30 seconds.


def wait_random(max_duration_sec):
    random_duration_sec = random.uniform(0, max_duration_sec)
    print "Rand: %s" % random_duration_sec
    sleep(random_duration_sec)


def main():
    print "This only executes when %s is executed rather than imported" % __file__
    print get_free_space_mb("O:\\")
    get_db_data()
    for i in range(50):
        wait_random(3)
        print "Loop: %s" % i

if __name__ == '__main__':
    main()
