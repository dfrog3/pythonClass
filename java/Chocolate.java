/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package david;

import java.util.Scanner;

/**
 *
 * @author David
 */
public class Chocolate {
    public static void main(String[] args){
        Scanner keyboard = new Scanner(System.in);
        System.out.println("Hello I will be calculating your chocolate dosage.\nPLease enter your height.");
        double height = keyboard.nextDouble();
        System.out.println("Thank you, weight please.");
        double weight = keyboard.nextDouble();
        System.out.println("Thank you, please enter your age.");
        double age = keyboard.nextDouble();
        double male = (66+(6.2 * weight)+(12.7 * height)-(6.76 * age));
        double female = (655.1+(4.35 * weight)+(4.7 * height)-(4.7 * age));
        male = male / 241;
        female = female /241;
        System.out.println("Males need " + male +" chocolate bars.\nFemales need " +female+ " chocolate bars.");
        
        
    }
}
