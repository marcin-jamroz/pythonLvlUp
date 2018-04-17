def hey_hi_hello_factory(welcome_txt='hello'):
    counter = 0

    def greet(name):
        nonlocal counter  # nonlocal - dostęp write do zmiennych funkcji okalającej
        # bez jest dostęp read tylko
        counter += 1
        print('{} {}!\tcounter: {}'.format(welcome_txt, name, counter))

    return greet


say_hello = hey_hi_hello_factory('hello')
say_hi = hey_hi_hello_factory('hi')

say_hello('Janek')
say_hi('Magda')
say_hello('Maciek')


def hello(name):
    hello.count += 1
    print(f"Hello {name}, count: {hello.count}")


hello.count = 0

goodbye = hello  # przekazywanie funkcji do zmiennej
hello("Kuba")
goodbye("Arek")


def censor(singer):
    def print_censor_msg():
        print("Nie pozwalam wykonać: {}".format(singer.__name__))

    return print_censor_msg


@censor
def play_music():
    print("gra muzyka")


play_music()
play_music()


def przodownik(wolna_funkcja):
    def inner():
        print("Pierwszy!")
        return wolna_funkcja()

    return inner


@przodownik
def play_music():
    print("Gra muzyka")


play_music()

from functools import wraps


def bumelant(szybka_funkcja):
    @wraps(szybka_funkcja)  # bardzo ważne, ustawia atrybut __name__ odpowiednio
    def inner():
        result = szybka_funkcja()
        print("zasada zachowania energii: na później")
        return result

    return inner


@bumelant
def play_music():
    print("Gra muzyka")


play_music()
print(play_music.__name__)


# def dekorator_pierwszy(do_udekorowania)
# def dekorator_drugi(do_udekorowania)

# @dekorator_pierwszy
# @dekorator_drugi
# def zywkla_funkcja():

# zwykla_funkcja = dekorator_pierwszy(dekorator_drugi(zwykla_funkcja))

# dekoratory wykonują się od wewnętrzengo do zewnętrznego

def bumelant(szybka_funkcja):
    @wraps(szybka_funkcja)  # bardzo ważne, ustawia atrybut __name__ odpowiednio
    def inner(**kwargs):
        result = szybka_funkcja(**kwargs)
        print("zasada zachowania energii: na później")
        return result

    return inner


# @bumelant
# def play_music(music):
#     print("Gra: {}".format(music))

# play_music("jazz")

@bumelant
def play(*, music='polskie regge'):
    print("Gra: {}".format(music))


play(music="jazz")
play()


def bumelant(sentence):
    print("decorator called with sentence:", sentence)

    def real_decorator(to_be_decorated):
        def wrapper(*args, **kwargs):
            result = to_be_decorated(*args, **kwargs)
            print('zasada zachowania energii')
            print("senstencja dekoratora:", sentence)
            return result

        return wrapper

    return real_decorator


@bumelant('co masz zrobić')
def play(music):
    print(f"Gra {music}")

play("song of victory")
