# Lossy_counting: Implementation Overview
This codebase embodies the lossy counting algorithm, developed specifically for the Data Stream course at the University of Porto.

# Utilizing the Implementation
The entire algorithm resides within the lossy_counting.py Python file. For a demonstration of how to employ the LossyCounting class, refer to demo.py.

# Instantiate the LossyCounting class with the following parameters:
- minSupport: Minimum support required for all items in the results.
- error: Maximum acceptable error in the results.
1. Stream data through the algorithm using LossyCounting().processNextElement(element).
2. Retrieve results via the LossyCounting().getFrequentItems() method.
3. Running Examples

#To execute the provided demos:

1. Unzip the file.
2. Navigate to the lossy_counting folder.
Ensure Python 3 is installed on your machine.
3. Run python3 main.py.
# Demo Contents:
1. Pareto Distribution Demo: Samples drawn from the Pareto distribution.
2. Web Data Demo: Samples sourced from logs of anonymous users on www.microsoft.com.
3. Paradise Demo: Word frequencies from the third and final part of Dante's Divine Comedy
