#!/usr/bin/env python

import fiber

def foo():
    fiber.sleep(1)
    print("foo()")

def main():
    print "foo"
    fiber.create(foo)
    fiber.sleep(1)
    print "bar"

if __name__ == "__main__":
    main()
