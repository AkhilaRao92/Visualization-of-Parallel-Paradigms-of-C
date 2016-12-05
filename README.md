# Visualization-of-Parallel-Paradigms-of-C

Tool to visualize parallel computing paradigms of C with the parallel paradigms OpenMP and Pthreads. The input to the tool is a C program which is run under gdb. The output from gdb is captured in the tool and depicted on the GUI. 
The visualization includes the instruction pointer which indicates the step by step execution of the program. The tool displays how exactly the threads are created and the distribution and/or sharing of the data. It also portrays local variables, global variables, activation records, function parameters (if any). 
In case of threads, the currently executing instruction is highlighted for each thread.
