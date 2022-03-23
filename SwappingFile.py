f1 = input("Ente the text1:")
f2 = input("Ente the text2:")

with open(f1, 'r') as a: data_a = a.read() 
with open(f2, 'r') as b: data_b = b.read() 

def SwapFileData:
    open(f1, 'w') as a: a.write(data_b)
    open(f2, 'w') as a: a.write(data_a)