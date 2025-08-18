limit = int(input("identif all primes up to what limit? "))
nums = []
for i in range(0, limit + 1):
    nums.append(i)

nums[1] = 0
p = 2
while p< limit:
    for i in range(p*2, limit + 1, p):
        nums[i] = 0
    p = p + 1
    while p < limit and nums[p] == 0:
        p = p + 1

print("The primes up to", limit, "are: ")
for i in nums:
    if nums[i] != 0:
        print(i) 