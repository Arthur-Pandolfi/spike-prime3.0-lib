class button:

    LEFT = 1
    RIGHT = 2

    def pressed(port:int) -> int:
        """
        int pressed(button: int) -> int

        O módulo permite acionar uma reação quando os botões são pressionados no Hub.

        Parâmetros
    button: int
    Botão do submódulo button no módulo hub.
        """
        pass

class light:

    POWER = 0
    CONNECT = 1

    def color(self, light:int, color:int) -> None:
        """
        color(light: int, color: int) -> None

        Altera a cor de uma luz no Hub.

        Parâmetros
        light: int
        A luz no Hub.

        color: int
        Uma cor do módulo color.
        """
        pass


class motion_sensor:

    TAPPED = 0
    DOUBLE_TAPPED = 1
    SHAKEN = 2
    FALLING = 3
    UNKNOWN = -1
    TOP = 0
    FRONT = 1
    RIGHT = 2
    BOTTOM = 3
    BACK = 4
    LEFT = 5

    def acceleration(raw_unfiltered:bool) -> tuple[int, int, int]:
        """
        acceleration(raw_unfiltered: bool) -> tuple[int, int, int]

        Devolve uma tupla contendo valores inteiros de aceleração x, y e z. Os valores são mili G, ou seja, 1/1000 G.

        Parâmetros
        raw_unfiltered: bool
        Usada para devolver dados brutos e sem filtro
        """
        pass

    def angular_velocity(raw_unfiltered:bool) -> tuple[int, int,int]:
        """
        angular_velocity(raw_unfiltered: bool) -> tuple[int, int, int]

        Devolve uma tupla contendo valores inteiros de velocidade angular x, y e z. Os valores são exibidos em decigraus por segundo.

        Parâmetros
        raw_unfiltered: bool
        Usada para devolver dados brutos e sem filtro.
        """
        pass

    def gesture() -> int:
        """
        gesture() -> int

        Devolve o gesto reconhecido.

        Os valores possíveis são:

        motion_sensor.TAPPED
        motion_sensor.DOUBLE_TAPPED
        motion_sensor.SHAKEN
        motion_sensor.FALLING
        motion_sensor.UNKNOWN
        """
        pass

    def get_yaw_face() -> int:
        """
        Recupere a face do Hub ao qual a guinada é relativa.
        Ao colocar o Hub em uma superfície plana com a face apontando para cima, somente a guinada é atualizada quando o Hub é girado.
        motion_sensor.TOP A face do SPIKE Prime Hub onde fica a porta USB para carregamento.
        motion_sensor.FRONT A face do SPIKE Prime Hub onde fica a Matriz de Luz.
        motion_sensor.RIGHT Olhando para a face frontal do SPIKE Prime Hub, o lado direito dele.
        motion_sensor.BOTTOM O lado onde fica a bateria do SPIKE Prime Hub.
        motion_sensor.BACK O lado onde fica a caixa de som do SPIKE Prime Hub.
        motion_sensor.LEFT Olhando para a face frontal do SPIKE Prime Hub, o lado esquerdo dele.
        """
        pass

    def quaternion() -> tuple[float, float, float, float]:
        """
        quaternion() -> tuple[float, float, float, float]

        Devolve o quatérnio de orientação do Hub como uma tuple[w: float, x: float, y: float, z: float].
        """
        pass

    def reset_tap_count() -> None:
        """
        reset_tap_count() -> None

        Redefine a contagem de toques devolvida pela função tap_count.
        """

    def reset_yaw(angle:int) -> None:
        """
        reset_yaw(angle: int) -> None

        Altera o deslocamento do ângulo de guinada.
        O ângulo definido será o novo valor de guinada.

        Parâmetros
        angle: int
        """
        pass

    def set_yaw_face(up:int) -> bool:
        """
        set_yaw_face(up: int) -> bool

        Altere a face do Hub usada como face de guinada. Ao colocar o Hub em uma superfície plana com essa face apontando para cima, somente a guinada é atualizada quando o Hub é girado.

        Parâmetros
        up: int
        A face do Hub que deve ficar virada para cima.
        Os valores disponíveis são:

        motion_sensor.TOP A face do SPIKE Prime Hub onde fica a porta USB para carregamento.
        motion_sensor.FRONT A face do SPIKE Prime Hub onde fica a Matriz de Luz.
        motion_sensor.RIGHT Olhando para a face frontal do SPIKE Prime Hub, o lado direito dele.
        motion_sensor.BOTTOM O lado onde fica a bateria do SPIKE Prime Hub.
        motion_sensor.BACK O lado onde fica a caixa de som do SPIKE Prime Hub.
        motion_sensor.LEFT Olhando para a face frontal do SPIKE Prime Hub, o lado esquerdo dele.
        """
        pass

    def stable() -> bool:
        """
        Identifica se o Hub está ou não em uma posição plana.
        """
        pass

    def tap_count() -> int:
        """
        tap_count() -> int

        Devolve o número de toques reconhecidos desde que o programa foi iniciado ou que motion_sensor.reset_tap_count() foi chamado pela última vez.
        """
        pass

    def tilt_angles() -> tuple[int, int, int]:
        """
        tilt_angles() -> tuple[int, int, int]

        Devolve uma tupla contendo valores inteiros de inclinação e rolagem. Os valores são exibidos em decigraus.
        """
        pass

    def up_face() -> int:
        """
        Devolve a face do Hub virada para cima no momento.
        motion_sensor.TOP A face do SPIKE Prime Hub onde fica a porta USB para carregamento.
        motion_sensor.FRONT A face do SPIKE Prime Hub onde fica a Matriz de Luz.
        motion_sensor.RIGHT Olhando para a face frontal do SPIKE Prime Hub, o lado direito dele.
        motion_sensor.BOTTOM O lado onde fica a bateria do SPIKE Prime Hub.
        motion_sensor.BACK O lado onde fica a caixa de som do SPIKE Prime Hub.
        motion_sensor.LEFT Olhando para a face frontal do SPIKE Prime Hub, o lado esquerdo dele.
        """

class port:
    A = 0
    B = 1
    C = 2
    D = 3
    E = 4
    F = 5


def device_uuid() -> str:
    """
    device_uuid() -> str

    Recupera o ID do dispositivo.
    """
    pass

def hardware_id() -> str:
    """
    hardware_id() -> str

    Recupera o ID do hardware
    """
    pass

def power_off() -> None:
    """
    power_off() -> None

    Desliga o Hub
    """
    pass

def temperature() -> int:
    """
    temperature() -> int

    Recupera a temperatura do Hub. Medida em decigraus celsius (d°C), que é 1/10 de um grau celsius (°C).
    """
