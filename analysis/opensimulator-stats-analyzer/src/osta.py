#!/usr/bin/python

import pprint
import re
import sys

if len(sys.argv) <= 1:
    print "Usage: %s <stats-log-path>"
    sys.exit(1)

lineRe = re.compile("(.* .*) - (.*) : (\d+)[ ,]([^:]*)")
data = {}

with open(sys.argv[1]) as f:
    for line in f:    
        match = lineRe.match(line)
        
        if match != None:
            statFullName = match.group(2)
            value = match.group(3)
            
            # print "%s: %s" % (statFullName, value)
            
            if not statFullName in data:
                data[statFullName] = []
                
            data[statFullName].append(float(value))
            
for stat, values in data.items():
    # print "%s: %s" % (stat, ", ".join(values))
    print "%s: min %s, max %s" % (stat, min(values), max(values))