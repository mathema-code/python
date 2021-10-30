import check50

def mismatch(expect, actual, help):
    return check50.Failure(fr'esperávamos {expect}, e não {actual}', help=help)

@check50.check()
def exists():
    """Verificando se existe o arquivo ola.py"""
    check50.exists('ola.py')


@check50.check(exists)
def imprime_algo():
    """Verificando se sua função imprime algum resultado"""
    actual = check50.run("python3 hello.py").stdout()
    help = 'parece que seu programa nao printa nada, você está invocando usa função?'
    if not actual:
        raise check50.Failure('esperávamos outro resultado', help=help)

@check50.check(imprime_algo)
def prints_hello():
    """printar "olá, mundo!" """
    from re import match

    expected = "[Oo]lá, mundo!"
    actual = check50.run("python3 hello.py").stdout()
    if not match(expected, actual):
        help = 'verifique se você escreveu "olá, mundo" corretamente.'
        if match(expected[:-1], actual):
            help = r"Você esqueceu uma nova linha ('\n') no final da sua string?"
        raise mismatch(repr('olá, mundo!'), repr(actual), help=help)
        # raise check50.Mismatch("hello, world\n", actual, help=help)n
