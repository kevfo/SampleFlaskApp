def calculate_bmi(height, weight):
    '''
    Ideally, the participant would make their own model using scikit-learn after 
    they've done their share of EDA using pandas, scikit-learn, or some other 
    piece of software, but for now...

    I'm just rolling with this simple formula.
    '''
    bmi = round(weight / height**2, 2)
    return bmi, "you're good!" if bmi < 25 else "you're a fatty!"