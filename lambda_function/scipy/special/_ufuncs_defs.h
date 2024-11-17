#ifndef UFUNCS_PROTO_H
#define UFUNCS_PROTO_H 1
#include "_cosine.h"
npy_double cosine_cdf(npy_double);
npy_double cosine_invcdf(npy_double);
#include "special_wrappers.h"
npy_double cephes_igam_fac(npy_double, npy_double);
npy_double cephes_kolmogc(npy_double);
npy_double cephes_kolmogci(npy_double);
npy_double cephes_kolmogp(npy_double);
npy_double cephes_lanczos_sum_expg_scaled(npy_double);
npy_double cephes_lgam1p(npy_double);
npy_double cephes_log1pmx(npy_double);
npy_double cephes_riemann_zeta(npy_double);
npy_double cephes_smirnovc(npy_int, npy_double);
npy_double cephes_smirnovci(npy_int, npy_double);
npy_double cephes_smirnovp(npy_int, npy_double);
npy_double cephes__struve_asymp_large_z(npy_double, npy_double, npy_int, npy_double *);
npy_double cephes__struve_bessel_series(npy_double, npy_double, npy_int, npy_double *);
npy_double cephes__struve_power_series(npy_double, npy_double, npy_int, npy_double *);
npy_double cephes_bdtr(npy_double, npy_int, npy_double);
npy_double cephes_bdtrc(npy_double, npy_int, npy_double);
npy_double cephes_bdtri(npy_double, npy_int, npy_double);
npy_double cephes_besselpoly(npy_double, npy_double, npy_double);
npy_double cephes_beta(npy_double, npy_double);
npy_double cephes_lbeta(npy_double, npy_double);
npy_double cephes_btdtr(npy_double, npy_double, npy_double);
npy_double cephes_btdtri(npy_double, npy_double, npy_double);
npy_double cephes_cbrt(npy_double);
npy_double cephes_chdtr(npy_double, npy_double);
npy_double cephes_chdtrc(npy_double, npy_double);
npy_double cephes_chdtri(npy_double, npy_double);
npy_double cephes_cosdg(npy_double);
npy_double cephes_cosm1(npy_double);
npy_double cephes_cotdg(npy_double);
npy_double cephes_ellpe(npy_double);
npy_double cephes_ellie(npy_double, npy_double);
npy_int cephes_ellpj_wrap(npy_double, npy_double, npy_double *, npy_double *, npy_double *, npy_double *);
npy_double special_ellipk(npy_double);
npy_double cephes_ellik(npy_double, npy_double);
npy_double cephes_ellpk(npy_double);
npy_double cephes_erf(npy_double);
npy_double cephes_erfc(npy_double);
npy_double cephes_erfcinv(npy_double);
npy_double cephes_exp10(npy_double);
npy_double cephes_exp2(npy_double);
npy_double cephes_expm1(npy_double);
npy_double cephes_expn(npy_int, npy_double);
npy_double cephes_fdtr(npy_double, npy_double, npy_double);
npy_double cephes_fdtrc(npy_double, npy_double, npy_double);
npy_double cephes_fdtri(npy_double, npy_double, npy_double);
npy_int cephes_fresnl_wrap(npy_double, npy_double *, npy_double *);
npy_int cfresnl_wrap(npy_cdouble, npy_cdouble *, npy_cdouble *);
npy_double cephes_igam(npy_double, npy_double);
npy_double cephes_igamc(npy_double, npy_double);
npy_double cephes_igamci(npy_double, npy_double);
npy_double cephes_igami(npy_double, npy_double);
npy_double cephes_gammasgn(npy_double);
npy_double cephes_gdtr(npy_double, npy_double, npy_double);
npy_double cephes_gdtrc(npy_double, npy_double, npy_double);
npy_cdouble chyp1f1_wrap(npy_double, npy_double, npy_cdouble);
npy_double cephes_i0(npy_double);
npy_double cephes_i0e(npy_double);
npy_double cephes_i1(npy_double);
npy_double cephes_i1e(npy_double);
npy_double cephes_j0(npy_double);
npy_double cephes_j1(npy_double);
npy_double cephes_k0(npy_double);
npy_double cephes_k0e(npy_double);
npy_double cephes_k1(npy_double);
npy_double cephes_k1e(npy_double);
npy_double special_cyl_bessel_k_int(npy_int, npy_double);
npy_double cephes_kolmogi(npy_double);
npy_double cephes_kolmogorov(npy_double);
npy_double cephes_log1p(npy_double);
npy_double pmv_wrap(npy_double, npy_double, npy_double);
npy_double cephes_struve_l(npy_double, npy_double);
npy_double cephes_nbdtr(npy_int, npy_int, npy_double);
npy_double cephes_nbdtrc(npy_int, npy_int, npy_double);
npy_double cephes_nbdtri(npy_int, npy_int, npy_double);
npy_double cephes_ndtr(npy_double);
npy_double cephes_ndtri(npy_double);
npy_double cephes_owens_t(npy_double, npy_double);
npy_double cephes_pdtr(npy_double, npy_double);
npy_double cephes_pdtrc(npy_double, npy_double);
npy_double cephes_pdtri(npy_int, npy_double);
npy_double cephes_poch(npy_double, npy_double);
npy_double cephes_radian(npy_double, npy_double, npy_double);
npy_double cephes_round(npy_double);
npy_int cephes_shichi_wrap(npy_double, npy_double *, npy_double *);
npy_int cephes_sici_wrap(npy_double, npy_double *, npy_double *);
npy_double cephes_sindg(npy_double);
npy_double cephes_smirnov(npy_int, npy_double);
npy_double cephes_smirnovi(npy_int, npy_double);
npy_double cephes_spence(npy_double);
npy_double cephes_struve_h(npy_double, npy_double);
npy_double cephes_tandg(npy_double);
npy_double cephes_tukeylambdacdf(npy_double, npy_double);
npy_double cephes_y0(npy_double);
npy_double cephes_y1(npy_double);
npy_double cephes_yn(npy_int, npy_double);
npy_double cephes_zetac(npy_double);
#endif
