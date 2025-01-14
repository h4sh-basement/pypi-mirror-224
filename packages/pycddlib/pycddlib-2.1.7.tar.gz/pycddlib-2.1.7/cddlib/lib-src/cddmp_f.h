/* generated automatically from cddmp.h */
/* cddmp.h       (cddlib arithmetic operations using gmp)
   written by Komei Fukuda, fukuda@math.ethz.ch
*/

/* This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 2 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program; if not, write to the Free Software
   Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
 */

#ifndef  _CDDMP_HF
#define  _CDDMP_HF
#endif  /* _CDDMP_HF */

/**********************************/
/*         MACROS                 */
/* dependent on mp implementation */
/**********************************/

#if defined ddf_GMPRATIONAL
 #include "gmp.h"
 #define ddf_ddf_ARITHMETIC "GMP rational"
 #define ddf_init(a)              mpq_init(a)     
 #define ddf_clear(a)             mpq_clear(a)     
 #define ddf_set(a, b)            mpq_set(a,b)     
 #define ddf_set_si(a, b)         dddf_mpq_set_si(a,b)  /* defined in cddgmp.c */
 #define ddf_set_si2(a, b, c)     mpq_set_si(a,b,c)    /* gmp 3.1 or higher */
 #define ddf_set_d(a, b)          mpq_set_d(a,b)       /* gmp 3.1 or higher */
 #define ddf_add(a, b, c)         mpq_add(a,b,c)
 #define ddf_sub(a, b, c)         mpq_sub(a,b,c)
 #define ddf_mul(a, b, c)         mpq_mul(a,b,c)
 #define ddf_div(a, b, c)         mpq_div(a,b,c)
 #define ddf_neg(a, b)            mpq_neg(a,b)
 #define ddf_inv(a, b)            mpq_inv(a,b)
 #define ddf_cmp(a, b)            mpq_cmp(a,b)  
    /* returns pos if a>b, 0 if a=b, negative if a<b */
 #define ddf_sgn(a)               mpq_sgn(a)
    /* returns nonzero if equal.  much faster than mpq_cmp. */
 #define ddf_get_d(a)             mpq_get_d(a)     
#elif defined GMPFLOAT
 #include "gmp.h"
 #define ddf_ddf_ARITHMETIC "GMP float"
 #define ddf_init(a)              mpf_init(a)     
 #define ddf_clear(a)             mpf_clear(a)     
 #define ddf_set(a, b)            mpf_set(a,b)     
 #define ddf_set_d(a, b)          mpf_set_d(a,b)     
 #define ddf_set_si(a, b)         mpf_set_si(a,b)     
 #define ddf_set_si2(a, b, c)     mpf_set_si(a,b,c)    /* gmp 3.1 or higher */
 #define ddf_add(a, b, c)         mpf_add(a,b,c)
 #define ddf_sub(a, b, c)         mpf_sub(a,b,c)
 #define ddf_mul(a, b, c)         mpf_mul(a,b,c)
 #define ddf_div(a, b, c)         mpf_div(a,b,c)
 #define ddf_neg(a, b)            mpf_neg(a,b)
 #define ddf_inv(a, b)            mpf_inv(a,b)
 #define ddf_cmp(a, b)            mpf_cmp(a,b)  
    /* returns pos if a>b, 0 if a=b, negative if a<b */
 #define ddf_sgn(a)               mpf_sgn(a)
 #define ddf_get_d(a)             mpf_get_d(a)     
#else /* built-in C double */
 #define ddf_ddf_ARITHMETIC "C double"
 #define ddf_ddf_CDOUBLE
 #define ddf_init(a)              dddf_init(a)     
 #define ddf_clear(a)             dddf_clear(a)     
 #define ddf_set(a, b)            dddf_set(a,b)     
 #define ddf_set_si(a, b)         dddf_set_si(a,b)     
 #define ddf_set_si2(a, b, c)     dddf_set_si2(a,b,c)  
 #define ddf_set_d(a, b)          dddf_set_d(a,b)     
 #define ddf_add(a, b, c)         dddf_add(a,b,c)
 #define ddf_sub(a, b, c)         dddf_sub(a,b,c)
 #define ddf_mul(a, b, c)         dddf_mul(a,b,c)
 #define ddf_div(a, b, c)         dddf_div(a,b,c)
 #define ddf_neg(a, b)            dddf_neg(a,b)
 #define ddf_inv(a, b)            dddf_inv(a,b)
 #define ddf_cmp(a, b)            dddf_cmp(a,b)  
    /* returns pos if a>b, 0 if a=b, negative if a<b */
 #define ddf_sgn(a)               dddf_sgn(a)
 #define ddf_get_d(a)             dddf_get_d(a)     
#endif


#if defined ddf_GMPRATIONAL
 typedef mpq_t myfloat;
#elif defined GMPFLOAT
 typedef mpf_t myfloat;
#else /* built-in C double */
 typedef double myfloat[1];
#endif

#if defined(__cplusplus)
extern "C" {
#endif

void dddf_mpq_set_si(myfloat,signed long);
void dddf_init(myfloat);  
void dddf_clear(myfloat);
void dddf_set(myfloat,myfloat);
void dddf_set_d(myfloat,double);
void dddf_set_si(myfloat,signed long);
void dddf_set_si2(myfloat,signed long, unsigned long);
void dddf_add(myfloat,myfloat,myfloat);
void dddf_sub(myfloat,myfloat,myfloat);
void dddf_mul(myfloat,myfloat,myfloat);
void dddf_div(myfloat,myfloat,myfloat);
void dddf_neg(myfloat,myfloat);
void dddf_inv(myfloat,myfloat);
int dddf_cmp(myfloat,myfloat);
int dddf_sgn(myfloat);
double dddf_get_d(myfloat);
void dddf_mpq_set_si(myfloat,signed long);

void ddf_set_global_constants(void);
void ddf_free_global_constants(void);  /* 094d */

#if defined(__cplusplus)
}
#endif

/* end of  cddmp.h  */
