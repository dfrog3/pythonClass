public class Board {


    private String X = "X";
    private String O = "O";
    private String[] a = {" ","="," ","="," " };
    private String[] b = {"||","==","||","==","||"};
    private String[] c = {" ","=="," ","=="," " };
    private String[] d = {"||","==","||","==","||"};
    private String[] e = {" ","=="," ","=="," " };
    private String[] f = {"1"," ","2"," ","3"," "};
    private String [][] GRID = {f,a,b,c,d,e};
    private boolean TURN = true;
    private String WON = "no";





    public String cordConverter(String cord){
        if (cord.length()!=2){
            return "error";
        }
        String letter = cord.substring(0,1);
        String number = cord.substring(1,2);
        String outLetter="";
        String outNumber="";



        if (letter.equals("a")){
            outLetter = "1";
        }else if (letter.equals("b")){
            outLetter = "3";
        }else if (letter.equals("c")){
            outLetter = "5";
        }else{
            return "error";
        }


        if (number.equals("1")){
            outNumber = "0";

        }else if (number.equals("2")){
            outNumber = "2";

        }else if (number.equals("3")){
            outNumber = "4";

        }else{
            return "error";
        }
        return (outLetter + outNumber);



    }

    public String wonGame(){
        if (this.GRID[1][0].equals(this.GRID[1][2])&&this.GRID[1][2].equals(this.GRID[1][4])&&!this.GRID[1][0].equals(" ")){//1
            return this.GRID[1][0];

        }else if(this.GRID[1][0].equals(this.GRID[3][2])&&this.GRID[3][2].equals(this.GRID[5][4])&&!this.GRID[1][0].equals(" ")){//2
            return this.GRID[1][0];
        }else if (this.GRID[1][0].equals(this.GRID[3][0])&&this.GRID[3][0].equals(this.GRID[5][0])&&!this.GRID[1][0].equals(" ")){//3
            return this.GRID[1][0];
        }else if (this.GRID[1][2].equals(this.GRID[3][2])&&this.GRID[3][2].equals(this.GRID[5][2])&&!this.GRID[1][2].equals(" ")){//4
            return this.GRID[1][2];
        }else if (this.GRID[3][0].equals(this.GRID[3][2])&&this.GRID[3][2].equals(this.GRID[3][4])&&!this.GRID[3][4].equals(" ")){//5
            return this.GRID[3][0];
        }else if (this.GRID[1][4].equals(this.GRID[3][2])&&this.GRID[3][2].equals(this.GRID[5][0])&&!this.GRID[5][0].equals(" ")){//6
            return this.GRID[5][0];
        }else if (this.GRID[1][4].equals(this.GRID[3][4])&&this.GRID[3][4].equals(this.GRID[5][4])&&!this.GRID[1][4].equals(" ")){//7
            return this.GRID[1][4];
        }else if (this.GRID[5][0].equals(this.GRID[5][2])&&this.GRID[5][2].equals(this.GRID[5][4])&&!this.GRID[5][4].equals(" ")){//8
            return this.GRID[5][0];
        }

        else return "no";


    }



    public void updateGrid(String tilePlace){
        int x = Integer.valueOf(tilePlace.substring(0,1));
        int y = Integer.valueOf(tilePlace.substring(1,2));
        if(this.TURN){
            this.GRID[x][y]= this.O;
        }else{
            this.GRID[x][y] = this.X;
        }
        this.TURN = !this.TURN;


    }



    public boolean getTURN() {
        return TURN;
    }

    public String getX() {
        return X;
    }

    public String getO() {
        return O;
    }

    public void printGrid(){
        System.out.println(" a  b  c");
        for (int i = 0; i < 5 ; i++) {
            for (int j = 0; j < 6; j++) {
                System.out.print(this.GRID[j][i]);
                if (j == 5){
                    System.out.println();
                }

            }

        }
    }







}
