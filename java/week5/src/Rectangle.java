//package objects;

import java.awt.*;

public class Rectangle {





    Point topLeft;





    // Attributes
    int length, height;


    // Constructor
    public Rectangle(int initialLength, int initialHeight) {
        length = initialLength;
        height = initialHeight;
        topLeft = new Point(0,0);
    }

    public Rectangle(int initialLength, int initialHeight, Point corner){
        length = initialLength;
        height = initialHeight;
        topLeft = corner;




    }






    // Behaviors

    public double getPerimeter(){
        return 2*height +2*length;
    }

    public double getArea() {
        return length*height;
    }

    public String toString() {
        return "I am a rectangle with length " + length + " and height "  + height;
    }



    public void Draw(Graphics g){
        g.fillRect(this.topLeft.getX(),this.topLeft.getY(),this.length,this.height);


    }


}