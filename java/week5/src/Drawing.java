
import java.awt.*;
import javax.swing.*;





public class Drawing extends Canvas  {
    public static void main(String[] args) {
        JFrame frame = new JFrame("My Drawing");
        Canvas canvas = new Drawing();
        canvas.setSize(400, 400);
        frame.add(canvas);
        frame.pack();
        frame.setVisible(true);
        frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
    }

    public void paint(Graphics g) {
        //g.fillOval(100, 100, 200, 200);
        Point p1 = new Point(1, 2);
        Point p2 = new Point(100,100);
        g.drawLine(p1.getX(),p1.getY(),p2.getX(),p2.getY());
        g.setColor(Color.red);
        Rectangle[] rex = new Rectangle[50];
        for (int i = 0; i < rex.length; i++) {
            rex[i]=new Rectangle(10*(i+1),10,new Point(10,i*20));
            rex[i].Draw(g);

        }

        Circle c = new Circle(new Point(100,100),10);
        Circle[][] circles = new Circle [40][40];
        for (int i = 0; i < circles.length; i++) {
            for (int j = 0; j <circles[i].length ; j++) {
                circles[i][j] = new Circle(new Point(i*20,j*20),10);
                circles[i][j].Draw(g);

            }

        }
        System.out.println("!");



    }










}
