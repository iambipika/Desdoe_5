# Desdoe_5
Desdoe Assignment 5

The code compare two optimization algorithms, namely: "Newton-Conjugate Gradient algorithm" and "Broyden-Fletcher-Goldfarb-Shanno algorithm" using python library "SciPy".

The comparision between two algorithm Newton-CG and BFGS result suggests BFGS to be better. 
The result from the code is as:

                  Result for Newton-CG:
                  Mean error: 8.291740335075504e-09
                  x: [1.00000049 1.00000054 0.99999916 0.99999784 0.99999535 0.99999049
                   0.99998087 0.99996169 0.99992323 0.99984607]
                  Mean gradient evaluations 76.2, 
                   median gradient evaluations 77.0, 
                   maximum value 109, 
                   minimum value 32


                  Result for BFGS:
                  Mean error: 2.7760219577639083e-14
                  x: [1.         1.         1.         1.         1.         0.99999999
                   0.99999999 0.99999999 0.99999998 0.99999997]
                  Mean gradient evaluations 150.2, 
                   median gradient evaluations 149.0, 
                   maximum value 240, 
                   minimum value 91
                   
                    
From above result, we can see the mean error of BFGS is smaller than that of Newton-CG. Gradient values is BFGS is higher. Therefore, BFGS is better performing in our case.
