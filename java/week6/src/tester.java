public class tester {

    public static void main(String[] args) {

        RoomOccupancy a = new RoomOccupancy();
        RoomOccupancy b = new RoomOccupancy();
        RoomOccupancy c = new RoomOccupancy();
        RoomOccupancy d = new RoomOccupancy();


        for (int i = 0; i < 3; i++) {
            a.addOneToRoom();

        }

        for (int i = 0; i < 5; i++) {
            b.addOneToRoom();

        }

        for (int i = 0; i < 10; i++) {
            c.addOneToRoom();

        }

        for (int i = 0; i < 15; i++) {
            d.addOneToRoom();

        }

        d.removeOneFromRoom();
        d.removeOneFromRoom();

        System.out.println(a.getNumber()+" "+a.getTOTALnUMBER());
        System.out.println(b.getNumber()+" "+b.getTOTALnUMBER());
        System.out.println(c.getNumber()+" "+c.getTOTALnUMBER());
        System.out.println(d.getNumber()+" "+d.getTOTALnUMBER());
        System.out.println("this was room occupanc\nNext is fake numbers");





        FakeNumber num1 = new FakeNumber(200,200);
        FakeNumber num2 = new FakeNumber(400,400);


        System.out.println("add "+num1.addFakeNumbers(num2).getFakeNumber());
        System.out.println("subtract "+ num1.subtractFakeNumbers(num2).getFakeNumber());
        System.out.println("multiply "+ num1.multiplyFakeNumbers(num2).getFakeNumber());
        System.out.println("divide "+ num1.divideFakeNumbers(num2).getFakeNumber());






    }



}
