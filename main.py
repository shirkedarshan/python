try:
    f = open('testfile.txt')
    f = oo
    # if f.name == 'testfile.txt':
    #     raise Exception
    pass
except FileNotFoundError:
    print('Sorry, This file does not exist')
    pass
except Exception:
    print('Something went wrong')
else:
    print(f.read())
    f.close()
    pass
finally:
    print("Finally block huh")
    pass