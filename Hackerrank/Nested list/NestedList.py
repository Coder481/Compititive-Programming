#https://www.hackerrank.com/challenges/nested-list/problem
if __name__ == '__main__':
    l=[]
    ln=[]
    ls=[]
    rl=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name,score])
        rl.append([score,name])
        ln.append(name)
        ls.append(score)
ls.sort()
rl.sort()
#ls=[20,23,23]
#rl=[[20,'abg'],[23,'dfg'],[23,'dtg']]
for i in range(1,len(ls)+1):
    if ls[0]==ls[i]:
        continue
    else:
        ele=rl[i]
        print(ele[1])
        for j in range(i,len(rl)):
            try:
                if ls[j]==ls[j+1]:
                  el=rl[j+1]
                  print(el[1])
                  continue
                else:
                    break
            except:
                break
        break




