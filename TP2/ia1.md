# IA

## Ecris une fonction Python qui teste si un nombre est premier

### Réponse IA (Claude)

```python
import math

def est_premier(n: int) -> bool:
    """Renvoie True si n est un nombre premier."""
    if n < 2:
        return False
    if n < 4:
        return True          # 2 et 3 sont premiers
    if n % 2 == 0 or n % 3 == 0:
        return False
    # Tout premier > 3 s'écrit 6k − 1 ou 6k + 1
    for d in range(5, math.isqrt(n) + 1, 6):
        if n % d == 0 or n % (d + 2) == 0:
            return False
    return True
```

### Analyse

Pour n=1 : FALSE

Pour n=2 : TRUE

Pour un nombre négatif : FALSE

La boucle s'arrète a sqrt