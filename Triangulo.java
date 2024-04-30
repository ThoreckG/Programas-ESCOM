package triangulo;

public class Triangulo {
    private double base;
    private double altura;
    private double lado1;
    private double lado2;
    private double lado3;
    private String color;

    public Triangulo(double base, double altura, double lado1, double lado2, double lado3, String color) {
        this.base = base;
        this.altura = altura;
        this.lado1 = lado1;
        this.lado2 = lado2;
        this.lado3 = lado3;
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
        return (base * altura) / 2;
    }

    private double perimetro() {
        return lado1 + lado2 + lado3;
    }

    public static void main(String[] args) {
        Triangulo triangulo = new Triangulo(3.0, 4.0, 3.0, 4.0, 5.0, "rojo");
        System.out.println("�?rea del triángulo: " + triangulo.getArea());
        System.out.println("Perímetro del triángulo: " + triangulo.getPerimetro());
        System.out.println("Color del triángulo: " + triangulo.getColor());
    }
}
