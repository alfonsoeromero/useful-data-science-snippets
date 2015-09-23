def count_unique_rows(X, cols):
    """ Receives a dataframe, a list of columns, 
        and returns a series with the set of
        unique rows and the count
    """
    return X.groupby(cols).size()
