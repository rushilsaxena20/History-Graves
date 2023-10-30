import json, time
import numpy as np
import matplotlib.pyplot as plt
from heapq import nlargest
from operator import itemgetter

from ignore import IGNORE

DAY = 86400000 # miliseconds - one day

# generate plots
def generate_plot(data:list, size,days):
    # define figure
    fig, links_plot = plt.subplots()
    fig.canvas.set_window_title("History Graves")

    # LINKS PLOT
    links_plot.invert_yaxis()
    links_plot.set_xlabel('Number of visits')
    links_plot.set_title('Top %d most visited websites in the last %d days' % (size, days))
    # plot variables
    sorted_data = nlargest(size, data[0], key=itemgetter(1)) #used to get sites from json file with highest views
    sitenames = [el[0] for el in sorted_data]
    occurences = [el[1] for el in sorted_data]

    # set figure variables
    links_plot.barh(np.arange(len(sitenames)), occurences, align='center', color="#bcefb3")
    links_plot.set_yticks(np.arange(len(sitenames)))
    links_plot.set_yticklabels(sitenames, minor=False, color="#43a408")
    for ind, oc in enumerate(occurences):
        links_plot.text(oc + oc * 0.005, ind + .25, str(oc), color='#43a408')
    print("[+] Your data was analyzed successfully")
    plt.show()

# process json file
def chart_json(json_file : str, days : int):

    required_time = int(round(time.time() * 1000)) - (days * DAY)
    # read json file
    with open(json_file, mode = 'r', encoding="utf8") as data_file:
        data = json.load(data_file)

    sites = []
    instances = []
    # process data
    for data_set in data['Browser History']: # accessing the values of the key(Browser history) in the dictionary

        timestamp = round(int(data_set['time_usec']) / 1000)
        if required_time > timestamp:
            continue

        url = data_set['url']
        try:
            url = url_formatter(url)
        except AssertionError:
            continue

        if url not in sites:
            # index url
            sites.append(url)
            instances.append(1)
        else:
            # increment instance
            instances[sites.index(url)] += 1

    # merge url and instance to a tuple
    merged_list = [(site, inst) for site, inst in zip(sites, instances)] 

    return merged_list

# format the url to a standart format "url.TLD"
def url_formatter(url : str) -> str:

    # check if needs to be skipped
    for ign in IGNORE:
        assert (ign not in url)

    # remove string following TLD
    url = '/'.join(url.split('/')[:3])

    # subtract subdomains
    dot_index = [i for i, ltr in enumerate(url) if ltr == '.']
    if len(dot_index) > 1:
        url = url[: url.find('/') + 2] + url[dot_index[-2] + 1 :]

    # subtract port
    colon_index = [i for i, ltr in enumerate(url) if ltr == ':']
    if len(colon_index) > 1:
        url = url[: colon_index[-1]]

    # remove url protocol
    url = url.replace('http://', '').replace('https://', '')

    assert (len(url) > 3)
    return url

