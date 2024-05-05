import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String tiles = input.nextLine();
        int ret = numTilePossibilities(tiles);        
        System.out.println(ret);
        input.close(); // close the scanner to avoid resource leak
    }
    
    public static int numTilePossibilities(String tiles) {
        // Convert the tiles string to a character array for easier manipulation
        char[] chars = tiles.toCharArray();
        // Create a frequency map to store the count of each character
        Map<Character, Integer> freqMap = new HashMap<>();
        for (char c : chars) {
            freqMap.put(c, freqMap.getOrDefault(c, 0) + 1);
        }
        // Initialize the result counter
        int[] result = new int[1];
        // Recursively generate all possible sequences
        generateSequences(freqMap, result);
        return result[0];
    }
    
    private static void generateSequences(Map<Character, Integer> freqMap, int[] result) {
        for (char c : freqMap.keySet()) {
            // If the count of the character is greater than 0, there are still tiles available
            if (freqMap.get(c) > 0) {
                // Add the current character to the sequence
                result[0]++;
                // Decrease the count of the current character
                freqMap.put(c, freqMap.get(c) - 1);
                // Recursively generate sequences with the updated frequency map
                generateSequences(freqMap, result);
                // Restore the count of the current character for backtracking
                freqMap.put(c, freqMap.get(c) + 1);
            }
        }
    }
}