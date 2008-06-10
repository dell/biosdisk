#!/usr/bin/python

def between(line, first, second):
    return line.split(first)[1].split(second)[0]
