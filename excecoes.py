"""
TRATAMENTO DE EXCEÇÕES MÚLTIPLAS

    O Python fornece uma forma para específicarmos um conjunto de exceções na qual desejamos disponibilizar uma mesma
    solução.

    Nós iremos agrupar as mensagens de erro que podem ser obtidas de uma mesma forma numa mesma estrutura "except".

    Não raramente poderíamos ter problemas diferentes que podem ser resolvidos com uma mesma solução.

    try:
        ...         ->  código que por alguma razão possa levantar uma exceção.

    except ErroClass1:
        ...         ->  Se há exceção "ErroCLass1", execute essa instrução.

    except (ErroClass2, ErroClass3):
        ...         ->  Se há exceção "ErroCLass2" ou "ErroClass3", execute essa instrução.


        Se não houve exceções, o cursor de execução passará por cima de todos os blocos "except".
"""

def erro(x):
    try:
        eval(x)
    except (TypeError, NameError):
        print("TypeError ou NameError ocorreu.")
    except ValueError:
        print("ValueError")
    except ZeroDivisionError:
        print("ZeroDivisionError")
        
erro('int+int')

erro('a')

erro("int('a')")

erro('10 / 0')

erro('5 / 5')

