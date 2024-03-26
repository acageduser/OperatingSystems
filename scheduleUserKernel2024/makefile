#       makefile for scheduleUserKernel2024, problem 2,
#       CSC 343 Operating Systems, Dr. Dale Parson. Spring 2024.

all:		test

TARGET = scheduleUserKernel2024
SIMLOGLEVEL = 3
DEBUG = 1
include ./makelib
DPOS := $(DPARSON)/OpSys
DPPY := $(DPOS)/state2codeV17

clean:		subclean
		-/bin/bash -c 'chmod 666 ~parson/tmp/$(STUDENT)_STM*'
		/bin/bash -c '/bin/rm -f *.out *.dif *.pyc junk parsetab.py *.vmlf'
		/bin/bash -c '/bin/rm -f *.dot *.png *.jpg testmachine.ck junk.* *.tmp *.log'
		/bin/bash -c '/bin/rm -f *.crunch ~parson/tmp/$(STUDENT)_STM_*.log $(STUDENT)_STM_*.log'
		/bin/bash -c '/bin/rm -f *.crunch *_crunch.py *.crunch *_crunch.csv ./__pycache__/*.pyc'
		/bin/bash -c '/bin/rm -f OneToOne.py OneToOne_crunch.png'
		/bin/bash -c '/bin/rm -f ManyToOne.py ManyToOne_crunch.png'
		/bin/bash -c '/bin/rm -f ManyToMany.py ManyToMany_crunch.png'

build:		build_OneToOne build_ManyToOne build_ManyToMany

test:		test_OneToOne test_ManyToOne test_ManyToMany

build_OneToOne:
		@echo 'COMPILING OneToOne'
		/bin/bash -c "PYTHONPATH=$(DPOS):.:.. $(PYTHON) $(DPPY)/State2CodeParser.py OneToOne.stm OneToOne.dot OneToOne.py CSC343Compile CSC343Compile"
		/bin/rm -f *.jpg *.png
		@echo "COMPILING COMPLETED"

test_OneToOne:	build_OneToOne
		@echo "SIMULATING (TESTING) OneToOne"
		/bin/rm -f ~parson/tmp/$(STUDENT)_STM_*.log $(STUDENT)_STM_*.log *.log
		/bin/bash -c "PYTHONPATH=$(DPOS):.:.. STMLOGDIR=~parson/tmp time $(PYTHON) OneToOne.py 2 4 100000 12345 $(SIMLOGLEVEL)"
		/bin/bash -c 'chmod 666 ~parson/tmp/$(STUDENT)_STM*'
		/bin/bash -c "PYTHONPATH=$(DPOS):.:.. $(PYTHON) crunchlog.py OneToOne.log"
		@echo "COMPLETED (OK) SIMULATING (TESTING) OneToOne"

build_ManyToOne:
		@echo 'COMPILING ManyToOne'
		/bin/bash -c "PYTHONPATH=$(DPOS):.:.. $(PYTHON) $(DPPY)/State2CodeParser.py ManyToOne.stm ManyToOne.dot ManyToOne.py CSC343Compile CSC343Compile"
		/bin/rm -f *.jpg *.png
		@echo "COMPILING COMPLETED"

test_ManyToOne:	build_ManyToOne
		@echo "SIMULATING (TESTING) ManyToOne"
		/bin/rm -f ~parson/tmp/$(STUDENT)_STM_*.log $(STUDENT)_STM_*.log *.log
		/bin/bash -c "PYTHONPATH=$(DPOS):.:.. STMLOGDIR=~parson/tmp time $(PYTHON) ManyToOne.py 2 4 100000 12345 $(SIMLOGLEVEL)"
		/bin/bash -c 'chmod 666 ~parson/tmp/$(STUDENT)_STM*'
		/bin/bash -c "PYTHONPATH=$(DPOS):.:.. $(PYTHON) crunchlog.py ManyToOne.log"
		@echo "COMPLETED (OK) SIMULATING (TESTING) ManyToOne"

build_ManyToMany:
		@echo 'COMPILING ManyToMany'
		/bin/bash -c "PYTHONPATH=$(DPOS):.:.. $(PYTHON) $(DPPY)/State2CodeParser.py ManyToMany.stm ManyToMany.dot ManyToMany.py CSC343Compile CSC343Compile"
		/bin/rm -f *.jpg *.png
		@echo "COMPILING COMPLETED"

test_ManyToMany:	build_ManyToMany
		@echo "SIMULATING (TESTING) ManyToMany"
		/bin/rm -f ~parson/tmp/$(STUDENT)_STM_*.log $(STUDENT)_STM_*.log *.log
		/bin/bash -c "PYTHONPATH=$(DPOS):.:.. STMLOGDIR=~parson/tmp time $(PYTHON) ManyToMany.py 2 4 100000 12345 $(SIMLOGLEVEL)"
		/bin/bash -c 'chmod 666 ~parson/tmp/$(STUDENT)_STM*'
		/bin/bash -c "PYTHONPATH=$(DPOS):.:.. $(PYTHON) crunchlog.py ManyToMany.log"
		@echo "COMPLETED (OK) SIMULATING (TESTING) ManyToMany"

graphs:		$(JPEGFILES)
		-mkdir $(ACCTWWW) 2>/dev/null
		ls *jpg
		cp -p *.jpg $(ACCTWWW)
		-/bin/bash -c 'chmod -R o+r+X $(ACCTWWW)' 2>/dev/null
		@echo "You can browse JPEGS in https://acad.kutztown.edu/~$(STUDENT)"
