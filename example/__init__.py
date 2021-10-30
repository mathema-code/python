from typing import ChainMap
import check50

@check50.check()
def exists():
    """Verificando se existe o arquivo hello.py"""
    check50.exists('hello.py')


@check50.check()
def imprime_algo():
    """"""
    actual = check50.run("python3 hello.py").stdout()
    if not actual:
        help = 'parece que seu programa nao printa nada, você está invocando usa função?'
    raise check50.Mismatch(help=help)

@check50.check(exists)
def prints_hello():
    """printar "hello, world\\n" """
    from re import match

    expected = "[Hh]ello, world!?\n"
    actual = check50.run("python3 hello.py").stdout()
    if not match(expected, actual):
        help = 'verifique se você escreveu "hello, world!?\\n" corretamente.'
        if match(expected[:-1], actual):
            help = r"did you forget a newline ('\n') at the end of your printf string?"
        raise check50.Mismatch("hello, world\n", actual, help=help)
