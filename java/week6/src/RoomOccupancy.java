public class RoomOccupancy {
    private int NUMBERiNrOOM;
    private static int TOTALnUMBER;





    public void addOneToRoom(){
        NUMBERiNrOOM += 1;
        TOTALnUMBER +=1;



    }

    public void removeOneFromRoom() {

        NUMBERiNrOOM -= 1;
        if (NUMBERiNrOOM<0){
            NUMBERiNrOOM = 0;
        }


        TOTALnUMBER -=1;
        if (TOTALnUMBER <0){
            TOTALnUMBER = 0;
        }
    }



    public int getNumber(){
        return NUMBERiNrOOM;
    }

    public int getTOTALnUMBER() {
        return TOTALnUMBER;
    }
}
