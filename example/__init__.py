import check50

def mismatch(expect, actual, help):
    return f'esperávamos "{expect}", e não "{actual}" \n{help}'

@check50.check()
def exists():
    """Verificando se existe o arquivo hello.py"""
    check50.exists('hello.py')


@check50.check()
def imprime_algo():
    """Verificando se sua função imprime algum resultado"""
    actual = check50.run("python3 hello.py").stdout()
    help = 'parece que seu programa nao printa nada, você está invocando usa função?'
    if not actual:
        raise check50.Failure('esperávamos outro resultado', help=help)

@check50.check(exists)
def prints_hello():
    """printar "hello, world\\n" """
    from re import match

    expected = "[Hh]ello, world!?\n"
    actual = check50.run("python3 hello.py").stdout()
    if not match(expected, actual):
        help = 'verifique se você escreveu "hello, world!?\\n" corretamente.'
        if match(expected[:-1], actual):
            help = r"Você esqueceu uma nova linha ('\n') no final da sua string?"
        raise mismatch("hello, world\n", actual, help=help)
        # raise check50.Mismatch("hello, world\n", actual, help=help)
