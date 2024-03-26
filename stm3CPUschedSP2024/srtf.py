# CSC343.template.txt, D. Parson, Fall 2013
# This file is a template for CSC343Compile.py that compiles a
# state machine into a Python simulation framework,
# for use in CSC 343 Operating Systems, beginning Fall 2013.
# See CSC343Compile.py and CSC343Sim.py.
# http://faculty.kutztown.edu/parson
# package state2codeV17

import os
import sys
import types
import random
import math
import operator
import functools
# ^^^ partial & reduce in 2.[67]
import traceback
from state2codeV17.CSC343Sim import __simulationScheduler__,                 \
    __ThreadRetireException__, _Processor_, _IOunit_, _Thread_,             \
    __simulationLogger__, gentestSampleDistribution, __scheduledObject__,   \
    Queue, _SubGraph_, __DEBUGLEVEL__, PCB, ModelState, __MAIN_THREAD_EXITED__

class processor(_Processor_):
    '''
    CSC343Compile.py generates the __init__ and run methods of
    class processor from a programmer-supplied state machine.
    '''
    def __init__(self, scheduler, logger, factory, contextLength,           \
            seed=None):
        '''
        Initialize variables from the state machine, and the contextCount,
        contextsFree, and fastio[] _IOunit_ fields, after calling the
        _Processor_ constructor.
        Parameter contextLength gives the number of contextCount & contextsFree
        (hardware thread) slots.
        See _Processor_'s constructor for the other parameters.
        Field fastiounits is the actual array of iounit objects
        for use in the processor's fastio[] vector. See setIOunits().
        '''
        _Processor_.__init__(self, scheduler, logger, factory,               \
            seed=seed)
        self.contextCount = contextLength
        self.contextsFree = contextLength
        self.__generator__ = self.run()     # Added August 2015
        if type(self.__generator__) != types.GeneratorType:
            raise AttributeError("ERROR, generated processor performs "
                + "no blocking operations, DEBUG info: "
                + str(type(self.__generator__)))
    def setIOunits(self, fastiounits):
        '''
        Set the fastio [] vector for this processor to fastiounits [].
        The constructor cannot do this because the iounit() constructor
        requires a reference to the processor; there is a circular
        dependency.
        '''
        self.fastio = fastiounits
    def run(self):
        '''
        This run() method runs the thread of the active processor object.
        CSC343Compile.py generates this method from a custom state machine.
        '''
        globals = {
            'math'      :   math,                   # module
            'functools' :   functools,              # module
            'operator'  :   operator,               # module
            'fork'      :   self.fork,              # method
            'idle'      :   self.idle,              # method
            'trigger'   :   self.trigger,           # method
            'time'      :   self.time,              # method
            'sample'    :   self.sample,            # method
            'msg'       :   self.msg,               # method
            'waitForEvent' : self.waitForEvent,     # method
            'signalEvent' : __scheduledObject__.signalEvent,       # method
            'assign'    :   self.assign,            # method
            'noop'      : __scheduledObject__.noop,       # method
            "pcb"       :   self.pcb,               # field
            "child"     :   self.child,             # field
            'fastio'    :   self.fastio,            # field
            'contextCount' : self.contextCount,     # field
            'contextsFree' : self.contextsFree,       # field
            'Queue'     :   Queue,                  # class
            'ModelState':   ModelState,             # class
            'processor' :   self,                   # this object
            'self'      :   self                    # this object
        }
        self.globals = globals
        locals = {
            'processesToGo' : 10,
            'pid' : -1,
            'tid' : -1,
        }
        self.__eventSet__ = {'init', 'fork'}
        self.locals = locals
        self.__localnames__ = locals.keys()
        self.__localcount__ = len(self.__localnames__)
        self.__objnames__ = None        # Need these 2 in the __dict__.
        self.__objcount__ = -1
        self.__objnames__ = self.__dict__.keys()
        self.__objcount__ = len(self.__objnames__)
        __lastMissedEvent__ = None
        try:
            try:
                self.state = 'init'
                self.waitingon = 'init'
                self.logger.log(self, tag="APPROACH")
                self.logger.log(self, tag="ARRIVE")
                stime = None        # simulation time
                event = None        # event is the event that got us here
                args = None         # args are the args passed from event
                __laststate__ = 'init'
                while True:         # processor runs until sys.exit.
                    if __laststate__ == 'init':
                        self.__localnames__ = list(locals.keys())
                        self.__localcount__ = len(self.__localnames__)
                        self.__objnames__ = list(self.__dict__.keys())
                        self.__objcount__ = len(self.__objnames__)
                    elif len(locals.keys()) != self.__localcount__:
                        errthing = "Assignment to undeclared variable(s):"
                        for k in locals.keys():
                            if not k in self.__localnames__:
                                errthing = errthing + " " + k
                        errthing = errthing + " in processor STM."
                        errthing = errthing + "\nInitialization must occur in "\
                            + "a variable declaration or init -> transition."
                        raise AttributeError(errthing)
                    elif len(self.__dict__.keys()) != self.__objcount__:
                      errthing = "Assignment to undeclared processor field(s):"
                      for k in self.__dict__.keys():
                        if not k in self.__objnames__:
                            errthing = errthing + " " + k
                      errthing = errthing + " in processor STM."
                      errthing = errthing + "\nInitialization must occur in " \
                            + "an init -> transition."
                      raise AttributeError(errthing)
                    __laststate__ = self.state
                    if self.__sleepResult__:
                        stime, event, args = self.__sleepResult__
                        # DEPRECATED self.logger.log(self)
                    else:
                        stime = self.scheduler.time
                        event = None
                        args = None
                    # CSC343Compile.py generates custom run() code here.
                    if self.state == 'init':
                        if event == 'init':
                            self.logger.log(self, tag="DEPART")
                            self.state = 'makingThreads'
                            self.logger.log(self, tag="APPROACH")
                            exec(__codeTable__[0],globals,locals)
                            exec(__codeTable__[1],globals,locals)
                            exec(__codeTable__[2],globals,locals)
                            self.logger.log(self, tag="ARRIVE")
                            yield None
                            __lastMissedEvent__ = None
                            continue
                        if event != __lastMissedEvent__ and self.logger.getLevel() >= (__DEBUGLEVEL__-1):
                            self.msg("INFO: Missed event: " + event + " From state: " + self.state)
                            __lastMissedEvent__ = event
                    elif self.state == 'makingThreads':
                        if event == 'fork':
                            locals["pid"] = args[0]
                            locals["tid"] = args[1]
                            if eval(__codeTable__[3],globals,locals):
                                self.logger.log(self, tag="REPEAT")
                                exec(__codeTable__[4],globals,locals)
                                exec(__codeTable__[5],globals,locals)
                                yield None
                                __lastMissedEvent__ = None
                                continue
                        if event == 'fork':
                            locals["pid"] = args[0]
                            locals["tid"] = args[1]
                            if eval(__codeTable__[6],globals,locals):
                                self.logger.log(self, tag="DEPART")
                                self.state = 'doneStartingThreads'
                                self.logger.log(self, tag="APPROACH")
                                self.logger.log(self, tag="ARRIVE")
                                __lastMissedEvent__ = None
                                continue
                        if event != __lastMissedEvent__ and self.logger.getLevel() >= (__DEBUGLEVEL__-1):
                            self.msg("INFO: Missed event: " + event + " From state: " + self.state)
                            __lastMissedEvent__ = event
                    elif self.state == 'doneStartingThreads':
                        self.logger.log(self, tag="DEPART")
                        return
            except Exception as xxx:
                if self.logger.isOpen():
                    self.logger.log(self)
                    self.state = '<defunct on Exception ' + str(xxx) + '>'
                    self.logger.log(self)
                    traceback.print_exc(file=self.logger.getFile())
                    self.logger.flush()
                    raise
        finally:
            if self.logger.isOpen() and not (self.state.startswith('<defunct')
                    or __MAIN_THREAD_EXITED__):
                # DEPRECATED self.logger.log(self)
                try:
                    self.state = '<defunct>'
                    self.waitingon = None
                    self.logger.log(self)
                    self.logger.flush()
                except ValueError as LogFileClosedByMainThread:
                    pass
            # DEPRECATED self.scheduler.notifyOfTerminatingSimThread()
            # Unblock sched for another Python Thread.

