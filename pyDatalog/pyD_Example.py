from pyDatalog import pyDatalog
# pyDatalog is required to run this!!
pyDatalog.create_terms('Taste, Price, sour, sweet, expensive, cheap, apple, grape, lemon, grapefruit, X, Y')
+Taste("lemon", "sour")
+Taste("grapefruit", "sour")
+Taste("apple", "sweet")
+Taste("grape", "sweet")
Price["apple"] = 5
Price["grape"] = 1
Price["lemon"] = 5
Price["grapefruit"] = 3
expensive(X) <= (Price[X] > 4)
cheap(X) <= (Price[X] < 4)

# 'Taste' is a relationship between a fruit and a flavor
# let's assume there are only 2 flavors, sour and sweet
# price > 4 = expensive, price < 4 = cheap
# please ignore the error marks, this code still works!
# queries are written with a Python print statement
print((Taste(X, "sour")) & cheap(X) & (Taste(Y, "sweet")) & cheap(Y))

