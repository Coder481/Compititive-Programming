def split_and_join(line):
    line=line.split()
    line='-'.join(line)
    return line
string=input()
output=split_and_join(string)
print(output)
