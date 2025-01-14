#ifndef __ARPACKDEF_H__
#define __ARPACKDEF_H__

/* arpackdef.h must be included only by C/C++, not by F77/F90. */

#define INTERFACE64 0

#if INTERFACE64
#include <stdint.h> /* Include this header for int64_t, uint64_t definition. */
#define a_int int64_t
#define a_uint uint64_t
#else
#define a_int int
#define a_uint unsigned int
#endif
#if !defined(__INTEL_LLVM_COMPILER) && defined(_MSC_VER)
#ifndef _CRT_USE_C_COMPLEX_H
#define _CRT_USE_C_COMPLEX_H
#include <complex.h>
#undef I
#undef _CRT_USE_C_COMPLEX_H
#else
#include <complex.h>
#endif
#define a_fcomplex _Fcomplex
#define a_dcomplex _Dcomplex
#ifndef CMPLXF
#define CMPLXF(r,i) _FCbuild(r,i)
#endif
#ifndef CMPLX
#define CMPLX(r,i) _Cbuild(r,i)
#endif
#else
#ifndef CMPLXF
#define CMPLXF(r,i) ((float _Complex)((float)(r) + _Complex_I * (float)(i)))
#endif
#ifndef CMPLX
#define CMPLX(r,i) ((double _Complex)((double)(r) + _Complex_I * (double)(i)))
#endif
#define a_fcomplex float _Complex
#define a_dcomplex double _Complex
#endif

#endif
