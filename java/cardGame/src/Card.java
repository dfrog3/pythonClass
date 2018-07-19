public class Card {
    public static final int HEARTS   = 1;
    public static final int CLUBS    = 2;
    public static final int DIAMONDS = 3;
    public static final int SPADES   = 4;



    public static final int ACE = 1;
    public static final int KING = 13;
    public static final int QUEEN = 12;
    public static final int JACK = 11;











    private int value;
    private int suit;

    public Card(int value, int suit ){
        this.value = value;
        this.suit = suit;
    }



    public int getValue(){
        return this.value;
    }

    public int getSuit() {
        return suit;
    }



    public String toString(){
        String value = "";
        if (this.value == Card.ACE){
            value ="Ace";
        }else if (this.value == Card.JACK){
            value = "Jack";
        }else if(this.value == Card.KING){
            value = "King";
        }else if (this.value== Card.QUEEN){
            value = "Queen";
        }

        String suit ="";
        if (this.suit == Card.DIAMONDS){
            suit ="\u2666";
        }else if (this.suit == Card.SPADES){
            suit = "\u2660";
        }else if(this.suit == Card.CLUBS){
            suit = "\u2663";
        }else if (this.suit== Card.HEARTS){
            suit = "\u2665";
        }



        return value + " of " + suit;
    }






}
