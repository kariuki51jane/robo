
% towards a given target. In addition to rotation, the robot moves forward
% with a constant velocity and stops when it has reached the target. Target
% and start position are then switched, and the robot returns to its start,
% indefinitely driving between start and target.
function driveToTarget(h, initial_position, initial_orientation_degrees, target_position)
    % here, we also add a plot of the robot's position for debugging
    % purposes
    figure;
    xlim([0 270]);
    ylim([0 400]);
    hold on;

    % some fixed parameter values for driving and turning
    speed = 200; % constant forward speed
    lambda = 2; % turning rate factor
    
    % as before, we start at the initial position/orientation and keep
    % track of how that position changes over time
    position = initial_position;
    orientation = initial_orientation_degrees;
    encoders = kGetEncoders(h);
    % counter again takes care of remembering the current target
    counter = 0;
    % current target: the one passed into the funcction
    target = target_position;
    while 1
        [position, orientation, encoders] = UpdatePositionAndOrientation(h, position, orientation, encoders);
        
        % check if we are close enough to the current target
        if norm(position - target) < 25
            % if so, switch target and log the position of the switch on
            % the plot
            counter = counter + 1;
            disp('switching target')
            plot(position(1), position(2), 'x');
            if mod(counter, 2) == 1
                target = initial_position;
            else
                target = target_position;
            end
        end
        
        % as before: get vector to target
        target_diff_vector = target - position;
        angle = atan2(target_diff_vector(2), target_diff_vector(1));
        target_angle_degrees = angle/pi * 180;
        
        % use these lines for the linear dynamical system
        %d_phi = dt * lambda * (-orientation + target_angle_degrees);
        %v_mm_per_second = d_phi / 360 * pi * 53;
        
        % use these for the sine-based dynamics
        % note, that we don't need the timestep, dt here; it is given
        % implicitly. To see this, think about the units of the dynamics:
        % it gives us rad/s; the robot then realizes this turning speed for
        % a short time (e.g., turn by 90 deg/s for 0.5s means a turn of 45
        % deg), thus implicitly implementing the Euler approach.
        d_phi = lambda * (-sin((orientation - target_angle_degrees)/180 * pi));
        v_mm_per_second = d_phi/pi * 53;
        
        % convert the wheel speeds to pulses/second
        v_pulses_per_second = v_mm_per_second / 0.13;
        
        % set speeds
        kSetSpeed(h, -v_pulses_per_second + speed, v_pulses_per_second + speed);
        
        % we have to wait a bit here; this is again because our robot had
        % very fast communication, leading to very small dts and thus also
        % small changes in orientation which could not properly be realized
        % by the stepper motors of the epuck; this pause can probably be
        % left out for robots with slow communication
        pause(0.3);
    end
end
