# scheduleUserKernel2024/diffset.py -- set of simulation properties to test
# after a simulation run. See crunchlog.py

# Map the property to be checked against its (TOLERANCE, RAWTOLERANCE),
# where TOLERANCE is a percatage as a fraction, and RAWTOLERANCE
# is the minimum difference between the simulation value and the
# reference value for the property required to trigger an error.
DIFFMAP = {
    'MIN_stallThread'	:	(.20, 10),
    'MEAN_stallThread'	:	(.20, 10),
    'MAX_stallThread'	:	(.20, 10),
}

# Make a separate plot for each crunch file.
PLOTLIST = (
    'MIN_stallThread'	,
    'MEAN_stallThread'	,
    'MAX_stallThread'	,
)
