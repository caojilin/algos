import random
import bisect

random.seed(0)
arr1 = list(range(10))
random.shuffle(arr1)
print("before:", arr1)


def quick_sort(arr):
    if len(arr) != 0:
        pivot = random.choice(arr)
        lt = [i for i in arr if i < pivot]
        eq = [i for i in arr if i == pivot]
        gt = [i for i in arr if i > pivot]
        return quick_sort(lt) + eq + quick_sort(gt)
    return []


def insert_sort(arr):
    for i in range(1, len(arr)):
        cur = arr[i]
        pos = i
        while pos > 0 and arr[pos - 1] > cur:
            arr[pos] = arr[pos - 1]
            arr[pos - 1] = cur
            pos -= 1


def merge(a, b):
    for i in b:
        a.insert(bisect.bisect(a, i), i)


t1 = list(range(10))
a1 = t1[:]
t2 = list(range(8, 18))
a2 = t2[:]
random.shuffle(t1)
random.shuffle(t2)


def mergesort(arr):
    queue = []
    for i in arr:
        queue.append([i])
    while len(queue) > 1:
        queue.append(merge(queue.pop(0), queue.pop(0)))
    return queue[0]

