//! Region 2 - Backward Equation:(p.s)->T
//! *  Page 25: 6.3.2 The Backward Equations T( p, s ) for Subregions 2a, 2b, and 2c.
//！   ps2T_reg2(p,s)

use crate::algo::*;
use crate::common::constant::*;
use crate::r2::region2_pT::*;

/// the backward equation T( p,s )
pub fn ps2T_reg2a(p: f64, s: f64) -> f64 {
    // Table 25. Page 26  the coefficients and exponents of equation T( p,s ) for  subregion 2a, Eq.(25)
    const IJn: [(f64, i32, f64); 46] = [
        (-1.5, -24, -0.39235983861984E+06),
        (-1.5, -23, 0.51526573827270E+06),
        (-1.5, -19, 0.40482443161048E+05),
        (-1.5, -13, -0.32193790923902E+03),
        (-1.5, -11, 0.96961424218694E+02),
        //6
        (-1.5, -10, -0.22867846371773E+02),
        (-1.25, -19, -0.44942914124357E+06),
        (-1.25, -15, -0.50118336020166E+04),
        (-1.25, -6, 0.35684463560015E+00),
        (-1.0, -26, 0.44235335848190E+05),
        // 11
        (-1.0, -21, -0.13673388811708E+05),
        (-1.0, -17, 0.42163260207864E+06),
        (-1.0, -16, 0.22516925837475E+05),
        (-1.0, -9, 0.47442144865646E+03),
        (-1.0, -8, -0.14931130797647E+03),
        // 16
        (-0.75, -15, -0.19781126320452E+06),
        (-0.75, -14, -0.23554399470760E+05),
        (-0.5, -26, -0.19070616302076E+05),
        (-0.5, -13, 0.55375669883164E+05),
        (-0.5, -9, 0.38293691437363E+04),
        //21
        (-0.5, -7, -0.60391860580567E+03),
        (-0.25, -27, 0.19363102620331E+04),
        (-0.25, -25, 0.42660643698610E+04),
        (-0.25, -11, -0.59780638872718E+04),
        (-0.25, -6, -0.70401463926862E+03),
        //26
        (0.25, 1, 0.33836784107553E+03),
        (0.25, 4, 0.20862786635187E+02),
        (0.25, 8, 0.33834172656196E-01),
        (0.25, 11, -0.43124428414893E-04),
        (0.5, 0, 0.16653791356412E+03),
        // 31
        (0.5, 1, -0.13986292055898E+03),
        (0.5, 5, -0.78849547999872E+00),
        (0.5, 6, 0.72132411753872E-01),
        (0.5, 10, -0.59754839398283E-02),
        (0.5, 14, -0.12141358953904E-04),
        // 36
        (0.5, 16, 0.23227096733871E-06),
        (0.75, 0, -0.10538463566194E+02),
        (0.75, 4, 0.20718925496502E+01),
        (0.75, 9, -0.72193155260427E-01),
        (0.75, 17, 0.20749887081120E-06),
        // 41
        (1.0, 7, -0.18340657911379E-01),
        (1.0, 18, 0.29036272348696E-06),
        (1.25, 3, 0.21037527893619E+00),
        (1.25, 15, 0.2568123972999E-03),
        (1.5, 5, -0.1279900293381E-01),
        // 46
        (1.5, 18, -0.82198102652018E-05),
    ];

    let pi: f64 = p / 1.0;
    let sigma: f64 = s / 2.0 - 2.0;
    let mut theta: f64 = 0.0;
    for k in IJn {
        theta += k.2 * pi.powf(k.0) * sigma.powi(k.1); // IJn[k].0 is float
    }
    1.0 * theta
}

