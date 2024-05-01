for (int i = 2; i*i*i*i <= n; i++) {
if (primeArray[i] == true) {
for (int j = i*i; j*j <= n; j+=i) {primeArray[j] = false;}
}}
#pragma omp parallel for ? Jaki podział pracy ?
for (int i = 2; i*i <= n; i++){
if (primeArray[i]) {
int firstMultiple = (m / i);
if (firstMultiple <= 1) {firstMultiple = i + i;}
else
if (m % i) { firstMultiple = (firstMultiple * i) + i;}
else {firstMultiple = (firstMultiple * i);}
for (int j = firstMultiple; j <= n; j+=i) { result[j-m] = false;}
}}