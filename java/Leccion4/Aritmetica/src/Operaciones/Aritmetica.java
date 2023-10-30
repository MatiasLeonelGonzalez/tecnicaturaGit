
package Operaciones;


public class Aritmetica {
    //atributos de la clase
    int a;
    int b;
    
    //Metodo
    public void sumarNumeros() {
        int resultado = a + b;
        System.out.println("resultado = " + resultado);
    }
    public int sumarConRetorno(){
        //int resultado = a + b;
        return a + b;
    }
    
    public int sumarConArgumentos(int arg1, int arg2){
        this.a = arg1; // el argumento a se asigna al atributo this.a
        this.b = arg2;
        //return a + b;
        return this.sumarConRetorno(); //video 5 clase 5
    }
    
}
