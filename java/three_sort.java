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
public class three_sort {
    public static void main(String[] args){
      Scanner keyboard = new Scanner(System.in);  
      System.out.println("I will sort three integers for you.\nPlease enter the first one now");
      int dai1 = keyboard.nextInt();
      System.out.println("Please enter the next number");
      int dai2 = keyboard.nextInt();
      System.out.println("Please enter the final number");
      int dai3 = keyboard.nextInt();
      
      int dai11 = dai1;
      int dai22 = dai2;
      int dai33 = dai3;
      
      int first = 0;
      int second = 0;
      int third = 0;
      
      if(dai1 > dai2 && dai1 > dai3){
          third = dai1;
          dai11 = 0;
      }else if(dai2 > dai1 && dai2 > dai3){
          third = dai2;
          dai22 = 0;
      } else if(dai3 > dai2 && dai3 > dai1){
          third = dai3;
          dai33 = 0;
      }  
      
      if(dai1 < dai2 && dai1 < dai3){
          first = dai1;
          dai11 = 0;
      } else if(dai2 < dai1 && dai2 < dai3){
          first = dai2;
          dai22 = 0;
      } else if(dai3 < dai2 && dai3 < dai1){
          first = dai3;
          dai33 = 0;
      }
      

      
      
      if(dai11 == 0 && dai22 ==0){
          second = dai3;
      } else if(dai11 == 0 && dai33 ==0){
          second = dai2;
      } else if(dai33 == 0 && dai22 ==0){
          second = dai1;
      }
      
      
      
      
      
      System.out.println(first +" "+ second +" "+ third );
      
        
    }
    
    
    
}
