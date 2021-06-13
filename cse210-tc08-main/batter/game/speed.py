def speed():
    """
    Have the player decide the speed
    Returns:
        Speed: How fast the ball moves
    """
    speed = float(input("How fast do you want:(between 1 and 10) "))
    return speed

frame = 0.8 / speed()
