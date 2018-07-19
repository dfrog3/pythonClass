public class Runner {

    public static void main(String[] args) {
        Rectangle r = new Rectangle(5, 1);
        System.out.println(r.getArea());
        BankAccount b = new BankAccount("bob", 100000);
        b.makeDeposite(1300);
        b.makeTransaction(1000);
        b.getBalance();



        /*
        Point p = new Point();
        Point other = new Point();
        p.x = 5.0;
        p.y = 0;
        other.x = -7.0;
        other.y = -200;
        p.printCoordinates();*/
    }
}