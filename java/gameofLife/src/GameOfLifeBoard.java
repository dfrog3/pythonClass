import java.util.Scanner;
import java.util.Arrays;

public class GameOfLifeBoard {

	private char[][] board;
	private char[][] nextBoard;
	public static final char LIVE = 'X';
	public static final char DEAD = '^';
	
	
	public GameOfLifeBoard(){
	    this.board = new char[100][100];
	    this.nextBoard = new char[100][100];
		
	}
	
	
	

	
	public int getNeighborCount(int row, int col){
		int numNeighbors = 0;
		try{
		    if(this.board[row-1][col]== LIVE){//n
		        numNeighbors += 1;
            }

        }catch (Exception e){


        }
        try{
            if(this.board[row+1][col]== LIVE){//s
                numNeighbors += 1;
            }

        }catch (Exception e){


        }
        try{
            if(this.board[row][col-1]== LIVE){//w
                numNeighbors += 1;
            }

        }catch (Exception e){


        }
        try{
            if(this.board[row][col+1]== LIVE){//e
                numNeighbors += 1;
            }

        }catch (Exception e){


        }
        try{
            if(this.board[row-1][col-1]== LIVE){//sw
                numNeighbors += 1;
            }

        }catch (Exception e){


        }
        try{
            if(this.board[row+1][col+1]== LIVE){//ne
                numNeighbors += 1;
            }

        }catch (Exception e){


        }
        try{
            if(this.board[row+1][col-1]== LIVE){//nw
                numNeighbors += 1;
            }

        }catch (Exception e){


        }
        try{
            if(this.board[row-1][col+1]== LIVE){//se
                numNeighbors += 1;
            }

        }catch (Exception e){


        }
        System.out.println(numNeighbors);


		
		
		return numNeighbors;
	}
	
	public void printBoard(){
        for (int i = 0; i < this.nextBoard[0].length ; i++) {
            System.out.println(Arrays.toString(this.nextBoard[i]));

        }
		
	}



	public void switchTile(int col, int row){
	    if(this.board[col][row]== LIVE){
	        setNextBoardDead(col,row);
        }else{
	        setNextBoardLive(col,row);
        }



    }

    public void COPY(){
	    for(int col=0; col < this.board.length; col ++){
            for (int row = 0; row < this.board.length; row++) {
                this.board[col][row]= this.nextBoard[col][row];

            }
        }
    }




    public void setNextBoardLive(int col, int row) {
        this.nextBoard[col][row]= LIVE;
    }

    public void setNextBoardDead(int col, int row) {
        this.nextBoard[col][row]= DEAD;
    }
    public char getBoardCellValue(int col, int row) {
        return board[col][row];
    }


    public static void main(String[] args){
	    Scanner keyboard = new Scanner(System.in);
	    int neigbors;

	    GameOfLifeBoard b = new GameOfLifeBoard();
	    boolean Continue = true;
	    boolean userPlay;
        int playerCol;
        int playerRow;
	    while (Continue){
	        userPlay = true;
	        while (userPlay){

                System.out.println("type pass to pass. any key to contineu");
                if (keyboard.nextLine().equals("pass")){
                    userPlay = false;
                    continue;
                }
                System.out.println("give a col");
                playerRow = keyboard.nextInt();
                System.out.println("give an int row");
                playerCol = keyboard.nextInt();
                b.switchTile(playerCol,playerRow);
                b.printBoard();
                System.out.println("make another move? true/false");
                b.COPY();
                userPlay = keyboard.nextBoolean();
                keyboard.nextLine();


            }


            for (int row = 0; row < 100 ; row++) {
                for (int col = 0; col < 100; col++) {
                    neigbors = b.getNeighborCount(col,row);
                    System.out.println(b.getBoardCellValue(1,1));
                    //System.out.print(col+" ");
                    //System.out.println(row);
                    if (neigbors < 2){
                        b.setNextBoardDead(col,row);
                    }else if(neigbors == 2 && b.getBoardCellValue(col,row)==LIVE|| neigbors==3){
                        b.setNextBoardLive(col,row);
                    }else if(neigbors>3){
                        b.setNextBoardDead(col,row);
                    }



                }

            }

            b.printBoard();
            System.out.println();
            b.COPY();
            Continue = false;
            while (!Continue){
                System.out.println("play again? true/quit");
                Continue = keyboard.nextBoolean();
                keyboard.nextLine();

            }

        }







		
	}
	
}
