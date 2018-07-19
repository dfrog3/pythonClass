import java.util.Arrays;
import java.util.Scanner;

public class Game {
    public static void main(String[] args) {
        boolean again = true;
        while (again){
            Scanner keyboard = new Scanner(System.in);
            String move;
            String tile="";
            boolean turn = true;
            Board b = new Board();
            while( b.wonGame().equals("no")){
                if (b.getTURN()){
                    tile = b.getO();
                }else{
                    tile = b.getX();
                }
                b.printGrid();
                System.out.println("It\'s " + tile +"\'s turn.\nPlease enter a coordinate.");
                move = keyboard.nextLine();
                move = b.cordConverter(move);
                if (move.equals("error")){
                    System.out.println("I didn\'t understand that.");
                    continue;
                }
                b.updateGrid(move);



            }
            System.out.println(tile+" wins!");
            b.printGrid();
            System.out.println("play again? enter: true for yes / any key for no");
            again = keyboard.hasNextBoolean();






        }





    }







}
