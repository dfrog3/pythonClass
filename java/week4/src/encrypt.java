import com.sun.org.apache.xerces.internal.impl.io.ASCIIReader;

public class encrypt {

    public static String Breaker(String ToBreak, int key){
        String j = "";
        char x;
        for(int i = 0; i < ToBreak.length(); i++){
            int encryptedChar = ToBreak.charAt(i);
            int methx = ((encryptedChar) + 127) -32;
            int meth = encryptedChar - key;
            if (methx > 126){
                x = ((char) (methx - key));
            }else{
                x = ((char)(meth));

            }
            j = j+ x;
        }
        return j;

    }


    public static void main(String[] args) {
        System.out.println((int)("y".charAt(0)));
        System.out.println("\u0121");





        for (int i = 0; i < 101; i++) {

            System.out.println(i+" "+Breaker(":mmZ\\dxZmx]Zpgy", i));


        }







    }



}
