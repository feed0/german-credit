import pandas as pd

def preprocess_dtypes(df):
    """
    optimize memory usage by:
    1. converting object Features to category 
    2. Target to bool

    @return: DataFrame with optimized memory usage
    """

    copy = df.copy()
    
    # 1. Objects to category -----------------------------------
    copy[copy.select_dtypes('object').columns] = copy.select_dtypes('object').astype('category')

    # 2. Booleans ----------------------------------------------

    ## Rename 'class' to 'Target'
    copy = copy.rename(columns={'class': 'Target'})

    ## Replace with booleans
    copy['Target'] = copy['Target'].map(lambda x: x == 1)
    copy['Attribute19'] = copy['Attribute19'].map(lambda x: x == 'A192')
    copy['Attribute20'] = copy['Attribute20'].map(lambda x: x == 'A201')

    ## Convert dtype to bool
    copy[['Target', 'Attribute19', 'Attribute20']] = copy[['Target', 'Attribute19', 'Attribute20']].astype('bool')

    return copy

def set_column_names(df):
    """
    Sets descriptive names for every column in the German Credit
    @df: the actual dataframe to rename columns
    """    
    df.columns = [
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
