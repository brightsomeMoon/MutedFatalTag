array = [76,3,2,1,2,3,4,5,6,23,432,534,6,12]

def func(array):
  for front_index in range(0, len(array)) :
    for index in range(front_index, len(array)) :
      if array[index] < array[front_index] :
        temp = array[front_index]
        array[front_index] = array[index]
        array[index] = temp
  return array

result = func(array)
print(result)