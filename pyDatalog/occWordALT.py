from pyDatalog import pyDatalog
pyDatalog.create_terms('Frequency, mostFreq, cat, rat, mat, sat, X, Y, Z')
# +Frequency('cat', 4)
# +Frequency('rat', 8)
# +Frequency('mat', 5)
# +Frequency('sat', 7)
Frequency["cat"] = 4
Frequency["rat"] = 8
Frequency["mat"] = 5
Frequency["sat"] = 7
# mostFreq(X) <= max_(Frequency[X])

# let's assume "cat", "rat", "mat", and "sat" are some words that appear in a paragraph of text

print(max_(Frequency["cat"], Frequency["rat"], Frequency["mat"], Frequency["sat"]) == X)
