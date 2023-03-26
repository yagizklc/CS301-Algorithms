

"""
find 2 algorithms with best asymptotic worst-case R.T. 
to find the k smallest numbers in this set, in sorted order.
    - sorting algo: comparison-based sort -> return k smallest (already sorted)
    - orderStatistic algo: find k'th smallest -> partition around that 
        -> use comp-based sorting (to sort k smallest numbers) -> return

"""

"""
sorting algo: heap, merge, quick are all optimum comp-based sorting.
They all have their drawbacks:
heap: requires building heap O(n), and has more insturctions -> 3 times slower than quicksort
merge: requires O(n) space complexity for temporary array
quick: takes O(n^2) for sorted or reverse-sorted input arrays

heap = O(n lgn + k lgn) (build + select) -- do not select this one !!!

merge = O(n lgn) always
quick = O(n lgn) most of the time - O(n^2) worst case 

orderStatistic algo: quickSelect


"""

