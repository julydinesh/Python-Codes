

# def fun(**argv):
#     for k, val in argv.items():
#         print("%s == %s" % (k, val))

# fun(Hello=4, Welcome=9)

numbers = [1, 2, 3, 4, 5]
e = 98

def get(t:int=len(numbers)):
    # e=9
    print(t)
    print(f"Is 't' in locals()? {'t' in locals()}")
    print(numbers.pop())

print(get())
print(f"Is 'e' in globals()? {'e' in globals()}")
print(globals())
print(locals())

