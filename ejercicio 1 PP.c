#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define TAM 1000
// generador de arreglo
void summonarray(int arreglo[],int tam){ 
    int i;
    for(i=0;i<tam;i++){
         arreglo[i]=rand()% 1000+1;               
        }
    }
//imprimir arreglo
void printarray(int arreglo[],int tam){
     int i;
     for(i=0;i<tam;i++){
         printf("%d ",arreglo[i]);
          if (i < tam - 1) {
            printf(", ");
        }
        }
     }
//busqueda secuencial
int searcharray(int arreglo[],int tam,int elemento){
     int i;
      for(i=0;i<tam;i++){
         if(arreglo[i]== elemento){
          return i;
          }               
        }
     return -1;
     }
//ordenar arreglo
void orderarray(int arreglo[],int tam ){
     int i,j,temp;
     for(i=0;i<tam -1;i++){
        for(j=i+1;j<tam;j++){
        if(arreglo[i]>arreglo[j]){
            temp=arreglo[i];
            arreglo[i]=arreglo[j];
            arreglo[j]=temp;
         } 
       }  
     }
}
///////////////////////////////////////////////////////////////////////////

int main(){
    int arreglo[TAM];
   srand(time(NULL));

 clock_t inicio = clock();
    //llamar funcion generar arreglo
     summonarray(arreglo,TAM);
    
    //imprimir arreglo
     printf("el arreglo generado es: \n");
     printarray(arreglo,TAM);
     
    //busqueda
    
    // int elemento = arreglo[0];
    //int indice = searcharray(arreglo,TAM, elemento);
  
    //busqueda 
   printf(" \n");
   int elemento = arreglo[0]; // Buscar el primer elemento del arreglo
    int posicion = searcharray(arreglo, TAM, elemento);
    if (posicion != -1) {
        printf("El valor %d se encuentra en la posicion %d del arreglo.\n", elemento, posicion);
    } else {
        printf("El valor %d no se encuentra en el arreglo.\n", elemento);
    }
   
   // Ordenar arreglo
    orderarray(arreglo, TAM);
    
   //imprimir arreglo ordenado
     printf("el arreglo ordenado es: \n");
     printarray(arreglo,TAM);
     
     //busqueda ordenado
   printf(" \n");
   
    posicion = searcharray(arreglo, TAM, elemento);
    printf("El valor %d se encuentra en la posicion %d del arreglo.\n", elemento, posicion);
 clock_t fin = clock();
      printf("Tiempo de ejecicion del programa: %f segundos\n", (double)(fin - inicio) / CLOCKS_PER_SEC);
  return 0;
    
	}
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
