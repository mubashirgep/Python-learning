# write a code for letter using replacment method.
letter = '''
\tTo: SDO <SD>,
\tFrom: SSO-I on duty,
\tSubject: BREAKDOWN on <FDR> feeder (CODE <CODE>),
Respected Sir,
\tIt is inform to your good office that <FDR> <CODE> feeder is tripped off and relay showing <FLT> fault.
After 5 minuts of delay try to close the VCB of <FDR> feeder it did not hold, try to close two more
times but the same <FLT> fault occours.
Now declare the above mantioned feeder under breakdown and tag the B/D caution on VCB.
Please depute your line staff to patrol the line and meet with the fault and resolve
the metter on urgent basis.
\n\t\t\t\t<NAME>,
\t\t\t\t<DESG>,
\t\t\t\t132KV Grid Station Eminabad,
\t\t\t\tGujranwala,
\t\t\t\t<DATE>,
\n\n\n\t\t\t\tSignature ____________.
'''
# Make the veriables which are replaced using input method
name = input("Enter your name:\n")
desg = input("Enter your designation:\n")
sd = input("Enter Subdivision name:\n")
fdr = input("Enter feeder name:\n")
flt = input("Enter fault on relay:\n")
code = input("Enter feeder code:\n")
date = input("Enter date:\n")

# applying the replacement method
letter=letter.replace("<NAME>", name)
letter=letter.replace("<DESG>", desg)
letter=letter.replace("<SD>", sd)
letter=letter.replace("<FDR>", fdr)
letter=letter.replace("<FLT>", flt)
letter=letter.replace("<CODE>", code)
letter=letter.replace("<DATE>", date)

print(letter)
