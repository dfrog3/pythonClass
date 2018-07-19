import java.util.Scanner;

public class rot13 {
    public static String crypt(String toCrypt) {
        String outputJar = "";
        String alpha ="abcdefghijklmnopqrstuvwxyz";
        for(int i = 0; i< toCrypt.length(); i++){
            if (toCrypt.substring(i,i+1).equals(" ")){
                outputJar = outputJar + " ";
                continue;
            }
            for (int j = 0; j< alpha.length(); j++){

                if (toCrypt.substring(i,i+1).equals(alpha.substring(j,j+1))){
                    int x = j;
                    x += 13;
                    if(x>26){
                        x -= 26;
                    }
                    outputJar = outputJar + alpha.substring(x,x+1);

                }
            }
        }
        return outputJar;

    }
    public static String dcrypt(String toCrypt) {
        String outputJar = "";
        String alpha ="abcdefghijklmnopqrstuvwxyz";
        for(int i = 0; i< toCrypt.length(); i++){
            if (toCrypt.substring(i,i+1).equals(" ")){
                outputJar = outputJar + " ";
                continue;
            }
            for (int j = 0; j< alpha.length(); j++){
                if (toCrypt.substring(i,i+1).equals(alpha.substring(j,j+1))){
                    int x = j;
                    x -= 13;
                    if(x<0){
                        x += 26;
                    }
                    outputJar = outputJar + alpha.substring(x,x+1);

                }
            }
        }
        return outputJar;

    }



    public static void main(String[] args) {

        while (1>0){
            System.out.println("are we encrypting or decrypting?(\"e\"/\"d\"");
            Scanner keyboard = new Scanner(System.in);
            while(1>0){
                String mode = keyboard.nextLine();
                if(mode.equals("e")){
                    System.out.println("give me a word");
                    System.out.println(crypt(keyboard.nextLine()));
                    break;

                } else if(mode.equals("d")){
                    System.out.println("give me a word");
                    System.out.println(dcrypt(keyboard.nextLine()));
                    break;
                }else{
                    System.out.println("could you say that again");
                }
            }


        }
    }
}
