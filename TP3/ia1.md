# IA

## Donne moi une fonction Python qui évalue un polynôme donné par ses coefficients

### Réponse IA (Claude)

Voici une fonction qui utilise la **méthode de Horner** (la plus efficace : n multiplications et n additions pour un polynôme de degré n) :

```python
def evaluer_polynome(coefficients, x):
    """
    Évalue P(x) = a0 + a1*x + a2*x^2 + ... + an*x^n.

    coefficients : liste [a0, a1, ..., an], du degré 0 au degré n.
    x : valeur où évaluer le polynôme (int, float, complex...).
    """
    resultat = 0
    for a in reversed(coefficients):
        resultat = resultat * x + a
    return resultat
```

Exemple : pour P(x) = 3 + 2x + x², soit `[3, 2, 1]` :

```python
print(evaluer_polynome([3, 2, 1], 2))   # 3 + 4 + 4 = 11
print(evaluer_polynome([], 5))          # polynôme nul → 0
```

Si vous préférez donner les coefficients du **degré le plus haut au plus bas** (`[an, ..., a1, a0]`, convention de `numpy.polyval`), il suffit d'enlever le `reversed` :

```python
for a in coefficients:
    resultat = resultat * x + a
```

### Analyse

L'IA donne directement Horner et non la version naive.

## De combien Horner est-il plus rapide que la version naïve, en Python, sur un polynôme de degré 20 000 évalué en un flottant ?

### Réponse IA (Claude)

Je mesure directement les deux versions dans le même environnement.

Sur cette machine (Python 3.13, polynôme de degré 20 000 à coefficients aléatoires, meilleur temps sur 7 séries de 50 appels) :

| Version | Temps par évaluation | Rapport à Horner |
|---|---|---|
| Horner | 0,46 ms | 1× |
| Naïve avec `x**i` | 1,72 ms | **≈ 3,7× plus lente** |
| Naïve avec puissance incrémentale (`p *= x`) | 0,64 ms | ≈ 1,4× plus lente |

Les trois donnent le même résultat. Le chiffre dépend donc de ce qu'on appelle « naïve » :

- **Avec `a * x**i`**, chaque terme recalcule une puissance flottante, ce qui coûte plus cher qu'une multiplication. On obtient un facteur d'environ 3,5 à 4.
- **En gardant la puissance courante dans une variable**, on fait aussi O(n) opérations, mais avec 2 multiplications par terme au lieu d'une. L'écart tombe à environ 40 %.

En Python pur, l'essentiel du temps vient de l'interpréteur (la boucle, les objets `float`), pas des opérations arithmétiques elles-mêmes. C'est pour ça que l'écart reste modeste. Pour aller vraiment plus vite, `numpy.polyval` fait la même chose en C et sera bien plus rapide que les trois versions.

J'ai choisi x = 0,99997 pour que x²⁰⁰⁰⁰ ne déborde pas. Avec |x| plus grand que 1, la version naïve produit vite `inf`, alors que Horner reste numériquement plus stable.

### Analyse

L'IA a refait le calcul par elle même plutôt que de donner une avis sur la question.
Je constate cependant que contrairement à ce que j'ai mesuré, l'ia évoque un facteur 4 (et non 2).
Les mesures de l'IA sont les mêmes si je lui demande de remesurer pour x = 1.0001 (elle trouve ici un temps similaire au mien sur horner, mais supérieur sur la version naive).