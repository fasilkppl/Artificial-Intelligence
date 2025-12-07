import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser() #creates an ArgumentParser object
    parser.add_argument("--physics", required=True, help="physics marks") #adding arguments to object
    parser.add_argument("--chemistry", required=True, help="chemistry marks")
    parser.add_argument("--maths", required=True, help="maths marks")
    #so this takes 3 arguments


    args = parser.parse_args() #parses the command-line input you provide and stores it in an object called args, eg physics marks = 45 it parses 45 and stores it in args variable.

    print(args.physics) #printing the inputed marks (default inputs are strings)
    print(args.chemistry)
    print(args.maths)

    print("Average mark of three subjects is : ", (
        int(args.physics) + int(args.chemistry) + int(args.maths)
    ) / 3) 
   # The three marks are added together. The total is divided by 3 to get the average.The average is printed


   #this is run by python3 cmd_args.py --physics 60 --chemistry 70 --maths 90
