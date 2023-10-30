from utils import generate_plot, chart_json
from argparse import ArgumentParser, RawTextHelpFormatter #to pass arguments in cli
import subprocess # to execute system commands

subprocess.call([r'incognito.bat'])

if __name__ == '__main__': #used to check if we are directly executing the main file

    def get_options():

        parser = ArgumentParser(formatter_class=RawTextHelpFormatter)
        parser.add_argument("file", metavar="file", type=str, help="Google takeout JSON file.") #positional arguments
        parser.add_argument("-s", "--size", dest="size", type=int, #optional arguments
        help="Number of top sites to be displayed.", default=20)
        parser.add_argument("-d", "--days", dest="days", type=int, #optional arguments
        help="Number of x last days of data to be displayed.", default=60)
        return parser.parse_args() #to handle user input from cli

    options = get_options()
    
    print("(1/2): Processing data")
    data = []
    data.append(chart_json(options.file, options.days))

    print("(2/2): Generating graph")
    generate_plot(data, options.size, options.days) 