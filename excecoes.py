"""
114 TRATAMENTO DE EXCEÇÕES MÚLTIPLAS II

Vamos dar continuidade ao estudo do tratamento de exceções múltiplas.

    "Diferentes tratamento para diferentes problemas".

    Não raramente poderíamos ter problemas diferentes que podem ser resolvidos com uma mesma solução.

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
    except (TypeError, NameError): # Se TypeError ocorrer ou NameError ocorrer, execute a tratativa do bloco "except".
        print("TypeError ocorreu, ou NameError ocorreu.")
    except ValueError:
        print("ValueError")
    except ZeroDivisionError:
        print("ZeroDivisionError")


erro('int+int')

erro('a')

erro("int('a')")

erro('10 / 0')

erro('5 / 5')





def error(a):
    try:
        eval(a)
    except (TypeError, NameError, ZeroDivisionError, ValueError):
        print("A Exceção TypeError ou NameError ou ZeroDivisionError foi levantada.")

error("str+str") # TypeError

error("zzz") # NameError

error("10 / 0") # ZeroDivisionError

error("int('b')") # ValueError









def error1(a):
    try:
        a = 10 / 0
        print(a)
    except ZeroDivisionError:
        print("ZeroDivisionError ocorreu aqui!!!")



error1(0)


