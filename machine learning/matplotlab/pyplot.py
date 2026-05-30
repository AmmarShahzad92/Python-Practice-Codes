import matplotlib.pyplot as plots
import numpy as npc

""" x = npc.array([0,6])
y = npc.array([0,250])

plots.plot(x, y)
plots.plot(x, y, "o")
plots.show() """

""" drafting point on matplotlib """
x = npc.array([1,8,6,42,15])
y = npc.array([0,4,5,75,101])

# plots.plot(x, y)
plots.title("Testing")
plots.bar(x,y)
plots.xlabel("Hello x")
plots.ylabel("Hello Y")

plots.show()
