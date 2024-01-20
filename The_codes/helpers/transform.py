def transform_yes_no(value):
    if value == 'No':
        return 0
    else:
        return 1


def transform_bmi(value):
    if value < 16:
        return 0
    elif 16 <= value < 17:
        return 1
    elif 17 <= value < 18.5:
        return 2
    elif 18.5 <= value < 25:
        return 3
    elif 25 <= value < 30:
        return 4
    elif 30 <= value < 35:
        return 5
    elif 35 <= value < 40:
        return 6
    elif value >= 40:
        return 7


def transform_mental_physical(value):
    if 0 < value <= 10:
        return 0
    elif 10 < value <= 20:
        return 1
    elif 20 <= value <= 25:
        return 2
    elif 25 <= value <= 30:
        return 3


def transform_gender(value):
    if value == 'Female':
        return 0
    else:
        return 1


def transform_age(value):
    if value >= 18 and value <= 39 :
        return 0
    elif value >= 40 and value <= 49:
        return 1
    elif value >= 50 and value <= 64:
        return 2
    elif value >= 65 and value <= 79:
        return 3
    else:
        return 4


print(transform_age(19))


def transform_diabetes(value):
    if value == 'Yes':
        return 0
    elif value == 'No':
        return 1
    elif value == 'No, borderline diabetes':
        return 2
    elif value == 'Yes (during pregnancy)':
        return 3


def transform_GenHealth(value):
    if value == 'Poor':
        return 0
    elif value == 'Fair':
        return 1
    elif value == 'Good':
        return 2
    elif value == 'Very good':
        return 3
    elif value == 'Excellent':
        return 4


def transform_sleepTime(value):
    if 0 <= value <= 6:
        return 0
    elif 6 < value <= 8:
        return 1
    elif 8 < value <= 24:
        return 2
