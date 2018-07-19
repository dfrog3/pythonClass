import java.util.Scanner;

public class allLoops {
    public static int digits(int ourInt) {


        //doesnt work with keyboard.next()
        String jar = String.valueOf(ourInt);
        int ourIntLen = jar.length();
        int answer = 0;
        if(ourInt<0){
            ourInt = ourInt* -1;
            ourIntLen -=1;
        }


        for (int i = 0; i < ourIntLen; i++ ){//splits the number and counts digits
            int base = ourInt % 10;
            ourInt = ourInt / 10;
            int x = base;
            if(base != 0){
                for(int j = 1; j < x; j++){
                    base -= 1;
                }
            }else{
                base += 1;
            }
            answer = answer + base;
        }
        return answer;
    }

    public static int vowelse(String userString) {

        int toScan = userString.length();
        userString = userString.toLowerCase();
        int x = 0;
        String vowels = "aeiou";
        for(int i = 0; i < toScan; i++){
            for( int j = 0; j< 5; j++){
                if (userString.substring(i, i+1).equals(vowels.substring(j, j+1))){
                    x += 1;
                }
            }
        }
        return x;
    }
    public static String Tarms(String y) {
        int number1 = 0;
        int number2 = 0;
        int number3 = 0;


        int x = Integer.valueOf(y);

        if( y.length() != 3){
            return "This is not a 3 digit number";


        }else{
            int counter = x;
            for(int i = 0; i < 3; i++){
                int j = counter % 10;
                counter = counter / 10;
                if(i ==0){
                    number3 = j;

                }else if(i == 1){

                    number2 = j;
                }else{

                    number1 = j;
                }
            }
            if( (number1 * number1 * number1 + number2 * number2 * number2 + number3 * number3 * number3) == x){

                return "This is an Armstrong number";

            } else{
                return "This is not an Armstrong number";
            }
        }
    }

    public static boolean DiffrentChecker( int digit1, int digit10, int digit100, int digit1000 ){

        int[] digits = {digit1, digit10, digit100, digit1000};
        for (int i = 0; i < 4; i++){
            for(int j = i +1; j < 4; j++ ){
                if (digits[i] == digits[j]){
                    return false;
                }
            }
        }
        return true;
    }

    public static int ToBeCalledInMain(){
        int digit1 = -1;
        int digit10 = 0;
        int digit100 = 0;
        int digit1000 = 0;
        boolean diffrent = false;
        boolean SUM = false;

        while(!(SUM && diffrent)){//main loop
            digit1 += 2; //digit1 increase
            if (digit1 > 9){ //checks digit1 out of bounds and resets
                digit1 = 1;
            }


            if(digit1 + digit10 + digit100 + digit1000 == 27){//checks for correct sum
                SUM = true;
            }else{
                SUM = false;
            }
            diffrent = DiffrentChecker(digit1, digit10, digit100, digit1000); //checks for same int
            if(SUM && diffrent){ //finishes program if correct answer is found
                break;
            }


            digit10 += 1;//adds one to digit10
            if (digit10 > 3){//resest digit10
                digit10 = 0;
            }
            digit1000 = digit10 * 3;//calculates digit1000



            if(digit1 + digit10 + digit100 + digit1000 == 27){//checks for correct sum
                SUM = true;
            }else{
                SUM = false;
            }
            diffrent = DiffrentChecker(digit1, digit10, digit100, digit1000); //checks for same int
            if(SUM && diffrent) { //finishes program if correct answer is found
                break;
            }


            digit100 += 1;//manages digit 100
            if (digit100 > 9){
                digit100 = 1;
            }// manages digit 100



            if(digit1 + digit10 + digit100 + digit1000 == 27){//checks for correct sum
                SUM = true;
            }else{
                SUM = false;
            }
            diffrent = DiffrentChecker(digit1, digit10, digit100, digit1000); //checks for same int
            if(SUM && diffrent) { //finishes program if correct answer is found
                break;
            }
        }
        return (digit1*1)+(digit10*10)+(digit100*100)+(digit1000*1000); //prints final answer
    }






    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        System.out.println("give me an int");
        int ourInt = Integer.valueOf(keyboard.next());
        System.out.println(digits(ourInt));

        System.out.println("give me a string");
        String userString = keyboard.next();
        System.out.println(vowelse(userString));

        System.out.println("please enter a three digit int");
        String y = keyboard.next();
        System.out.println(Tarms(y));


        System.out.println(ToBeCalledInMain());




    }
}
