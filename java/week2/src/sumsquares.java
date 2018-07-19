/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package week2;

import java.util.Scanner;

/**
 *
 * @author David
 */
public class sumsquares {
    
    public static void Math(int userNumber){
        int y = 0;
        for(int i = 1; i < userNumber +1; i++){
            y = y + i*i;
        }
        System.out.println(y); 
        
        
        
    }
    
    public static void main(String[] args){
        Scanner keyboard = new Scanner(System.in);
        System.out.println("give me a number");
        int userNumber = keyboard.nextInt();
        Math(userNumber);
        
        
        
    }
    
}
