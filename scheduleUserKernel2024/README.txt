These are the Q&A for CSC343 Spring 2024 Assignment 2.
Please place your answers starting on the ANSWER line below each question,
adding lines as necessary, within the *** paragraph delimters.
********************************************
YOUR NAME: Ryan Livinghouse

********************************************
The following simulation times apply to the next questions.
You will need to go into your code and examine some variable values
before answering these question.
OneToOne:
DIFFing OneToOne_crunch.py OneToOne_crunch.ref
OK: MIN_stallThread at 20.0% tolerance = 0
OK: MEAN_stallThread at 20.0% tolerance = 0
OK: MAX_stallThread at 20.0% tolerance = 0

ManyToOne:
DIFFing ManyToOne_crunch.py ManyToOne_crunch.ref
OK: MIN_stallThread at 20.0% tolerance = 499
OK: MEAN_stallThread at 20.0% tolerance = 21142.19
OK: MAX_stallThread at 20.0% tolerance = 24931

ManyToMany:
DIFFing ManyToMany_crunch.py ManyToMany_crunch.ref
OK: MIN_stallThread at 20.0% tolerance = 496
OK: MEAN_stallThread at 20.0% tolerance = 6760.59
OK: MAX_stallThread at 20.0% tolerance = 9130
********************************************
Q1: (10% of assignment): Given the fact that ManyToOne has only 1
kernel region that can be entered from only 1 user thread at a time,
while ManyToMany allows up to 3 user threads to enter the kernel at a
time, why do both have almost the same MIN_stallThread time
spent in the stallThread state, unlike the MEAN and MAX stallThread times?
ANSWER 1:
The MIN_stallThread time being similar in both ManyToOne and ManyToMany 
suggests that the minimum time a thread had to wait in the stall state is
nearly the same for both scenarios. This could be because the shortest
waiting times likely occur when there is minimal competition for the kernel,
which can happen in both scheduling strategies. It's the average and
maximum times where the difference in kernel access between ManyToOne
and ManyToMany significantly impacts, reflected in the MEAN and MAX values.
********************************************
Q2: (10% of assignment): 
What accounts for the value in range 20000 to 25000 ticks in state stallThread?
ManyToOne
OK: MAX_stallThread at 20.0% tolerance = 24931
ANSWER 2:
The value in the range 20000 to 25000 ticks for ManyToOne's MAX_stallThread
time indicates the longest time a thread had to wait in the stallThread state.
In ManyToOne, since there's only one kernel region available, threads might
experience significant waiting times, especially under high competition. The
maximum value observed reflects a scenario where a thread had to wait for an
extended period, likely due to many other threads trying to access the single
available kernel region, causing a longer queue and increased wait time.
********************************************
