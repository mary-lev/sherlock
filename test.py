from collatex import *

with open("scarlet1_2.txt", "r") as f:
    text1 = f.read()

with open("scarlet2_2.txt", "r") as f:
    text2 = f.read()

collation = Collation()
collation.add_plain_witness("A", text1)
collation.add_plain_witness("B", text2)

alignment_table = collate(collation, layout="vertical")
print(alignment_table)