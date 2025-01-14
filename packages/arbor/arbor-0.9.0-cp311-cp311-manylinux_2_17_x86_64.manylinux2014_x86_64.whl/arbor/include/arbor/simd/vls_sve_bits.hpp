#pragma once

// SVE SIMD intrinsics implementation with fixed sizes (VLS_SVE)

#ifdef __ARM_FEATURE_SVE

#include <arm_sve.h>

namespace arb {
namespace simd {
namespace detail {

// number of elements in a vector
static constexpr unsigned vls_sve_width = 128/64;

// Check required compiler features for VLS_SVE
#if (!defined(__ARM_FEATURE_SVE_BITS) || __ARM_FEATURE_SVE_BITS != 128)
#error "Vector length specific scalable vector extension (VLS_SVE) not enabled - did you compile with -msve-vector-bits=128?" 
#endif

// We currently do not rely on GNU vector extension, __attribute__((vector_size(vls_sve_width)). If defined, we could
// use basic vector operators and interoperability with GNU vectors. However, this seems not to be widely available.
// To test for these extensions, use feature detection macros
// - #if defined(__ARM_FEATURE_SVE_VECTOR_OPERATORS) && __ARM_FEATURE_SVE_VECTOR_OPERATORS == 1
// - #if defined(__ARM_FEATURE_SVE_PREDICATE_OPERATORS) && __ARM_FEATURE_SVE_PREDICATE_OPERATORS == 1

// sized types are obtained by type attribute
using fvuint32_t  = svuint32_t __attribute__((arm_sve_vector_bits(128)));
using fvuint64_t  = svuint64_t __attribute__((arm_sve_vector_bits(128)));
using fvint32_t   = svint32_t __attribute__((arm_sve_vector_bits(128)));
using fvint64_t   = svint64_t __attribute__((arm_sve_vector_bits(128)));
using fvfloat64_t = svfloat64_t __attribute__((arm_sve_vector_bits(128)));
using fvbool_t    = svbool_t __attribute__((arm_sve_vector_bits(128)));

// Due a limitation of the SVE implementation, it is currently not possible to store constant values
// in constexpr variables (even for the fixed-width case), such as
// static constexpr fvbool_t fvtrue = svptrue_b64();
// Therefore, all constants are created on the fly in the code just like in VLA SVE

} // namespace detail
} // namespace simd
} // namespace arb

#endif  // def __ARM_FEATURE_SVE
