/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package david;

import java.util.Scanner;


public class hours {
    public static void main(String[] args){
        Scanner keyboard = new Scanner(System.in);
        System.out.println("please input an amount in seconds.");
        int seconds = keyboard.nextInt();
        int hours = seconds / 3600;
        int remaining = seconds % 3600;
        int minutes = remaining / 60;
        int remaining2 = (remaining % 60);
        System.out.println( seconds + " seconds is " + hours + " hours and " + minutes + " minutes and " + remaining2 + " seconds." );
        
        
        
        
        
        
        
        
        
        
        
    }
        
}
