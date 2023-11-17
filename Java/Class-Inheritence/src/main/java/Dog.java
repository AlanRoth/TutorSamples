public class Dog extends Animal {
    private String name;
    private int age;

    public Dog(String dogName, int dogAge) {
        name = dogName;
        age = dogAge;
    }

    @Override
    public String speak() {
        return "woof";
    }

    @Override
    public void move() {

    }
}
