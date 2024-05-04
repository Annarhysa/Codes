import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // Get the target price
        System.out.print();
        int targetPrice;
        try {
            targetPrice = Integer.parseInt(input.nextLine());
        } catch (NumberFormatException e) {
            System.out.println("Invalid Input");
            return;
        }

        // Get the number of stocks
        System.out.print();
        int numberOfStocks;
        try {
            numberOfStocks = Integer.parseInt(input.nextLine());
        } catch (NumberFormatException e) {
            System.out.println("Invalid Input");
            return;
        }

        // Create a list to store stock names and prices
        List<Stock> stocks = new ArrayList<>();

        // Get stock names and prices
        for (int i = 0; i < numberOfStocks; i++) {
            System.out.printf("Stock%d name and price: ", i + 1);
            String[] stockInfo = input.nextLine().split(" ");
            String stockName = stockInfo[0];
            int stockPrice;

            try {
                stockPrice = Integer.parseInt(stockInfo[1]);
            } catch (NumberFormatException e) {
                System.out.println("Invalid Input");
                return;
            }

            if (stockPrice <= 0) {
                System.out.println("The stock prices should be at least greater than 0");
                return;
            }

            if (stockPrice > targetPrice) {
                System.out.println("One of the stock prices is higher than the target price");
                return;
            }

            stocks.add(new Stock(stockName, stockPrice));
        }

        // Find all valid combinations that match the target price
        List<int[]> combinations = new ArrayList<>();
        findCombinations(targetPrice, stocks, new int[stocks.size()], 0, combinations);

        // Print the valid combinations and their count
        for (int[] combination : combinations) {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < combination.length; i++) {
                if (combination[i] > 0) {
                    sb.append(stocks.get(i).name).append(": ").append(combination[i]).append(" ");
                }
            }
            System.out.println(sb.toString().trim());
        }

        System.out.println(combinations.size());
    }

    // Method to find valid combinations that meet the target price
    public static void findCombinations(int target, List<Stock> stocks, int[] currentCombination, int index, List<int[]> combinations) {
        // Base case: if we've found a combination that matches the target
        if (target == 0) {
            combinations.add(currentCombination.clone());
            return;
        }

        if (index >= stocks.size() || target < 0) {
            return;  // No valid combination possible
        }

        // Recurse: try including more of the current stock
        int stockPrice = stocks.get(index).price;

        int quantity = 0;
        while (target - (quantity * stockPrice) >= 0) {
            currentCombination[index] = quantity;
            findCombinations(target - (quantity * stockPrice), stocks, currentCombination, index + 1, combinations);
            quantity++;
        }

        // Set the current stock quantity to zero for the next combination search
        currentCombination[index] = 0;
    }

    // Stock class to represent a stock with a name and a price
    static class Stock {
        String name;
        int price;

        Stock(String name, int price) {
            this.name = name;
            this.price = price;
        }
    }
}
