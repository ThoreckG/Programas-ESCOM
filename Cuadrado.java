package cuadrado;

public class Cuadrado {
    private double lado;
    private String color;

    public Cuadrado(double lado, String color) {
        this.lado = lado;
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
        return lado * lado;
    }

    private double perimetro() {
        return 4 * lado;
    }

    public static void main(String[] args) {
        Cuadrado cuadrado = new Cuadrado(4.0, "negro");
        System.out.println("El área del cuadrado es: " + cuadrado.getArea());
        System.out.println("El perímetro del cuadrado es: " + cuadrado.getPerimetro());
        System.out.println("El color del cuadrado es: " + cuadrado.getColor());
    }
}
