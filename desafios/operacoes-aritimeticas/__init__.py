import check50

arquivo = 'operacoes.py'

def mismatch(expect, actual, help):
    return check50.Failure(fr'esperávamos "{expect}", e não "{actual}"', help=help)

@check50.check()
def exists():
    """Verificando se existe o arquivo ola.py"""
    check50.exists(arquivo)


@check50.check(exists)
def imprime_algo():
    """Verificando se sua função imprime algum resultado"""
    actual = check50.run(f"python3 {arquivo}").stdin().stdout()
    help = 'parece que seu programa nao printa nada, você está invocando usa função?'
    if not actual:
        raise check50.Failure('esperávamos outro resultado', help=help)

@check50.check(imprime_algo)
def prints_hello():
    """Verificando se as operações fornecem o resuldado correto"""

    check50.run(f"python3 {arquivo}").stdin("foo").stdout("foo").stdin("bar").stdout("bar")