class thread(_Thread_):
    '''
    CSC343Compile.py generates the __init__ and run methods of
    class thread from a programmer-supllied state machine.
    '''
    def __init__(self, scheduler, logger, factory, processor, pcb,          \
            processNumber, threadNumber, terminal, seed=None):
        '''
        See _Thread_.__init__ documentation for parameters.
        '''
        _Thread_.__init__(self, scheduler, logger, factory, processor,      \
            pcb, processNumber, threadNumber, terminal, seed=seed)
        self.__generator__ = self.run()     # Added August 2015
        if type(self.__generator__) != types.GeneratorType:
            raise AttributeError("ERROR, generated thread performs "
                + "no blocking operations, DEBUG info: "
                + str(type(self.__generator__)))
    def run(self):
        '''
        This run() method runs the thread of the active thread object.
        CSC343Compile.py generates this method from a custom state machine.
        '''
        __lastMissedEvent__ = None
        globals = {
            'math'      :   math,                   # module
            'functools' :   functools,              # module
            'operator'  :   operator,               # module
            'fork'      :   self.fork,              # method
            'spawn'     :   self.spawn,             # method
            'retire'    :   self.retire,            # method
            'cpu'       :   self.cpu,               # method
            'io'        :   self.io,                # method
            'sleep'     :   self.sleep,             # method
            'yieldcpu'  :   self.yieldcpu,          # method
            'trigger'   :   self.trigger,           # method
            'sample'    :   self.sample,            # method
            'time'      :   self.time,              # method
            'getid'     :   self.getid,             # method
            'waitForEvent' : self.waitForEvent,     # method
            'wait'      :   self.wait,              # method
            'exit'      :   self.exit,              # method
            'kill'      :   self.kill,              # method
            'join'      :   self.join,              # method
            'signalEvent' : __scheduledObject__.signalEvent,       # method
            'assign'    :   self.assign,            # method
            'noop'      : __scheduledObject__.noop,       # method
            'msg'       :   self.msg,               # method
            "pcb"       :   self.pcb,               # field
            'processor' :   self.processor,         # field
            'thread'    :   self,                   # this object
            'Queue'     :   Queue,                  # class
            'ModelState':   ModelState,             # class
            'self'      :   self                    # this object
        }
        self.globals = globals
        locals = {
            'quantum' : 125,
            'machineid' : -1,
            'pid' : -1,
            'tid' : -1,
            'iobound' : eval('False',globals,{}),
            'endtime' : 100000,
            'iodevice' : 0,
            'alpha' : 0.5,
        }
        self.__eventSet__ = {'cpu', 'io', 'init', 'contextAvailable', 'yieldcpu'}
        self.locals = locals
        self.__localnames__ = locals.keys()
        self.__localcount__ = len(self.__localnames__)
        self.__pcbnames__ = self.pcb.__dict__.keys()
        self.__pcbcount__ = len(self.__pcbnames__)
        self.__processornames__ = self.processor.__dict__.keys()
        self.__processorcount__ = len(self.__processornames__)
        self.__objnames__ = None        # Need these 2 in the __dict__.
        self.__objcount__ = -1
        self.__objnames__ = self.__dict__.keys()
        self.__objcount__ = len(self.__objnames__)
        try:
            try:
                self.state = 'init'
                self.waitingon = 'init'
                self.logger.log(self, tag="APPROACH")
                self.logger.log(self, tag="ARRIVE")
                stime = None        # simulation time
                event = None        # event is the event that got us here
                args = None         # args are the args passed from event
                __laststate__ = 'init'
                while not self.__isdead__:
                    if __laststate__ == 'init':
                        self.__localnames__ = list(locals.keys())
                        self.__localcount__ = len(self.__localnames__)
                        self.__objnames__ = list(self.__dict__.keys())
                        self.__objcount__ = len(self.__objnames__)
                    elif len(locals.keys()) != self.__localcount__:
                        errthing = "Assignment to undeclared variable(s):"
                        for k in locals.keys():
                            if not k in self.__localnames__:
                                errthing = errthing + " " + k
                        errthing = errthing + " in thread STM."
                        errthing = errthing + "\nInitialization must occur in "\
                            + "a variable declaration or init -> transition."
                        raise AttributeError(errthing)
                    elif len(self.__dict__.keys()) != self.__objcount__:
                      errthing = "Assignment to undeclared thread field(s):"
                      for k in self.__dict__.keys():
                        if not k in self.__objnames__:
                            errthing = errthing + " " + k
                      errthing = errthing + " in thread STM."
                      errthing = errthing + "\nInitialization must occur in " \
                            + "an init -> transition."
                      raise AttributeError(errthing)
                    if self.threadNumber == 0:
                        # Only thread 0 can initialize the PCB.
                        self.__pcbnames__ = list(self.pcb.__dict__.keys())
                        self.__pcbcount__ = len(self.__pcbnames__)
                    elif len(self.pcb.__dict__.keys()) != self.__pcbcount__:
                      errthing = "Assignment to undeclared pcb field(s):"
                      for k in self.pcb.__dict__.keys():
                            if not k in self.__pcbnames__:
                                errthing = errthing + " " + k
                      errthing = errthing + " in thread "       \
                        + str(self.threadNumber) + "'s STM."
                      errthing = errthing + "\nInitialization must occur in " \
                            + "thread 0 before spawning other threads."
                      raise AttributeError(errthing)
                    if len(self.processor.__dict__.keys())              \
                            != self.__processorcount__:
                      errthing = "Assignment to undeclared processor field(s):"
                      errthing = errthing + "\nInitialization must occur in " \
                            + "the processor object's init -> transition."
                      for k in self.processor.__dict__.keys():
                            if not k in self.__processornames__:
                                errthing = errthing + " " + k
                      errthing = errthing + " disallowed in thread STM."
                      raise AttributeError(errthing)
                    __laststate__ = self.state
                    # Run until state machine sets __isdead__ or return.
                    self.exclusiveWait = False
                    if self.__sleepResult__:
                        stime, event, args = self.__sleepResult__
                        # DEPRECATED self.logger.log(self)
                    else:
                        stime = self.scheduler.time
                        event = None
                        args = None
                    # CSC343Compile.py generates custom run() code here.
                    if self.state == 'init':
                        if event == 'init':
                            self.logger.log(self, tag="DEPART")
                            self.state = 'scheduling'
                            self.logger.log(self, tag="APPROACH")
                            exec(__codeTable__[7],globals,locals)
                            exec(__codeTable__[8],globals,locals)
                            exec(__codeTable__[9],globals,locals)
                            exec(__codeTable__[10],globals,locals)
                            exec(__codeTable__[11],globals,locals)
                            exec(__codeTable__[12],globals,locals)
                            self.logger.log(self, tag="ARRIVE")
                            yield None
                            __lastMissedEvent__ = None
                            continue
                        if event != __lastMissedEvent__ and self.logger.getLevel() >= (__DEBUGLEVEL__-1):
                            self.msg("INFO: Missed event: " + event + " From state: " + self.state)
                            __lastMissedEvent__ = event
                    elif self.state == 'scheduling':
                        if event == 'yieldcpu':
                            if eval(__codeTable__[13],globals,locals):
                                self.logger.log(self, tag="DEPART")
                                self.state = 'running'
                                self.logger.log(self, tag="APPROACH")
                                exec(__codeTable__[14],globals,locals)
                                exec(__codeTable__[15],globals,locals)
                                self.logger.log(self, tag="ARRIVE")
                                yield None
                                __lastMissedEvent__ = None
                                continue
                        if event == 'yieldcpu':
                            if eval(__codeTable__[16],globals,locals):
                                self.logger.log(self, tag="DEPART")
                                self.state = 'ready'
                                self.logger.log(self, tag="APPROACH")
                                exec(__codeTable__[17],globals,locals)
                                exec(__codeTable__[18],globals,locals)
                                self.logger.log(self, tag="ARRIVE")
                                yield None
                                __lastMissedEvent__ = None
                                continue
                        if event != __lastMissedEvent__ and self.logger.getLevel() >= (__DEBUGLEVEL__-1):
                            self.msg("INFO: Missed event: " + event + " From state: " + self.state)
                            __lastMissedEvent__ = event
                    elif self.state == 'ready':
                        if event == 'contextAvailable':
                            self.logger.log(self, tag="DEPART")
                            self.state = 'scheduling'
                            self.logger.log(self, tag="APPROACH")
                            exec(__codeTable__[19],globals,locals)
                            self.logger.log(self, tag="ARRIVE")
                            yield None
                            __lastMissedEvent__ = None
                            continue
                        if event != __lastMissedEvent__ and self.logger.getLevel() >= (__DEBUGLEVEL__-1):
                            self.msg("INFO: Missed event: " + event + " From state: " + self.state)
                            __lastMissedEvent__ = event
                    elif self.state == 'running':
                        if event == 'cpu':
                            self.logger.log(self, tag="DEPART")
                            self.state = 'rescheduling'
                            self.logger.log(self, tag="APPROACH")
                            exec(__codeTable__[20],globals,locals)
                            exec(__codeTable__[21],globals,locals)
                            exec(__codeTable__[22],globals,locals)
                            self.logger.log(self, tag="ARRIVE")
                            yield None
                            __lastMissedEvent__ = None
                            continue
                        if event != __lastMissedEvent__ and self.logger.getLevel() >= (__DEBUGLEVEL__-1):
                            self.msg("INFO: Missed event: " + event + " From state: " + self.state)
                            __lastMissedEvent__ = event
                    elif self.state == 'waiting':
                        if event == 'io':
                            self.logger.log(self, tag="DEPART")
                            self.state = 'scheduling'
                            self.logger.log(self, tag="APPROACH")
                            exec(__codeTable__[23],globals,locals)
                            exec(__codeTable__[24],globals,locals)
                            exec(__codeTable__[25],globals,locals)
                            exec(__codeTable__[26],globals,locals)
                            exec(__codeTable__[27],globals,locals)
                            self.logger.log(self, tag="ARRIVE")
                            yield None
                            __lastMissedEvent__ = None
                            continue
                        if event != __lastMissedEvent__ and self.logger.getLevel() >= (__DEBUGLEVEL__-1):
                            self.msg("INFO: Missed event: " + event + " From state: " + self.state)
                            __lastMissedEvent__ = event
                    elif self.state == 'rescheduling':
                        if event == 'yieldcpu':
                            if eval(__codeTable__[28],globals,locals):
                                self.logger.log(self, tag="DEPART")
                                self.state = 'terminated'
                                self.logger.log(self, tag="APPROACH")
                                self.logger.log(self, tag="ARRIVE")
                                __lastMissedEvent__ = None
                                continue
                        if event == 'yieldcpu':
                            if eval(__codeTable__[29],globals,locals):
                                self.logger.log(self, tag="DEPART")
                                self.state = 'waiting'
                                self.logger.log(self, tag="APPROACH")
                                exec(__codeTable__[30],globals,locals)
                                exec(__codeTable__[31],globals,locals)
                                self.logger.log(self, tag="ARRIVE")
                                yield None
                                __lastMissedEvent__ = None
                                continue
                        if event == 'yieldcpu':
                            if eval(__codeTable__[32],globals,locals):
                                self.logger.log(self, tag="DEPART")
                                self.state = 'scheduling'
                                self.logger.log(self, tag="APPROACH")
                                exec(__codeTable__[33],globals,locals)
                                exec(__codeTable__[34],globals,locals)
                                exec(__codeTable__[35],globals,locals)
                                self.logger.log(self, tag="ARRIVE")
                                yield None
                                __lastMissedEvent__ = None
                                continue
                        if event != __lastMissedEvent__ and self.logger.getLevel() >= (__DEBUGLEVEL__-1):
                            self.msg("INFO: Missed event: " + event + " From state: " + self.state)
                            __lastMissedEvent__ = event
                    elif self.state == 'terminated':
                        self.logger.log(self, tag="DEPART")
                        return
            except __ThreadRetireException__ as ignoreme:
                pass
            except Exception as xxx:
                if self.logger.isOpen():
                    self.logger.log(self)
                    self.state = '<defunct on Exception ' + str(xxx) + '>'
                    self.logger.log(self)
                    traceback.print_exc(file=self.logger.getFile())
                    self.logger.flush()
                    raise
        finally:
            if self.logger.isOpen() and not (self.state.startswith('<defunct')
                    or __MAIN_THREAD_EXITED__):
                # DEPRECATED self.logger.log(self)
                try:
                    self.state = '<defunct>'
                    self.waitingon = None
                    self.logger.log(self)
                    self.logger.flush()
                except ValueError as LogFileClosedByMainThread:
                    pass
            try:
                self.retire()       # make sure any join()ers are released.
            except __ThreadRetireException__ as IdontCare:
                pass
            # DEPRECATED self.scheduler.notifyOfTerminatingSimThread()
            # Unblock sched for another Python Thread.

