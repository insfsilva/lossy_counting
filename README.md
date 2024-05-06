# lossy_counting
Implementation of the lossy counting algorithm for purposes of Data Stream course at University of Porto

## How to work with the implementation
The whole algorithm is implemented in the single python file lossy_counting.py. The example of use of the LossyCounting class can be seen in the demo.py file General use of the implementation:

1. create LossyCounting class with parameters:
minSupport - minimal support of all items in the results
error - maximal error in the results
2. process stream by calling LossyCounting().processNextElement(element)
3. get results by calling the method LossyCounting().getFrequentItems()
# Run example
to run the included demos
1. extract the zip file
2. enter the lossy-counting folder
to run the example you have to have install python3 on your machine
then simply run python3 main.py
Included demos:
pareto distribuition demo - with samples drawn from the pareto distribution
web data demo - with samples from logs of anonymous users of www.microsoft.com
paradise demo - with word frequencies from the third and final part of Dante's Divine Comedy
