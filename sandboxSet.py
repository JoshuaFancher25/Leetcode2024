# for sets we don't have duplicates
# sets are great for checking if something has been visited
# Thus lets call sets vis - visited
vis = set()

nums = [1,1,1,2,2,2,3,4,5,10,10,10,11]
for num in nums:
    vis.add(num)
print(vis)

# we can call a set seen
seen = set()
for num in nums:
    seen.add(num)
print(seen)