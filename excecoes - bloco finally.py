"""
EXCEÇÕES
    BLOCO FINALLY

    Mostrarei o funcionamento do "bloco finally" quando implementado em uma estrutura de tratamento de "exceções".

    Uma subestrutura de ("finally") "try", que sempre indiferente do que aconteça, terá seu bloco de código executado.

    O "bloco finally" permite a execução de códigos nas piores situações.

    É nesse trecho de código que temos a certeza que sempre indiferente do que aconteça será executado.

    Também nesse "bloco" em que fecharemos algum arquivo aberto ou então alguma conexão de rede ou internet que esteja
    em adamento.

    Se um exceção for ou não levantada, o bloco definido após a instrução "finally" sempre, em qualquer situação será
    executado. Dessa forma conseguimos implementar códigos que serão executados em todas as situações.



    ENTRADA

    try:
        ...
        ... Se não levantar nenhuma exceção, o cursor pulará o bloco "except"
    except ErrorClass:
        ...
        ...
    finally:
        ... todas as instruções do bloco "finally" serão executadas indiferente do que aconteça.
        ...



    SALTO

    try:
        ...xx Exceção levantada, o cursor logo pulará para o bloco "except".
        ...
    except ErrorClass:
        ... Instrução "except" captura a exceção, e o cursor executará as instruções bloco "except".
        ...
    finally:
        ... todas as instruções do bloco "finally" serão executadas indiferente do que aconteça.
        ...



    INTERRUPÇÃO

    try:
        ...xx Exceção levantada, o cursor logo pulará para o bloco "except".
        ...
    except ErrorClass:
        ... Se não houver tratamento no bloco "except", a aplicação em tese será finalida. O cursor pulará para o bloco finally.
        ...
    finally:
        ... todas as instruções do bloco "finally" serão executadas indiferente do que aconteça.
        ...

"""


def error(x):
    try:
        eval(x)
    except (ZeroDivisionError, TypeError) as e:
        print(type(e))
    except NameError as e:
        print(type(e))
    else:
        print("Se não houver exceção, essa instrução será executada.")
    finally:
        print("Indiferente do que aconteça, essa instrução será executada.")


error("10 / 0")

error("int + int")

error("a")

error("10 * 10")



