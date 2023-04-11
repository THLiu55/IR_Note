import timeit

from Worksheet3 import SkipList, intersect


def quick_intersect(l1, l2):
    answer = []  # a list to store the answer (for now: we will return a SkipList at the end)
    p1 = l1.start  # start the first reference (p1) at the beginning list 1
    p2 = l2.start  # start the second reference (p2) at the beginning list 2

    # haven't reached the end of either list
    while p1 is not None and p2 is not None:
        # if p1 and p2 point to the equal elements, add it to the answer and move both pointers
        if p1.element == p2.element:
            answer.append(p1.element)
            p1 = p1.next
            p2 = p2.next
        # p1's element is smaller, so move p1
        elif p1.element < p2.element:
            p1 = p1.skip if p1.skip is not None and p1.skip.element <= p2.element else p1.next
        # p2's element is smaller, so move p2
        else:
            p2 = p2.skip if p2.skip is not None and p2.skip.element <= p1.element else p2.next
    return SkipList(answer)


# This is the code that will run when you execute this file with Python.
if __name__ == '__main__':
    list1 = SkipList(range(0, 100000))
    list2 = SkipList([2, 3, 46, 70, 7222, 999999])

    # measure the time to run the intersect(...) function
    time_taken = timeit.timeit('quick_intersect( list1, list2 )', number=1000, globals=globals())
    print('Efficient insert operation took {:.4f} seconds'.format(time_taken))
    time_taken = timeit.timeit('intersect( list1, list2 )', number=1000, globals=globals())
    print('Normal insert operation took {:.4f} seconds'.format(time_taken))
