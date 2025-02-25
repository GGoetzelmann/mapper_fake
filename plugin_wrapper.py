import sys
import logging

if __name__ == "__main__":
    # Extract arguments from the command line
    received_arguments = sys.argv[1:]
    for a in received_arguments:
      logging.info("Received parameter: {}".format(a))
