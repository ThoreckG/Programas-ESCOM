package circulo;

public class Circulo {
    private double radio;
    private String color;

    public Circulo(double radio, String color) {
        this.radio = radio;
        this.color = color;
    }

    public double getArea() {
        return area();
    }

    public double getPerimetro() {
        return perimetro();
    }

    public String getColor() {
        return color;
    }

    private double area() {
        return Math.PI * radio * radio;
    }

    private double perimetro() {
        return 2 * Math.PI * radio;
    }

    public static void main(String[] args) {
        Circulo circulo = new Circulo(5.0, "azul");
        System.out.println("El área del círculo es: " + circulo.getArea());
        System.out.println("El perímetro del círculo es: " + circulo.getPerimetro());
        System.out.println("El color del círculo es: " + circulo.getColor());
    }
}
