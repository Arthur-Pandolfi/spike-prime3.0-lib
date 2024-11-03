from typing import Awaitable

# Constantes
READY = 1
RUNNING = 2
STALLED = -1
CANCELED = -2
ERROR = -3
DISCONNECTED = 0
COAST = 1
BRAKE = 2
HOLD = 3
CONTINUE = 0
SMART_COAST = 4
SMART_BRAKE = 5
CLOCKWISE = 0
COUNTERCLOCKWISE = 1
SHORTEST_PATH = 2
LONGEST_PATH = 3

def absolute_position(port:int) -> int:
    """
    absolute_position(port: int) -> int

    Obtém a posição absoluta de um motor.

    Parâmetros
    port: int
    Uma porta do submódulo port no módulo hub.
    """
    pass

def get_duty_cycle(port:int) -> int:
    """
    get_duty_cycle(port: int) -> int

    Obtém o valor de PWM de um motor.

    Parâmetros
    port: int
    Uma porta do submódulo port no módulo hub.
    """
    pass

def relative_position(port:int) -> int:
    """
    relative_position(port: int) -> int

    Obtém a posição relativa de um motor.

    Parâmetros
    port: int
    Uma porta do submódulo port no módulo hub.
    """
    pass

def reset_relative_position(port:int, position:int) -> None:
    """
    reset_relative_position(port: int, position: int) -> None

    Altera a posição usada como deslocamento ao usar a função run_to_relative_position.

    Parâmetros
    port: int
    Uma porta do submódulo port no módulo hub.

    position: int
    O grau do motor.
    """
    pass

def run(port:int, velocity:int, acceleration:int = 1000):
    """
    run(port: int, velocity: int, *, acceleration: int = 1000) -> None

    Gira um motor a uma velocidade constante.

    Parâmetros
    port: int
    Uma porta do submódulo port no módulo hub.

    velocity: int
    A velocidade em graus/seg

    Os intervalos de valor dependem do tipo de motor.

    Motor pequeno (Essential): -660 a 660
    Motor Médio: -1110 a 1110
    Motor grande: -1050 a 1050

    Argumentos de palavra reservada opcionais:
    acceleration: int
    A aceleração (grau/s²) (0 - 10000).
    """
    pass

def run_for_degrees(port: int, degrees: int, velocity: int, stop: int = BRAKE, acceleration: int = 1000, deceleration: int = 1000) -> Awaitable:
    """
    run_for_degrees(port: int, degrees: int, velocity: int, *, stop: int = BRAKE, acceleration: int = 1000, deceleration: int = 1000) -> Awaitable

    Gira um motor por um número específico de graus.
    Quando "aguardado" devolve um status do movimento que corresponde a uma das seguintes constantes:

    motor.READY
    motor.RUNNING
    motor.STALLED
    motor.CANCELED
    motor.ERROR
    motor.DISCONNECTED

    Parâmetros
    port: int
    Uma porta do submódulo port no módulo hub.

    degrees: int
    O número de graus.

    velocity: int
    A velocidade em graus/seg

    Os intervalos de valor dependem do tipo de motor.

    Motor pequeno (Essential): -660 a 660
    Motor Médio: -1110 a 1110
    Motor grande: -1050 a 1050

    Argumentos de palavra reservada opcionais:
    stop: int
    O comportamento do Motor depois de parar. Use as constantes no módulo motor.

    Os valores possíveis são:
    motor.COAST para liberar o motor até uma parada.
    motor.BREAK para frear e continuar a frear após a parada.
    motor.HOLD para orientar o motor a manter sua posição.
    motor.CONTINUE para orientar o motor a continuar girando na velocidade atual até receber outro comando.
    motor.SMART_COAST para frear o motor até parar e, depois, liberá-lo e compensar imprecisões no próximo comando.
    motor.SMART_BRAKE para frear o motor, continuar freando até parar e então compensar imprecisões no próximo comando.

    acceleration: int
    A aceleração (grau/s²) (0 - 10000).

    deceleration: int
    A desaceleração (grau/s²), no intervalo (0 - 10000).
    """
    pass

def run_for_time(port: int, duration: int, velocity: int, *, stop: int = BRAKE, acceleration: int = 1000, deceleration: int = 1000) -> Awaitable:
    """
    Gira um Motor por um período limitado.
    Quando "aguardado" devolve um status do movimento que corresponde a uma das seguintes constantes:

    motor.READY
    motor.RUNNING
    motor.STALLED
    motor.ERROR
    motor.DISCONNECTED


    from hub import port
    import runloop
    import motor

    async def main():
        # Gire o motor a velocidade 1000 por 1 segundo.
        await motor.run_for_time(port.A, 1000, 1000)

        # Gire o motor a velocidade 280 por 1 segundo.
        await motor_pair.run_for_time(port.A, 1000, 280)

        # Gire o motor a velocidade 280 por 10 segundos com desaceleração lenta.
        await motor_pair.run_for_time(port.A, 10000, 280, deceleration=10)

    runloop.run(main())
    Parâmetros
    port: int
    Uma porta do submódulo port no módulo hub.

    duration: int
    Duração em milissegundos

    velocity: int
    A velocidade em graus/seg

    Os intervalos de valor dependem do tipo de motor.

    Motor pequeno (Essential): -660 a 660
    Motor Médio: -1110 a 1110
    Motor grande: -1050 a 1050

    Argumentos de palavra reservada opcionais:
    stop: int
    O comportamento do Motor depois de parar. Use as constantes no módulo motor.

    Os valores possíveis são:
    motor.COAST para liberar o motor até uma parada.
    motor.BREAK para frear e continuar a frear após a parada.
    motor.HOLD para orientar o motor a manter sua posição.
    motor.CONTINUE para orientar o motor a continuar girando na velocidade atual até receber outro comando.
    motor.SMART_COAST para frear o motor até parar e, depois, liberá-lo e compensar imprecisões no próximo comando.
    motor.SMART_BRAKE para frear o motor, continuar freando até parar e então compensar imprecisões no próximo comando.

    acceleration: int
    A aceleração (grau/s²) (0 - 10000).

    deceleration: int
    A desaceleração (grau/s²), no intervalo (0 - 10000).
    """
    pass

