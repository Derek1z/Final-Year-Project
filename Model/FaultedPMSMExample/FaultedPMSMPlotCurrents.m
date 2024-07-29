% Code to plot simulation results from FaultedPMSM
%% Plot Description:
%
% The plot below shows motor winding currents and rotor torque.

% Copyright 2020-2023 The MathWorks, Inc.

sim('FaultedPMSM');

% Reuse figure if it exists, else create new figure
if ~exist('h1_FaultedPMSM', 'var') || ...
        ~isgraphics(h1_FaultedPMSM, 'figure')
    h1_FaultedPMSM = figure('Name', 'FaultedPMSM');
end
figure(h1_FaultedPMSM)
clf(h1_FaultedPMSM)

% Get simulation results
t = simlog_FaultedPMSM.RL4.i.series.time;
simlog_iAm = simlog_FaultedPMSM.RL4.i.series.values;
simlog_iBm = simlog_FaultedPMSM.RL5.i.series.values;
simlog_iCm = simlog_FaultedPMSM.RL6.i.series.values;
simlog_iAe = simlog_FaultedPMSM.RL1.i.series.values;
simlog_iBe = simlog_FaultedPMSM.RL2.i.series.values;
simlog_iCe = simlog_FaultedPMSM.RL3.i.series.values;

% Plot results
subplot(411)
plot(t,simlog_iAe,t,simlog_iAm);
title('A-phase currents')
ylabel('A-phase current')
legend({'Electrical model','Magnetic model'})
subplot(412)
plot(t,simlog_iBe,t,simlog_iBm);
title('B-phase currents')
ylabel('B-phase current')
subplot(413)
plot(t,simlog_iCe,t,simlog_iCm);
title('C-phase currents')
ylabel('C-phase current')
subplot(414)
plot(t,simlog_FaultedPMSM.Dyno_1.Ideal_Angular_Velocity_Source.t.series.values, ...
     t,simlog_FaultedPMSM.Dyno_2.Ideal_Angular_Velocity_Source.t.series.values);
axis([0 t(end) -3.5 0.5])
title('Torques') 
ylabel('Torques')
xlabel('Time (s)')

% Remove temporary variables
clear t simlog_iAm simlog_iBm simlog_iCm simlog_iAe simlog_iBe simlog_iCe
