for (int i = 2; i*i*i*i <= n; i++) {
if (primeArray[i] == true) {
for (int j = i*i; j*j <= n; j+=i) {primeArray[j] = false;}
}}
#pragma omp parallel for ? Jaki podział pracy ?
for (int i = 2; i*i <= n; i++){
if (primeArray[i]) {
…
for (int j = firstMultiple; j <= n; j+=i) {
if (result[j-m]) result[j-m] = false;} FS!
}}