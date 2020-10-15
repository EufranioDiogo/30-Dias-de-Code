import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int iterationQuant = Integer.parseInt(scanner.nextLine());
        int counter = 0;
        String phrase = "";
        String rightCharacters = "";
        String leftCharacters = "";
        String [] results = new String[iterationQuant];

        while (counter < iterationQuant) {
            phrase = scanner.nextLine();
            rightCharacters = "";
            leftCharacters = "";
    
            for(int index = 0; index < phrase.length(); index++){
                if (index % 2 == 0) {
                    rightCharacters += phrase.charAt(index);
                } else {
                    leftCharacters += phrase.charAt(index);
                }
            }
            results[counter] = rightCharacters + " " + leftCharacters;
            counter++;
        }

        for (String element : results) {
            System.out.println(element);
        }
    }
}