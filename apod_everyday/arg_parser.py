import argparse
import datetime
import sys

class DateParseAction(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs is not None:
            raise ValueError("nargs not allowed")
        super(DateParseAction, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        if values < datetime.date(1995, 6, 20): 
            #I know there is also entry for 16th of June,
            # but starting from 20th of June entries goes continuous
            parser.error("Minimum correct date is 20th of June 1995")

        setattr(namespace, self.dest, values)

#Parse args and return date
def get_date_from_args(argv=None):
    parser = argparse.ArgumentParser(argv[0], description='Download and set background from \'Astronomy Picture of the Day\'')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--today', help='choose today\'s picture', action='store_true')
    group.add_argument('--date', help='choose picture from gievn date (ISO format e.g. \'2021-03-28\')',
                        type=datetime.date.fromisoformat, action=DateParseAction)

    ret_date = None

    args = parser.parse_args(argv[1:])

    if args.today == True:
        ret_date = datetime.datetime.now()
    else:
        ret_date = args.date

    return ret_date

if __name__ == "__main__":
    ret = get_date_from_args(argv=sys.argv)
    print(ret)