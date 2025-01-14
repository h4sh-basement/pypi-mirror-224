r"""
 _
| |                          ████████╗██████╗  █████╗ ██╗  ██╗
| |_ ___ _ __  ___  ___  _ __╚══██╔══╝██╔══██╗██╔══██╗╚██╗██╔╝
| __/ _ \ '_ \/ __|/ _ \| '__|  ██║   ██████╔╝███████║ ╚███╔╝
| ||  __/ | | \__ \ (_) | |     ██║   ██╔══██╗██╔══██║ ██╔██╗
 \__\___|_| |_|___/\___/|_|     ██║   ██║  ██║██║  ██║██╔╝ ██╗
                                ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
"""

import numpy as np


def det(A):
    "Determinant of an Array."
    if A.shape[0] == 3:
        detA = (
            A[0, 0] * A[1, 1] * A[2, 2]
            + A[0, 1] * A[1, 2] * A[2, 0]
            + A[0, 2] * A[1, 0] * A[2, 1]
            - A[2, 0] * A[1, 1] * A[0, 2]
            - A[2, 1] * A[1, 2] * A[0, 0]
            - A[2, 2] * A[1, 0] * A[0, 1]
        )
    elif A.shape[0] == 2:
        detA = A[0, 0] * A[1, 1] - A[0, 1] * A[1, 0]
    elif A.shape[0] == 1:
        detA = A[0, 0]
    else:
        detA = np.linalg.det(A.T).T
    return detA


def inv(A):
    "Inverse of an Array."

    detAinvA = np.zeros_like(A)
    detA = det(A)

    if A.shape[0] == 3:
        detAinvA[0, 0] = -A[1, 2] * A[2, 1] + A[1, 1] * A[2, 2]
        detAinvA[1, 1] = -A[0, 2] * A[2, 0] + A[0, 0] * A[2, 2]
        detAinvA[2, 2] = -A[0, 1] * A[1, 0] + A[0, 0] * A[1, 1]

        detAinvA[0, 1] = A[0, 2] * A[2, 1] - A[0, 1] * A[2, 2]
        detAinvA[0, 2] = -A[0, 2] * A[1, 1] + A[0, 1] * A[1, 2]
        detAinvA[1, 2] = A[0, 2] * A[1, 0] - A[0, 0] * A[1, 2]

        detAinvA[1, 0] = A[1, 2] * A[2, 0] - A[1, 0] * A[2, 2]
        detAinvA[2, 0] = -A[1, 1] * A[2, 0] + A[1, 0] * A[2, 1]
        detAinvA[2, 1] = A[0, 1] * A[2, 0] - A[0, 0] * A[2, 1]

    elif A.shape[0] == 2:
        detAinvA[0, 0] = A[1, 1]
        detAinvA[0, 1] = -A[0, 1]
        detAinvA[1, 0] = -A[1, 0]
        detAinvA[1, 1] = A[0, 0]

    elif A.shape[0] == 1:
        detAinvA[0, 0] = 1

    else:
        detAinvA = detA * np.linalg.inv(A.T).T

    return detAinvA / detA


def pinv(A, hermitian=False):
    "Pseudo-inverse of an Array."

    return np.linalg.pinv(A.T, hermitian=hermitian).T
