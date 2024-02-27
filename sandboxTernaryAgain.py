# learning ternary operators in python
# dont' really like ternary --- feel like it makes code more confusing but
# it does make the code more succinct so why not lets learn it \
x = 10
val = "true" if x > 10 else "false"
print(val)

print("something" if False else "no")

# essentially we have the return value listed first
# if the expression to evaluate is true then return the first value
# otherwise return the value specified in the else statement.

z = 20
a = 100 if z > 20 else 5000
print(a)