These are the Q&A for CSC343 Spring 2024 Assignment 3. Each is worth 5%.
Please place your answers starting on the ANSWER line below each question,
adding lines as necessary, within the *** paragraph delimters.
********************************************
YOUR NAME: Ryan Livinghouse

********************************************
Q1: Why are these two time measurements from RR:

DIFFing rr_crunch.py rr_crunch.ref
OK: MEAN_running at 15.0% tolerance = 101.24
OK: MEAN_ready at 15.0% tolerance = 78.75

significantly shorter than these from FCFS:

DIFFing fcfs_crunch.py fcfs_crunch.ref
OK: MEAN_running at 15.0% tolerance = 395.96
OK: MEAN_ready at 15.0% tolerance = 419.95

STUDENT ANSWER:

The RR scheduling algorithm's preemptive nature allows processes to be executed in a
more balanced manner, with each process receiving a fair share of CPU time. This leads
to shorter mean running and ready times compared to FCFS, where processes are executed
sequentially, often resulting in longer wait times for subsequent processes,
especially if a lengthy process occupies the CPU.

********************************************
Q2: Why are these two time measurements from SJFEST:

DIFFing sjfEst_crunch.py sjfEst_crunch.ref
OK: MEAN_running at 15.0% tolerance = 392.27
OK: MEAN_ready at 15.0% tolerance = 317.14

significantly longer than these from SRTF:

DIFFing srtf_crunch.py srtf_crunch.ref
OK: MEAN_running at 15.0% tolerance = 198.05
OK: MEAN_ready at 15.0% tolerance = 164.97

STUDENT ANSWER:

SRTF's preemptive capability allows it to switch to shorter jobs even when a process
is currently running, optimizing the CPU utilization and minimizing waiting times. In
contrast, SJFEST, despite using burst time estimation, does not preempt ongoing
processes, leading to potentially longer waiting times if shorter jobs arrive during
the execution of a longer job.

********************************************
Q3: Why are these two time measurements from SRTF:

DIFFing srtf_crunch.py srtf_crunch.ref
OK: MEAN_running at 15.0% tolerance = 198.05
OK: MEAN_ready at 15.0% tolerance = 164.97

significantly longer than these from RR:

DIFFing rr_crunch.py rr_crunch.ref
OK: MEAN_running at 15.0% tolerance = 101.24
OK: MEAN_ready at 15.0% tolerance = 78.75

STUDENT ANSWER:

SRTF is designed to prioritize shorter jobs, which can lead to longer jobs waiting for
an extended period, especially in a diverse workload scenario. RR, with its
time sharing approach, ensures a more balanced distribution of CPU time, which can
lead to shorter average waiting times across all jobs, demonstrating a more equitable
scheduling approach.

********************************************
