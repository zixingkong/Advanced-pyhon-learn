def fun():
    yield 1
    yield 2
    yield 3


gen_list = [fun(), fun(), fun()]

while True:
    for gen in gen_list:
        print(next(gen))
