# Driver: Julia Sales
# Navigator: Anthony Overton
# HW5 Problem 5

def print_yourName(name, boolean=None):
        if boolean is None:
            print name[0].capitalize() + " " + name[1].capitalize()
        elif boolean is True:
            print name[0].capitalize() + " " + name[1].capitalize()
        elif boolean is False:
            print name[1].capitalize() + " " + name[0].capitalize()
   
print_yourName(['julia', 'sales'])
print_yourName(['julia', 'sales'], False)
print_yourName(['julia', 'sales'], True)
