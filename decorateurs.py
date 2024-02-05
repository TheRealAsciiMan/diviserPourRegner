from functools import wraps
from time import perf_counter_ns
def intouchable():
    print("Fonction intouchable !")

def chrono(functiont):
    @wraps(functiont)
    def wrap():
        start = perf_counter_ns()
        print("\nExécution commencée :", start)
        functiont()
        stop = perf_counter_ns()
        print("Exécution finie :", stop)
        print("Durée de l'exécution :", stop-start,"nanosecondes")
    return wrap


def decorateur(functiont):
    @wraps(functiont)
    def wrap():
        """
        jaaj
        """
        print("\nAvant")
        functiont()
        print("Après")
    return wrap

fonction_dec = decorateur(intouchable)
fonction_dec()

@decorateur
def another_one():
    print("Don't Touch")

another_one()
print("\n",another_one.__name__)
print("\n", another_one.__doc__)

@chrono
def jaaj():
    print("JAAAAJ !")

jaaj()
