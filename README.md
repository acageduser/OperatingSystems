# OperatingSystems
CSC 343 Operating Systems Coursework

### prisonerd2024:
The first project introduced me to state machines through the Iterated Prisoner's Dilemma simulation. I developed a program that dynamically adjusted its strategy based on the game's outcomes, delving deep into state transitions and variable initializations. This exercise offered a visual for the decision-making processes within a simulated environment.

### schedualUserKernel2024:
In the second assignment, I included user-to-kernel mode scheduling, where I implemented many-to-one and many-to-many scheduling algorithms. This task required an understanding of how multiple user threads interact with kernel processes, pushing me to consider efficiency and resource management in a multi-threaded context.

### stm3CPUschedSP2024:
The third project involved the implementation and modification of various thread scheduling algorithms, such as First-Come, First-Served (FCFS), Shortest Job First (SJF), and Shortest Remaining Time First (SRTF). Each algorithm required a unique approach to process prioritization and resource allocation, building into preemptive and non-preemptive scheduling. By predicting and estimating process burst times, I developed an understanding of how operating systems optimize task execution and resource utilization.

### DemandPagingCSC343Spring2024:
The fourth project compared relative times spent on page replacement across multiple algorithms. The purpose was to create a 'perfect scenario' with a hypothetical 'perfectly simulated' test that was 100% efficient to create a general benchmark and test other algorithms against it. The following algorithms were then compared to the 'perfect scenario' to see how close to 'perfect' the algorithm would run. The 'perfect scenario' cannot be implemented in real life as it uses future knowledge of page requests, so alternative algorithms were developed to get as close as possible.

- 'First In, First Out' (FIFO), 'Least Recently Used' (LRU), and 'Least Recently Used Dirty' (LRUDirty) algorithms were all tested.

- RESULT: LRU was the most effective, balancing the simple common pattern of memory access that 'pages that have not been used recently are more likely to be unused in the near future.'
