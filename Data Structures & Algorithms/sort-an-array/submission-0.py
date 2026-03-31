class Solution:
    def sortArray(self, my_array: List[int]) -> List[int]:
        n = len(my_array)
        for i in range(n-1):
            for j in range(n-i-1):
                if my_array[j] > my_array[j+1]:
                    my_array[j], my_array[j+1] = my_array[j+1], my_array[j]

        return my_array