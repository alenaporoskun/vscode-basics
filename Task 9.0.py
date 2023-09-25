
def main():

    print(complicated(14,2))

    print('-'*10)

    some_str = 'aaAbbB C F DDd EEe'
    for i in filter(lambda x: x.isupper(), some_str):
        print(i)

    print('-'*10)

    for i in filter(lambda x: x % 2, range(1, 10+1)):
        print(i)



def logged_func(func):
    def inner(x, y):
        print(f'called with {x}, {y}')
        result = func(x, y)
        print(f'result: {result}')
        return result
    return inner


@logged_func
def complicated(x, y):
    return x / y


if __name__ == "__main__":
    main()

# def complicated(x, y):
#     return x / y


# def logged_func(func):
#     def inner(x, y):
#         print(f'called with {x}, {y}')
#         result = func(x, y)
#         print(f'result: {result}')
#         return result
#     return inner


# complicated = logged_func(complicated)