# chaser details seconds, m/s
chaserA = [15, 3]
chaserB = [30, 2.5]
chaserC = [75, 4]
chaserA_time = -15
chaserB_time = -30
chaserC_time = -75
totalTreadmillDistance = 0
lenOfChasers = [1, 1, 1]
chaser_caught = False
chaser_time = 0
total_time = 0
treadmill_speed = 3.5
chaser_finished = False


def onTreadmillData(chasers_time, distance, t):
    chaser_speed = [3, 2.5, 4]
    for i in chasers_time:
        chaser_time = i

        if chaser_time < 0:
            pass
        else:
            chaser_distance = chaser_speed[i] * (t - chaser_time)
            if chaser_time > 300:
                chaser_finished = True
            if distance < chaser_distance and not chaser_finished:
                chaser_caught = True

    return chaser_caught


while totalTreadmillDistance < 5000 and not chaser_caught:
    total_time += 1
    totalTreadmillDistance += treadmill_speed
    chaserA_time += 1
    chaserB_time += 1
    chaserC_time += 1
    chasers_time = [chaserA_time, chaserB_time, chaserC_time]
    chaser_caught = onTreadmillData(chasers_time, totalTreadmillDistance, total_time)

if chaser_caught:
    print("Mission Failed")
elif not chaser_caught and totalTreadmillDistance >= 5000:
    print("Mission Passed")
