import java.util.HashMap;
import java.util.Map;
import java.util.Random;
import java.util.Scanner;

public class NumberGuess {
    private int number;
    private int guesses;
    private static Map<HighLow, String> stringValues = new HashMap<>();

    private Random random;
    private Scanner scanner;

    enum HighLow {
        HIGH,
        WIN,
        LOW,
        LOST
    }

    public NumberGuess() {
        this.random = new Random();
        this.scanner = new Scanner(System.in);

        this.number = random.nextInt(101);
        this.guesses = 10;

        System.out.println(this.number);

        stringValues.put(HighLow.HIGH, "Too High!");
        stringValues.put(HighLow.WIN, String.format("You win! The number was %d", this.number));
        stringValues.put(HighLow.LOW, "Too Low!");
        stringValues.put(HighLow.LOST, String.format("You loose! The number was %d", this.number));
    }

    private HighLow parse_guess(int guess) {
        if (guess > this.number) {
            return HighLow.HIGH;
        } else if (guess < this.number) {
            return HighLow.LOW;
        }
        return HighLow.WIN;
    }

    private HighLow makeGuess(int guess) {
        this.guesses -= 1;
        if (this.guesses == 0) {
            return HighLow.LOST;
        }
        return parse_guess(guess);
    }

    private int getUserInput() {
        System.out.println(String.format("Make your guess, you have %d guesses left: ", this.guesses));
        return scanner.nextInt();
    }

    public String gameLoop() {
        while(this.guesses != 0) {
            int guess = getUserInput();
            HighLow result = makeGuess(guess);
            if (result == HighLow.WIN || result == HighLow.LOST) {
                return stringValues.get(result);
            }
            System.out.println(stringValues.get(result));
        }
        return "";
    }
}
