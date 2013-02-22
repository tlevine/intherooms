#!/usr/bin/env Rscript

tau <- pi * 2

# Broken
waste <- function(theta, r = 150) {
    ((1/2) * tau * r^2 / theta) - (2 * r^2 * sin(theta) * cos(theta))
}

# Broken in turn
prop.covered <- function(theta) {
    (tau / 8) * ((1 - (1 / theta)) / cos(theta)) + (sin(theta) / 2)
}

curve(prop.covered, from = 0, to = 0.99 * tau/4 )

curve(waste, from = 0, to = 0.99 * tau/4 )
