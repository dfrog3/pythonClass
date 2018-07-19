import java.util.Scanner;

public class digitArm {
    public static void ToBeCalledInMain() {
        Scanner keyboard = new Scanner(System.in);
        int number1 = 0;
        int number2 = 0;
        int number3 = 0;

        System.out.println("please enter a three digit int");
        String y = keyboard.next();
        int x = Integer.parseInt(y);

        if( y.length() != 3){
            System.out.println("This is not a 3 digit number");


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

                System.out.println("This is an Armstrong number");

            } else{
                System.out.println("This is not an Armstrong number");
            }
        }
    }
    public static void main(String[] args) {
        ToBeCalledInMain();
    }
}
