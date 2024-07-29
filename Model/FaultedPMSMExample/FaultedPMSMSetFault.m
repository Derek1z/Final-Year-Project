function FaultedPMSMSetFault(modelName,faultScenario)
% function FaultedPMSMSetFault(modelName,faultScenario)
% Utility used by example FaultedPMSM to manage fault settings.

% Copyright 2020-2023 The MathWorks, Inc.

    windingBlockPath = [modelName '/Magnetic Domain Implementation of an SPMSM/Tooth 1 (faulted)'];    
    magneticRotorBlockPath = [modelName '/Magnetic Domain Implementation of an SPMSM/Magnetic Rotor'];   
    if strcmp(faultScenario,'None')
        disableAllFaultsInModel(modelName);
        disp("All faults disabled");
    elseif strcmp(faultScenario,'Demagnetized')
        MagnetFault = getFaultObject(magneticRotorBlockPath, "Rotor poles");           
        MagnetFault.Name = "DemagnetizedFirstRotorPole";
        setFaultParameter(MagnetFault, 'LambdaVec','[0.5,1,1,1,1,1,1,1,1,1]');  
        setFaultParameter(MagnetFault, 'FaultTransitionTime','0.1');   
        setTimedTrigger(MagnetFault, 0.5);        
        disableAllFaultsInModel(modelName); % disable all faults       
        MagnetFault.activate; % enable this fault
        disp("Fault scenario: Demagnetized first rotor pole");
    elseif strcmp(faultScenario,'OpenCircuit')
        WindingFault = getFaultObject(windingBlockPath, "Winding");
        WindingFault.Name = "Tooth1_OpenCircuit";
        setFaultParameter(WindingFault, 'openCct','ee.enum.faults.faultTurnsOpenCkt.yes');
        setTimedTrigger(WindingFault, 0.5);        
        % Unselect the other winding fault options
        setFaultParameter(WindingFault,'groundShort','ee.enum.faults.faultTurnsGroundShort.no');
        setFaultParameter(WindingFault,'turnsShort','ee.enum.faults.faultTurnsShort.no');
        disableAllFaultsInModel(modelName); % disable all faults        
        WindingFault.activate; % enable this fault
        disp("Fault scenario: Open circuit in Tooth 1");
    elseif strcmp(faultScenario,'Ground')
        WindingFault = getFaultObject(windingBlockPath, "Winding");
        WindingFault.Name = "Tooth1_Grounded";
        setFaultParameter(WindingFault, 'groundShort','ee.enum.faults.faultTurnsGroundShort.positiveTerminal');
        setFaultParameter(WindingFault, 'groundShortG','1e3');
        setTimedTrigger(WindingFault, 0.5);
        % Unselect the other winding fault options
        setFaultParameter(WindingFault,'openCct','ee.enum.faults.faultTurnsOpenCkt.no');
        setFaultParameter(WindingFault,'turnsShort','ee.enum.faults.faultTurnsShort.no');
        disableAllFaultsInModel(modelName); % disable all faults        
        WindingFault.activate; % enable this fault
        disp("Fault scenario: Grounded Tooth 1");
    elseif strcmp(faultScenario,'IsolatedTurns')
        WindingFault = getFaultObject(windingBlockPath, "Winding");
        WindingFault.Name = "Tooth1_IsolatedTurns";
        setFaultParameter(WindingFault, 'turnsShort','ee.enum.faults.faultTurnsShort.positiveTerminal');
        setTimedTrigger(WindingFault, 0.5);
        % Unselect the other winding fault options
        setFaultParameter(WindingFault,'openCct','ee.enum.faults.faultTurnsOpenCkt.no');
        setFaultParameter(WindingFault,'groundShort','ee.enum.faults.faultTurnsGroundShort.no');
        disableAllFaultsInModel(modelName); % disable all faults        
        WindingFault.activate; % enable this fault
        disp("Fault scenario: Isolated turns in Tooth 1");
    else
        % No valid option to set
    end
end

function setFaultParameter(fault, name, value)
    % Set parameter to a Simulink.fault.Fault object
    %   Input arguments: 
    %       fault [Simulink.fault.Fault]
    %       name [1x1 string or char array] (parameter name)
    %       value [1x1 string or char array] (parameter value, converted to text)

    faultBehaviorBlock = fault.getBehavior;
    load_system(fault.getFaultModel)
    set_param(faultBehaviorBlock,name,value);
end

function disableAllFaultsInModel(model)
    % Deactivate all existing faults in the model
    %   Input arguments: 
    %       model [1x1 string, char array, or handle]

    faults = [Simulink.fault.findFaults(model)];
    if ~isempty(faults)
        for idxFault = 1:length(faults)
            thisFault = faults(idxFault);
            Simulink.fault.enable(thisFault.ModelElement, false); % disable fault
        end
    end
end

function setTimedTrigger(fault, triggerTime)
    % Set a Timed fault trigger
    %   Input arguments: 
    %       fault [Simulink.fault.Fault]
    %       triggerTime [1x1 double]

    fault.TriggerType = "Timed";
    fault.StartTime = triggerTime;
end

function fault = getFaultObject(block, subelem)
    % Get the Simulink.fault.Fault object associated to the faultable model element
    % with path "block/subelem". If no fault exists, then this function
    % adds the fault and returns the fault object.
    %   Input arguments: 
    %       block   [1x1 string, char array, or handle]
    %       subelem [1x1 string or char array]

    model = bdroot(block);
    ExistingFaults = [Simulink.fault.findFaults(model)];
    if ~isempty(ExistingFaults)
        fault = ExistingFaults(contains({ExistingFaults(:).ModelElement}, subelem)); % find if target fault is included in existing faults
        if isempty(fault) % not included in existing faults           
            fault = Simulink.fault.addFault(strcat(block, '/', subelem)); % create the fault
            addBehaviorToFault(fault);
        end
    else % no faults exist
        fault = Simulink.fault.addFault(strcat(block, '/', subelem));
        addBehaviorToFault(fault);
    end
end

function addBehaviorToFault(fault)    
    % Add behavior block to the associated fault model
    %   Input arguments: 
    %       fault [Simulink.fault.Fault]

    faultModelName = strcat(fault.getAssociatedModel, "_FaultModel");
    fault.addBehavior(faultModelName);
end