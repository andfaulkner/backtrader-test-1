import os.path  # To manage paths
import sys  # To find out the script name (in argv[0])

def get_data_feed_path():
    # Datas are in a subfolder of the samples. Need to find where the script is
    # because it could have been called from anywhere
    modpath = os.path.dirname(os.path.abspath(sys.argv[0]))
    datapath = os.path.join(modpath, 'datas/sample-data/orcl-1995-2014.txt')
    return datapath
