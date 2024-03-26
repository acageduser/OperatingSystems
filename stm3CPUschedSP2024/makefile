#       makefile for stm3sched, project 3 for CSC 343 Operating Systems
#       Dr. Dale Parson. Spring 2024

all:		build

TARGET = stm3CPUschedSP2024
DEBUG = 1
DPOS := /home/kutztown.edu/parson/OpSys
DPPY := $(DPOS)/state2codeV17
PARSONHOME := /home/kutztown.edu/parson

include ./makelib

clean:		subclean
		/bin/rm -f *.out *.dif *.pyc junk parsetab.py *.vmlf ./__pycache__/*
		/bin/rm -f *.dot *.gif *.jpg testmachine.ck junk.* *.tmp *.log
		/bin/rm -f fcfs.py sjf.py rr.py *.crunch fcfs_crunch.py sjf_crunch.py
		/bin/rm -f rr_crunch.py srtf.py srtf_crunch.py sjfEst.py
		/bin/rm -f sjfEst_crunch.py
		/bin/rm -f $(PARSONHOME)/tmp/$(STUDENT)_STM_*.log $(STUDENT)_STM_*.log
		/bin/rm -f plotcrunch.csv

build:	buildfcfs buildsjf buildsjfEst buildrr buildsrtf

buildfcfs:
		@echo 'COMPILING fcfs'
		/bin/bash -c "PYTHONPATH=$(DPOS):.:.. $(PYTHON) $(DPPY)/State2CodeParser.py fcfs.stm fcfs.dot fcfs.py CSC343Compile CSC343Compile"
		@echo "COMPILING COMPLETED"

test:		testfcfs testsjf testsjfEst testrr testsrtf

testfcfs:	buildfcfs
		@echo "SIMULATING (TESTING) fcfs"
		/bin/rm -f $(PARSONHOME)/tmp/$(STUDENT)_STM_*.log $(STUDENT)_STM_*.log Mutex.log
		/bin/bash -c "PYTHONPATH=$(DPOS):.:.. STMLOGDIR=$(PARSONHOME)/tmp time $(PYTHON) fcfs.py 2 4 110000 12345 2"
		/bin/bash -c "PYTHONPATH=$(DPOS):.:.. $(PYTHON) crunchlog.py fcfs.log"
		@echo "TESTING fcfs COMPLETED"

buildsjf:
		@echo 'COMPILING sjf'
		/bin/bash -c "PYTHONPATH=$(DPOS):.:.. $(PYTHON) $(DPPY)/State2CodeParser.py sjf.stm sjf.dot sjf.py CSC343Compile CSC343Compile"
		@echo "COMPILING COMPLETED"

testsjf:	buildsjf
		@echo "SIMULATING (TESTING) sjf"
		/bin/rm -f $(PARSONHOME)/tmp/$(STUDENT)_STM_*.log $(STUDENT)_STM_*.log Mutex.log
		/bin/bash -c "PYTHONPATH=$(DPOS):.:.. STMLOGDIR=$(PARSONHOME)/tmp time $(PYTHON) sjf.py 2 4 110000 12345 2"
		/bin/bash -c "PYTHONPATH=$(DPOS):.:.. $(PYTHON) crunchlog.py sjf.log"
		@echo "TESTING sjf COMPLETED"

buildsjfEst:
		@echo 'COMPILING sjfEst'
		/bin/bash -c "PYTHONPATH=$(DPOS):.:.. $(PYTHON) $(DPPY)/State2CodeParser.py sjfEst.stm sjfEst.dot sjfEst.py CSC343Compile CSC343Compile"
		@echo "COMPILING COMPLETED"

testsjfEst:	buildsjfEst
		@echo "SIMULATING (TESTING) sjfEst"
		/bin/rm -f $(PARSONHOME)/tmp/$(STUDENT)_STM_*.log $(STUDENT)_STM_*.log Mutex.log
		/bin/bash -c "PYTHONPATH=$(DPOS):.:.. STMLOGDIR=$(PARSONHOME)/tmp time $(PYTHON) sjfEst.py 2 4 110000 12345 2"
		/bin/bash -c "PYTHONPATH=$(DPOS):.:.. $(PYTHON) crunchlog.py sjfEst.log"
		@echo "TESTING sjfEst COMPLETED"

buildsrtf:
		@echo 'COMPILING srtf'
		/bin/bash -c "PYTHONPATH=$(DPOS):.:.. $(PYTHON) $(DPPY)/State2CodeParser.py srtf.stm srtf.dot srtf.py CSC343Compile CSC343Compile"
		@echo "COMPILING COMPLETED"

testsrtf:	buildsrtf
		@echo "SIMULATING (TESTING) srtf"
		/bin/rm -f $(PARSONHOME)/tmp/$(STUDENT)_STM_*.log $(STUDENT)_STM_*.log Mutex.log
		/bin/bash -c "PYTHONPATH=$(DPOS):.:.. STMLOGDIR=$(PARSONHOME)/tmp time $(PYTHON) srtf.py 2 4 110000 12345 2"
		/bin/bash -c "PYTHONPATH=$(DPOS):.:.. $(PYTHON) crunchlog.py srtf.log"
		@echo "TESTING srtf COMPLETED"


buildrr:
		@echo 'COMPILING rr'
		/bin/bash -c "PYTHONPATH=$(DPOS):.:.. $(PYTHON) $(DPPY)/State2CodeParser.py rr.stm rr.dot rr.py CSC343Compile CSC343Compile"
		@echo "COMPILING COMPLETED"

testrr:	buildrr
		@echo "SIMULATING (TESTING) rr"
		/bin/rm -f $(PARSONHOME)/tmp/$(STUDENT)_STM_*.log $(STUDENT)_STM_*.log Mutex.log
		/bin/bash -c "PYTHONPATH=$(DPOS):.:.. STMLOGDIR=$(PARSONHOME)/tmp time $(PYTHON) rr.py 2 4 110000 12345 2"
		/bin/bash -c "PYTHONPATH=$(DPOS):.:.. $(PYTHON) crunchlog.py rr.log"
		@echo "TESTING rr COMPLETED"

graphs:		$(JPEGFILES)
		-mkdir $(ACCTWWW)
		cp -p $(JPEGFILES) $(ACCTWWW)
		-chmod -R o+r+X $(ACCTWWW)
		@echo "You can browse JPEGS in https://acad.kutztown.edu/~$(STUDENT)"
