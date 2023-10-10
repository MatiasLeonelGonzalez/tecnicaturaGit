
package Clases;

public class PruebaPersona {
        public static void main(String[] args) {
        Persona persona1;
        persona1 = new  Persona(); //llamamos al constructor
        persona1.nombre = "Ariel"; //el valor hexadecimal normalmente comienza con ox
        persona1.apellido = "bentancud";
        persona1.ObtenerInformacion();

        Persona persona2 = new Persona();
        System.out.println("persona2 = " + persona2);
        System.out.println("persona1 = " + persona1);
        persona2.ObtenerInformacion();
        persona2.nombre = "osvaldo";
        persona2.apellido = "giordanini";
        persona2.ObtenerInformacion();
    }
}

