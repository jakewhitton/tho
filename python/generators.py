def g():
    yield 1
    yield 2
    yield 3

a = g()
arr = [1, 3, 5, 6, 7]
arr_iter = iter(arr)
print(f'arr_iter = {arr_iter}')
print(f'next(arr_iter) = {next(arr_iter)}')
print(f'next(arr_iter) = {next(arr_iter)}')
i = iter(arr_iter)
print('yes' if i is arr_iter else 'no')
print(f'i = iter({arr_iter}) = {i}')
print(f'next(i) = {next(i)}')
print(f'next(i) = {next(i)}')
print(f'next(arr_iter) = {next(arr_iter)}')


# import pdb; pdb.set_trace()