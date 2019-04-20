nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
nums1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print("PRE SORT: {0}".format(nums))

def bubble_sort_unoptimized(arr):
  iteration_count = 0
  for el in arr: #first for 9
    for i in range(len(arr) - 1): #going through list and comparing 9 and swaping
      iteration_count += 1
      if arr[i] > arr[i + 1]:
        arr[i], arr[i + 1] = arr[i + 1], arr[i] #swap

  print("PRE-OPTIMIZED ITERATION COUNT: {0}".format(iteration_count))

def bubble_sort(arr):
  iteration_count = 0
  for el in range(len(arr)):
    for i in range(len(arr) - el - 1): #going through list without the index of the previous element
    #only through unplaced elements basically
      iteration_count += 1
      if arr[i] > arr[i + 1]:
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
        
  print("POST-OPTIMIZED ITERATION COUNT: {0}".format(iteration_count))

bubble_sort_unoptimized(nums)
bubble_sort(nums1)
print("POST SORT: {0}".format(nums))
print(nums1)