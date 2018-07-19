import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;



public class pizza {
    public static String PizzaBox(List<String> pizzaNames, List<String> pizzaPrices, Boolean chicagox) {
        Double king = Double.valueOf(pizzaPrices.get(0));
        int kingsMark = 0;
        double contender;
        int counter = 0;
        for (String i : pizzaPrices)
            counter = counter + 1;
        for (int i = 0; i < counter; i++) {
            contender = Double.valueOf(pizzaPrices.get(i));
            if (king < contender) {
                continue;
            } else {
                king = contender;
                kingsMark = i;
            }

        }
        if(chicagox){
            return "The best deal is "+ pizzaNames.get(kingsMark) + "'s pizza at $" + String.valueOf(king) + " per cube inch.";
        }else{
            return "The best deal is "+ pizzaNames.get(kingsMark) + "'s pizza at $" + String.valueOf(king) + " per square inch.";
        }

    }




    public static String printer(String ppsenchi ) {
        String toPrint = "";
        boolean round = false;
        int x = ppsenchi.length();
        for(int i = 0;i<x;i++){
            String check = ppsenchi.substring(i,i+1);
            toPrint = toPrint + check;
            if (check.equals(".")){
                x = i + 3;
                if((Integer.valueOf(ppsenchi.substring(i+3,i+4)))>5){
                    round = true;

                }
            }
        }
        if (round){
            toPrint = String.valueOf(00.01+ Double.valueOf(toPrint));
        }

        return toPrint;

    }

    public static String Kakaku(double okisa, double price) {
        double ppsenchi = (price / okisa);
        return String.valueOf(ppsenchi);


    }




    public static double Okisa(double diamater, double depth) {
        return Math.PI *((diamater/2) * (diamater/2)) * depth;


    }


    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        List<String> pizzaPrices = new ArrayList<>();
        List<String> pizzaNames = new ArrayList<>();
        System.out.println("Are these pizzas from Chicago? \"yes\" or \"no\"?");
        boolean chicagox = false;
        boolean keep = true;
        while(keep) {
            String chicago = keyboard.next();
            if (chicago.equals("yes")) {
                chicagox = true;
                keep = false;
            } else if (chicago.equals("no")) {
                chicagox = false;
                keep = false;
            } else {
                System.out.println("Could you say that again?");
            }

        }


        while(1>0){

            System.out.println("Who made this pizza?");
            String pizzaName = keyboard.next();
            System.out.println("How many inches is the diameter of this pizza？");
            double diameter = keyboard.nextDouble();
            double depth = 1;
            if (chicagox) {
                System.out.println("How deep is this pizza?");
                depth = keyboard.nextDouble();
            }
            double okisa = Okisa(diameter, depth);
            System.out.println("How much is the pizza？");
            double price = keyboard.nextDouble();

            String ppsenchi = Kakaku(okisa, price);
            if (chicagox){
                System.out.println("This pizza costs $" + printer(ppsenchi)+" per inches cubed.");
            } else {
                System.out.println("This pizza costs $" + printer(ppsenchi) + " per inches squared.");
            }
            pizzaNames.add(pizzaName);
            ppsenchi = printer(ppsenchi);
            pizzaPrices.add(ppsenchi);







            System.out.println("Any more pizzas?");
            System.out.println("Type \"yes\" for more. Type \"no\" to find the best deal.");
            int x = 2;
            while (x>1) {
                String test = keyboard.next();
                if(test.equals("yes")) {
                    x = 1;
                }else if(test.equals("no")){
                    x = 0;
                }else{
                    System.out.println("Could you say that again?");
                }

            }
            if (x == 1){
                continue;
            } else if(x ==0){
                break;
            }










        }
        System.out.println( PizzaBox(pizzaNames, pizzaPrices, chicagox));
    }
}
