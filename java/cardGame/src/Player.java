import java.util.ArrayList;

public class Player {

    private int score;
    private ArrayList <Card> hand;


    public Player(){
        this.score =0;
        this.hand = new ArrayList();
    }


    public void drawHand(Deck d) {
        this.hand.add(d.Draw());
        this.hand.add(d.Draw());

    }

    public int getHandValue(){
        int value = 0;
        for (int i = 0; i < hand.size() ; i++) {
            Card c = hand.get(i);
            if(c.getValue()==Card.ACE){
                value +=11;
            }else if (c.getValue()= Card.KING || c.getValue()= Card.KING || c.getValue()= Card.JACK || c.getValue()= Card.QUEEN){
                value += 10;
            }else {
                value += c.getValue();
            }

        }
    }


}
