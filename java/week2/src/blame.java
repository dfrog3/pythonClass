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
public class blame{
    public static void Error(String x){
        System.out.println(x);
        Date();
                
        
        
        
    }
    
    
    
    
    public static void Date(){
        Scanner keyboard = new Scanner(System.in);
        int year;
        int month;
        int day;
        int monthCount = 0;
        boolean leap;
        
        System.out.println("please enter a date formatted MM/DD/YYYY");
        String userDate = keyboard.next();
        year = Integer.parseInt(userDate.substring(6, 10));
        month = Integer.parseInt(userDate.substring(0, 2));
        day = Integer.parseInt(userDate.substring(3, 5));
        if(month > 12){       
            Error("Invalid month");
        }
        
        if(year % 4 == 0){
            if(year % 100 == 0){
                if(year % 400 == 0){
                    leap = true;
                    
                }else{
                    leap = false;
                }
            }else{
                leap = true;
            }
        }else{
            leap = false;
            
        }
        
        
        
        
        
        
        
        
        switch(month){
            case 1:
                if(day>31 || day<= 0){
                    Error("Invalid day");
                }
                break;
            case 2:
                if(leap){
                    if(day>29 || day<= 0){
                    Error("Invalid day");
                }
                }else{
                    if(day>28 || day<= 0){
                    Error("Invalid day");
                }
                }
                break;
            case 3:
                if(day>31 || day<= 0){
                    Error("Invalid day");
                }
                break;
            case 4:
                if(day>30 || day<= 0){
                    Error("Invalid day");
                }
                break;
            case 5:
                if(day>31 || day<= 0){
                    Error("Invalid day");
                }
                break;
            case 6:
                if(day>30 || day<= 0){
                    Error("Invalid day");
                }
                break;
            case 7:
                if(day>31 || day<= 0){
                    Error("Invalid day");
                }
                break;
            case 8:
                if(day>31 || day<= 0){
                    Error("Invalid day");
                }
                break;    
            case 9:
                if(day>30 || day<= 0){
                    Error("Invalid day");
                }
                break;    
            case 10:
                if(day>31 || day<= 0){
                    Error("Invalid day");
                }
                break;    
            case 11:
                if(day>30 || day<= 0){
                    Error("Invalid day");
                }
                break;    
            case 12:
                if(day>31 || day<= 0){
                    Error("Invalid day");
                }
                break;    
            default:
                Error("invalid month");
                
                
                
        }
    System.out.println("This is a valid date");
    Date();
        
        
        
        
        
    }
    
  
    public static void main(String[] args){
        
        
      Date();
        
        
        
        
        
            
        }
        
        
        
        
    
    
    
}
