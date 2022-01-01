#include "stdio.h"
#include "float.h"

#define SURVIVE 0.96
#define EMERGE 0.3
#define CLUTCH_PROP 1.2
#define TIME 100
#define INIT_LARVAL 100

int main (int args, char **argv){

  FILE *fp;
  fp = fopen("output","w");
  // params
  const double S = SURVIVE;
  const double E = EMERGE;
  const double A = CLUTCH_PROP;
  
  int larval = INIT_LARVAL; // 幼虫の数
  int period = 10; // 周期
  for (int t=1; t<=TIME;t++) {
    // write here
    int adults = 0; // 成虫の数
    if (t%period == 0) {
      adults = E * larval;
      larval = adults/2*(A*period);
    } else {
      larval = S*larval;
    }
    fprintf(fp, "%d %d\n",t,larval);
  }
  return 0;
}
