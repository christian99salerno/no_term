#include <stdio.h>

int main ()
{
  int num = 0;
  int num_input = 0;

  int somma = 0;

  FILE *f = fopen("sum.dat", "r");

  if (!f) {
   printf("File inesistente, il valore di partenza e' 0'\n");
  } else {
    printf("Lettura in sum.dat in corso ...\n");
    fscanf(f, "%d", &num);
    printf("Valore attuale in sum.dat: %d\n", num);
    fclose(f);
  }

  printf("Digita un valore da sommare: ");
  scanf("%d", &num_input);  

  somma = num + num_input;

  printf("Nuovo valore: %d\n", somma);
  printf("Salvataggio in sum.dat in corso ...\n");
  f = fopen("sum.dat", "w");
  fprintf(f, "%d",somma);
  fclose(f);
  return 0;
}

