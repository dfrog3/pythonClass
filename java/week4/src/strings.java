import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.Scanner;


public class strings {

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


    public static Boolean isSorted( int[] y) {
        int[] x = arrCopy.copyIntArr(y);
        y = bubbleSort(y);
        for (int i = 0; i < x.length; i++) {
            if (x[i]!=y[i]){
                return false;
            }

        }
        return true;

    }


    public static int[] RoundAllUp(double[] toRound){
        int[] out= new int[toRound.length];
        for (int i = 0; i < toRound.length ; i++) {
            int temp = ((int) Math.ceil(toRound[i]));
            out[i]=temp;

        }
        return out;
    }


    public static int[] generateTriangleNumbers(int x){
        int[] out = new int[x];
        for (int i = 1; i < x+1; i++) {
            int y = (i*(i+1))/2;
            out[i-1] = y;
        }
        return out;
    }


    public static void reverseAll(String[] toR){
        for (int i = 0; i <toR.length ; i++) {
            String outBox ="";
            for (int j = toR[i].length(); j > 0; j--) {
                outBox = outBox + toR[i].substring(j-1,j);

            }
            toR[i]=outBox;
        }

    }


    public static boolean isPalindrome(String word){
        int x = 0;
        if (word.length() % 2 != 0){
            x = word.length();
        }else{
            x = word.length()-1;
        }
        for (int i = 0; i < x; i++) {
            if(word.charAt(i) == (word.charAt(word.length()-1-i))){
                continue;
            } else{
                return false;
            }

        }
        return true;
    }


    public static int minGap(int[] theArray){
        int out;
        int[] answer = new int[theArray.length];
        for (int i = 0; i <theArray.length-1 ; i++) {
            if (theArray[i]> theArray[i+1]){
                out = (theArray[i]-theArray[i+1]);
            }else{
                out = (theArray[i+1]-theArray[i]);
            }
            answer[i] = out;


        }
        bubbleSort(answer);
        return answer[1];

    }


    public static void main(String[] args) {
        int[] isSort = {10,20,30,40,50,60,70};
        System.out.println(isSorted(isSort)) ;
        double[] rounder = {1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0};
        System.out.println(Arrays.toString(RoundAllUp(rounder)));
        Scanner keyboard = new Scanner(System.in);
        System.out.println("number please");
        int triangle = keyboard.nextInt();
        keyboard.nextLine();
        System.out.println(Arrays.toString(generateTriangleNumbers(triangle)));
        String[] reverse = {"hello","bello","cello","mello"};
        reverseAll(reverse);
        System.out.println(Arrays.toString(reverse));
        System.out.println("word please");
        String pal = keyboard.nextLine();
        System.out.println(isPalindrome(pal));
        int[] gap = {1,5,6,4,8,2,14,9,6,3,4,6,5,123,654,644,23,6,7};
        System.out.println(minGap(gap));






    }
}
