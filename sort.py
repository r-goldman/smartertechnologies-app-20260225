def sort(width: float, height: float, length: float, mass: float) -> str:
    '''
    Determines the category of a package based on its dimensions and mass.
    Returns "REJECTED" if the package is both bulky and heavy, "SPECIAL" if it is either bulky or heavy, and "STANDARD" if it is neither.
    A package is considered bulky if its volume (width * height * length) is at least 1,000,000 cubic cm or if any of its dimensions is at least 150 cm
    A package is considered heavy if its mass is at least 20 kg

    Executes in O(1) time and space.
    All inputs are expected to be non-negative. If any input is negative or zero, a ValueError is raised.
    '''

    if not width or not height or not length or not mass:
        raise ValueError("All parameters must be non-null.")
    elif width <= 0 or height <= 0 or length <= 0 or mass <= 0:
        raise ValueError("All parameters must be positive.")
    
    volume = width * height * length
    is_bulky = volume >= 1000000 or max(width, height, length) >= 150
    is_heavy = mass >= 20

    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"
    