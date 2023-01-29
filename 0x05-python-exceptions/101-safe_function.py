#!/usr/bin/python3
def safe_function(fct, *args):
     try:
          e = fct(*args)
          return e
      except Exception as error:
          import sys
          print("Exception: {}".format(error), file=sys.stderr)
          return None
