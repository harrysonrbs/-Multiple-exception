# Exceções -  Python
Tratando exceções (TraceBack - Erros)

O Python fornece uma forma para específicarmos um conjunto de exceções na qual desejamos disponibilizar uma mesma solução.

Não raramente poderíamos ter problemas diferentes que podem ser resolvidos com uma mesma solução.

    try:
        ...         ->  código que por alguma razão possa levantar uma exceção.

    except ErroClass1:
        ...         ->  Se há exceção "ErroCLass1", execute essa instrução.

    except (ErroClass2, ErroClass3):
        ...         ->  Se há exceção "ErroCLass2" ou "ErroClass3", execute essa instrução.


     Se não houve exceções, o cursor de execução passará por cima de todos os blocos "except".