class iounit(_IOunit_):
    '''
    Class iounit simply uses base class _IOunit_ as is to provide
    iounit behavior. Later versions of this class will extend iounit
    to run according to custom state machine specifications.
    '''
    def __init__(self, scheduler, logger, factory, processor, isfast,       \
            seed=None):
        '''
        Invoke the base class _IOunit_ constructor without extension.
        See constructor _IOunit_.__init__ for parameter documentation.
        '''
        _IOunit_.__init__(self, scheduler, logger, factory, processor,      \
            isfast, seed=seed)
        self.__generator__ = self.run()     # Added August 2015
        if type(self.__generator__) != types.GeneratorType:
            raise AttributeError("ERROR, generated iounit performs "
                + "no blocking operations, DEBUG info: "
                + str(type(self.__generator__)))

def __processorFactory__(scheduler, logger, factory, contextLength,         \
        seed=None):
    ''' See processor and _Processor_. '''
    return processor(scheduler, logger, factory, contextLength,             \
        seed=seed)

def __threadFactory__(scheduler, logger, factory, processor, pcb,           \
        processNumber, threadNumber, terminal, seed=None):
    ''' See thread and _Thread_. '''
    return thread(scheduler, logger, factory, processor,                    \
        pcb, processNumber, threadNumber, terminal,                         \
            seed=(seed if seed is None else (seed ^ processNumber ^ (threadNumber < 1) ^ 1)))

