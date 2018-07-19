import java.util.Scanner;

public class stringManipulationPig {
    public static int FindFirstValue(String word) {
        String vs = "aeiou";
        for(int i = 0; i < word.length(); i++){
            for(int j = 0; j<5; j++){
                if (word.substring(i, i+1).equals(vs.substring(j, j+1))){

                    return i;
                }

            }

        }
        return -1;


    }
    public static String ConvertToPigLatin(String word, int firstVowel){
        if(firstVowel<0){
            return word + "ay";
        } else if(firstVowel == 0){
            String jarStart = word.substring(firstVowel+1);
            String jarEnd = word.substring(0, firstVowel+1);
            return jarStart + jarEnd + "way";
        }
        String jarStart = word.substring(firstVowel);
        String jarEnd = word.substring(0, firstVowel);
        return jarStart + jarEnd + "ay";



    }






    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        System.out.println("give me a word");
        String word = "";
        while(!word.equals("done")){
            word = keyboard.nextLine();
            word = word.toLowerCase();
            if(word.equals("done")){
                break;
            }

            int firstVowel = FindFirstValue(word);

            String pigged = ConvertToPigLatin(word, firstVowel);
            System.out.println(pigged);
        }

    }
}