pub fn ps2T_reg2b(p: f64, s: f64) -> f64 {
    // Table 26. Page 27 the coefficients and exponents of  the equation T(p,s) for subregion 2b, Eq (26)
    const IJn: [(i32, i32, f64); 44] = [
        (-6, 0, 0.31687665083497e6),
        (-6, 11, 0.20864175881858e2),
        (-5, 0, -0.39859399803599e6),
        (-5, 11, -0.21816058518877e2),
        (-4, 0, 0.22369785194242e6),
        (-4, 1, -0.27841703445817e4),
        (-4, 11, 0.99207436071480e1),
        (-3, 0, -0.75197512299157e5),
        (-3, 1, 0.29708605951158e4),
        (-3, 11, -0.34406878548526e1),
        (-3, 12, 0.38815564249115),
        (-2, 0, 0.17511295085750e5),
        (-2, 1, -0.14237112854449e4),
        (-2, 6, 0.10943803364167e1),
        (-2, 10, 0.89971619308495),
        (-1, 0, -0.33759740098958e4),
        (-1, 1, 0.47162885818355e3),
        (-1, 5, -0.19188241993679e1),
        (-1, 8, 0.41078580492196),
        (-1, 9, -0.33465378172097),
        (0, 0, 0.13870034777505e4),
        (0, 1, -0.40663326195838e3),
        (0, 2, 0.41727347159610e2),
        (0, 4, 0.21932549434532e1),
        (0, 5, -0.10320050009077e1),
        (0, 6, 0.35882943516703),
        (0, 9, 0.52511453726066e-2),
        (1, 0, 0.12838916450705e2),
        (1, 1, -0.28642437219381e1),
        (1, 2, 0.56912683664855),
        (1, 3, -0.99962954584931e-1),
        (1, 7, -0.32632037778459e-2),
        (1, 8, 0.23320922576723e-3),
        (2, 0, -0.15334809857450),
        (2, 1, 0.29072288239902e-1),
        (2, 5, 0.37534702741167e-3),
        (3, 0, 0.17296691702411e-2),
        (3, 1, -0.38556050844504e-3),
        (3, 3, -0.35017712292608e-4),
        (4, 0, -0.14566393631492e-4),
        (4, 1, 0.56420857267269e-5),
        (5, 0, 0.41286150074605e-7),
        (5, 1, -0.20684671118824e-7),
        (5, 2, 0.16409393674725e-8),
    ];

    let pi: f64 = p / 1.0;
    let sigma: f64 = 10.0 - s / 0.7853;
    let steps: [(usize, usize); 2] = [(0, 22), (22, 44)];
    1.0 * poly_powi_steps(pi, sigma, &IJn, &steps)
}

pub fn ps2T_reg2c(p: f64, s: f64) -> f64 {
    // Table 27. Page 28  the coefficient s and exponents of the equation T(p,s) for subregion 2c, Eq.(27)
    const IJn: [(i32, i32, f64); 30] = [
        (-2, 0, 0.90968501005365e3),
        (-2, 1, 0.24045667088420e4),
        (-1, 0, -0.59162326387130e3),
        (0, 0, 0.54145404128074e3),
        (0, 1, -0.27098308411192e3),
        (0, 2, 0.97976525097926e3),
        (0, 3, -0.46966772959435e3),
        (1, 0, 0.14399274604723e2),
        (1, 1, -0.19104204230429e2),
        (1, 3, 0.53299167111971e1),
        (1, 4, -0.21252975375934e2),
        (2, 0, -0.31147334413760),
        (2, 1, 0.60334840894623),
        (2, 2, -0.42764839702509e-1),
        (3, 0, 0.58185597255259e-2),
        (3, 1, -0.14597008284753e-1),
        (3, 5, 0.56631175631027e-2),
        (4, 0, -0.76155864584577e-4),
        (4, 1, 0.22440342919332e-3),
        (4, 4, -0.12561095013413e-4),
        (5, 0, 0.63323132660934e-6),
        (5, 1, -0.20541989675375e-5),
        (5, 2, 0.36405370390082e-7),
        (6, 0, -0.29759897789215e-8),
        (6, 1, 0.10136618529763e-7),
        (7, 0, 0.59925719692351e-11),
        (7, 1, -0.20677870105164e-10),
        (7, 3, -0.20874278181886e-10),
        (7, 4, 0.10162166825089e-9),
        (7, 5, -0.16429828281347e-9),
    ];

    let pi: f64 = p / 1.0;
    let sigma: f64 = 2.0 - s / 2.9251;
    1.0 * poly_powi(pi, sigma, &IJn)
}

pub fn ps2T_reg2(p: f64, s: f64) -> f64 {
    let mut T: f64 = 0.0;
    if p > 4.0 {
        if s < 5.85 {
            T = ps2T_reg2c(p, s);
        } else {
            T = ps2T_reg2b(p, s);
        }
    } else {
        T = ps2T_reg2a(p, s);
    }
    T
}
