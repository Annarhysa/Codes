import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] input = scanner.nextLine().split(" ");

        // Count the frequency of each plant ID
        Map<Integer, Integer> frequencyMap = new HashMap<>();
        for (String s : input) {
            int plantID = Integer.parseInt(s);
            frequencyMap.put(plantID, frequencyMap.getOrDefault(plantID, 0) + 1);
        }

        // Find the most common plant ID
        int mostCommonPlantID = Integer.MAX_VALUE;
        int maxFrequency = 0;
        for (Map.Entry<Integer, Integer> entry : frequencyMap.entrySet()) {
            int plantID = entry.getKey();
            int frequency = entry.getValue();
            if (frequency > maxFrequency || (frequency == maxFrequency && plantID < mostCommonPlantID)) {
                mostCommonPlantID = plantID;
                maxFrequency = frequency;
            }
        }

        // Output the most common plant ID
        System.out.println(mostCommonPlantID);
    }
}
                                                                                                                            