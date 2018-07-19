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
public class multiplication {

    public static void LineMaker(int table) {

        int y;
        int m = 0;
        for (int i = 1; i < table + 1; i++) {
            y = 0;
            String output = "";
            for (int j = 1; j < table; j++) {
                y = y + i;
                output = output + " " + y;
            

            }
            System.out.println(output);

        }
    }

    public static void main(String[] args) {

        System.out.println("give me a number");
        Scanner keyboard = new Scanner(System.in);
        int table = keyboard.nextInt();
        LineMaker(table);

    }

}
