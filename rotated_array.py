def rotated_array_search (input_list, number):
        start = 0
        end = len(input_list) - 1
        
        while start <= end:
            
            mid = int((start + end)/2)
            
            if input_list[mid] == number:
                return mid
            
            if input_list[mid] <= input_list[end]: 
                if input_list[mid] < number and input_list[end] >= number:
                    start = mid + 1
                else:
                    end = mid - 1
            elif input_list[start] <= input_list[mid]:
                if number >= input_list[start] and number < input_list[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            
        return -1
    
def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 0])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])