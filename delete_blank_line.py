filename = "sample.txt"
output_filename = "no_blank.txt"
with open(filename,'r',encoding='UTF-8') as f:
    line_lists = f.read().splitlines()

line_lists = [i for i in line_lists if i!='']
data="\n".join(line_lists)

with open(output_filename,'w',encoding='UTF-8') as f:
    f.write(data)