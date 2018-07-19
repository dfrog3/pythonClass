import java.util.Arrays;
import java.util.Random;

public class sort {


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



    public static void swap(int[] arr, int i, int j){
        int temp = arr[i];
        arr[i] =arr[j];
        arr[j] = temp;
    }

    public static void selectSort(int[] tosort){
        for (int i = 0; i < tosort.length; i++) {
            int indexOfMin = i;
            for (int j = i; j < tosort.length; j++) {
                if( tosort[j] < tosort[indexOfMin] ){
                    indexOfMin =j;
                }

            }
            swap(tosort,indexOfMin,i);

        }

    }




    public static void insertionSort(int[] tosort){

        for (int i = 0; i <tosort.length-1 ; i++) {
            //System.out.println(i);
            //System.out.println(tosort[i]);
            //System.out.println("   "+ (i+1));
            //System.out.println("   "+ (tosort[i+1]));
            if(tosort[i]>tosort[i+1]){
                swap(tosort,i,i+1);
                if (i==0){
                    i=-1;
                    continue;
                }else if (i==1){
                    i=-1;
                    continue;
                }
                i -= 3;
            }

        }
    }










    public static void main(String[] args) {
        int[] box = new int[50];
        for (int i = 0; i <50 ; i++) {
            Random rand = new Random();
            int value = rand.nextInt(50);
            box[i] = value;

        }
        System.out.println(Arrays.toString(box));
        insertionSort(box);
        //bubbleSort(box);
        //selectSort(box);
        System.out.println(Arrays.toString(box));
    }










}
