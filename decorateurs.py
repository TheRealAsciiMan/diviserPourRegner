from functools import wraps
from time import perf_counter_ns
def intouchable():
    print("Fonction intouchable !")


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

