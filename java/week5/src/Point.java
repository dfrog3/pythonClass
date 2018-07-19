public class Point {

    // Attributes
    // What the object has
    private int x;
    private int y;

    // Constructors
    // How to build an object
    public Point(int initX, int initY) {
        x = initX;
        y = initY;
    }
    public Point(){
        this(0,0);
    }


    //Behaviors
    //What the object can do
    public void printCoordinates(){

        System.out.println(x + " " + y);
    }

    public int getX() {
        return x;
    }


    public int getY(){
        return y;
    }





}