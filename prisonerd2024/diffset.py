# swapping2016/diffset.py -- set of simulation properties to test after
# a simulation run. See crunchlog.py

# Map the property to be checked against its (TOLERANCE, RAWTOLERANCE),
# where TOLERANCE is a percatage as a fraction, and RAWTOLERANCE
# is the minimum difference between the simulation value and the
# reference value for the property required to trigger an error.
DIFFMAP = {
    'SUM_timeInJail_thread_0_process_0'	:	(.20, 10),
    'SUM_timeInJail_thread_1_process_0'	:	(.20, 10),
    'SUM_timeInJail_thread_0_process_1'	:	(.20, 10),
    'SUM_timeInJail_thread_1_process_1'	:	(.20, 10),
    'SUM_timeInJail_thread_0_process_2'	:	(.20, 10),
    'SUM_timeInJail_thread_1_process_2'	:	(.20, 10),
    'SUM_timeInJail_thread_0_process_3'	:	(.20, 10),
    'SUM_timeInJail_thread_1_process_3'	:	(.20, 10),
    'SUM_timeInJail_thread_0_process_4'	:	(.20, 10),
    'SUM_timeInJail_thread_1_process_4'	:	(.20, 10),
    'SUM_timeInJail_thread_0_process_5'	:	(.20, 10),
    'SUM_timeInJail_thread_1_process_5'	:	(.20, 10),
    'SUM_timeInJail_thread_0_process_6'	:	(.20, 10),
    'SUM_timeInJail_thread_1_process_6'	:	(.20, 10),
    'SUM_timeInJail_thread_0_process_7'	:	(.20, 10),
    'SUM_timeInJail_thread_1_process_7'	:	(.20, 10),
    'SUM_timeInJail_thread_0_process_8'	:	(.20, 10),
    'SUM_timeInJail_thread_1_process_8'	:	(.20, 10),
    'SUM_timeInJail_thread_0_process_9'	:	(.20, 10),
    'SUM_timeInJail_thread_1_process_9'	:	(.20, 10),
}

# Make a separate plot for each crunch file.
PLOTLIST = (
    'SUM_timeInJail_thread_0_process_0'	,
    'SUM_timeInJail_thread_1_process_0'	,
    'SUM_timeInJail_thread_0_process_1'	,
    'SUM_timeInJail_thread_1_process_1'	,
    'SUM_timeInJail_thread_0_process_2'	,
    'SUM_timeInJail_thread_1_process_2'	,
    'SUM_timeInJail_thread_0_process_3'	,
    'SUM_timeInJail_thread_1_process_3'	,
    'SUM_timeInJail_thread_0_process_4'	,
    'SUM_timeInJail_thread_1_process_4'	,
    'SUM_timeInJail_thread_0_process_5'	,
    'SUM_timeInJail_thread_1_process_5'	,
    'SUM_timeInJail_thread_0_process_6'	,
    'SUM_timeInJail_thread_1_process_6'	,
    'SUM_timeInJail_thread_0_process_7'	,
    'SUM_timeInJail_thread_1_process_7'	,
    'SUM_timeInJail_thread_0_process_8'	,
    'SUM_timeInJail_thread_1_process_8'	,
    'SUM_timeInJail_thread_0_process_9'	,
    'SUM_timeInJail_thread_1_process_9'	,
)
