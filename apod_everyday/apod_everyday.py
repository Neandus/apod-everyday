import argparse
import datetime
import sys

#Parse args and return date
def get_date_from_args(argv=None):
    parser = argparse.ArgumentParser(description='Download and set background from \'Astronomy Picture of the Day\'')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--today', help='choose today\'s picture', action='store_true', required=False)
    group.add_argument('--date', help='choose picture from gievn date (ISO format e.g. \'2021-03-28\')',
                        type=datetime.date.fromisoformat, required='--today' in sys.argv) #required only if --today is not given

    ret_date = None

    args = parser.parse_args(argv)
    
    if args.today == True:
        ret_date = datetime.datetime.now()
    else:
        ret_date = args.date

    return ret_date

if __name__ == "__main__":
    pass