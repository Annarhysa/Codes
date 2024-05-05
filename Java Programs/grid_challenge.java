import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String inputString = input.nextLine();
        String[] parts = inputString.split(" ");
        int gridSize = Integer.parseInt(parts[0].split(",")[1]);
        String[] characters = parts[1].split(",");
        
        char[][] grid = new char[gridSize][gridSize];
        int k = 0;
        for (int i = 0; i < gridSize; i++) {
            for (int j = 0; j < gridSize; j++) {
                grid[i][j] = characters[k++].charAt(0);
            }
        }

        for (int i = 0; i < gridSize; i++) {
            Arrays.sort(grid[i]);
        }

        boolean columnsSorted = true;
        for (int j = 0; j < gridSize; j++) {
            for (int i = 1; i < gridSize; i++) {
                if (grid[i][j] < grid[i - 1][j]) {
                    columnsSorted = false;
                    break;
                }
            }
            if (!columnsSorted) {
                break;
            }
        }

        if (columnsSorted) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
    }
}
                                                                                                                            