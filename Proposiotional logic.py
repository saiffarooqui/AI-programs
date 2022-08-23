import itertools

def findInps(exp):
    inps=[]
    for c in exp:
        if c!='*' and c!='+' and c!='-' and c!='(' and c!=')' and c not in inps:
            inps.append(c)
    return inps    


def evaluate(exp, row):
    replaced=[]
    inp=0
    for c in exp:
        if c!='*' and c!='+' and c!='-' and c!='(' and c!=')' and c not in replaced:
            exp=exp.replace(c,str(row[inp]))
            inp+=1
            replaced.append(c)
    exp=exp.replace('+','&')        
    exp=exp.replace('*','|')
    exp=exp.replace('-','~')
    result=eval(exp)
    return result

n=int(input("Enter number of inputs: "))
print("Rules:")
print("1.For AND enter +")
print("2.For OR enter *")
print("3.For NOT enter -")
exp=input("Enter logical exp: ")

truth_table=list(itertools.product([0,1],repeat=n))

outputs=[]
for row in truth_table:
    outputs.append(evaluate(exp,row))
print(outputs)

for c in findInps(exp):
    print(c,end="  ")
print("output")

for i in range(len(truth_table)):
    for v in truth_table[i]:
        print(v,end="  ")
    print("  ",outputs[i])

if outputs.count(1)>=1:
    print("logical exp is satisfiable")
else:
    print("logical exp is not satisfiable")        