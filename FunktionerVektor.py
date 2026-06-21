import math


# -------------------------
# Hjælpefunktioner
# -------------------------

def tjek_nulvektor(laengde):
    if laengde == 0:
        raise ValueError("Nulvektoren kan ikke bruges til denne beregning.")


def afrund_tuple(tal_tuple, decimaler=4):
    return tuple(round(tal, decimaler) for tal in tal_tuple)


# -------------------------
# 2D VEKTORER
# -------------------------

def Vektor2Dsum(x1, y1, x2, y2):
    return x1 + x2, y1 + y2


def Vektor2Dminus(x1, y1, x2, y2):
    return x1 - x2, y1 - y2


def Vektor2Dskalar(x1, y1, s):
    return x1 * s, y1 * s


def Vektor2Dlaengde(x1, y1):
    return math.sqrt(x1**2 + y1**2)


def Vektor2Dvinkel(x1, y1):
    
    return math.degrees(math.atan2(y1, x1))


def Vektor2Dprikprodukt(x1, y1, x2, y2):
    return x1 * x2 + y1 * y2


def Vektor2Denhedsvektor(x1, y1):
    laengde = Vektor2Dlaengde(x1, y1)
    tjek_nulvektor(laengde)

    return x1 / laengde, y1 / laengde


def VinkelMellem2D(x1, y1, x2, y2):
    laengde1 = Vektor2Dlaengde(x1, y1)
    laengde2 = Vektor2Dlaengde(x2, y2)

    tjek_nulvektor(laengde1)
    tjek_nulvektor(laengde2)

    cos_vinkel = Vektor2Dprikprodukt(x1, y1, x2, y2) / (laengde1 * laengde2)

   
    cos_vinkel = max(-1, min(1, cos_vinkel))

    return math.degrees(math.acos(cos_vinkel))


def KartesiskTilPolaer(x, y):
    r = Vektor2Dlaengde(x, y)
    vinkel = math.degrees(math.atan2(y, x))

    return r, vinkel


def PolaerTilKartesisk(r, vinkel_grader):
    vinkel_radianer = math.radians(vinkel_grader)

    x = r * math.cos(vinkel_radianer)
    y = r * math.sin(vinkel_radianer)

    return x, y


def PunktTilVektor2D(x1, y1, x2, y2):
    # Vektor fra punkt A til punkt B
    return x2 - x1, y2 - y1


def Tvaervektor2D(x, y):
    # En vektor der står vinkelret på den oprindelige
    return -y, x


def Projektion2D(x1, y1, x2, y2):
    # Projektion af vektor A på vektor B
    prik = Vektor2Dprikprodukt(x1, y1, x2, y2)
    laengde_b_i_anden = x2**2 + y2**2

    if laengde_b_i_anden == 0:
        raise ValueError("Man kan ikke projicere på nulvektoren.")

    faktor = prik / laengde_b_i_anden

    return faktor * x2, faktor * y2


# -------------------------
# 3D VEKTORER
# -------------------------

def Vektor3Dsum(x1, y1, z1, x2, y2, z2):
    return x1 + x2, y1 + y2, z1 + z2


def Vektor3Dminus(x1, y1, z1, x2, y2, z2):
    return x1 - x2, y1 - y2, z1 - z2


def Vektor3Dskalar(x1, y1, z1, s):
    return x1 * s, y1 * s, z1 * s


def Vektor3Dlaengde(x1, y1, z1):
    return math.sqrt(x1**2 + y1**2 + z1**2)


def Vektor3Dprikprodukt(x1, y1, z1, x2, y2, z2):
    return x1 * x2 + y1 * y2 + z1 * z2


def Vektor3Denhedsvektor(x1, y1, z1):
    laengde = Vektor3Dlaengde(x1, y1, z1)
    tjek_nulvektor(laengde)

    return x1 / laengde, y1 / laengde, z1 / laengde


def VinkelMellem3D(x1, y1, z1, x2, y2, z2):
    laengde1 = Vektor3Dlaengde(x1, y1, z1)
    laengde2 = Vektor3Dlaengde(x2, y2, z2)

    tjek_nulvektor(laengde1)
    tjek_nulvektor(laengde2)

    cos_vinkel = Vektor3Dprikprodukt(x1, y1, z1, x2, y2, z2) / (laengde1 * laengde2)

    cos_vinkel = max(-1, min(1, cos_vinkel))

    return math.degrees(math.acos(cos_vinkel))


def PunktTilVektor3D(x1, y1, z1, x2, y2, z2):
    # Vektor fra punkt A til punkt B
    return x2 - x1, y2 - y1, z2 - z1


def Krydsprodukt(x1, y1, z1, x2, y2, z2):
    krydsproduktX = y1 * z2 - z1 * y2
    krydsproduktY = z1 * x2 - x1 * z2
    krydsproduktZ = x1 * y2 - y1 * x2

    return krydsproduktX, krydsproduktY, krydsproduktZ


def Tvaervektor3D(x1, y1, z1, x2, y2, z2):
    # I 3D kan man finde en vektor, der står vinkelret på to vektorer,
    # ved hjælp af krydsproduktet.
    return Krydsprodukt(x1, y1, z1, x2, y2, z2)


def KartesiskTilSfaerisk3D(x, y, z):
    r = Vektor3Dlaengde(x, y, z)
    tjek_nulvektor(r)

    theta = math.degrees(math.atan2(y, x))
    phi = math.degrees(math.acos(z / r))

    return r, theta, phi


def SfaeriskTilKartesisk3D(r, theta_grader, phi_grader):
    theta = math.radians(theta_grader)
    phi = math.radians(phi_grader)

    x = r * math.sin(phi) * math.cos(theta)
    y = r * math.sin(phi) * math.sin(theta)
    z = r * math.cos(phi)

    return x, y, z