#!/usr/bin/env python 
# Sean Meadows - designed27@gmail.com
# FizzBuzz

import logging
#logging.basicConfig(level=logging.DEBUG)

import sys
w = sys.stdout.write

def fizzbuzz(start=1, stop=101):
    logging.debug("Fizzbuzz from %d to %d." % (start, stop))
    for i in range(start,stop):
        logging.debug("%s: " % i)
        if i%3==0:
            w("Fizz")
        if i%5==0:
            w("Buzz")
        if (i%3<>0 and i%5<>0):
            # Not divisible by either
            w("%d" % i)
        w("\n")
if __name__ == "__main__":
    fizzbuzz()
