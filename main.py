from random import randint


def attack(char_name: str, char_class: str) -> str:
    """Esta es la función de ataque.
    Recibe nombre y clase del personaje
    y devuelve un string con la cantidad
    de daño impartido.
    """
    if char_class == 'guerrero':
        return (f'{char_name} causó {5 + randint(3, 5)} de daño al enemigo')
    if char_class == 'mago':
        return (f'{char_name} causó {5 + randint(5, 10)} de daño al enemigo')
    if char_class == 'sanador':
        return (f'{char_name} causó {5 + randint(-3, -1)} de daño al enemigo')


def defense(char_name: str, char_class: str) -> str:
    """Esta es la función de defensa.
    Recibe nombre y clase del personaje
    y devuelve un string con la cantidad
    de daño bloqueado.
    """
    if char_class == 'guerrero':
        return (f'{char_name} bloqueó {10 + randint(5, 10)} de daño')
    if char_class == 'mago':
        return (f'{char_name} bloqueó {10 + randint(-2, 2)} de daño')
    if char_class == 'sanador':
        return (f'{char_name} bloqueó {10 + randint(2, 5)} de daño')


def special(char_name: str, char_class: str) -> str:
    """Esta es la función de habilidades especiales.
    Recibe nombre y clase del personaje
    y devuelve un string con incrementos
    en atributos seleccionados.
    """
    if char_class == 'guerrero':
        return f'{char_name} usó una habilidad especial "Aguante {80 + 25}"'
    if char_class == 'mago':
        return f'{char_name} usó una habilidad especial "Ataque {5 + 40}"'
    if char_class == 'sanador':
        return f'{char_name} usó una habilidad especial "Defensa {10 + 30}"'


def start_training(char_name: str, char_class: str) -> str:
    """Esta es la función de entrenamiento.
    Recibe nombre y clase del personaje,
    devuelve un string con un mensaje personalizado,
    en función de la clase del personaje
    y ofrece la posibilidad de entrenar.
    en atributos seleccionados.
    """
    if char_class == 'guerrero':
        print(f'{char_name}, eres un Guerrero, experto '
              'en combate cuerpo a cuerpo.')
    elif char_class == 'mago':
        print(f'{char_name}, eres un Mago, dominando '
              'magistralmente los elementos.')
    elif char_class == 'sanador':
        print(f'{char_name}, eres un Sanador, un hechicero que cura heridas.')
    print('Entrena tus habilidades.')
    print('Introduce uno de estos comandos: atacar, para atacar un enemigo; '
          'defender, para bloquear un ataque enemigo; o '
          'especial, para usar tu poder especial.')
    print('Si no quieres entrenar, presiona saltar (skip).')
    cmd: str = None
    while cmd != 'skip':
        cmd = input('Introduce un comando: ')
        if cmd == 'ataque':
            print(attack(char_name, char_class))
        elif cmd == 'defensa':
            print(defense(char_name, char_class))
        elif cmd == 'especial':
            print(special(char_name, char_class))
    return 'El entrenamiento ha terminado.'


def choice_char_class() -> str:
    """Permite elegir la clase con la que
    jugará el personaje.
    """
    approve_choice: str = None
    char_class: str = None
    while approve_choice != 'y':
        char_class = input('Introduce la clase '
                           'de tu personajes: Guerrero, guerrero; '
                           'Mago, mago; Sanador, sanador: ')
        if char_class == 'warrior':
            print('Guerrero: un feroz luchador cuerpo a cuerpo. '
                  'Fuerte, resiliente y valiente.')
        if char_class == 'magician':
            print('Mago: un brillante luchador de largo alcance. '
                  'Maestro de poderes mágicos.')
        if char_class == 'healer':
            print('Sanador: un poderoso chamán. '
                  'Extrae fuerza de la naturaleza, la fe y los espíritus.')
        approve_choice = input('Presiona (Y) para confirmar '
                               'o cualquier otro botón '
                               'para seleccionar cualquier otra clase').lower()
    return char_class

    