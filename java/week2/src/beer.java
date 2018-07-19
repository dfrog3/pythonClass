package week2;

import java.util.Scanner;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author David
 */
public class beer {
    
    public static void Beersong(int x){
        for(int i = x; i >=0; i--){
            System.out.println(i +" bottels of beer on the wall, "+ i + " bottles of beer.\nTake one down, pass it arround "+ (i-1)+ " bottles of bear on the wall!");
            
        }
        
        
        
    }
    
    
    
    public static void main(String[] args){
        Scanner keyboard = new Scanner(System.in);
        System.out.println("Start us off!");
        int x = keyboard.nextInt();
        Beersong(x);
        
        
        
        
    }
    
    
    
    
    
}
