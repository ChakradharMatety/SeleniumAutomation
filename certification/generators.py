# def my_generator():
#     print("First Yield")
#     yield 10
#     print("Second Yield")
#     yield 20
#     print("Third Yield")
#     yield 30
#
#
# gen = my_generator()
# while True:
#     try:
#         print(next(gen))
#     except StopIteration:
#         break
#
#
# def get_seq(x):
#     for i in range(x):
#         yield i
#
#
# gen = get_seq(10)
# while True:
#     try:
#         print(next(gen))
#     except StopIteration:
#         break


def fibo_naci(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a + b


gen = fibo_naci(15)
while True:
    try:
        print(next(gen))
    except StopIteration:
        break

