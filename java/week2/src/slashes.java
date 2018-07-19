import java.util.Scanner;

public class slashes {
    public static final void banana(){
        Scanner keyboard = new Scanner(System.in);
        System.out.println("give me an int");
        int base = keyboard.nextInt();
        int rowLength;
        rowLength = rowFinder(base); // gives us the number of char
        int x = rowLength;




        for(int i = 0; i < base +1; i++ ){ //makes lines
            String point = "";
            point = "";// resets !
            for(int j = 0; j < x; j++){ // makes !
                point = point +"!";
            }
            x = x - 4; // makes ! smaller




            String slash1 = ""; // reset slash 1 and 2 / \
            String slash2 = "";
            slash1 = "";
            slash2 = "";

            if(i != base){ //checking for the last itteration
                for(int j = 0; j < i; j++ ){// make slashes
                    slash1 = slash1 + "\\\\";
                    slash2 = slash2 + "//";
                }
            }else{ // prevents final line from being printed
                break;


            }
            System.out.println(slash1 + point + slash2);

        }


    }


    public static int rowFinder(int base){ // gives us char length
        int length = 2;
        for(int i = 1; i < base; i++){
            length = length +4;
        }
        return length;
    }


    public static void main(String[] args) {

        banana();


    }





}
