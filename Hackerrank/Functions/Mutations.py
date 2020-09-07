#https://www.hackerrank.com/challenges/python-mutations/problem
def mutate_string(string, position, character):
    return string[:position]+character+string[position+1:]
s,p,c=input(),int(input()),input()
output=mutate_string(s,p,c)
print(output)
