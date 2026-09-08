import re

# a list that holds patient information as dictionaries
medical_records = [
    {
        'patient_id': 'P1001',        # unique id for the patient
        'age': 34,                     # patient age in years
        'gender': 'Female',            # patient gender
        'diagnosis': 'Hypertension',   # main medical condition
        'medications': ['Lisinopril'], # list of current medications
        'last_visit_id': 'V2301',      # id of the most recent visit
    },
    {
        'patient_id': 'p1002',
        'age': 47,
        'gender': 'male',
        'diagnosis': 'Type 2 Diabetes',
        'medications': ['Metformin', 'Insulin'],
        'last_visit_id': 'v2302',
    },
    {
        'patient_id': 'P1003',
        'age': 29,
        'gender': 'female',
        'diagnosis': 'Asthma',
        'medications': ['Albuterol'],
        'last_visit_id': 'v2303',
    },
    {
        'patient_id': 'p1004',
        'age': 56,
        'gender': 'Male',
        'diagnosis': 'Chronic Back Pain',
        'medications': ['Ibuprofen', 'Physical Therapy'],
        'last_visit_id': 'V2304',
    }
]


# function that checks each patient record for invalid values
def find_invalid_records(
    patient_id, age, gender, diagnosis, medications, last_visit_id
):
    # create a dictionary containing validation results
    constraints = {
        # check that patient_id is a string and matches the correct pattern
        'patient_id': isinstance(patient_id, str)
        and re.fullmatch('p\d+', patient_id, re.IGNORECASE),

        # check that age is an integer and is at least 18
        'age': isinstance(age, int) and age >= 18,

        # check that gender is either male or female
        'gender': isinstance(gender, str)
        and gender.lower() in ('male', 'female'),

        # check that diagnosis is a string or None
        'diagnosis': isinstance(diagnosis, str) or diagnosis is None,

        # check that medications is a list containing only strings
        'medications': isinstance(medications, list)
        and all([isinstance(i, str) for i in medications]),

        # check that last_visit_id matches the correct pattern
        'last_visit_id': isinstance(last_visit_id, str)
        and re.fullmatch('v\d+', last_visit_id, re.IGNORECASE)
    }

    # return a list containing the keys with invalid values
    return [key for key, value in constraints.items() if not value]


# function that checks if the data structure is correct
def validate(data):
    # check if the input is a list or tuple
    is_sequence = isinstance(data, (list, tuple))

    # if it is not a list or tuple, print error and stop
    if not is_sequence:
        print('Invalid format: expected a list or tuple.')
        return False

    # flag to track if any item is invalid
    is_invalid = False

    # the keys every record must have
    key_set = set(['patient_id', 'age', 'gender', 'diagnosis', 'medications', 'last_visit_id'])

    # loop through each item with its position
    for index, dictionary in enumerate(data):
        # check if the current item is actually a dictionary
        if not isinstance(dictionary, dict):
            print(f'Invalid format: expected a dictionary at position {index}.')
            is_invalid = True
            continue

        # check if the dictionary has exactly the required keys
        if set(dictionary.keys()) != key_set:
            print(
                f'Invalid format: {dictionary} at position {index} has missing and/or invalid keys.'
            )
            is_invalid = True
            continue

        # find the invalid values in the current dictionary
        invalid_records = find_invalid_records(**dictionary)

        # loop through each invalid key
        for key in invalid_records:
            # print the invalid key, value, and position
            print(f"Unexpected format '{key}: {dictionary[key]}' at position {index}.")
            # mark the data as invalid
            is_invalid = True

    # if any item was not a dict, return False
    if is_invalid:
        return False

    # everything passed, data is valid
    print('Valid format.')
    return True


# run the validation on the medical records
validate(medical_records)

# test the find_invalid_records function with the first medical record
print(find_invalid_records(**medical_records[0]))
