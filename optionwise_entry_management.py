class Sequence:

    def __init__(self, ID, seq_type, sequence, entry_year):
        self.ID=ID
        self.seq_type=seq_type
        self.sequence=sequence
        self.entry_year=entry_year

    def print_info(self):
        print ("ID: " + str(self.ID) + "\nSEQ_TYPE: " + self.seq_type + "\nSEQUENCE: " + self.sequence + "\nENTRY YEAR: " + str(self.entry_year))
        
    def validate(self):
        biotype=self.seq_type.upper()
        if biotype == "DNA" or biotype == "RNA":
            print ("\nAppropriate sequence type")
        else:
            print ("\nNon biological sequence type!")

print("How do you wish to proceed?: " + "\n\n1.Register new sequence" + "\n2.Delete a sequence" + "\n3.Print a sequence" + "\n4.Close and exit")

choice=int(input("\nType a number: "))

import mysql.connector as mysql
mydb=mysql.connect(host="localhost",user="root",passwd="",db="test")
cur=mydb.cursor()

if choice==1:
    new_seq_ID=int(input("Insert new sequence's ID: "))
    new_seq_type=input("Insert new sequence's type: ")
    new_seq_type=new_seq_type.upper()
    new_seq_sequence=input("Insert new sequence: ")
    new_seq_entry_year=int(input("Insert new sequence's registration year: "))
    new_seq=Sequence(new_seq_ID,new_seq_type,new_seq_sequence,new_seq_entry_year)
    new_seq.validate()
    if new_seq_type!="DNA" and new_seq_type!="RNA":
        exit()
elif choice==2:
    del_id=int(input("Provide sequence's ID for deletion: "))
    try:
        del_id_ex=cur.execute("SELECT FROM sequence WHERE ID = %s" %(del_id))
    except:
        print("Error! Non existent ID")
    else:
        cur.execute("DELETE FROM sequence WHERE ID = %s" %(del_id))    
elif choice==3:
    print_opt=int(input("Provide sequence's ID to print: "))
    cur.execute("""SELECT * FROM sequence WHERE ID= %s""" %(print_opt))
    ch3_sel=cur.fetchall()
    pr_ID=ch3_sel[0][0]
    pr_seq_type=ch3_sel[0][1]
    pr_sequence=ch3_sel[0][2]
    pr_entry_year=ch3_sel[0][3]
    pr_obj=Sequence(pr_ID,pr_seq_type,pr_sequence,pr_entry_year)
    pr_obj.print_info()
elif choice==4:
    cur.execute("""SELECT * FROM sequence""")
    results=cur.fetchall()
    for i in range(0,len(results)): print(results[i])
    exit()
