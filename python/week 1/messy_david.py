def main():
    print("It’s time to go on a scavenger hunt!") 
    print("You'd be amazed how many things can go wrong!") 
    print("Please enter how long you want to travel for:")
main()
initialPos = 7.0;
time = float(input());
velocity = 5.0;
acceleration = 1.0;
# there is no error here causing any problems
# an incorrect answer in the line below does not exsist
position = initialPos + velocity * time + .5 *acceleration*time*time;
#if you are stuck on the math error, look at the footnote print(position);
print("your new postion is: " + str(position))
 