def __iounitFactory__(scheduler, logger, factory, processor, isfast,        \
        seed=None):
    ''' See iounit and _IOunit_. '''
    return iounit(scheduler, logger, factory, processor, isfast, seed=seed)

usage = 'USAGE: python THISFILE.py NUMCONTEXTS NUMFASTIO SIMTIME SEED|None LOGLEVEL'
#<<<<<USAGE>>>>>

def main():
    if len(sys.argv) != 6 or len(sys.argv[0]) < 4                           \
            or not sys.argv[0].endswith('.py'):
        sys.stderr.write(usage + '\n')
        sys.exit(1)
    else:
        sys.stderr.write('MSG cmd line: ' + str(sys.argv) + ", usage " + usage + '\n')
    numcontexts = None
    try:
        numcontexts = int(sys.argv[1])
        if numcontexts < 1:
            raise ValueError("ERROR, invalid number of contexts: "        \
                + str(numcontexts))
    except Exception as xxx:
        sys.stderr.write('ERROR: ' + str(xxx) + '\n')
        sys.stderr.write(usage + '\n')
        sys.exit(2)
    numfastio = None
    try:
        numfastio = int(sys.argv[2])
        if numfastio < 1:
            raise ValueError("ERROR, invalid number of fast IO units: "   \
                + str(numfastio))
    except Exception as xxx:
        sys.stderr.write('ERROR: ' + str(xxx) + '\n')
        sys.stderr.write(usage + '\n')
        sys.exit(3)
    simtime = None
    try:
        simtime = int(sys.argv[3])
        if simtime < 1:
            raise ValueError("ERROR, invalid simulation time limit: "     \
                + str(simtime))
    except Exception as xxx:
        sys.stderr.write('ERROR: ' + str(xxx) + '\n')
        sys.stderr.write(usage + '\n')
        sys.exit(4)
    loglevel = None
    try:
        loglevel = int(sys.argv[5])
        if loglevel < 0:    # Currently everything > 3 treated as 3
            raise ValueError("ERROR, invalid simulation logging level: "  \
                + str(loglevel))
    except Exception as xxx:
        sys.stderr.write('ERROR: ' + str(xxx) + '\n')
        sys.stderr.write(usage + '\n')
        sys.exit(6)
    seed = None
    if sys.argv[4] != 'None':
        try:
            seed = int(sys.argv[4])
        except Exception as xxx:
            sys.stderr.write('ERROR: ' + str(xxx) + '\n')
            sys.stderr.write(usage + '\n')
            sys.exit(5)
    basename = sys.argv[0][:-2]
    logfilename = basename + 'log'
    if 'STMLOGDIR' in os.environ:
        logdir = os.environ['STMLOGDIR'] + '/'
    else:
        logdir = './'
    logfiletmp = logdir + os.environ['USER'] + '_STM_' + logfilename
    try:
        os.system('rm -f ' + logfilename + ' ; ln -s ' + logfiletmp
            + ' ' + logfilename)
    except Exception as estr:
        sys.stderr.write('WARNING(ignored) on ln -s ' + logfiletmp
            + ' ' + logfilename + '\n')
    # logger = __simulationLogger__(logfilename, loglevel)
    logger = __simulationLogger__(logfiletmp, loglevel)
    scheduler = __simulationScheduler__(logger, simtime)
    logger.setScheduler(scheduler)
    factory = {"processor" : __processorFactory__,
        "thread" : __threadFactory__, "io" : __iounitFactory__}
    p = __processorFactory__(scheduler, logger, factory, numcontexts,
        seed=None if seed is None else seed-1)
    # Do not use identical seed. That makes all IOunits have the same numbers!
    io = [__iounitFactory__(scheduler, logger, factory, p, True, seed=None if seed is None else seed+i)
        for i in range (0, numfastio)]
    p.setIOunits(io)
    # DEPRECATED for eieio in io:
        # DEPRECATED eieio.start()
    # DEPRECATED p.start()
    scheduler.sleep(0, p, 'init', None)
    scheduler.__run__()
    sys.exit(0)
