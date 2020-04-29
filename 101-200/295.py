# method 1: brutal force
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []


    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        if not self.arr: return
        # only 1 element
        if len(self.arr) == 1: return self.arr[0]

        self.arr.sort()
        length = len(self.arr)
        if length % 2 == 0:
            # even, find middle two and get average
            return (self.arr[length//2] +  self.arr[length//2 - 1]) / 2
        else:
            # odd, find the middle index number
            return self.arr[length//2]




# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []
        self.min_heap = []


    def addNum(self, num: int) -> None:
        # if number is smaller than/equal to the top of max heap, add to max heap
        # otherwise, add to min heap
        if num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        # make sure max heap has at least one more element than min heap
        if len(self.max_heap) > len(self.min_heap) + 1:
            # move top of max heap to min heap
            heapq.heappush(self.min_heap, -heapq.pop(self.max_heap))
        else:
            # move top of min heap to max heap
            heapq.heappush(self.max_heap, -heapq.pop(self.min_heap))

    def findMedian(self) -> float:
            if (len(self.max_heap) + len(self.min_heap)) % 2 == 0:
                # if even then get the medium of top of max and min heap
                return ( -self.max_heap[0] + self.min_heap[0] ) / 2.000
            else:
                # if odd then get the top of max heap
                return -self.max_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# Author's comments:
# The above solution is missing the edge case if max_heap has no elements yet, thus it'll result
# in runtime error (index out of range error)

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []
        self.min_heap = []


    def addNum(self, num: int) -> None:
        # if number is smaller than/equal to the top of max heap, add to max heap
        # otherwise, add to min heap
        if not self.max_heap or num <= -self.max_heap[0] :
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        # make sure max heap has at least one more element than min heap
        if len(self.max_heap) > len(self.min_heap) + 1:
            # move top of max heap to min heap
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        else:
            # move top of min heap to max heap
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
            if (len(self.max_heap) + len(self.min_heap)) % 2 == 0:
                # if even then get the medium of top of max and min heap
                return ( -self.max_heap[0] + self.min_heap[0] ) / 2.000
            else:
                # if odd then get the top of max heap
                return -self.max_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# Author's comments:
# The above solution is still wrong, giving IndexError: index out of range error on
# heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
# because we are not moving elements between max_heap and min_heap all the time
# if and ONLY if there are more than 1 element number difference

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []
        self.min_heap = []


    def addNum(self, num: int) -> None:
        # if number is smaller than/equal to the top of max heap, add to max heap
        # otherwise, add to min heap
        if not self.max_heap or num <= -self.max_heap[0] :
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        # make sure max heap has at least one more element than min heap
        if len(self.max_heap) > len(self.min_heap) + 1:
            # move top of max heap to min heap
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap) + 1: # <----- this is wrong as well!!!
            # move top of min heap to max heap
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
            if (len(self.max_heap) + len(self.min_heap)) % 2 == 0:
                # if even then get the medium of top of max and min heap
                return ( -self.max_heap[0] + self.min_heap[0] ) / 2.000
            else:
                # if odd then get the top of max heap
                return -self.max_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


# HAHAHHA this solution is still wrong!!
# in findMedian function we don't care if the total number of elements in max_heap and min_heap
# is even or odd, what we care about is if number of elements in max_heap is the same as the number
# of elements in min_heap
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []
        self.min_heap = []


    def addNum(self, num: int) -> None:
        # if number is smaller than/equal to the top of max heap, add to max heap
        # otherwise, add to min heap
        if not self.max_heap or num <= -self.max_heap[0] :
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        # make sure max heap has at least one more element than min heap
        if len(self.max_heap) > len(self.min_heap) + 1:
            # move top of max heap to min heap
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            # move top of min heap to max heap
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
            if len(self.max_heap) == len(self.min_heap):
                # if even then get the medium of top of max and min heap
                print(f"max_heap = {self.max_heap}, min_heap = {self.min_heap}")
                return ( -self.max_heap[0] + self.min_heap[0] ) / 2.000

            # if odd then get the top of max heap
            print(f"max_heap = {self.max_heap}, min_heap = {self.min_heap}")
            return -self.max_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
