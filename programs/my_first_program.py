from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Perform an arithmetic operation (addition) on the secret integers
    result = my_int1 * my_int2

    # Return the result as the output
    return [Output(result, "Arithmetic_output", party1)]