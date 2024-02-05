from functools import wraps
from time import perf_counter_ns
def intouchable():
    print("Fonction intouchable !")

def chrono(functiont):
    @wraps(functiont)
    def wrap(*args,**kwargs):
        start = perf_counter_ns()
        print("Exécution commencée :", start)
        functiont(*args,**kwargs)
        stop = perf_counter_ns()
        print("Exécution finie :", stop)
        dure = stop-start
        print("Durée de l'exécution :", dure,"nanosecondes =", dure/1000000, "secondes")
    return wrap


def decorateur(functiont):
    @wraps(functiont)
    def wrap(*args,**kwargs):
        """
        jaaj
        """
        print("\nDébut de fonction")
        functiont(*args,**kwargs)
        print("Fin de fonction")
    return wrap

fonction_dec = decorateur(intouchable)
fonction_dec()

@decorateur
def another_one():
    print("Don't Touch")

another_one()
print("\n",another_one.__name__)
print("\n", another_one.__doc__)

@decorateur
@chrono
def boucle(n):
    """
    Qui compte jusqu'à n
    """
    for _ in range(n):
        if _ == n:
            print ("Fin !")
        pass

boucle(1000)
print("Nom de la fonction :",boucle.__name__,"\nDoc de la fonction :", boucle.__doc__)