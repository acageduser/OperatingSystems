README.txt file for CSC343 Spring 2024 Assignment 5 on
Page Replacement Algorithms, due via D2L by end of May 9.

STUDENT NAME:

Each answer contributes 10% of the overall project grade.
This like the first 4 projects is worth 20% of your semester grade.
*************************************************************
Q1. Which one of the four page reference distributions in Table 1 --
    gaussian, exponential, revexponential, or uniform -- exhibits the
    worst Locality of Reference in terms of SUM_findVictim cost of
    page replacement? What numeric SUM_findVictim pattern makes you say that?

YOUR ANSWER:
The uniform distribution has the highest SUM_findVictim cost of page replacement, showing the 
worst locality of reference. This is evident from the high numbers in the uniform distribution 
across all frame counts and algorithms, particularly the numbers like 89334 for FIFO_100_uniform 
and 68929 for FIFO_200_uniform, which are significantly higher than those for other distributions.

*************************************************************
Q2. Why does the page reference distribution you chose in Q1 exhibit
    the worst Locality of Reference behavior? Refer to one or more of
    Figure 2 through 6 in your answer.

YOUR ANSWER:
The uniform distribution spreads page references evenly across the entire page range, which means 
there is no concentration of references around any particular set of pages. This leads to frequent
page faults and replacements, as there is no predictable pattern that the page replacement 
algorithms can optimize for. This lack of pattern increases the number of page replacements 
needed, increasing the SUM_findVictim cost.

*************************************************************
Q3. Which one of the four page reference distributions in Table 1 --
    gaussian, exponential, revexponential, or uniform -- exhibits the
    best Locality of Reference in terms of SUM_findVictim cost of page
    replacement, for a given frameCount value of either 100 or 200?
    What numeric SUM_findVictim pattern makes you say that?

YOUR ANSWER:
The gaussian distribution shows the best locality of reference with the lowest SUM_findVictim 
costs for both frame counts of 100 and 200. The specific numbers that highlight this are 4213 
for Optimal_100_gaussian and 0 for Optimal_200_gaussian, indicating a highly effective 
management of pages due to the concentration of references around the mean of the distribution.

*************************************************************
Q4. Why does the page reference distribution you chose in Q3 exhibit the
    best Locality of Reference behavior for a given frameCount value?
    Refer to one or more of Figure 2 through 6 and their discussions
    in your answer.

YOUR ANSWER:
The gaussian distribution, with its concentration of references around the mean, allows page 
replacement algorithms to effectively keep the most frequently accessed pages in memory. This 
reduces the need for page replacements. Since a significant portion of references hit a smaller 
range of pages, this distribution matches well with how page replacement algorithms optimize for 
pages that are likely to be accessed again soon.

*************************************************************
Q5. Which one of the four page reference distributions in Table 1 --
    gaussian, exponential, revexponential, or uniform -- is the
    least sensitive to the page replacement algorithm used (Optimal,
    FIFO, or LRU)?  What numeric SUM_findVictim pattern makes you say that?

YOUR ANSWER:
The gaussian distribution is the least sensitive to the choice of page replacement algorithm. 
For example, the change in SUM_findVictim from FIFO to LRU or Optimal does not swing as 
dramatically as with other distributions. This is shown in the consistently lower SUM_findVictim 
values across different algorithms when using the gaussian distribution, as seen in the table.

*************************************************************
Q6. Which one or more of the four page reference distributions in Table 1
    -- gaussian, exponential, revexponential, or uniform -- give
    greater-than-linear improvements when the frameCount doubles from
    100 to 200? In other words, when frameCount doubles from 100 to 200,
    cost in terms of SUM_findVictim is reduced by more than half. Why do
    it or they give greater-than-linear improvement?

YOUR ANSWER:
The gaussian distribution shows greater than linear improvements when the frame count doubles 
from 100 to 200. This is apparent from Optimal_100_gaussian at 4213 to Optimal_200_gaussian at 
0, indicating more than a 50% reduction in cost. This happens because increasing frame count 
allows more of the heavily used pages (around the mean) to stay in memory, greatly reducing page 
faults.

*************************************************************
Q7. Which property dominates the minimization of SUM_findVictim for a given
    frameCount value, page replacement algorithm or locality of reference?
    Why? I am not looking for a specific page replacement algorithm like
    (Optimal, FIFO, LRU), nor locality of reference like (gaussian,
    exponential, revexponential, uniform), but rather just
    "page replacement algorithm" OR "locality of reference".
    Justify your answer in terms of Table 1 and optionally the figures.

YOUR ANSWER:
Locality of reference dominates the minimization of SUM_findVictim for a given frame count. 
This is obvious from how different distributions affect the SUM_findVictim values more 
significantly than changes in the page replacement algorithm. Algorithms perform better or worse 
based on how page references are clustered or spread out.

*************************************************************
Q8. Do any of the frameCount increases from 100 to 200 in Table 1 exhibit
    Belady's Anomaly as discussed in Chapter 9 slides? If so, cite an
    example from Table 1 that shows Belady's Anomaly.

YOUR ANSWER:
No, none of the frame count increases from 100 to 200 in Table 1 exhibit Belady's Anomaly. 
Beladys Anomaly would imply higher SUM_findVictim costs with increased frame count, which does 
not occur in any of the data.

*************************************************************
Q9. From what value to what value does the translation-lookaside-buffer
    (TLB) register set provide a MAPPING? Why is it important to maintain
    this mapping in a register and not just in the page table of the process?

YOUR ANSWER:
The TLB provides a mapping from virtual page numbers to physical frame numbers. Maintaining this 
mapping in a register speeds up the memory access process significantly. Accessing a register is 
much faster than repeatedly querying a page table stored in memory (which is slow).

*************************************************************
Q10. What status bit or bits would be added to the TLB to support the LRU
     and LRUDirty page replacement algorithms without forcing the kernel to
     consult the page table on every application memory access?

YOUR ANSWER:
To support LRU and LRUDirty without constant page table checks, a 'last accessed' timestamp or 
a 'use bit' could be added to the TLB. This would allow the system to update access records 
directly in the TLB during memory access operations, making the  LRU operations efficient by 
quickly identifying the least recently used pages.

*************************************************************