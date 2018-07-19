import java.awt.Graphics;
public class Circle {



    private Point loc;
    private int radius;
    public final static double PI = 3.14159;


    public Circle() {
        this.loc= new Point(0,0);
        this.radius = 10;
    }


    public Circle(Point loc, int radius) {
        this.loc = loc;
        this.radius = radius;
    }


    public Point getLoc() {
        return loc;
    }

    public double getRadius() {
        return radius;
    }

    public double getPI() {
        return PI;
    }

    public double getCircumfrence(){
        return 2*PI*radius;
    }


    public double getArea(){
        return PI*radius*radius;

    }

    public void Draw(Graphics g){
        g.fillOval(loc.getX(),loc.getY(),2*radius,2*radius);

    }

}