__codeTable__ = [
    compile('processesToGo -= 1','nofile','exec'),
    compile('processor.readyQ = Queue(True)','nofile','exec'),
    compile('fork()','nofile','exec'),
    compile('processesToGo > 0','nofile','eval'),
    compile('processesToGo -= 1','nofile','exec'),
    compile('fork()','nofile','exec'),
    compile('processesToGo == 0','nofile','eval'),
    compile('machineid, pid, tid = getid()','nofile','exec'),
    compile('iobound = True if ((pid % 2) == 1) else False','nofile','exec'),
    compile("cpuTicksB4IO = sample(1, 250, 'exponential', 25) if iobound             else sample(100, 1100, 'revexponential', 1000)",'nofile','exec'),
    compile('tickstorun = min(cpuTicksB4IO, quantum)','nofile','exec'),
    compile('tickstodefer = cpuTicksB4IO - tickstorun','nofile','exec'),
    compile('yieldcpu()','nofile','exec'),
    compile('processor.contextsFree > 0','nofile','eval'),
    compile('processor.contextsFree -= 1','nofile','exec'),
    compile('cpu(tickstorun)','nofile','exec'),
    compile('processor.contextsFree == 0','nofile','eval'),
    compile('processor.readyQ.enq(thread, quantum)','nofile','exec'),
    compile("waitForEvent('contextAvailable', False)",'nofile','exec'),
    compile('yieldcpu()','nofile','exec'),
    compile('processor.contextsFree += 1','nofile','exec'),
    compile("signalEvent(processor.readyQ.deq(), 'contextAvailable', 0)             if len(processor.readyQ) > 0 else 0",'nofile','exec'),
    compile('yieldcpu()','nofile','exec'),
    compile('quantum = round((alpha * cpuTicksB4IO) + ((1.0 - alpha) * quantum))','nofile','exec'),
    compile("cpuTicksB4IO = sample(1, 250, 'exponential', 25) if iobound             else sample(100, 1100, 'revexponential', 1000)",'nofile','exec'),
    compile('tickstorun = min(cpuTicksB4IO, quantum)','nofile','exec'),
    compile('tickstodefer = cpuTicksB4IO - tickstorun','nofile','exec'),
    compile('yieldcpu()','nofile','exec'),
    compile('time() >= endtime','nofile','eval'),
    compile('time() < endtime             and tickstodefer < 1','nofile','eval'),
    compile("iodevice = sample(-1, len(processor.fastio)-1, 'uniform')",'nofile','exec'),
    compile('io(iodevice)','nofile','exec'),
    compile('time() < endtime             and tickstodefer > 0','nofile','eval'),
    compile('tickstorun = min(tickstodefer, quantum)','nofile','exec'),
    compile('tickstodefer = tickstodefer - tickstorun','nofile','exec'),
    compile('yieldcpu()','nofile','exec'),
    None
]
if __name__ == "__main__":
    main()
