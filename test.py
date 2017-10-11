#!/usr/bin/env python

import fiber

def main():
    print "foo"
    fiber.sleep(1)
    print "bar"

if __name__ == "__main__":
    main()
