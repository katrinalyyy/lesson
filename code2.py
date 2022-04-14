import pickle


class stud:
    fam = None
    surn = None
    name = None
    bal = None


f = open('students.txt', 'r', encoding='utf-8')
St = []
while True:
    x = f.readline()
    if not x: break
    x = x.split(' ', 3)
    st = stud()
    st.fam = x[0]
    st.name = x[1]
    st.surn = x[2]
    st.bal = list(map(int, x[3].split()))
    St.append(st)
    print(st.fam, st.name, st.surn, *st.bal)
fout = open('students.dat', 'wb')
pickle.dump(St, fout)
fout.close()
f.close()
