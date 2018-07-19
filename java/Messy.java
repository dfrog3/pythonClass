/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package java.pkgclass;

import java.util.Scanner;

/**
 *
 * @author David
 */
public class Messy {
    
    
    public static void main(String[] args){
        System.out.println("It’s time to go on a scavenger hunt!");
        System.out.println("You\'d be amazed how many things can go wrong!"); 
        System.out.println("Please enter how long you want to travel for:");
        Scanner keyboard = new Scanner(System.in);
        double initialPos = keyboard.nextDouble();
        double time = keyboard.nextDouble();
        double velocity = 5.0;
        double acceleration = 1.0;
            // there is a math error in here causing
            // an incorrect answer in the line below
        double position = initialPos + (velocity * time) + (0.5 *acceleration*(time*time));
        System.out.println(position);
    
    }
}
