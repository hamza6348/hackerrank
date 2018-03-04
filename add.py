n = input()
s = set(map(int, raw_input().split())) 
num=raw_input()
sum1=0
for i in range(int(num)):
    command=raw_input()
    if(command=='pop'):
        
        s.pop()
    elif(command[0]=='r'):
        op=command.split(' ')
        r=int(op[1])
        s.remove(r)
    elif(command[0]=='d'):
        op=command.split(' ')
        r=int(op[1])
        s.discard(r)    
for em in s:
    sum1=sum1+em
print sum1    
