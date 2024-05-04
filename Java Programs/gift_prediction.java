import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] inputs = scanner.nextLine().split(" ");

        int[] scores = new int[inputs.length];
        for (int i = 0; i < inputs.length; i++) {
            try {
                scores[i] = Integer.parseInt(inputs[i]);
            } catch (NumberFormatException e) {
                System.out.println("Invalid input");
                return;
            }
        }

        int[] gifts = new int[scores.length];

        for (int i = 0; i < scores.length; i++) {
            if (i == 0) {
                gifts[i] = 1;
            } else {
                if (scores[i] > scores[i - 1]) {
                    gifts[i] = gifts[i - 1] + 1;
                    int specialGifts = 0;
                    if (scores[i] % 3 == 0) {
                        specialGifts += 3;
                    }
                    if (scores[i] % 5 == 0) {
                        specialGifts += 5;
                    }
                    gifts[i] += specialGifts;
                    if (scores[i] % 7 == 0) {
                        gifts[i]++;
                    }
                } else if (scores[i] < scores[i - 1]) {
                    gifts[i] = 1;
                } else {
                    System.out.println("Should not receive the same number of gifts");
                    return;
                }
            }
        }

        for (int gift : gifts) {
            System.out.print(gift + " ");
        }
    }
}
                                                                                                                            