# plotcrunch.py, D. Parson, fall 2015
# Plot the PLOTLIST from diffset.py for all crunch files.

import copy
import math
import sys
# See __main__ below: from diffset import DIFFMAP

usage = "python plotcrunch.py DIFFSET.py CRUNCHFILE..."
if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.stderr.write(usage + '\n')
        sys.exit(1)
    newstats = {}
    exec("from " + sys.argv[1] + " import PLOTLIST")
    metric2crfile = {}
    crunchlist = []
    for crunchfilename in sys.argv[2:]:
        try:
            fcrunch = open(crunchfilename, 'r')
        except IOError:
            fcrunch = None
            sys.stderr.write("Skipping missing file " + crunchfilename + "\n.")
        if fcrunch == None:
            continue
        crunchlist.append(crunchfilename)
        line = fcrunch.readline()
        while line:
            line = line.strip()
            if line:
                exec(line, newstats, newstats)
            line = fcrunch.readline()
        fcrunch.close()
        for metric in PLOTLIST:
            try:
                v = eval(metric, newstats, newstats)
            except NameError:
                v = 0
            if not metric2crfile.has_key(metric):
                metric2crfile[metric] = {}
            metric2crfile[metric][crunchfilename] = v
    plotfile = open("plotcrunch.csv", "w")
    # plotfile.write('METRIC')
    # for cr in crunchlist:
        # plotfile.write(',' + cr)
    # plotfile.write('\n')
    for metric in PLOTLIST:
        plotfile.write('METRIC')
        for cr in crunchlist:
            plotfile.write(',' + cr)
        plotfile.write('\n')
        plotfile.write(metric)
        for cr in crunchlist:
            plotfile.write(',' + str(metric2crfile[metric][cr]))
        plotfile.write('\n')
    plotfile.close()
