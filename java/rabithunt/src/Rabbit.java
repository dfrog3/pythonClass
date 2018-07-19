import com.sun.org.apache.xpath.internal.operations.Mod;
import com.sun.tools.corba.se.idl.constExpr.Not;

import java.lang.reflect.Field;
import java.lang.reflect.Method;

import java.lang.reflect.Array;

import java.util.Arrays;
//MAX_NUMBER_OF_STEPS

public class Rabbit extends Animal {
    private int danger = 0;
    private boolean dangerNow = false;
    private int shimur =0;//2,4,6;
    private int lastdirection;
    private boolean wallSkip;

    public Rabbit(Model model, int row, int column) {
        super(model, row, column);
    }



//todo panic variable to keep track of the last tim rabbit saw the fox

//todo bush trick to lose the fox
//todo use distance and edge=0 to cut corners when on the edge


    static final int













    
    int decideMove(){


        int wise = 8;



        int[] surround = new int[8];
        int wall = 0;

        for (int i = 0; i < 8 ; i++) {
            surround[i] = look(i);
        }


        for (int i = 0; i < 8; i++) {
            if (surround[i]==Model.FOX){
                //System.out.println(surround[7]);
                danger =5;
                wise = (i+ 3);
                //System.out.println(wise);

                if (wise > 7){
                    wise = wise -8;
                }

                if (wise == Model.EDGE&&distance(wise)==1){
                    wise +=4;
                    if (wise > 7){
                        wise = wise -8;
                    }

                }

                if (surround[wise]==Model.FOX){
                    wise = lastdirection +4;
                    if (wise > 7){
                        wise = wise -8;
                    }
                }

                break;
            }

        }

        if (danger>0&& danger <=4){
            wise = lastdirection;
            danger -= 1;
        }

        if (danger==5){
            danger= danger-1;
        }










        while (!canMove(wise)) {
            if (canMove(wise)) {
                lastdirection = wise;
                return wise;


            } else {
                wise += 2;
            }
            if (wise > 7){
                wise = 0;
            }
        }












        //System.out.println("\n\n\n\n\n\n\n\n\n\n\n\nRabbit escapes: 300 times out of 300, or 100%");
        lastdirection = wise;
        return wise;


    }



}
