class QuickFindUF:
    """
    This is an implementation of the union-find data structure - see module documentation for
    more info.

    This implementation uses quick find. Initializing a data structure with n sites takes linear time.
    Afterwards, the find, connected, and count operations take constant time but the union operation
    takes linear time.

    For additional documentation, see Section 1.5 of Algorithms, 4th Edition by Robert Sedgewick and Kevin Wayne.
    """

    def __init__(self, n):
        """
        Initializes an empty union-find data structure with n sites,
        0 through n-1. Each site is initially in its own component.

        :param n: the number of sites
        """
        self._count = n
        self._id = list(range(n))

    def _validate(self, p):
        # validate that p is a valid index
        n = len(self._id)
        if p < 0 or p >= n:
            raise ValueError('index {} is not between 0 and {}'.format(p, n))

    def union(self, p, q):
        """
        Merges the component containing site p with the
        component containing site q.

        :param p: the integer representing one site
        :param q: the integer representing the other site
        """
        self._validate(p)
        self._validate(q)

        p_id = self._id[p] # needed for correctness
        q_id = self._id[q] # to reduce the number of array accesses

        # p and q are already in the same component
        if p_id == q_id:
            return

        for i in range(len(self._id)):
            if self._id[i] == p_id:
                self._id[i] = q_id
        self._count -= 1

    def find(self, p):
        """
        Returns the component identifier for the component containing site p.

        :param p: the integer representing one site
        :return: the component identifier for the component containing site p
        """
        self._validate(p)
        return self._id[p]

    def connected(self, p, q):
        """
        Returns true if the two sites are in the same component.

        :param p: the integer representing one site
        :param q: the integer representing the other site
        :return: true if the two sites p and q are in the same component; false otherwise
        """
        self._validate(p)
        self._validate(q)
        return self._id[p] == self._id[q]

    def count(self):
        return self._count

import sys
import time
from algs4.stdlib import stdio

if __name__ == '__main__':
    if len(sys.argv) > 1:
        try:
            sys.stdin = open(sys.argv[1])
        except IOError:
            print("File not found, using standard input instead")
    start_time = time.time()
    n = stdio.readInt()
    quf = QuickFindUF(n)
    while not stdio.isEmpty():
        p = stdio.readInt()
        q = stdio.readInt()
        if quf.connected(p, q):
            continue
        quf.union(p, q)	
    
    for i in range(n):
        print(quf._id[i])
    
    if quf.connected(1, 0):
        sys.stdout.write('True\n')
        #print("--- %s seconds ---" % (time.time() - start_time))
    else:
        sys.stdout.write('False\n')
        #print("--- %s seconds ---" % (time.time() - start_time))