def state_vec(t0, u_, k, ad):
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




def form_segment(k, r0, v0, tof, rtol=1e-10, ad=None, callback=None, nsteps=10000):
    x, y, z = r0
    vx, vy, vz = v0
    u0 = np.array([x, y, z, vx, vy, vz])

    # Set the non Keplerian acceleration
    if ad is None:
        ad = lambda t0, u_, k_: (0, 0, 0)

    # Set the integrator
    rr = ode(state_vec).set_integrator('dop853', rtol=rtol, nsteps=nsteps)
    rr.set_initial_value(u0)  # Initial time equal to 0.0
    rr.set_f_params(k, ad)  # Parameters of the integration
    if callback:
        rr.set_solout(callback)

    # Make integration step
    rr.integrate(tof)

    if rr.successful():
        r, v = rr.y[:3], rr.y[3:]
    else:
        raise RuntimeError("Integration failed")

    return r, v
