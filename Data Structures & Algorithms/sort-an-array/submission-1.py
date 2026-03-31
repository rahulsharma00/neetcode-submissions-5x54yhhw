class Solution:
    def sortArray(self, my_array: List[int]) -> List[int]:
        def merge_sort(arr):
            if len(arr) > 1:
                middle = len(arr)//2
                left = arr[:middle]
                right = arr[middle:]

            # Calling merge_sort recursively
                merge_sort(left)
                merge_sort(right)

            # merge step
                i,j = 0,0 # left, right array index
                k = 0 # merged array index
                while i < len(left) and j < len(right):
                    if left[i] < right[j]:
                        arr[k] = left[i]
                        i +=1
                    else:
                        arr[k] = right[j]
                        j +=1 
                    k +=1

                while i < len(left):
                    arr[k] = left[i]
                    i += 1
                    k += 1
                while j < len(right):
                    arr[k] = right[j]
                    j += 1
                    k += 1
        merge_sort(my_array)
        return my_array