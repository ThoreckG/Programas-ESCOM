package rectangulo;

public class Rectangulo {
    private double ancho;
    private double alto;
    private String color;

    public Rectangulo(double ancho, double alto, String color) {
        this.ancho = ancho;
        this.alto = alto;
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
        return ancho * alto;
    }

    private double perimetro() {
        return 2 * (ancho + alto);
    }

    public static void main(String[] args) {
        Rectangulo rectangulo = new Rectangulo(5.0, 3.0, "verde");
        System.out.println("El área del rectángulo es: " + rectangulo.getArea());
        System.out.println("El perímetro del rectángulo es: " + rectangulo.getPerimetro());
        System.out.println("El color del rectángulo es: " + rectangulo.getColor());
    }
}
