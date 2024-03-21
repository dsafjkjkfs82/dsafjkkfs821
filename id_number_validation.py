def validate_id_number(id_number):
    """
    Validate a Chinese ID number.
    
    Args:
        id_number (str): The ID number to be validated.
        
    Returns:
        bool: True if the ID number is valid, False otherwise.
    """
    if len(id_number) != 18:
        return False
    for char in id_number[:-1]:
        if not char.isdigit():
            return False
    weights = [int(x) for x in "7 9 10 5 8
