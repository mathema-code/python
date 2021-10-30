import check50

@check50.check()
def exists():
    """Verificando se existe o arquivo hello.py"""
    check50.exists('hello.py')

@check50.check(exists)
def hello_world():
    """imprimindo "hello world" \n"""
    check50.run("python3 hello.py").stdout("Hello, world!", regex=False).exit(0)