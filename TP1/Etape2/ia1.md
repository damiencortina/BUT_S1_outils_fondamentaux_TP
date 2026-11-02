# IA 1

## Ecris une fonction Python qui teste si deux nombres décimaux sont égaux

### Réponse IA (Claude)

Comparer deux flottants avec `==` est risqué à cause des erreurs d'arrondi (par exemple `0.1 + 0.2 == 0.3` renvoie `False`). Il faut comparer avec une tolérance :

```python
import math

def sont_egaux(a: float, b: float, rel_tol: float = 1e-9, abs_tol: float = 1e-12) -> bool:
    """Teste si deux nombres décimaux sont égaux à une tolérance près."""
    return math.isclose(a, b, rel_tol=rel_tol, abs_tol=abs_tol)


# Exemples
print(0.1 + 0.2 == 0.3)            # False
print(sont_egaux(0.1 + 0.2, 0.3))  # True
print(sont_egaux(1e-15, 0.0))      # True (grâce à abs_tol)
print(sont_egaux(1.0, 1.001))      # False
```

Les deux tolérances jouent des rôles différents :
- **`rel_tol`** (tolérance relative) s'adapte à l'ordre de grandeur des nombres. C'est utile pour comparer de grandes valeurs.
- **`abs_tol`** (tolérance absolue) est indispensable pour comparer à zéro ou à des valeurs très proches de zéro. Sans elle, la tolérance relative ne fonctionne pas dans ce cas.

Si vous avez besoin d'une égalité **exacte** en base 10, par exemple pour des montants financiers, utilisez plutôt le module `decimal`. Avec lui, `Decimal("0.1") + Decimal("0.2") == Decimal("0.3")` renvoie bien `True`.

### Analyse

Bonne réponse de la part de l'IA.

## Pourquoi une tolérance fixe de 1e-9 est mal choisie pour comparer deux nombres de l'ordre de 1e20

### Réponse IA (Claude)

Parce qu'à cette échelle, une tolérance **absolue** de `1e-9` est bien plus petite que l'écart minimal entre deux flottants voisins. Elle revient donc à exiger une égalité exacte.

Un `float` Python (double précision) a 53 bits de mantisse, soit environ 15 à 17 chiffres significatifs. L'écart entre deux flottants consécutifs (l'« ulp ») grandit avec la valeur :

```python
import math
print(math.ulp(1.0))    # 2.220446049250313e-16
print(math.ulp(1e20))   # 16384.0
```

Autour de `1e20`, les flottants représentables sont espacés de **16 384**. Deux nombres qui diffèrent sont donc séparés d'au moins 16 384, une distance 10¹³ fois plus grande que `1e-9`. Le test `abs(a - b) <= 1e-9` n'accepte alors que `a == b`, et la moindre erreur d'arrondi le fait échouer :

```python
a = 1e20
b = a + math.ulp(a)              # le flottant juste au-dessus
print(abs(a - b) <= 1e-9)        # False : écart = 16384
print(math.isclose(a, b))        # True  : écart relatif ≈ 1.6e-16
```

Le problème inverse existe aussi. Une tolérance absolue fixe est **trop large** pour les très petits nombres : `1e-12` et `1e-15` seraient jugés « égaux » avec `abs_tol=1e-9`, alors qu'ils diffèrent d'un facteur 1000.

La solution est la **tolérance relative**, qui compare l'écart à la taille des nombres :

```python
abs(a - b) <= rel_tol * max(abs(a), abs(b))
```

C'est le rôle de `rel_tol` dans `math.isclose` : `rel_tol=1e-9` signifie « égaux à 9 chiffres significatifs près », quelle que soit l'échelle. La tolérance absolue ne sert plus que de filet de sécurité autour de zéro, où la tolérance relative ne fonctionne pas.

### Analyse

En python, on dispose de 54bits pour stocker la mantisse d'un float (environ 15 chiffres). Si la mantisse contient d'avantage de chiffres, on va perdre des informations (les chiffres au delà du 15ème)
Ainsi, pour un nombre de l'ordre de 1e20, la précision maximale s'arrètera environ aux dizaines de milliers
Une précision inférieure à 0 comme 1e-9 ne permet donc pas de différencier deux nombres de cet ordre, d'où l'intérêt de la tolérance relative.