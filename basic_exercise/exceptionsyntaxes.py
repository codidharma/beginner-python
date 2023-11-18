import traceback


try:
    i = int(input('Enter a number'))
    print(i)
    print( i + '1')

except Exception as e:
    print(type(e))
    print(e.__cause__)
    print(traceback.format_exception(type(e), e, e.__traceback__))
