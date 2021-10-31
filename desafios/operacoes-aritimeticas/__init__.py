import check50

arquivo = 'operacoes.py'

def mismatch(expect, actual, help):
    return check50.Failure(fr'esperávamos "{expect}", e não "{actual}"', help=help)

@check50.check()
def exists():
    f"""Verificando se existe o arquivo {arquivo}.py"""
    check50.exists(arquivo)
    check50.log(f"Parabéns o arquivo {arquivo} foi criado com sucesso!")


@check50.check(exists)
def imprime_algo():
    """Verificando seu stdout"""
    actual = check50.run(f"python3 {arquivo}").stdin('5').stdout()
    check50.log('')
    check50.log('abaixo é o print do seu programa')
    check50.log(actual)

@check50.check(imprime_algo)
def prints_hello():
    """Verificando se as operações fornecem o resuldado correto"""

    check50.run(f"python3 {arquivo}").stdin("foo").stdout("foo")