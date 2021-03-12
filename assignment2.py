def calculate(min, max):
    sum = 0
    n = min
    while n <= max:
        sum = sum + n
        n = n + 1
    print(sum)

calculate(1, 3)# 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8)# 你的程式要能夠計算 4+5+6+7+8，最後印出 30

def avg(data):
    sum = 0
    result = 0
    count = data["count"]   
    for item in data["employees"]:
      sum = sum + item["salary"]             
    result = sum / count

    print(result)

avg({
     "count":3,
     "employees":[
        {
         "name":"John",
         "salary":30000
        },
        {
         "name":"Bob",
        "salary":60000
        },
        {
         "name":"Jenny",
         "salary":50000
     }
     ]
}) # 呼叫 avg 函式

def maxProduct(nums):
  product = []
  for i in range(len(nums)-1):
    for j in range(i+1, len(nums)):
        product.append(nums[i]*nums[j])
  return max(product)
    
print(maxProduct([5,20,2,6]))
print(maxProduct([10,-20,0,3]))


def twoSum(nums, target):
  Sum = []
  for i in range(len(nums)-1):
    for j in range(i+1, len(nums)):
      if nums[i]+nums[j]== target:
        Sum.append(i)
        Sum.append(j)
        break
  return Sum

result = twoSum([2,11,7,15],9)
print(result)

    