from typing import  Awaitable
import motor

# Constantes
PAIR_1 = 0
PAIR_2 = 1
PAIR_3 = 2

def move(pair: int, steering: int, *, velocity: int = 360, acceleration: int = 1000) -> None:
    """
    move(pair: int, steering: int, *, velocity: int = 360, acceleration: int = 1000) -> None

    Gire um Par de Motores a uma velocidade constante até ser dado um novo comando.

    Parâmetros
    pair: int
    O slot do Par de Motores.

    steering: int
    A direção (-100 a 100).

    Argumentos de palavra reservada opcionais:
    velocity: int
    A velocidade em graus/seg

    Os intervalos de valor dependem do tipo de motor.

    Motor pequeno (Essential): -660 a 660
    Motor Médio: -1110 a 1110
    Motor grande: -1050 a 1050

    acceleration: int
    A aceleração (grau/s²) (0 - 10000).
    """
    pass

def move_for_degrees(pair: int, degrees: int, steering: int, *, velocity: int = 360, stop: int = motor.BRAKE, acceleration: int = 1000, deceleration: int = 1000) -> Awaitable:
    """
    move_for_degrees(pair: int, degrees: int, steering: int, *, velocity: int = 360, stop: int = motor.BRAKE, acceleration: int = 1000, deceleration: int = 1000) -> Awaitable

    Gire um Par de Motores a uma velocidade constante por um número específico de graus.
    Quando "aguardado" devolve um status do movimento que corresponde a uma das seguintes constantes do módulo do motor:

    motor.READY
    motor.RUNNING
    motor.STALLED
    motor.CANCELED
    motor.ERROR
    motor.DISCONNECTED

    Parâmetros
    pair: int
    O slot do Par de Motores.

    degrees: int
    O número de graus.

    steering: int
    A direção (-100 a 100).

    Argumentos de palavra reservada opcionais:
    velocity: int
    A velocidade em graus/seg

    Os intervalos de valor dependem do tipo de motor.

    Motor pequeno (Essential): -660 a 660
    Motor Médio: -1110 a 1110
    Motor grande: -1050 a 1050

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

def move_tank_for_degrees(pair: int, degrees: int, left_velocity: int, right_velocity: int, *, stop: int = motor.BRAKE, acceleration: int = 1000, deceleration: int = 1000) -> Awaitable:
    """
    move_tank_for_degrees(pair: int, degrees: int, left_velocity: int, right_velocity: int, *, stop: int = motor.BRAKE, acceleration: int = 1000, deceleration: int = 1000) -> Awaitable

    Faça um Par de Motores realizar um movimento de tanque a uma velocidade constante até ser dado um novo comando.
    Quando "aguardado" devolve um status do movimento que corresponde a uma das seguintes constantes do módulo do motor:

    motor.READY
    motor.RUNNING
    motor.STALLED
    motor.CANCELED
    motor.ERROR
    motor.DISCONNECTED

    Parâmetros
    pair: int
    O slot do Par de Motores.
    
    degrees: int
    O número de graus.
    
    left_velocity: int
    A velocidade (grau/s) do motor esquerdo.
    
    right_velocity: int
    A velocidade (grau/seg) do motor direito.
    
    Argumentos de palavra reservada opcionais:
    stop: int
    O comportamento do Motor depois de parar. Use as constantes no módulo motor.
    
    Os valores possíveis são:
    motor.COAST para liberar o motor até uma parada.
    motor.BRAKE para frear e continuar a frear após a parada.
    motor.HOLD para orientar o motor a manter sua posição.
    motor.CONTINUE para orientar o motor a continuar girando na velocidade atual até receber outro comando.
    motor.SMART_COAST para frear o motor até parar e, depois, liberá-lo e compensar imprecisões no próximo comando.
    motor.SMART_BRAKE para frear o motor, continuar freando até parar e então compensar imprecisões no próximo comando.
    
    acceleration: int
    A aceleração (grau/s²) (1 - 10000).
    
    deceleration: int
    A desaceleração (grau/s²), no intervalo (1 - 10000).
    """

def move_tank(pair: int, left_velocity: int, right_velocity: int, *, acceleration: int = 1000) -> None:
    """
    move_tank(pair: int, left_velocity: int, right_velocity: int, *, acceleration: int = 1000) -> None

    Faça um Par de Motores realizar um movimento de tanque a uma velocidade constante até ser dado um novo comando.

    Parâmetros
    pair: int
    O slot do Par de Motores.
    
    left_velocity: int
    A velocidade (grau/s) do motor esquerdo.
    
    right_velocity: int
    A velocidade (grau/seg) do motor direito.
    
    Argumentos de palavra reservada opcionais:
    acceleration: int
    A aceleração (grau/s²) (1 - 10000).
    """

def move_tank_for_time(pair: int, left_velocity: int, right_velocity: int, duration: int, *, stop: int = motor.BRAKE, acceleration: int = 1000, deceleration: int = 1000) -> Awaitable:
    """
    move_tank_for_time(pair: int, left_velocity: int, right_velocity: int, duration: int, *, stop: int = motor.BRAKE, acceleration: int = 1000, deceleration: int = 1000) -> Awaitable

    Faça um Par de Motores realizar um movimento de tanque a uma velocidade constante por um período específico.
    Quando "aguardado" devolve um status do movimento que corresponde a uma das seguintes constantes do módulo do motor:

    motor.READY
    motor.RUNNING
    motor.STALLED
    motor.CANCELLED
    motor.ERROR
    motor.DISCONNECTED

    Parâmetros
    pair: int
    O slot do Par de Motores.

    duration: int
    Duração em milissegundos

    left_velocity: int
    A velocidade (grau/s) do motor esquerdo.

    right_velocity: int
    A velocidade (grau/seg) do motor direito.

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

def pair(pair: int, left_motor: int, right_motor: int) -> None:
    """
    pair(pair: int, left_motor: int, right_motor: int) -> None

    Agrupe dois Motores (left_motor e right_motor) e armazene o Par de Motores em pair.
    Use pair em todas as chamadas da função motor_pair relacionadas subsequentes.

    Parâmetros
    pair: int
    O slot do Par de Motores.

    left_motor: int
    A porta do motor esquerdo. Use o submódulo port no módulo hub.

    right_motor: int
    A porta do motor direito. Use o submódulo port no módulo hub.
    """
    pass

def stop(pair: int, stop: int = motor.BRAKE) -> None:
    """
    stop(pair: int, *, stop: int = motor.BRAKE) -> None

    Para um Par de Motores.

    Parâmetros
    pair: int
    O slot do Par de Motores.

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

def unpair(pair: int) -> None:
    """
    Desagrupa um Par de Motores

    Parâmetros
    pair: int
    O slot do Par de Motores
    """
    pass
