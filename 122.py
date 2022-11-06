# a = 5
# b = input(('B '))
# print(a / b)

# print('Start')
# try:
#     print(a / int(b))
# except ZeroDivisionError:
#     print('Деление на 0')
# except (ZeroDivisionError, ValueError, TypeError) as error:
#     print(error,'Вы ввели буквы')
# else:
#     print('Else')
# finally:
#     print('Finally')
# print('ok')

# def checker(var_1):
#         if type(var_1) != str:
#             raise TypeError(f"Sorry, we can't work with {type(var_1)}, we need class str")
#         else:
#             return var_1
#
# first_var = 10
# first_var = [1,2,3]
# print(checker(first_var))

# class BuildingError(Exception):
#     def __str__(self):
#         return f"With so much material the house can't be build"
#
# def check_material(amount_materials, material):
#     if amount_materials > material:
#         print('ok')
#         return 'enough material'
#     else:
#         raise BuildingError(amount_materials)
# material = 120
# check_material(material,300)


# lst = [1,2,3,4,5]
# for i in lst:
#     print(i)
# s = 'qwert'
# for i in s:
#     print(i)

lst = [1,2,3,4,5]
iterator = iter(lst)
print(iterator)
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# for i in iterator:
#     print(i)
# while True:
#     try:
#         print(iterator.__next__())
#     except StopIteration:
#         break

# class Counter:
#
#     def __init__(self, max_number):
#         self.i = 0
#         self.max_number = max_number
#
#     def __iter__(self):
#         self.i = 0
#         return self
#
#     def __next__(self):
#         self.i += 1
#         if self.i > self.max_number:
#             raise StopIteration
#         return self.i
#
# count = Counter(10)

# for elem in count:
#     print(elem)

# print(count.__iter__())
# print(count.__next__())
# print(count.__next__())
# print(count.__next__())

# def raise_to_the_degrees(number):
#     i = 0
#     while True:
#         result = number ** i
#         yield  result
#         if result > 10000:
#             return
#         i +=1
#
# res = raise_to_the_degrees(2)
# for _ in res:
#     print(_)

def cheker(function):

    def cheker(*args, **kwargs):
        try:
            result = function(*args, **kwargs)
        except Exception as exc:
            print(f'We have problems{exc}')
        else:
            print(f'No problems.Result = {result}')
    return cheker

def calculate():
    print(eval('2+2'))

calculate = cheker(calculate())
#calculate()





