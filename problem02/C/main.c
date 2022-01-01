#include "stdio.h"
#include "float.h"

#define SURVIVE 0.96
#define EMERGE 0.3
#define CLUTCH_PROP 1.2
#define TIME 200
#define INIT_LARVAL 100

int main (int args, char **argv){

  FILE *fp;
  fp = fopen("output","w");
  // params
  const double S = SURVIVE;
  const double E = EMERGE;
  const double A = CLUTCH_PROP;
  
  int larval_10 = INIT_LARVAL; // 10年周期の幼虫の数
  int larval_13 = INIT_LARVAL;
  int period_10 = 10, period_13 = 13;
  for (int t=1; t<=TIME;t++) {
    // write here
    int adults_10=0,adults_13=0;
    if (t%period_10 == 0) {
      adults_10 = E * larval_10;
      larval_10 = 0;
    }
    if (t%period_13 == 0) {
      adults_13 = E * larval_13;
      larval_13 = 0;
    }
    larval_10 = S*larval_10;
    larval_13 = S*larval_13;
    larval_10 += adults_10/2 * (A*period_10);
    larval_13 += adults_13/2 * (A*period_13);
    fprintf(fp, "%d %d %d\n",t,larval_10,larval_13);
  }
  return 0;
}
