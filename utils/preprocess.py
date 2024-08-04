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

    # df_bin['Target'] = df_bin['Target'].map(lambda x: x == 1)
    # df_bin['Attribute19'] = df_bin['Attribute19'].map(lambda x: x == 'A192')
    # df_bin['Attribute20'] = df_bin['Attribute20'].map(lambda x: x == 'A201')

    # # Convert to bool dtype
    # df_bin[['Target', 'Attribute19', 'Attribute20']] = df_bin[['Target', 'Attribute19', 'Attribute20']].astype('bool')

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
