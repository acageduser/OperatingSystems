#       makefile for prisonerd2024, problem 1, CSC 343 Operating Systems
#       Dr. Dale Parson. Spring 2024. Updated for state2codeV17 January

all:		build

TARGET = prisonerd2024
DEBUG = 1
DPOS := /home/kutztown.edu/parson/OpSys
DPPY := $(DPOS)/state2codeV17

include ./makelib

clean:		subclean
		-/bin/bash -c 'chmod 666 ~parson/tmp/$(STUDENT)_STM*' ./__pycache__/*
		/bin/bash -c '/bin/rm -f *.out *.dif *.pyc junk parsetab.py *.vmlf prisonerd2024_crunch.png'
		/bin/bash -c '/bin/rm -f *.dot *.gif *.jpg testmachine.ck junk.* *.tmp *.log prisonerd2024.py'
		/bin/bash -c '/bin/rm -f *.crunch ~parson/tmp/$(STUDENT)_STM_*.log $(STUDENT)_STM_*.log Unsafe*.log'
		/bin/bash -c '/bin/rm -f rr*.py sjf*.py fcfs*.py plotcrunch.csv *.crunch *_crunch.py *.crunch *_crunch.csv'
		bash -c '/bin/rm -f ~parson/tmp/$(STUDENT)_STM_*.log $(STUDENT)_STM_*.log prisonerd2024*.log'

test:		test_prisonerd2024

csv:
		# /bin/bash -c "PYTHONPATH=$(DPOS):.:..:/usr/local/lib/python3.7 $(PYTHON) plotcrunch.py diffset prisonerd2024_crunch.py"

build:
		@echo 'COMPILING prisonerd2024'
		/bin/bash -c "PYTHONPATH=$(DPOS):.:..:/usr/local/lib/python3.7 $(PYTHON) $(DPPY)/State2CodeParser.py prisonerd2024.stm prisonerd2024.dot prisonerd2024.py CSC343Compile CSC343Compile"
		@echo "COMPILING COMPLETED"

test_prisonerd2024:	build
		@echo "SIMULATING (TESTING) prisonerd2024"
		/bin/rm -f ~parson/tmp/$(STUDENT)_STM_*.log $(STUDENT)_STM_*.log prisonerd2024.log
		/bin/bash -c "PYTHONPATH=$(DPOS):.:..:/usr/local/lib/python3.7 STMLOGDIR=~parson/tmp time $(PYTHON) prisonerd2024.py 2 4 500 12345 2"
		/bin/bash -c 'chmod 666 ~parson/tmp/$(STUDENT)_STM*'
		/bin/bash -c "PYTHONPATH=$(DPOS):.:..:/usr/local/lib/python3.7 $(PYTHON) crunchlog.py prisonerd2024.log"
		@echo "COMPLETED (OK) SIMULATING (TESTING) prisonerd2024"

graphs:		$(JPEGFILES)
		-/bin/bash -c "python graphcrunch.py f1 prisonerd2024_crunch SUM_timeInJail_thread_0_process_0 SUM_timeInJail_thread_1_process_0 SUM_timeInJail_thread_0_process_1 SUM_timeInJail_thread_1_process_1 SUM_timeInJail_thread_0_process_2 SUM_timeInJail_thread_1_process_2 SUM_timeInJail_thread_0_process_3 SUM_timeInJail_thread_1_process_3 SUM_timeInJail_thread_0_process_4 SUM_timeInJail_thread_1_process_4 SUM_timeInJail_thread_0_process_5 SUM_timeInJail_thread_1_process_5 SUM_timeInJail_thread_0_process_6 SUM_timeInJail_thread_1_process_6 SUM_timeInJail_thread_0_process_7 SUM_timeInJail_thread_1_process_7 SUM_timeInJail_thread_0_process_8 SUM_timeInJail_thread_1_process_8 SUM_timeInJail_thread_0_process_9 SUM_timeInJail_thread_1_process_9"
		-mkdir $(ACCTWWW)
		cp -p prisonerd2024.jpg $(ACCTWWW)
		-cp -p prisonerd2024_crunch.png $(ACCTWWW)
		-/bin/bash -c 'chmod -R o+r+X $(ACCTWWW)'
		@echo "You can browse JPEGS and PNGS in https://acad.kutztown.edu/~$(STUDENT)"
