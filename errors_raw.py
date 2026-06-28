try:
    print(1)
    raise Exception('error')
except Exception as exec:
    print('tratamento')
    print(exec)
