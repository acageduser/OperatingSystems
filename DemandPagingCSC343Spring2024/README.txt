README.txt file for CSC343 Spring 2024 Assignment 4 on
Page Replacement Algorithms, due by end of May 2.

STUDENT NAME:
Each answer contributes 9% of the overall project grade.

*************************************************************
Q1 9%: Here are the relative times spent on page replacement in
       the the order of assignment steps:

PageReplaceOptimal_crunch.ref:SUM_findVictim=25281
PageReplaceFIFO_crunch.ref:SUM_findVictim=58804
PageReplaceLRU_crunch.ref:SUM_findVictim=55730
PageReplaceLRUDirty_crunch.ref:SUM_findVictim=64169

1. Since Optimal Page Replacement simulates looking into the
   future and hence cannot be implemented in a real operating
   system, what is the purpose in studying & simulating it?

YOUR ANSWER:

The purpose of studying and simulating Optimal Page Replacement is to 
establish a benchmark for comparing the efficiency of the other page 
replacement algorithms. Although it cannot be implemented due to its 
requirement for future knowledge of page requests, it serves as a best
case scenario. By understanding how close other algorithms come to this 
optimal performance, we can gauge their effectiveness and make informed 
choices about which algorithms to implement in real systems.


*************************************************************
Q2 9%: Why does PageReplaceLRU outperform PageReplaceFIFO on this
       measure. In other words, what is the reason to use the
       Least Recently Used page replacement algorithm?

YOUR ANSWER:

PageReplaceLRU outperforms PageReplaceFIFO because LRU makes decisions 
based on recent usage history, which tends to align well with common 
patterns of memory access in real applications. Pages that have not 
been used recently are more likely to be unused in the near future, 
making them better for replacement. FIFO replaces pages based on their 
arrival time without considering how frequently or recently they have 
been accessed. This is a sort of oversight in scenarios where older 
pages are still frequently accessed, making it less efficient in this 
case.


*************************************************************
Q3: 9%: Notice that the simulated time for page replacement in
        PageReplaceLRUDirty at 64169 is bigger (worse) than
        PageReplaceLRU. This had me baffled at first, so I did some
        profiling. Notice "the Gaussian Distribution of page references,
        giving pretty good Locality of Reference" in the assigment page.
        Also notice this line in the code:
            isModified = 1 if ((sample(0,1024,'uniform') % 10) == 0) else 0;
        Only 1/10th of all page references start out dirty (they write to
        their page), but with high locality, we night expect a page to become
        dirty in the average time of 10 accesses, before it is victimized
        and paged out.

        The average time in ticks a page number spends in its
        FIFO referenceQueues in LRU is:

$ python testLRUDEBUG.py
MEAN DELAYS 79.853263 MEDIAN 80

        The average time in ticks a page number spends in its
        FIFO referenceQueues in LRUDirty is:

python testLRUDirtyDEBUG.py
MEAN DELAYS 56.483471 MEDIAN 56.0

How does prefering clean, unmodified pages for replacement in LRUDirty
affect the recency of replacement victims in this workload and why?

YOUR ANSWER:

Preferring clean and unmodified pages for replacement in LRUDirty 
affects the recency of replacement victims by reducing the average time 
pages spend in memory before being replaced. This is shown in the 
shorter MEAN DELAYS in LRUDirty compared to LRU. Clean pages are often 
less costly to replace because they do not require writing back to disk, 
allowing the system to replace them more swiftly. This strategy is 
while efficient in terms of write operations but it seems to lead to 
more frequent page replacements of potentially useful pages that have 
NOT been modified. The high locality of reference means that pages are 
more likely to be accessed repeatedly within a short period, so 
replacing them too early (even if they are clean) can lead to decreased 
performance.


*************************************************************
