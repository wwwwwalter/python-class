try:
    s_age = input("input:")
    age = int(s_age)
    assert 20 < age < 80, "age error"
    print("age currect")
except ArithmeticError as e:
    print("ArithmeticError:", e)
