import check50

@check50.check()
def exists():
    """Verificando se existe o arquivo hello.py"""
    check50.exists('hello.py')

@check50.check(exists)
def hello_world():
    """imprimindo "hello world" \n"""
    check50.run("python3 hello.py").stdout("Hello, world!", regex=False).exit(0)


@check50.check()
def prints_hello():
    """prints "hello, world\\n" """
    from re import match

    expected = "[Hh]ello, world!?\n"
    actual = check50.run("python3 hello.py").stdout()
    if not match(expected, actual):
        help = 'nao foi printado o esperado'
        if match(expected[:-1], actual):
            help = r"did you forget a newline ('\n') at the end of your printf string?"
        raise check50.Mismatch("hello, world\n", actual, help=help)