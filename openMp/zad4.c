#include <stdio.h>
#include <time.h>
#include <omp.h>

long long num_steps = 1000000000;
double step;
int ilosci[2] = {6, 12};
int main(int argc, char* argv[])
{
	clock_t spstart, spstop,ppstart,ppstop;
	
	double sswtime, sewtime, pswtime, pewtime;
//volatile
	double x, pi, sum=0.0;
	int i;
//SEKWENCYJNIE
	sswtime = omp_get_wtime();
	spstart = clock();
 
	step = 1./(double)num_steps;

	for (i=0; i<num_steps; i++)
	{
		x = (i + .5)*step;
		sum = sum + 4.0/(1.+ x*x);
	}
	
	pi = sum*step;

	spstop = clock();
   sewtime = omp_get_wtime();


    printf("%15.12f artosc liczby PI sekwencyjnie \n", pi);
	printf("Czas procesorów przetwarzania sekwencyjnego  %f sekund \n", ((double)(spstop - spstart)/CLOCKS_PER_SEC));
	printf("Czas trwania obliczen sekwencyjnych - wallclock %f sekund \n",  sewtime-sswtime);

	
	




//RÓWNOLEGLE 
    step = 1. / (double)num_steps;
    for (int j = 0; j < 2; j++){
        omp_set_num_threads(ilosci[j]);
	    pswtime = omp_get_wtime();
	    ppstart = clock();
        sum = 0.0;
	
        #pragma omp parallel 
        {
            double local_sum = 0.0;
        #pragma omp for
	    for (i = 0; i < num_steps; i++)
	        {   
		        double x = (i + .5) * step;
                
		        local_sum = local_sum + 4.0 / (1. + x * x);
	        }
            #pragma omp atomic 
            sum += local_sum;
        }
	    pi = sum * step;

	    ppstop = clock();
	    pewtime = omp_get_wtime();
        printf("Ilość wątków: %d\n", ilosci[j]);
        printf("%15.12f Wartosc liczby PI rownolegle \n",pi);
        printf("Czas procesorów przetwarzania równoleglego  %f sekund \n", ((double)(ppstop - ppstart)/CLOCKS_PER_SEC));
        printf("Czas trwania obliczen rownoleglych - wallclock %f sekund \n", pewtime-pswtime);
        printf("Przyspieszenie %5.3f \n", (sewtime - sswtime) / (pewtime - pswtime));


    }


}