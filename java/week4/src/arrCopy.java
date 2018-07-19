public class arrCopy {

    public static int[] copyIntArr(int[] toCopy){
        int[] newBoy = new int[toCopy.length];
        for (int i = 0; i < toCopy.length; i++) {
            newBoy[i]=toCopy[i];

        }
        return newBoy;
    }



    public static double[] copyDoubleArr(double[] toCopy){
        double[] newBoy = new double[toCopy.length];
        for (int i = 0; i < toCopy.length; i++) {
            newBoy[i]=toCopy[i];

        }
        return newBoy;
    }



    public static String[] copyStringArr(String[] toCopy){
        String[] newBoy = new String[toCopy.length];
        for (int i = 0; i < toCopy.length; i++) {
            newBoy[i] = toCopy[i];

        }
        return newBoy;
    }








}
