import numpy as np
import math
import os
import math
from scipy.integrate import odeint
from scipy.integrate import *
# getting variabls from GUI:

class solve_baza():
    def __init__(self):
        self.baza=[]

    def get_from_GUI(self,free, BCS):
        subset_of_free = [1000000, 10000000, 100000000]
        fvv = [a for a in free if a not in subset_of_free]
        num = len(fvv)
        num1 = len(free)
        fvn0 = np.zeros(num1)
        nfvn0 = np.zeros(num1)
        for l in range(num1):
            if free[l] == 1000000:
                fvn0[l] = l
                nfvn[l] = 0
            else:
                fvn0[l] = 0
                nfvn[l] = 1
        dummy = [0, 1000]
        dummy2 = [1, 1000]
        fvn = [a for a in fvn0 if a not in dummy]
        nfvn = [a for a in nfvn0 if a not in dummy2]
        subset_of_Bcs = [1000000, 10000000, 100000000]
        BCsv = [a for a in BCS if a not in subset_of_Bcs]
        num2 = len(BCS)
        BCsn0 = np.zeros(num2)
        for l in range(num2):
            if BCS[l] == 1000000:
                BCsn0[l] = l
            else:
                BCsn0[l] = 0
        BCSn = [a for a in BCsn0 if a not in dummy]
        return fvn, fvv, nfvn, BCSn, BCsv

    # firs the propagator:
    def state_vec(self,t0, u_, k, ad):
        ax, ay, az = ad(t0, u_, k)

        x, y, z, vx, vy, vz = u_
        r3 = (x ** 2 + y ** 2 + z ** 2) ** 1.5

        du = np.array([
            vx,
            vy,
            vz,
            -k * x / r3 + ax,
            -k * y / r3 + ay,
            -k * z / r3 + az
        ])
        return du

    def form_segment(self,yy, tof, rtol=1e-11, ad=None, callback=None, nsteps=1e8):
        k = 398600
        r0 = [yy[0], yy[1], yy[2]]
        v0 = [yy[3], yy[4], yy[5]]
        x, y, z = r0
        vx, vy, vz = v0
        u0 = np.array([x, y, z, vx, vy, vz])

        if ad is None:
            ad = lambda t0, u_, k_: (0, 0, 0)

        # Set the integrator
        rr = ode(state_vec).set_integrator('dopri5', rtol=rtol, nsteps=nsteps)
        rr.set_initial_value(u0)  # Initial time equal to 0.0
        rr.set_f_params(k, ad)
        if callback:
            rr.set_solout(callback)

        # Make integration step
        rr.integrate(tof)

        if rr.successful():
            r, v = rr.y[:3], rr.y[3:]
        else:
            raise RuntimeError("Integration failed")

        return r, v

    # the transformation function from VUW to ECI
    def transformation(self,r0, v0):
        V0 = np.linalg.norm(v0)
        vhat = np.array([v0 / V0], dtype=float)
        rcrosv = np.cross(r0, v0)
        W = np.linalg.norm(rcrosv)
        what = np.array([rcrosv / W], dtype=float)
        uhat = np.cross(what, vhat)
        Rtransform = np.zeros((3, 3), dtype=float)
        for r in range(3):
            Rtransform[0, :] = vhat
            Rtransform[1, :] = uhat
            Rtransform[2, :] = what
        return Rtransform

    def jac(self,r0, v0, x0, freev, bcs):
        pare = np.array([0, 0, 0, 0, 0, 0, 0], dtype=float)
        pari = np.array([0, 0, 0, 0, 0, 0, 0], dtype=float)
        parv = np.array([0, 0, 0, 0, 0, 0, 0], dtype=float)
        parr = np.array([0, 0, 0, 0, 0, 0, 0], dtype=float)
        para = np.array([0, 0, 0, 0, 0, 0, 0], dtype=float)
        parE = np.array([0, 0, 0, 0, 0, 0, 0], dtype=float)
        partp = np.array([0, 0, 0, 0, 0, 0, 0], dtype=float)
        homan = np.array([0, 0, 0, 0, 0, 0, 0], dtype=float)
        for i in range(7):
            if i < 3:
                epslon = np.array([0, 0, 0], dtype=float)
                epslon[i] = 1
                epslon = .0000001 * epslon
                x001 = np.array([x0[0], x0[1], x0[2]], dtype=float)
                x00 = x001 + epslon
                vdd = float(x00[0] * np.cos(x00[2]) * np.cos(x00[1]))
                udd = float(x00[0] * np.cos(x00[2]) * np.sin(x00[1]))
                wdd = float(x00[0] * np.sin(x00[2]))
                vuw = np.array([vdd, udd, wdd], dtype=float)
                Rtransform0 = self.transformation(r0, v0)
                delta = np.dot(vuw, Rtransform0)
                vp = v0 + delta
                yy = [r0[0], r0[1], r0[2], vp[0], vp[1], vp[2]]
                [rf2, v12] = form_segment(yy, x0[6])
                x000 = np.array([x0[3], x0[4], x0[5]], dtype=float)
                vdd1 = float(x000[0] * np.cos(x000[2]) * np.cos(x000[1]))
                udd1 = float(x000[0] * np.cos(x000[2]) * np.sin(x000[1]))
                wdd1 = float(x000[0] * np.sin(x000[2]))
                vuw1 = np.array([vdd1, udd1, wdd1], dtype=float)
                Rtransform2 = self.transformation(rf2, v12)
                dv22 = np.dot(vuw1, Rtransform2)
                vf2 = v12 + dv22
                x01 = np.array([x0[0], x0[1], x0[2]], dtype=float)
                vdd0 = float(x01[0] * np.cos(x01[2]) * np.cos(x01[1]))
                udd0 = float(x01[0] * np.cos(x01[2]) * np.sin(x01[1]))
                wdd0 = float(x01[0] * np.sin(x01[2]))
                vuw0 = np.array([vdd0, udd0, wdd0], dtype=float)
                delta1 = np.dot(vuw0, Rtransform0)
                vp0 = v0 + delta1
                yy0 = [r0[0], r0[1], r0[2], vp0[0], vp0[1], vp0[2]]
                [rf1, v11] = form_segment(yy0, x0[6])
                Rtransform1 = self.transformation(rf1, v11)
                dv21 = np.dot(vuw1, Rtransform1)
                vf1 = v11 + dv21
                # then we calculate the orbital elements
                # orbit with epselon
                h2 = np.cross(rf2, vf2)
                H2 = float(np.linalg.norm(h2))
                i2 = float(np.arccos(h2[2] / H2))
                Vf2 = float(np.linalg.norm(vf2))
                Rf2 = float(np.linalg.norm(rf2))
                Enf2 = float(((Vf2 ** 2) / 2) - (398600 / Rf2))
                Ef2 = np.cross(vf2, h2) / 398600 - rf2 / Rf2
                ef2 = float(np.linalg.norm(Ef2))
                af2 = -float(398600 / (2 * Enf2))
                tp2 = float(2 * pi * np.sqrt((abs(af2) ** 3) / 398600))
                # orbit without epselon
                h1 = np.cross(rf1, vf1)
                H1 = float(np.linalg.norm(h1))
                i1 = float(np.arccos(h1[2] / H1))
                Vf1 = float(np.linalg.norm(vf1))
                Rf1 = float(np.linalg.norm(rf1))
                Enf1 = float(((Vf1 ** 2) / 2) - (398600 / Rf1))
                Ef1 = np.cross(vf1, h1) / 398600 - rf1 / Rf1
                ef1 = float(np.linalg.norm(Ef1))
                af1 = -float(398600 / (2 * Enf1))
                tp1 = float(2 * pi * np.sqrt((abs(af1) ** 3) / 398600))
                rdotv1 = float(np.dot(rf1, vf1))
                rdotv2 = float(np.dot(rf2, vf2))

                # clculat the partial direvativs
                pare[i] = (ef2 - ef1) / .00000001
                pari[i] = (i2 - i1) / .00000001
                parv[i] = (Vf2 - Vf1) / .00000001
                parr[i] = (Rf1 - Rf2) / .00000001
                parE[i] = (Enf2 - Enf1) / .00000001
                para[i] = (af2 - af1) / .00000001
                partp[i] = (tp2 - tp1) / .00000001
                homan[i] = (rdotv2 - rdotv1) / .00000001
            elif i >= 3 and i < 6:
                epslon = np.array([0, 0, 0], dtype=float)
                epslon[i - 3] = 1
                epslon = .00000001 * epslon
                x00 = np.array([x0[0], x0[1], x0[2]])
                vdd = x00[0] * np.cos(x00[2]) * np.cos(x00[1])
                udd = x00[0] * np.cos(x00[2]) * np.sin(x00[1])
                wdd = x00[0] * np.sin(x00[2])
                vuw = np.array([vdd, udd, wdd])
                Rtransform0 = self.transformation(r0, v0)
                delta = np.dot(vuw, Rtransform0)
                vp0 = v0 + delta
                yy0 = [r0[0], r0[1], r0[2], vp0[0], vp0[1], vp0[2]]
                [rf, v1] = self.form_segment(yy0, x0[6])
                rf1 = rf
                rf2 = rf
                x000 = np.array([x0[3], x0[4], x0[5]])
                vdd1 = x000[0] * np.cos(x000[2]) * np.cos(x000[1])
                udd1 = x000[0] * np.cos(x000[2]) * np.sin(x000[1])
                wdd1 = x000[0] * np.sin(x000[2])
                vuw1 = np.array([vdd1, udd1, wdd1])
                trans = self.transformation(rf, v1)
                dv221 = np.dot(vuw1, trans)
                vf1 = v1 + dv221
                x001 = x000 + epslon
                vdd2 = x001[0] * np.cos(x001[2]) * np.cos(x001[1])
                udd2 = x001[0] * np.cos(x001[2]) * np.sin(x001[1])
                wdd2 = x001[0] * np.sin(x001[2])
                vuw2 = np.array([vdd2, udd2, wdd2])
                trans2 = self.transformation(rf, v1)
                dv221 = np.dot(vuw2, trans2)
                vf2 = v1 + dv221
                h2 = np.cross(rf2, vf2)
                H2 = float(np.linalg.norm(h2))
                i2 = float(np.arccos(h2[2] / H2))
                Vf2 = float(np.linalg.norm(vf2))
                Rf2 = float(np.linalg.norm(rf2))
                Enf2 = float(((Vf2 ** 2) / 2) - (398600 / Rf2))
                Ef2 = np.cross(vf2, h2) / 398600 - rf2 / Rf2
                ef2 = float(np.linalg.norm(Ef2))
                af2 = float(-398600 / (2 * Enf2))
                tp2 = float(2 * pi * np.sqrt((abs(af2) ** 3) / 398600))
                # orbit without epselon
                h1 = float(np.cross(rf1, vf1))
                H1 = float(np.linalg.norm(h1))
                i1 = float(np.arccos(h1[2] / H1))
                Vf1 = float(np.linalg.norm(vf1))
                Rf1 = float(np.linalg.norm(rf1))
                Ef1 = np.cross(vf1, h1) / 398600 - rf1 / Rf1
                ef1 = float(np.linalg.norm(Ef1))
                af1 = float(-398600 / (2 * Enf1))
                tp1 = float(2 * pi * np.sqrt((abs(af1) ** 3) / 398600))
                Enf1 = ((Vf1 ** 2) / 2) - (398600 / Rf1)
                rdotv1 = float(np.dot(rf1, vf1))
                rdotv2 = float(np.dot(rf2, vf2))
                pare[i] = (ef2 - ef1) / .00000001
                pari[i] = (i2 - i1) / .00000001
                parv[i] = (Vf2 - Vf1) / .00000001
                parr[i] = (Rf1 - Rf2) / .00000001
                parE[i] = (Enf2 - Enf1) / .00000001
                para[i] = (af2 - af1) / .00000001
                partp[i] = (tp2 - tp1) / .00000001
                homan[i] = (rdotv2 - rdotv1) / .00000001
            elif i == 6:
                epslon = float(.00000001)
                x00 = np.array([x0[0], x0[1], x0[2]])
                vdd = x00[0] * np.cos(x00[2]) * np.cos(x00[1])
                udd = x00[0] * np.cos(x00[2]) * np.sin(x00[1])
                wdd = x00[0] * np.sin(x00[2])
                vuw = np.array([vdd, udd, wdd])
                Rtransform0 = self.transformation(r0, v0)
                delta = np.dot(vuw, Rtransform0)
                vp0 = v0 + delta
                yy0 = [r0[0], r0[1], r0[2], vp0[0], vp0[1], vp0[2]]
                [rf1, v11] = self.form_segment(yy0, x0[6])
                x000 = np.array([x0[3], x0[4], x0[5]])
                vdd1 = x000[0] * np.cos(x000[2]) * np.cos(x000[1])
                udd1 = x000[0] * np.cos(x000[2]) * np.sin(x000[1])
                wdd1 = x000[0] * np.sin(x000[2])
                vuw1 = np.array([vdd1, udd1, wdd1])
                Rtransform2 = self.transformation(rf1, v11)
                dv22 = np.dot(vuw1, Rtransform2)
                vf1 = v11 + dv22
                tof = x0[6] + epslon
                [rf2, v12] = self.form_segment(yy0, tof)
                vf2 = v12 + dv22
                h2 = np.cross(rf2, vf2)
                H2 = float(np.linalg.norm(h2))
                i2 = float(np.arccos(h2[2] / H2))
                Vf2 = float(np.linalg.norm(vf2))
                Rf2 = float(np.linalg.norm(rf2))
                Enf2 = float(((Vf2 ** 2) / 2) - (398600 / Rf2))
                Ef2 = np.cross(vf2, h2) / 398600 - rf2 / Rf2
                ef2 = float(np.linalg.norm(Ef2))
                af2 = float(-398600 / (2 * Enf2))
                tp2 = float(2 * pi * np.sqrt((abs(af2) ** 3) / 398600))
                # orbit without epselon
                h1 = np.cross(rf1, vf1)
                H1 = float(np.linalg.norm(h1))
                i1 = float(np.arccos(h1[2] / H1))
                Vf1 = float(np.linalg.norm(vf1))
                Rf1 = float(np.linalg.norm(rf1))
                Enf1 = float(((Vf1 ** 2) / 2) - (398600 / Rf1))
                Ef1 = np.cross(vf1, h1) / 398600 - rf1 / Rf1
                ef1 = float(np.linalg.norm(Ef1))
                af1 = float(-398600 / (2 * Enf1))
                tp1 = float(2 * pi * np.sqrt((abs(af1) ** 3) / 398600))
                rdotv1 = float(np.dot(rf1, vf1))
                rdotv2 = float(np.dot(rf2, vf2))
                # clculat the partial direvativs
                pare[i] = (ef2 - ef1) / .00000001
                pari[i] = (i2 - i1) / .00000001
                parv[i] = (Vf2 - Vf1) / .00000001
                parr[i] = (Rf1 - Rf2) / .00000001
                parE[i] = (Enf2 - Enf1) / .00000001
                para[i] = (af2 - af1) / .00000001
                partp[i] = (tp2 - tp1) / .00000001
                homan[i] = (rdotv2 - rdotv1) / .00000001
        generaljac = np.zeros((8, 7), dtype=float)
        for m in range(7):
            generaljac[0, m] = pare[m]
            generaljac[1, m] = pari[m]
            generaljac[2, m] = parv[m]
            generaljac[3, m] = parr[m]
            generaljac[4, m] = parE[m]
            generaljac[5, m] = para[m]
            generaljac[6, m] = partp[m]
            generaljac[7, m] = homan[m]
        dummy = len(bcs)
        jacki = np.zeros((dummy, dummy), dtype=float)
        for i in range(0, dummy):
            for j in range(0, dummy):
                jacki[i, j] = generaljac[bcs[i], freev[j]]
        return jacki

    def main_func(self,freevnumber, nonfreevalu, nonfreenumber, bcsnum, bcsvalues, r0, v0):
        cc = len(freevnumber)
        fff = len(nonfreenumber)
        x0 = [0, 0, 0, 0, 0, 0, 0]
        for j in range(0, cc):
            x0[freevnumber[j]] = 2
            if freevnumber[j] == 6:
                x0[freevnumber[j]] = 5000

        for sss in range(0, fff):
            x0[nonfreenumber[sss]] = nonfreevalu[sss]

        error = 1
        while error > .001:
            x00 = np.array([x0[0], x0[1], x0[2]])
            vdd = x00[0] * np.cos(x00[2]) * np.cos(x00[1])
            udd = x00[0] * np.cos(x00[2]) * np.sin(x00[1])
            wdd = x00[0] * np.sin(x00[2])
            vuw = np.array([vdd, udd, wdd])
            Rtransform0 = self.transformation(r0, v0)
            delta = np.dot(vuw, Rtransform0)
            vp0 = v0 + delta
            y = [r0[0], r0[1], r0[2], vp0[0], vp0[1], vp0[2]]
            [rf, v1] = self.form_segment(y, x0[6])
            x000 = np.array([x0[3], x0[4], x0[5]], dtype=float)
            vdd1 = float(x000[0] * np.cos(x000[2]) * np.cos(x000[1]))
            udd1 = float(x000[0] * np.cos(x000[2]) * np.sin(x000[1]))
            wdd1 = float(x000[0] * np.sin(x000[2]))
            vuw1 = np.array([vdd1, udd1, wdd1], dtype=float)
            Rtransform2 = self.transformation(rf, v1)
            dv2 = np.dot(vuw1, Rtransform2)
            vf = v1 + dv2
            h = np.cross(rf, vf)
            H = float(np.linalg.norm(h))
            i = float(np.arccos(h[2] / H))
            Vf = float(np.linalg.norm(vf))
            Rf = float(np.linalg.norm(rf))
            Enf = float(((Vf ** 2) / 2) - (398600 / Rf))
            Ef = (1 / 398600) * (((Vf ** 2 - (398600 / Rf)) * rf) - (np.dot(rf, vf) * vf))
            ef = float(np.linalg.norm(Ef))
            af = float(-398600 / (2 * Enf))
            tp = float(2 * pi * np.sqrt((abs(af) ** 3) / 398600))
            rdotv = float(np.dot(rf, vf))
            dummyvector = np.array([ef, i, Vf, Rf, Enf, af, tp, rdotv])
            fx = np.array([0, 0, 0], dtype=float)
            for db in range(cc):
                fx[db] = bcsvalues[db] - dummyvector[bcsnum[db]]
            my_new_jacobian = self.jac(r0, v0, x0, freevnumber, bcsnum)
            jac_inv = np.linalg.inv(my_new_jacobian)
            delsol = np.dot(-fx, jac_inv)
            x1 = np.array(x0, dtype=float)
            for b in range(0, cc):
                x1[freevnumber[b]] = x0[freevnumber[b]] + delsol[b]
            ddd = np.linalg.norm(delsol)
            error = ddd
            x0 = x1
            continue

        return x0

    def run(self,free, BCS, r0, v0):
        [fvn, fvv, nfvn, BCSn, BCsv] = self.get_from_GUI(free, BCS)
        dx = self.main_func(fvn, fvv, nfvn, BCsn, BCsv, r0, v0)
        return dx

