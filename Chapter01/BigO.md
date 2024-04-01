# BigO Notation 

BigO tells how fast a algorithm grows in term of number of operations
algorithm grows = number of operations grows

Given that an algorithm is tested on "n" elements.
BigO notation doesn't care if the algorithm perfomed better in one take, or worse in another take.
It only cares about how that algorithm perform in the worst possible case.

Based on this number of operations, this algorithm can be considered slow or fast.

Notation: O(n), where n is equal to the number of operations

Linear execution-time: the number of operations is equal to the number of elements the algorithm needs to be tested. Notation: O(n)
Logarithmic execution-time: log2 n is equal to the number of operations. Notation: O(log n)

Others BigO's execution-time:
-> O(n * log n)
-> O(n^2)
-> O(n!);

Simple search: linear exection-time -> O(n)


Binary search: logarithmic execution-time -> O(log n)

Arrays:
    -> Insertion: O(n)
    -> Reading: O(1)

Linked Lists:
    -> Insertion: O(1)
    -> Reading: O(n)
