import my_package



funcs = [e for e in dir(my_package) if not e.startswith('_')]
for index , func in enumerate(funcs):
    print(f"{index:>3}: {func}")

