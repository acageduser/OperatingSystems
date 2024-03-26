'''
Usage: python graphcrunch.py [z]f1|[z]m1 ARGS
    where f1 args are one crunchFileName followed by parameters to graph, or
    where m1 args are one parameter to graph followed by multiple crunchFiles.
    A 'z' in front of f1 or m1 forces the y axis to start at 0.
'''
# graphcrunch.py, D. Parson, fall 2016
# Graph data from one or more simulation algorithm runs.

import copy
import math
import sys
import numpy as np  # for bar graph, 9/24/2016
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.axes as axes
from matplotlib.ticker import FuncFormatter, MaxNLocator

__usage__ = '''
USAGE: python graphcrunch.py f1|m1 ARGS
    where f1 args are one crunchFileName followed by parameters to graph, or
    where m1 args are one parameter to graph followed by multiple crunchFiles.
'''

if __name__ == '__main__':
    if ((len(sys.argv) < 5)
        or (sys.argv[1] != 'f1' and sys.argv[1] != 'm1'
            and sys.argv[1] != 'xf1' and sys.argv[1] != 'xm1')):
        sys.stderr.write(__usage__)
        sys.exit(1)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    csvhdr = ''
    csvvalues = ''
    if sys.argv[1] == 'f1' or sys.argv[1] == 'xf1':
        # for bar graph, 9/24/2016, morphed to plot adjacent pairs
        iszeroed = (sys.argv[1] == 'xf1')
        csvhdr = 'FILE'
        csvvalues = sys.argv[2]
        exec("from " + sys.argv[2] + " import *")
        plotlist = []
        xlbls = []
        plotlist = [[], []] # morphed to plot adjacent pairs
        xlbls = [[], []] # morphed to plot adjacent pairs
        tid = 0 # morphed to plot adjacent pairs
        maxy = 0
        miny = -10
        for vname in sys.argv[3:]:
            v = eval(vname)
            plotlist[tid].append(v)
            maxy = max(maxy, v)
            if miny < 0:
                miny = v
            else:
                miny = min(miny, v)
            xlbls[tid].append(vname.replace('SUM_timeInJail_thread_','T').replace('_process_','P'))
            csvhdr = csvhdr + "," + vname
            csvvalues = csvvalues + "," + str(v)
            tid = 1 - tid
        ## old plt.ylabel('f1 ' + sys.argv[2])
        # if iszeroed:
            # plotlist.append(0)
            # xlbls.append('0')
            # # ax.autoscale_view(scaley=False)
            # # ax.axis([0, len(xlbls)-1, 0, maxy])
            # # plt.ylim(0, maxy)
        # START STUFF ADDED FOR PAIRED BAR GRAPHS 9/24/2016
        # http://people.duke.edu/~ccc14/pcfb/numpympl/MatplotlibBarPlots.html
        ## necessary variables
        ind = np.arange(len(plotlist[0])) # # the x locations for the groups
        width = 0.35 # the width of the bars
        ## the bars
        rects1 = ax.bar(ind, plotlist[0], width,
            color='black',yerr=None)
        rects2 = ax.bar(ind+width, plotlist[1], width,
            color='gray',yerr=None)
        # old xs = range(len(xlbls))
        def format_fn(tick_val, tick_pos): # not used here
            if int(tick_val) in xs:
                return xlbls[int(tick_val)]
            else:
                return ''
        # old ax.xaxis.set_major_formatter(FuncFormatter(format_fn))
        # old ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        # old for tick in ax.get_xticklabels():
            # old tick.set_rotation(90)
        # axes and labels
        ax.set_xlim(-width,len(ind)+width)
        ax.set_ylim(miny-10,maxy)
        ax.set_ylabel('f1 ' + sys.argv[2])
        ax.set_title("timeInJail by pairs of partner threads, "
            + "Pn is process, Tn is thread")
        xTickMarks = ['P'+str(i) for i in range(0,10)]
        ax.set_xticks(ind+width)
        xtickNames = ax.set_xticklabels(xTickMarks)
        plt.setp(xtickNames, rotation=45, fontsize=10)
        ## add a legend
        ax.legend( (rects1[0], rects2[0]), ('T0', 'T1') )
        ## old plt.plot(plotlist)
        # END STUFF ADDED FOR PAIRED BAR GRAPHS 9/24/2016
        fig.savefig(sys.argv[2] + '.png')
        # plt.show()
    else: # NOT if sys.argv[1] == 'f1' or sys.argv[1] == 'xf1':
        iszeroed = (sys.argv[1] == 'xm1')
        vname = sys.argv[2]
        csvhdr = 'METRIC'
        csvvalues = sys.argv[2]
        # exec("from " + sys.argv[2] + " import *")
        plotlist = []
        xlbls = []
        maxy = 0
        miny = -1
        for fname in sys.argv[3:]:
            exec("from " + fname + " import *")
            v = eval(vname)
            plotlist.append(v)
            maxy = max(maxy, v)
            if miny < 0:
                miny = v
            else:
                miny = min(miny, v)
            xlbls.append(fname[:-7].replace('SUM_timeInJail_thread_','T').replace('_process_','P'))
            csvhdr = csvhdr + "," + fname
            csvvalues = csvvalues + "," + str(v)
        plt.ylabel('m1 ' + sys.argv[2])
        if iszeroed:
            plotlist.append(0)
            xlbls.append('0')
        xs = range(len(xlbls))
        def format_fn(tick_val, tick_pos):
            if int(tick_val) in xs:
                return xlbls[int(tick_val)]
            else:
                return ''
        ax.xaxis.set_major_formatter(FuncFormatter(format_fn))
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        plt.plot(plotlist)
        fig.savefig(vname + '.png')
        # plt.show()
    if csvhdr and csvvalues:
        f = open(sys.argv[2] + ".csv", 'w');
        f.write(csvhdr + '\n' + csvvalues + '\n')
        f.close()
