all_nums = list(range(2,21))
ans = 1

while all_nums:
     head = all_nums[0]
     for i,j in enumerate(all_nums):
         if j % head == 0:
             all_nums[i] //= head
     all_nums = list(filter(lambda x: x != 1,all_nums))
     ans *= head
print(ans)
