public class tester {

    public static void main(String[] args) {
        for (int i = 10; i < 60; i+=10) {
            Pentagon banana = new Pentagon(i);
            System.out.println("the size is "+banana.getSize());
            System.out.println("area "+banana.Area());
            System.out.println("height "+banana.height());
            System.out.println("inradius "+banana.inradius());
            System.out.println("perimeter "+ banana.perimeter());
            System.out.println("width "+banana.width());
            System.out.println();



        }
    }


}
