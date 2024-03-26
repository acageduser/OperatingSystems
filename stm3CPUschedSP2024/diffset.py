# stm3CPUschedSP2024/diffset.py -- set of simulation properties to test after
# a simulation run. See crunchlog.py

# Map the property to be checked against its (TOLERANCE, RAWTOLERANCE),
# where TOLERANCE is a percatage as a fraction, and RAWTOLERANCE
# is the minimum difference between the simulation value and the
# reference value for the property required to trigger an error.
DIFFMAP = {
    'MEAN_running' :                    (.15, 10),
    'MEAN_ready' :                      (.15, 10),
    'MEAN_waiting' :                    (.15, 10),
    'MEAN_TURNAROUNDTIME' :             (.15, 10),
    'MAX_running' :                     (.15, 10),
    'MAX_ready' :                       (.15, 10),
    'MAX_waiting' :                     (.15, 10),
    'MAX_TURNAROUNDTIME' :              (.15, 10),
    'MIN_running' :                     (.15, 10),
    'MIN_ready' :                       (.15, 10),
    'MIN_waiting' :                     (.15, 10),
    'MIN_TURNAROUNDTIME' :              (.15, 10),
}

# Make a separate plot for each crunch file. Not used in this assignment.
PLOTLIST = (
)
