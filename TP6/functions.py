import math

def vecteur(A, B):
    return (B[0]-A[0],B[1]-A[1])

def produit_scalaire(u, v):
    return u[0]*v[0] + u[1]*v[1]

def norme(u):
    return math.sqrt(produit_scalaire(u,u))

def angle(u,v):
    return produit_scalaire(u,v)/(norme(u)*norme(v))