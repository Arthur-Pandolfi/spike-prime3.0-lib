from typing import Awaitable, Callable


def run(functions: Awaitable) -> None:
    """
    run(*functions: Awaitable) -> None

    Inicie todas as funções async paralelas que desejar. Essa é a função a ser usada para criar programas com uma estrutura similar a dos Blocos de Palavras.

    Parâmetros
    *functions: awaitable
    The functions to run
    """
    pass

def sleep_ms(duration: int) -> Awaitable:
    """
    sleep_ms(duration: int) -> Awaitable

    Pausa a execução do aplicativo por qualquer número de milissegundos.

    Parâmetros
    duration: int
    Duração em milissegundos
    """
    pass

def until(function: Callable[[], bool], timeout: int = 0) -> Awaitable:
    """
    until(function: Callable[[], bool], timeout: int = 0) -> Awaitable

    Devolve um aguardável que será devolvido quando a condição na função ou no lambda passado for True ou quando o tempo limite for alcançado.

    Parâmetros
    function: Callable[[], bool]
    Um chamável sem parâmetros que devolve True ou False.
    Chamável é qualquer coisa que pode ser chamada, como def ou lambda

    timeout: int
    Tempo limite (em milissegundos) para a função.
    Se o chamável não devolver True dentro do tempo limite, until ainda será resolvido após o tempo limite.
    0 significa que não há tempo limite; nesse caso, ele não será resolvido até que o chamável devolva True.
    """
    pass