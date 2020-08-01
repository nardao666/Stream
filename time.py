import time

#Entre com o tempo para contagem regressiva
tempo ="02:50"
x = tempo.split(':')
y = int(x[0])
t = int(x[1])

if t >= 60:
    t = t - 60
    y += 1
arquivo = open('tempo.txt','w')
timer = '{:02d}:{:02d}'.format(y, t)
arquivo.write(str(timer))
arquivo.close
#print(str(timer))

for minutos in range(y,-1,-1):
    for segundo in range(t,-1,-1):
        timer = '{:02d}:{:02d}'.format(minutos, segundo)
        arquivo = open('tempo.txt','w')
        arquivo.write(str(timer))
        arquivo.close
 #       print(str(timer))
        time.sleep(1)
    t=59
timer = '{:02d}:{:02d}'.format(minutos, segundo)
arquivo = open('tempo.txt','w')
arquivo.write(str(timer))
arquivo.close



    
