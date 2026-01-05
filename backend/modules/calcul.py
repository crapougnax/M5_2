def carre(nombre: int) -> int:
    """
    Retourne le carré d'un entier donné.
    
    Args:
        nombre (int): L'entier à élever au carré.
        
    Returns:
        int: Le carré de l'entier.
        
    Raises:
        TypeError: Si l'entrée n'est pas un entier.
    """
    if not isinstance(nombre, int):
        raise TypeError("L'entrée doit être un entier.")
    return nombre ** 2
