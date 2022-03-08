print('''
██╗░░░██╗███████╗███████╗███╗░░██╗░█████╗░  ██████╗░░█████╗░██╗
██║░░░██║██╔════╝██╔════╝████╗░██║██╔══██╗  ██╔══██╗██╔══██╗██║
╚██╗░██╔╝█████╗░░█████╗░░██╔██╗██║██║░░██║  ██████╔╝███████║██║
░╚████╔╝░██╔══╝░░██╔══╝░░██║╚████║██║░░██║  ██╔══██╗██╔══██║██║
░░╚██╔╝░░███████╗███████╗██║░╚███║╚█████╔╝  ██║░░██║██║░░██║██║
░░░╚═╝░░░╚══════╝╚══════╝╚═╝░░╚══╝░╚════╝░  ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝''')
print()
with open("website.txt",'r') as f:
    print("IP\t\t\tDate_Time\t\t\tRequest\t\tProtocol\tSuccess\tSize\tUser_agent\n\n")
    lines=f.readlines()
    for i in lines:
        i=i.replace('"',"")
        i=i.replace("[","")
        i=i.replace("]","")
        line=i.split()
        for j in range (len(line[0]),16):
            print(" ",end="")
        print(f"{line[0]}\t{line[3]+line[4]}\t{line[5]}\t\t{line[7]}\t{line[8]}\t{line[9]}\t{line[11]}")
f.close()

