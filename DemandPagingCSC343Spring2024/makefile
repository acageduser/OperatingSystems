#       makefile for DemandPagingCSC343Spring2024, project 4
#       CSC 343 Operating Systems
#       Dr. Dale Parson. Spring 2024

all:		test

TARGET = DemandPagingCSC343Spring2024
SIMLOGLEVEL = 3
include ./makelib
PARSONHOME := $(DPARSON)
DPOS := $(DPARSON)/OpSys
DPPY := $(DPOS)/state2codeV17

clean:		subclean
		/bin/rm -f *.out *.dif *.pyc junk parsetab.py *.vmlf
		/bin/rm -f *.dot *.gif *.jpg testmachine.ck junk.* *.tmp *.log
		/bin/rm -f PageReplaceOptimal.py PageReplaceLRU.py *.crunch *_crunch.py
		/bin/rm -f PageReplaceFIFO.py PageReplaceLRUDirty.py
		/bin/rm -f $(PARSONHOME)/tmp/$(STUDENT)_STM_*.log $(STUDENT)_STM_*.log

build:	buildOptimal buildFIFO buildLRU buildLRUDirty

test:	testOptimal testFIFO testLRU testLRUDirty

buildOptimal:
		@echo 'COMPILING PageReplaceOptimal'
		/bin/bash -c "PYTHONPATH=$(DPOS):.:.. $(PYTHON) $(DPPY)/State2CodeParser.py PageReplaceOptimal.stm PageReplaceOptimal.dot PageReplaceOptimal.py CSC343Compile CSC343Compile"
		@echo "COMPILING COMPLETED"

testOptimal:	buildOptimal
		@echo "SIMULATING (TESTING) PageReplaceOptimal"
		/bin/bash -c "PYTHONPATH=$(DPOS):.:.. STMLOGDIR=$(PARSONHOME)/tmp time $(PYTHON) PageReplaceOptimal.py 1 2 900000 12345 2"
		/bin/bash -c "PYTHONPATH=$(DPOS):.:.. $(PYTHON) crunchlog.py PageReplaceOptimal.log"
		@echo "TESTING COMPLETED"

buildFIFO:
		@echo 'COMPILING PageReplaceFIFO'
		/bin/bash -c "PYTHONPATH=$(DPOS):.:.. $(PYTHON) $(DPPY)/State2CodeParser.py PageReplaceFIFO.stm PageReplaceFIFO.dot PageReplaceFIFO.py CSC343Compile CSC343Compile"
		@echo "COMPILING COMPLETED"

testFIFO:	buildFIFO
		@echo "SIMULATING (TESTING) PageReplaceFIFO"
		/bin/bash -c "PYTHONPATH=$(DPOS):.:.. STMLOGDIR=$(PARSONHOME)/tmp time $(PYTHON) PageReplaceFIFO.py 1 2 900000 12345 2"
		/bin/bash -c "PYTHONPATH=$(DPOS):.:.. $(PYTHON) crunchlog.py PageReplaceFIFO.log"
		@echo "TESTING COMPLETED"

buildLRU:
		@echo 'COMPILING PageReplaceLRU'
		/bin/bash -c "PYTHONPATH=$(DPOS):.:.. $(PYTHON) $(DPPY)/State2CodeParser.py PageReplaceLRU.stm PageReplaceLRU.dot PageReplaceLRU.py CSC343Compile CSC343Compile"
		@echo "COMPILING COMPLETED"

testLRU:	buildLRU
		@echo "SIMULATING (TESTING) PageReplaceLRU"
		/bin/bash -c "PYTHONPATH=$(DPOS):.:.. STMLOGDIR=$(PARSONHOME)/tmp time $(PYTHON) PageReplaceLRU.py 1 2 900000 12345 2"
		/bin/bash -c "PYTHONPATH=$(DPOS):.:.. $(PYTHON) crunchlog.py PageReplaceLRU.log"
		@echo "TESTING COMPLETED"

buildLRUDirty:
		@echo 'COMPILING PageReplaceLRUDirty'
		/bin/bash -c "PYTHONPATH=$(DPOS):.:.. $(PYTHON) $(DPPY)/State2CodeParser.py PageReplaceLRUDirty.stm PageReplaceLRUDirty.dot PageReplaceLRUDirty.py CSC343Compile CSC343Compile"
		@echo "COMPILING COMPLETED"

testLRUDirty:	buildLRUDirty
		@echo "SIMULATING (TESTING) PageReplaceLRUDirty"
		/bin/bash -c "PYTHONPATH=$(DPOS):.:.. STMLOGDIR=$(PARSONHOME)/tmp time $(PYTHON) PageReplaceLRUDirty.py 1 2 900000 12345 2"
		/bin/bash -c "PYTHONPATH=$(DPOS):.:.. $(PYTHON) crunchlog.py PageReplaceLRUDirty.log"
		@echo "TESTING COMPLETED"

buildLRUDEBUG:
		@echo 'COMPILING PageReplaceLRUDEBUG'
		/bin/bash -c "PYTHONPATH=$(DPOS):.:.. $(PYTHON) $(DPPY)/State2CodeParser.py PageReplaceLRUDEBUG.stm PageReplaceLRUDEBUG.dot PageReplaceLRUDEBUG.py CSC343Compile CSC343Compile"
		@echo "COMPILING COMPLETED"

testLRUDEBUG:	buildLRUDEBUG
		@echo "SIMULATING (TESTING) PageReplaceLRUDEBUG"
		/bin/bash -c "PYTHONPATH=$(DPOS):.:.. STMLOGDIR=$(PARSONHOME)/tmp time $(PYTHON) PageReplaceLRUDEBUG.py 1 2 900000 12345 2"
		/bin/bash -c "PYTHONPATH=$(DPOS):.:.. $(PYTHON) crunchlog.py PageReplaceLRUDEBUG.log"
		@echo "TESTING COMPLETED"

buildLRUDirtyDEBUG:
		@echo 'COMPILING PageReplaceLRUDirtyDEBUG'
		/bin/bash -c "PYTHONPATH=$(DPOS):.:.. $(PYTHON) $(DPPY)/State2CodeParser.py PageReplaceLRUDirtyDEBUG.stm PageReplaceLRUDirtyDEBUG.dot PageReplaceLRUDirtyDEBUG.py CSC343Compile CSC343Compile"
		@echo "COMPILING COMPLETED"

testLRUDirtyDEBUG:	buildLRUDirtyDEBUG
		@echo "SIMULATING (TESTING) PageReplaceLRUDirtyDEBUG"
		/bin/bash -c "PYTHONPATH=$(DPOS):.:.. STMLOGDIR=$(PARSONHOME)/tmp time $(PYTHON) PageReplaceLRUDirtyDEBUG.py 1 2 900000 12345 2"
		/bin/bash -c "PYTHONPATH=$(DPOS):.:.. $(PYTHON) crunchlog.py PageReplaceLRUDirtyDEBUG.log"
		@echo "TESTING COMPLETED"

graphs:		$(JPEGFILES)
		-mkdir $(ACCTWWW)
		cp -p $(JPEGFILES) $(ACCTWWW)
		-chmod -R o+r+X $(ACCTWWW)
		@echo "You can browse JPEGS in http://acad.kutztown.edu/~$(STUDENT)"
