import java.util.Scanner;

public class numberOfVowels {
    public static void ToBeCalledInMain() {
        System.out.println("give me a string");
        Scanner keyboard = new Scanner(System.in);
        String userString = keyboard.nextLine();
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
        System.out.println(x);
    }
    public static void main(String[] args) {
        ToBeCalledInMain();




    }



}
