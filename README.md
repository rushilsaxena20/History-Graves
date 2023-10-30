# History-Graves

History Graves is a python script that analyses Google Chrome browsing history and provides a detailed graph of the websites visited and the frequency of the number of visits using Google Takeouts. It also dumps the incognito history of your system.

# Initial Setup

Follow the below steps and make sure you satisfy all requirements:
-Install Python 3+: If you don't already have Python 3+ installed, grab it from
https://www.python.org/downloads/. You'll want to download and install the latest version of Python
3.x. As of 2019-10-14, that is Version 3.8.

# Get Your Location Data

You can get all of the information Google has on you here: https://takeout.google.com/
You only need to download the data mentioned in the repository scope, which Google will supply to you, to utilise this script.
You only need to download your "Chrome BrowserHistory," which Google will send to you as a JSON file by default, to utilise this script. Make sure to put the file in the same file/directory with the script.

# Usage

In the command prompt or Terminal window, type the following, and press enter:
python main.py <file> Replace <file> with BrowserHistory.json file from Google Takeout (the file name might vary, so use the one suitable in your case).
* commands:
* main.py [file-name] [-h] [-s SIZE] [-d DAYS]
* positional arguments:
  * file-name: Your JSON file downloaded from Google Takeout.
* optional arguments:
  * -h The Help option prints the console's usage section.
  * -s, --size Number of sites display (15 by default)
  * -d, --days Number of last X days to show data for (60 by default)
  
# Examples
* python main.py BrowserHistory.json
* python main.py BrowserHistory.json -d 80
* python main.py BrowserHistory.json --size 30
* python main.py BrowserHistory.json -s 60 --days 9
