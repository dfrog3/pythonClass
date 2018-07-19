import java.util.Scanner;

// doesn't accept ints longer than 9 or ten.

public class NUmberOfDigits {
    public static void ToBeCalledInMain() {
        Scanner keyboard = new Scanner(System.in);
        System.out.println("give me an int");
        int ourInt = Integer.valueOf(keyboard.next());
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
        System.out.println(answer);
    }
    public static void main(String[] args) {
        ToBeCalledInMain();

    }
}
