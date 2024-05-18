package lecturanumeros;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.Reader;

public class LecturaNumeros extends BufferedReader {

  
    public LecturaNumeros() {                      // Constructor objeto
        super(new InputStreamReader(System.in));
    }

   
    public LecturaNumeros(Reader r) {            // Constructor recibe objeto 
        super(r);
    }

    // Método devuelve  dato numérico 
    public int readInt() throws IOException {
        return Integer.parseInt(readLine());
    }

    // Método  devuelve  dato numérico  última línea de caracteres 
    public int readInt(String mensaje) throws IOException {
        System.out.print(mensaje);
        return readInt();
    }

    // Método devuelve dato numérico  a la última línea  como objeto Integer
    public Integer readInteger() throws IOException {
        return Integer.valueOf(readLine());
    }

    // Método que devuelve el dato numérico  objeto Integer con mensaje
    public Integer readInteger(String mensaje) throws IOException {
        System.out.print(mensaje);
        return readInteger();
    }

    // Método que devuelve el dato numérico leído como un dato de tipo double
    public double readDouble() throws IOException {
        return Double.parseDouble(readLine());
    }

    // Método que devuelve el dato numérico leído como un dato de tipo double con mensaje
    public double readDouble(String mensaje) throws IOException {
        System.out.print(mensaje);
        return readDouble();
    }

    // Método principal para probar la clase
    public static void main(String[] args) {
        try {
            LecturaNumeros ln = new LecturaNumeros();

            System.out.println("Ingrese 2 números enteros:");
            int int1 = ln.readInt("Entero 1: ");
            Integer int2 = ln.readInteger("Entero 2: ");
            System.out.println("Ingrese 1 número double:");
            double double1 = ln.readDouble("Double 1: ");
            System.out.println("Ingrese 1 número Double:");
            Double double2 = ln.readDouble("Double 2: ");
            
            // Despliegue de los valores ingresados
            System.out.println("Entero 1: " + int1);
            System.out.println("Entero 2: " + int2);
            System.out.println("Double 1: " + double1);
            System.out.println("Double 2: " + double2);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

