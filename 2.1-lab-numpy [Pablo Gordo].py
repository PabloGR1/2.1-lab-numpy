#1. Import the NUMPY package under the name np.

import numpy as np

#2. Print the NUMPY version and the configuration.

print(np.__version__)

#mi versión: 1.21.5

#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?
#Genera una matriz tridimensional 2x3x5 con valores aleatorios. Asignar la matriz a la variable "a" Desafío: hay al menos tres formas fáciles de usar numpy para generar matrices aleatorias. ¿Cuántas formas puedes encontrar?
    
a = np.random.random(((5,3,5)))    

#4. Print a.

print(a)

#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"
#Crea una matriz tridimensional de 5x2x3 con todos los valores iguales a 1.Asignar la matriz a la variable "b"

b = np.ones(((5,2,3)))


#6. Print b.

print(b)


#7. Do a and b have the same size? How do you prove that in Python code?

print(a.size)
print(b.size)

if a.size == b.size:
    print ('si, son iguales')
else:
    print ('no, son diferentes')


#8. Are you able to add a and b? Why or why not?

np.add(a,b)

print('no, por que tienen distinta estructura')



#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

c= np.transpose(b,(1,2,0))


#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

d=np.add(a,c)

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

'''las dos matrices son iguales (2x3x5)'''
''' a los valores de la matriz a, ha sumado 1 a todos, puesto que la matriz c valia 1 en cualquier valor'''


#12. Multiply a and c. Assign the result to e.

e = np.multiply(a,c)

#13. Does "e" equal to "a"? Why or why not?

'''si, por que hemos multiplicado el valor de a por 1, es decir, el resultado es su mismo valor'''


#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

d_max=d.max()
d_min=d.min()
d_mean=d.mean()


#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

f = np. empty((2, 3, 5))


"""
#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.

     -------- traductor -----------

#16. Rellenar los valores en f. Para cada valor en d, si es mayor que d_min pero menor que d_mean, asigne 25 al valor correspondiente en f.

Si un valor en d es mayor que d_mean pero menor que d_max, asigna 75 al valor correspondiente en f.

Si un valor es igual a d_mean, asigna 50 al valor correspondiente en f.

Asignar 0 a los valores correspondientes en f para d_min en d.

Asigna 100 al valor o valores correspondientes en f para d_max en d.

Al final, f solo debe tener los siguientes valores: 0, 25, 50, 75 y 100.

Nota: no tienes que usar Numpy en esta pregunta.
"""



a=0
b=0
c=0

for x in d:
    for y in x:
        for z in y:
            if z>d_min and z<d_mean:
                f[a][b][c]=25
            if z>d_mean and z<d_max:
                f[a][b][c]=75
            if z==d_mean:
                f[a][b][c]=50
            if z==d_min:
                f[a][b][c]=0
            if z==d_max:
                f[a][b][c]=100
            
            c+=1
        c=0
        b+=1
    b=0
    a+=1  

print(f)



"""
#17. Print d and f. Do you have your expected f?
For instance, if your d is:
array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

Your f should be:
array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],

       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])
"""
print(f)

"""
#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
Again, you don't need Numpy in this question.
"""

g = np. empty((2, 3, 5), str)

a=0
b=0
c=0

for x in d:
    for y in x:
        for z in y:
            if z>d_min and z<d_mean:
                g[a][b][c]="B"
            if z>d_mean and z<d_max:
                g[a][b][c]="D"
            if z==d_mean:
                g[a][b][c]="C"
            if z==d_min:
                g[a][b][c]="A"
            if z==d_max:
                g[a][b][c]="E"
            
            c+=1
        c=0
        b+=1
    b=0
    a+=1  

print(g)