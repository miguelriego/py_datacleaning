# Snippet #1: tfinder
# This little snippet will look at an entire DF from a list in Pandas and return the last item where TARGETCOLUMN is notna()
# The stepsize variable is the number of rows the function will check back on (15 default)
# Notice in the example that I use a partial index in order to make the search more efficient

def backpedal(ix, df, stepsize=15):
    """Look for index in previous rows and returns last matched TL."""
        return(df.loc[(ix - stepsize):ix - 1, ('TARGETCOLUMN')].dropna().iloc[-1])
    
"""
Example:
subset = df[df['SUBSET']]
for ix in subset.index:
    df['TCOLUMN'].iloc[ix] = backpedal(ix, df=df)
"""
