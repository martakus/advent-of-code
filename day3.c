/* totally stolen from askalski on reddit, I just wanna see it work */
/* Compile with gcc -msse4.1 */

#include <stdio.h>
#include <x86intrin.h>

#define NUMBER_OF_SIDES_IN_A_TRIANGLE 3

int main(void)
{
  int a, b, c, i;

  __m128i vlongest = _mm_setzero_si128();
  __m128i vperimeter = _mm_setzero_si128();
  __m128i vpossible = _mm_setzero_si128();

  i = 0;
  while (scanf("%d %d %d", &a, &b, &c) == NUMBER_OF_SIDES_IN_A_TRIANGLE) {
    __m128i vside = _mm_set_epi32(0, c, b, a);
    vlongest = _mm_max_epi32(vlongest, vside);
    vperimeter = _mm_add_epi32(vperimeter, vside);
    if ((++i % NUMBER_OF_SIDES_IN_A_TRIANGLE) == 0) {
      __m128i vlongest_x2 = _mm_add_epi32(vlongest, vlongest);
      __m128i vcmp = _mm_cmpgt_epi32(vperimeter, vlongest_x2);
      vpossible = _mm_sub_epi32(vpossible, vcmp);
      vlongest = _mm_setzero_si128();
      vperimeter = _mm_setzero_si128();
    }
  }

  int possible = 0;
  for (i = 0; i < NUMBER_OF_SIDES_IN_A_TRIANGLE; i++) {
    possible += ((__v4si) vpossible)[i];
  }
  printf("Possible: %d\n", possible);

  return 0;
}
