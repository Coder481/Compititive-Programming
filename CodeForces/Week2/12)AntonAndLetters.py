#https://codeforces.com/contest/443/problem/A
s=input()
st=set()
count=0
for i in range(1,len(s)):
    if i==1:
        if s[1]!='}':
            st.add(s[i])
    if  count==3:
        st.add(s[i])
        count=0
    count+=1
print(len(st))