def run_to_absolute_position(port: int, position: int, velocity: int, *, direction: int, stop: int = BRAKE, acceleration: int = 1000, deceleration: int = 1000) -> Awaitable:
    """
    Gira o motor para uma posição absoluta.
    Quando "aguardado" devolve um status do movimento que corresponde a uma das seguintes constantes:

    motor.READY
    motor.RUNNING
    motor.STALLED
    motor.CANCELED
    motor.ERROR
    motor.DISCONNECTED

    Parâmetros
    port: int
    Uma porta do submódulo port no módulo hub.

    position: int
    O grau do motor.

    velocity: int
    A velocidade em graus/seg

    Os intervalos de valor dependem do tipo de motor.

    Motor pequeno (Essential): -660 a 660
    Motor Médio: -1110 a 1110
    Motor grande: -1050 a 1050

    Argumentos de palavra reservada opcionais:
    direction: int
    A direção do giro.
    As opções são:

    motor.CLOCKWISE
    motor.COUNTERCLOCKWISE
    motor.SHORTEST_PATH
    motor.LONGEST_PATH

    stop: int
    O comportamento do Motor depois de parar. Use as constantes no módulo motor.

    Os valores possíveis são:
    motor.COAST para liberar o motor até uma parada.
    motor.BREAK para frear e continuar a frear após a parada.
    motor.HOLD para orientar o motor a manter sua posição.
    motor.CONTINUE para orientar o motor a continuar girando na velocidade atual até receber outro comando.
    motor.SMART_COAST para frear o motor até parar e, depois, liberá-lo e compensar imprecisões no próximo comando.
    motor.SMART_BRAKE para frear o motor, continuar freando até parar e então compensar imprecisões no próximo comando.

    acceleration: int
    A aceleração (grau/s²) (0 - 10000).

    deceleration: int
    A desaceleração (grau/s²), no intervalo (0 - 10000).
    """
    pass

def run_to_relative_position(port: int, position: int, velocity: int, *, stop: int = BRAKE, acceleration: int = 1000, deceleration: int = 1000) -> Awaitable:
    """
    run_to_relative_position(port: int, position: int, velocity: int, *, stop: int = BRAKE, acceleration: int = 1000, deceleration: int = 1000) -> Awaitable

    Gira um motor para uma posição relativa à atual.
    Quando "aguardado" devolve um status do movimento que corresponde a uma das seguintes constantes:

    motor.READY
    motor.RUNNING
    motor.STALLED
    motor.CANCELED
    motor.ERROR
    motor.DISCONNECTED

    Parâmetros
    port: int
    Uma porta do submódulo port no módulo hub.

    position: int
    O grau do motor.

    velocity: int
    A velocidade em graus/seg

    Os intervalos de valor dependem do tipo de motor.

    Motor pequeno (Essential): -660 a 660
    Motor Médio: -1110 a 1110
    Motor grande: -1050 a 1050

    Argumentos de palavra reservada opcionais:
    stop: int
    O comportamento do Motor depois de parar. Use as constantes no módulo motor.

    Os valores possíveis são:
    motor.COAST para liberar o motor até uma parada.
    motor.BREAK para frear e continuar a frear após a parada.
    motor.HOLD para orientar o motor a manter sua posição.
    motor.CONTINUE para orientar o motor a continuar girando na velocidade atual até receber outro comando.
    motor.SMART_COAST para frear o motor até parar e, depois, liberá-lo e compensar imprecisões no próximo comando.
    motor.SMART_BRAKE para frear o motor, continuar freando até parar e então compensar imprecisões no próximo comando.

    acceleration: int
    A aceleração (grau/s²) (0 - 10000).

    deceleration: int
    A desaceleração (grau/s²), no intervalo (0 - 10000).
    """
    pass

def set_duty_cycle(port: int, pwm: int) -> None:
    """
    set_duty_cycle(port: int, pwm: int) -> None

    Gira um motor a um PWM específico.

    Parâmetros
    port: int
    Uma porta do submódulo port no módulo hub.

    pwm: int
    O valor de PWM, no intervalo (-10000-10000)
    """
    pass

def stop(port: int, *, stop: int = BRAKE) -> None:
    """
    stop(port: int, *, stop: int = BRAKE) -> None

    Para um motor.

    Parâmetros
    port: int
    Uma porta do submódulo port no módulo hub.

    Argumentos de palavra reservada opcionais:
    stop: int
    O comportamento do Motor depois de parar. Use as constantes no módulo motor.

    Os valores possíveis são:
    motor.COAST para liberar o motor até uma parada.
    motor.BREAK para frear e continuar a frear após a parada.
    motor.HOLD para orientar o motor a manter sua posição.
    motor.CONTINUE para orientar o motor a continuar girando na velocidade atual até receber outro comando.
    motor.SMART_COAST para frear o motor até parar e, depois, liberá-lo e compensar imprecisões no próximo comando.
    motor.SMART_BRAKE para frear o motor, continuar freando até parar e então compensar imprecisões no próximo comando.
    """
    pass

def velocity(port:int) -> int:
    """
    velocity(port: int) -> int

    Obtém a velocidade (grau/s) de um Motor.

    Parâmetros
    port: int
    Uma porta do submódulo port no módulo hub.
    """
    pass
