"""
EXCEÇÕES
    BLOCO ELSE

    Mostrarei o funcionamento do bloco 'else' quando implementado em uma estrutura de tratamento de "exceções".

    A subestrutura ("else") de 'try' será executada quando não houverem exceções levantadas.



    ** Entrada em "else" **

    Quando nenhuma exceção é levantada no bloco "try", o cursor de execução passará por cima do bloco "except",
    iniciará a execução do bloco "else" e continuará com a execução da aplicação.

    try:
        ... nunhuma exceção levantada
        ...
    except ErrorClass:
        ... o cursor pulará o bloco "except"
        ...
    else:
        ... execução do bloco "else" será INICIADA
        ...



    ** Salto de "else" ***

    Quando uma exceção é levantada no bloco "try", o cursor iniciará a execução do bloco "except" para tratativa da
    mesma, dessa forma, o cursor pulará o bloco "else" e continuará com a execução da aplicação.

    try:
        ...
        ... xx exceção levantada
    except ErrorClass:
        ... execução do bloco "except" será iniciada
        ...
    else:
        ... o cursor pulará o bloco "else"
        ...



    ** Aplicação Interrompida **

    Quando uma exceção é levantada no bloco "try", o Python verificará se há uma tratativa da mesma em "except".
    Se não houver, a aplicação será interrompida.

        try:
        ...
        ...xx exceção
    except ErrorClass:
        ... não possui tratativa, logo a aplicação será INTERROMPIDA.
        ...
    else:
        ...
        ...


    O BLOCO "ELSE" SÓ SERÁ EXECUTADO CASO O BLOCO DE INSTRUÇÕES "TRY" NÃO LEVANTE EXCEÇÃO.

"""


def error(x):
    try:
        eval(x)
    except ZeroDivisionError as e:
        print(e)
        print(e.args)
        print("impossível dividir números por zero.")
    else:
        print("Nenhuma exceção levantada no bloco 'try', logo a execução do bloco de 'else' é iniciada e concluída. ")


error("10 + 10")
