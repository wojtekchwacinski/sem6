#include <stdio.h>
#include <time.h>
#include <omp.h>

long long num_steps = 1000000;
double step;

int main(int argc, char* argv[])

{	volatile double tab[50];
	clock_t spstart, spstop,ppstart,ppstop;
	
	double sswtime, sewtime, pswtime, pewtime;
//volatile
	double x, pi, sum=0.0;
	int i;
  
  
  
  
  
  
 	for(int j = 0; j < 49; j++){
//RÓWNOLEGLE 
	
	pswtime = omp_get_wtime();
	ppstart = clock();
	sum = 0.0;
	step = 1. / (double)num_steps;
	
	#pragma omp parallel num_threads(2)
	{
	int id = 2*omp_get_thread_num();
	tab[id+j] = 0;
	tab[id] = 0;
	
	#pragma omp for
	for (i = 0; i < num_steps; i++)
	{	
		double x = (i + .5) * step;
		#pragma omp flush(tab)
		tab[id+j] = tab[id+j] + 4.0 / (1. + x * x);
		#pragma omp flush(tab)
	}
	#pragma omp atomic
	sum += tab[id+j];
	}
	pi = sum * step;
	
	ppstop = clock();
	pewtime = omp_get_wtime();

	printf("%15.12f Wartosc liczby PI rownolegle \n",pi);
	
	//printf("Czas procesorów przetwarzania równoleglego  %f sekund \n", ((double)(ppstop - ppstart)/CLOCKS_PER_SEC));

	printf("Czas trwania obliczen rownoleglych - wallclock %f sekund \n", pewtime-pswtime);
	}
	return 0;
}	
