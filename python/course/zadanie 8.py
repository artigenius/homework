# min max
def minmax(lst):
  min_number = min (lst, key=lambda i:int(i))
  max_number = max (lst, key=lambda i:int(i))
  list_len = len (lst)
  return list_len, max_number, min_number

print('enter several numbers with spaces')
print(minmax(input().split()))
input('press ENTER to exit')





