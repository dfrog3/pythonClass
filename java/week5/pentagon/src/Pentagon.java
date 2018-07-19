import java.math.*;
public class Pentagon {

    private double size;


    public Pentagon(double size) {
        this.size = size;
    }

    public double getSize() {
        return size;
    }

    public void setSize(double size) {
        this.size = size;
    }

    public double perimeter(){
        return size*5;
    }

    public double height(){
        return (Math.sqrt(5+2*Math.sqrt(5))/2)*size;
    }

    public double inradius(){
        return size/(2*Math.tan(Math.PI/5));
    }



    public double Area(){
        return .5*perimeter()*inradius();
    }

    public double width(){
        return  ((1+ Math.sqrt(5))/ 2)*size;
    }



}
