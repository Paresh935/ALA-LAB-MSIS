# This file includes steps 6 and 8 (Steps.txt)

import timeit

from LAB1.vec import Vec


# Vector sizes required by the assignment
sizes = [2000, 4000, 8000, 16000, 32000, 64000, 128000, 256000, 512000, 1024000]


for n in sizes:

    print("\n---------")
    print(f"Vector dimension: {n}")
    print("-----------")

    # Create two random vectors
    v1 = Vec.uniform(n)
    v2 = Vec.uniform(n)

    # Addition
    addition_time = timeit.timeit(
        lambda: v1 + v2,     #small anonymous function
        number=100
    )

    # Subtraction
    subtraction_time = timeit.timeit(
        lambda: v1 - v2,
        number=100
    )

    # Scalar multiplication
    multiplication_time = timeit.timeit(
        lambda: 2 * v1,
        number=100
    )

    # In-place scalar multiplication
    imul_time = timeit.timeit(
    lambda: v1.__imul__(2),
    number=100
    )

    # Negative
    negative_time = timeit.timeit(
    lambda: -v1,
    number=100
    )

    # Representation
    repr_time = timeit.timeit(
    lambda: repr(v1),
    number=100
    )

    # Zeros
    zeros_time = timeit.timeit(
    lambda: Vec.zeros(n),
    number=100
    )

    # Ones
    ones_time = timeit.timeit(
    lambda: Vec.ones(n),
    number=100
    )

    # Uniform
    uniform_time = timeit.timeit(
    lambda: Vec.uniform(n),
    number=100
    )

    # Norm
    norm_time = timeit.timeit(
        lambda: v1.norm(),
        number=100
    )

    print(f"Addition:       {addition_time:.8f} seconds")     #output till 6th decimal
    print(f"Subtraction:    {subtraction_time:.8f} seconds")
    print(f"Multiplication: {multiplication_time:.8f} seconds")
    print(f"In-place multiplication: {imul_time:.8f} seconds")
    print(f"Negative:               {negative_time:.8f} seconds")
    print(f"Representation:         {repr_time:.8f} seconds")
    print(f"Zeros:                  {zeros_time:.8f} seconds")
    print(f"Ones:                   {ones_time:.8f} seconds")
    print(f"Uniform:                {uniform_time:.8f} seconds")
    print(f"Norm:            {norm_time:.8f} seconds")




