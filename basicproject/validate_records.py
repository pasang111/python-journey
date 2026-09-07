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
def find_invalid_records(
    patient_id, age, gender, diagnosis, medications, last_visit_id
):
    constraints = {
        'patient_id': isinstance(patient_id, str)
    }
    return constraints

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

        if set(dictionary.keys()) != key_set:
            print(
                f'Invalid format: {dictionary} at position {index} has missing and/or invalid keys.'
            )
            is_invalid = True

    # if any item was not a dict, return False
    if is_invalid:
        return False

    # everything passed, data is valid
    print('Valid format.')
    return True

# run the validation on the medical records
validate(medical_records)   
print(find_invalid_records(**medical_records[0]))