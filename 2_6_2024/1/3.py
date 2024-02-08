import builtins

# Lọc ra các biến là hàm từ module builtins
functions = filter(lambda x: callable(getattr(builtins, x)), dir(builtins))

# In ra tất cả các hàm
for function in functions:
    print(function)
print(help(ascii()))