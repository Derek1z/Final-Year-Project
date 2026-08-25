%% Faulted PMSM - Define geometry and other parameters
% This script creates parameter data for the FaultedPMSM model. 

% Copyright 2020-2023 The MathWorks, Inc.   

%% Electrical parameterization
Ld = 7.5e-3;   % Ld
Lq = 7.5e-3;   % Lq
L0 = 5e-3;     % L0
Rw = 0.01;     % Stator resistance per phase
PHI = 0.06;    % Permanent magnet peak flux linkage

%% Magnetic parameterization
% Geometric data
Npp = 5;    % Number of rotor pole pairs
Ns = 9;     % Number of stator teeth
g = 1;      % Air gap (mm)
gT = 1;     % Cross-tooth air gap (mm)
csaT = 10;  % Cross-tooth area (mm^2)
r = 65;     % Rotor radius (mm)
l = 50;     % Iron stack length (mm)
wY = 5;     % Yoke cuboid width (mm)
rY = 100;   % Yoke average diameter (mm)
wS = 5;     % Tooth cuboid width (mm)
Nws = 70;   % Number of windings per stator coil
lm = 5;     % Permanent magnet length (mm)

% Materials data
B0 = 0.3;   % Magnet strength
mur = 7e3;  % Relative permeability of the core material
mu0 = 4e-7*pi; % Permeability of air

% Derived data
gY = rY*2*pi/Ns; % Yoke cuboid path length
gS = rY-r-g;     % Tooth cuboid path length
Ry = gY*1e-3/(mu0*mur*l*wY*1e-6); % Yoke cuboid reluctance
Rs = gS*1e-3/(mu0*mur*l*wS*1e-6); % Tooth cuboid reluctance
Rsl = gT*1e-3/(mu0*csaT*1e-6); % Cross-tooth leakage reluctance

% Parasitics
gWinding = 1e-6; % Small parallel conductance across slot windings

%% Mechanical parameterization
J = 1e-3; % Inertia
InitialRotorAnglePMSM = 4*360/Ns/Npp; % to match magnetic circuit rotor position reference

%% Resistive test load
RL = 0.1;