import datetime
import sys

def log_error(error):
    print('❌ Error: ', datetime.datetime.now(), error, file=sys.stderr)

def log_info(info):
    print('📝 Info: ', datetime.datetime.now(), info)