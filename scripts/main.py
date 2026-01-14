import random
alter_metirial=open('data/p53_sequence.fa','r')
alter_metirial2=''


DNA_codon_table = dict () 
def Read_dict():
  file1 = open('data/codon_to_amino','r')
  for line in file1:
    part=line.split("\t")
    part1=part[0].rstrip("\n\r")
    part2 = part[1].rstrip("\n\r")
    DNA_codon_table[part1]=part2
  file1.close()
  return DNA_codon_table

DNA_codon_table = Read_dict()


for line in alter_metirial:
    if line[0] != ">":
        line=line.rstrip()
        alter_metirial2 = alter_metirial2 + line
i=0
amino_seq=""
curr_codon=""
while i<= len(alter_metirial2)-3:
    curr_codon=alter_metirial2[i]+alter_metirial2[i+1]+alter_metirial2[i+2]
    amino_seq = amino_seq + DNA_codon_table[curr_codon]
    i=i+3

alterd_metirial=alter_metirial2
print_sqwenceopen=open('results/p53_sequence.fa','w')
print_sqwenceopen.write("results/unolterd amino seqwence:")
print_sqwenceopen.write("\n")
print_sqwenceopen.write(amino_seq)
print_sqwenceopen.write("\n")


g=0
while g<=3:
    g=g+1
    base_list = ['A','T','G','C']
    randy=random.randrange(0,len(alterd_metirial))
    base_list.remove(alterd_metirial[randy])
    loock=random.randrange(0,3)
    new_base=base_list[loock]
    alterd_metirial=alterd_metirial[:randy]+new_base+alterd_metirial[randy+1:]


k=0
amino_seq2=""
while k<= len(alterd_metirial)-3:
    curr_codon=alterd_metirial[k]+alterd_metirial[k+1]+alterd_metirial[k+2]
    amino_seq2 = amino_seq2 + DNA_codon_table[curr_codon]
    k=k+3

print_sqwenceopen.write("results/alterd amino seqwence:")
print_sqwenceopen.write("\n")
print_sqwenceopen.write(amino_seq2)

if amino_seq2 == amino_seq:
  print_sqwenceopen.write("\n")
  print_sqwenceopen.write("the mutetad seqwence is the same length")
elif amino_seq2 < amino_seq:
  print_sqwenceopen.write("\n")
  print_sqwenceopen.write("the mutetad seqwence is shorter")