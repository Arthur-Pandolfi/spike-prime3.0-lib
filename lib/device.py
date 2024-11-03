def data(port:int) -> tuple[int]:
    """
    data(port: int) -> tuple[int]

    Recupera os dados brutos de LPF-2 de um dispositivo.

    Parâmetros
    port: int
    Uma porta do submódulo port no módulo hub
        """
    pass
def device_id(port:int) -> int:
    """
    device_id(port: int) -> int

    Recupere o ID de um dispositivo. Cada dispositivo tem um ID com base no tipo.

    Parâmetros
    port: int
    Uma porta do submódulo port no módulo hub.
    """
    pass
def get_duty_cycle(port:int) -> int:
    """
    get_duty_cycle(port: int) -> int

    Recupera o ciclo de trabalho de um dispositivo. Os valores devolvidos estão no intervalo de 0 a 10000.

    Parâmetros
    port: int
    Uma porta do submódulo port no módulo hub.
    """
    pass
def ready(port:int) -> int:
    """
    ready(port: int) -> bool

    Após ser conectado ao Hub, o dispositivo pode precisar de um breve momento para começar a aceitar solicitações.
    Use ready para testar a prontidão dos dispositivos conectados.

    Parâmetros
    port: int
    Uma porta do submódulo port no módulo hub."""
    pass
def set_duty_cycle(port:int) -> int:
    """
    set_duty_cycle(port: int, duty_cycle: int) -> None

    Define o ciclo de trabalho em um dispositivo. Intervalo de 0 a 10000.

    Parâmetros
    port: int
    Uma porta do submódulo port no módulo hub.

    duty_cycle: int
    O valor de PWM, no intervalo (0-10000)
    """
