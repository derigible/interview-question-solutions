'''
This module is used to determine the efficiency of an algorithm or process.
The main reason for this is t validate that an idea works better than another,
or that one language performs better in one way over another.

Output for each class should be in a dictionary with the following keys:

reps
best_case_time
worst_case_time
expected_case_time
iterative_data_best
iterative_data_worst
-- TO DO --
best_mem_peak
worst_mem_peak
expected_mem_peak
-- Possibly Add? --
Memory usages averaged for each case

****Note: Iterative data should be a list of runs with an increasing size of input N, places as a list of
          tuples with position 0 being N and position 1 being the time.

These stats should be returned and not printed. Decisions shall be made
as to how the data from these tests will be presented (most likely printed,
but don't limit yourself to that case).

Possibly in the future learn how to take output data and make some interesting points
out of it.

Profiling can also be done in this module. See below for examples.

Created on Mar 13, 2014

@author: marphill
'''

import profile, timeit, csv

def time_nameformatter(reps = 100000, expected_case="Marc Phillips", profile = False):
    """ Testing the time it takes for nameformatter to output best and worst_case.
        
        Expected case can be just a normal type of name. For example: "Marc Phillips"
    """
    results = {}
    print "Starting the expected case..."
    results['expected_case'] = min(timeit.repeat("nameformatter('{}')".format(expected_case), "from output_algorithms import nameformatter", number=reps))/reps
    
    best = ('xX', 'xX'*(5/2), 'xX'*(15/2), 'xX'*(20/2), 'xX'*(25/2), 'xX'*(30/2), 'xX'*(35/2), 'xX'*(40/2), 'xX'*(45/2), 'xX'*(50/2), 'xX'*(55/2), 'xX'*(60/2), 'xX'*(65/2), 'xX'*(100/2))
    worst = ('x', 'x'*5, 'x'*15, 'x'*20, 'x'*25, 'x'*30, 'x'*35, 'x'*40, 'x'*45, 'x'*50, 'x'*55, 'x'*60, 'x'*65, 'x'*100)

    print "Expected case ended."
    print "Starting the best data cases..."
    
    datab = []
    for x in best:
        print "Do string length {}".format(len(x))
        y = min(timeit.repeat("nameformatter('{}')".format(x), "from output_algorithms import nameformatter", number=reps))/reps
        datab.append((len(x),y*10000))
    results['iterative_data_best'] = datab
    with open('best.csv', 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(datab)
        f.close()
    
    print "Best data cases ended."
    print "Starting the worst data cases..."
    
    dataw = []
    for x in worst:
        print "Do string length {}".format(len(x))
        y = min(timeit.repeat("nameformatter('{}')".format(x), "from output_algorithms import nameformatter", number=reps))/reps
        dataw.append((len(x),y*10000))
        if len(x) == 1:
            results['best_case_time'] = y
        if len(x) == 100:
            results['worst_case'] = y
    results['iterative_data_worst'] = dataw
    with open('worst.csv', 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(dataw)
        f.close()
    
    print "Best data cases ended."
    
    if profile:
        profile.run("output_algorithms.nameformatter('Marc PHillips')")
        
    return results

if __name__ == '__main__':
    print time_nameformatter()