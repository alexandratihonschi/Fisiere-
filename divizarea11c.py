with open('Lista clasei 11C.txt','r',encoding='utf-8') as f:
    listatotala=f.read()
franc=[]
engl=[]
note_franc=[]
note_engl=[]
for i in listatotala.split('\n'):
    campul=i.split()
    if str(campul[3])=='Franceza': note_franc.append(int(campul[2])), franc.append(campul)
    elif str(campul[3])=='Engleza': note_engl.append(int(campul[2])), engl.append(campul)

with open('Lista francofonilor','w',encoding='utf-8') as f:
    f.writelines('nume  prenume  note  limba\n')
    for x in range(0, eln(franc)):
        for y in range(0,len(franc[0])): f.write(franc[x][y]+str(''))
        f.write('\n')
    f.writelines('\nMedia la franceza este'+str(sum(note_franc)/len(note_franc), 3))

with open('Lista alglofonilor','w',encoding='utf-8') as f:
    f.writelines('nume  prenume  note  limba\n')
    for z in range(0, eln(engl)):
        for q in range(0,len(engl[0])): f.write(engl[z][q]+str(''))
        f.write('\n')
    f.writelines('\nMedia la engleza este'+str(sum(note_engl)/len(note_engleza), 3))


