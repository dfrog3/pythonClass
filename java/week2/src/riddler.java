public class riddler {
    public static boolean DiffrentChecker( int digit1, int digit10, int digit100, int digit1000 ){

        int[] digits = {digit1, digit10, digit100, digit1000};
        for (int i = 0; i < 4; i++){
            for(int j = i +1; j < 4; j++ ){
                if (digits[i] == digits[j]){
                    return false;
                }
            }
        }
        return true;
    }
    public static void ToBeCalledInMain(){
        int digit1 = -1;
        int digit10 = 0;
        int digit100 = 0;
        int digit1000 = 0;
        boolean diffrent = false;
        boolean SUM = false;

        while(!(SUM && diffrent)){//main loop
            digit1 += 2; //digit1 increase
            if (digit1 > 9){ //checks digit1 out of bounds and resets
                digit1 = 1;
            }


            if(digit1 + digit10 + digit100 + digit1000 == 27){//checks for correct sum
                SUM = true;
            }else{
                SUM = false;
            }
            diffrent = DiffrentChecker(digit1, digit10, digit100, digit1000); //checks for same int
            if(SUM && diffrent){ //finishes program if correct answer is found
                break;
            }


            digit10 += 1;//adds one to digit10
            if (digit10 > 3){//resest digit10
                digit10 = 0;
            }
            digit1000 = digit10 * 3;//calculates digit1000



            if(digit1 + digit10 + digit100 + digit1000 == 27){//checks for correct sum
                SUM = true;
            }else{
                SUM = false;
            }
            diffrent = DiffrentChecker(digit1, digit10, digit100, digit1000); //checks for same int
            if(SUM && diffrent) { //finishes program if correct answer is found
                break;
            }


            digit100 += 1;//manages digit 100
            if (digit100 > 9){
                digit100 = 1;
            }// manages digit 100



            if(digit1 + digit10 + digit100 + digit1000 == 27){//checks for correct sum
                SUM = true;
            }else{
                SUM = false;
            }
            diffrent = DiffrentChecker(digit1, digit10, digit100, digit1000); //checks for same int
            if(SUM && diffrent) { //finishes program if correct answer is found
                break;
            }
        }
        System.out.println((digit1*1)+(digit10*10)+(digit100*100)+(digit1000*1000)); //prints final answer
    }

    public static void main(String[] args) {
        ToBeCalledInMain();
    }
}
