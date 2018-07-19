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
public class temperature {
    
    public static void main(String[] args){
        Scanner keyboard = new Scanner(System.in);
        System.out.println("please enter a temperature in celsius");
        double celsius = keyboard.nextDouble();
        double fract = (1.8);
        double f = ((celsius * fract) + 32);
        System.out.println(celsius + " is " + f +" in Farenheit.");
        
     // why doesnt double fract = (9/5) give me fract = 1?   
        
        
    }
    
    
    
    
    
    
    
}
