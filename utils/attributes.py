import pandas as pd

def get_column_names() -> list[str]:
    """
    Returns descriptive names for every column in the German Credit Data
    @df: the actual dataframe to rename columns

    @return: a list of the new column names
    """    

    return [
        'Checking Acc.', 
        'Duration (mo)',
        'Credit History',
        'Purpose',
        'Credit Amount',
        'Savings Acc.',
        'Employment Since',
        'Installment/Income',
        'Marital Status',
        'Other Debtors',
        'Residence Since',
        'Property',
        'Age',
        'Other Installment',
        'Housing',
        'Existing Credits',
        'Job',
        'Dependents',
        'Telephone',
        'Foreigner',
        'Target'
    ]
