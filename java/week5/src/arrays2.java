import java.util.Arrays;
public class arrays2 {




    public static int[] bubbleSort(int[] theArray) {

        int counter = theArray.length;
        int box = 0;

        for(int i=0; i < counter; i++){

            for(int j=1; j < (counter-i); j++){

                if(theArray[j-1] > theArray[j]){
                    box = theArray[j-1];
                    theArray[j-1] = theArray[j];
                    theArray[j] = box;
                }
            }
        }
        return theArray;

    }


    public static void sortAll(int[][] myArrays) {
        for (int i = 0; i < myArrays.length ; i++) {
           myArrays[i] = bubbleSort(myArrays[i]);
        }
    }


    public static int[][] matrixSum(int[][] one, int[][] two) {
        int[][] out= new int[one.length][one[0].length];
        for (int i = 0; i < one.length; i++) {
            for (int j = 0; j < one[0].length; j++) {
                if (one.length != two.length|| one[i].length != two[i].length){
                    return null;
                }
                out[i][j] = one[i][j] + two[i][j];
            }

        }
        return out;

    }






    public static void main(String[] args) {
        int[][] aroar = new int[10][10];
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10 ; j++) {
                aroar[i][j] = 10-j;

            }

        }
        int[][] test1 = new int[9][9];
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9 ; j++) {
                test1[i][j] = 9-j;

            }

        }


        System.out.println(Arrays.toString(aroar[0]));
        sortAll(aroar);
        System.out.println(Arrays.toString(aroar[9]));
        System.out.println(Arrays.toString(matrixSum(aroar,aroar)[0]));
        try{
            System.out.println(Arrays.toString(matrixSum(aroar,test1)[0]));
        } finally {
            System.out.println("null");
        }




    }


}
