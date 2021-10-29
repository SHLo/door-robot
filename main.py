from dotenv import load_dotenv
load_dotenv()

import argparse
import os
from users import users
from robot import robot

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('action', type=str)
    parser.add_argument( '-log',
                     '--loglevel',
                     default='warning',
                     help='Provide logging level. Example --loglevel debug, default=warning')

    args = parser.parse_args()

    if args.action == 'register':
        users.register()
    
    else:
        robot.power_on()