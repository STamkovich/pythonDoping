def function_python():
    a = 5
    type(a)
    b = 2.0
    type(b)
    c = 1 + 2j
    type(c)
    e = [1, 2.2, 'python']
    type(e)
    f = (5, 'program', 1 + 3j)
    type(f)
    g = "Простая строка"
    type(g)
    k = {1, 2, 3, 4, 5}
    type(k)
    my_dict = {"int": a,
               "flout": b,
               "complex": c,
               "list": e,
               "tuple": f,
               "str": g,
               "set": k}

    for key, value in my_dict.items():
        print("Ключь: " + str(key) + " / значение: " + str(value))


print(function_python())