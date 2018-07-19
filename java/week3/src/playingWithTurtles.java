import java.awt.*;
import java.util.stream.Collector;

public class playingWithTurtles {
    public static void square(Turtle jake ) {
        for(int i = 0; i<50;i++){
            jake.forward(i);
            jake.turnRight(144);


        }

    }

    public static void shape(Turtle bob, int sides, int size) {
        double angles = 360.0/sides;
        for(int i = 0; i < sides; i++){
            bob.forward(size);
            bob.turnLeft(angles);
        }


    }




    public static void main(String[] args) {
        World worldNameVariable = new World();
        Turtle james = new Turtle(worldNameVariable);
        /*Turtle david = new Turtle(worldNameVariable);
        Turtle mike = new Turtle(worldNameVariable);
        Turtle pike = new Turtle(worldNameVariable);
        mike.turnLeft(180);
        david.turnLeft(90);
        james.turnRight(90);
        square(mike);
        square(david);
        square(james);
        square(pike);*/
        //shape(james,8,100);
        int x = 10;
        for (int i = 0; i < 100; i++){

            james.forward(x);
            james.turnLeft(90);
            x += 10;
            james.setColor(new Color(x,10,10));
        }






    }
}
