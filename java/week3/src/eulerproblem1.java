public class eulerproblem1 {
    public static int checker(int toCheck) {
        if((toCheck % 3 == 0) || (toCheck % 5== 0)){
            return toCheck;
        }else{
            return 0;
        }

    }



    public static void main(String[] args) {
        int answer = 0;
        int jar =0;
        for (int i = 1000; i>0; i--){
            jar =checker(i);
            answer = answer + jar;

        }
        System.out.println(answer);
    }



}
