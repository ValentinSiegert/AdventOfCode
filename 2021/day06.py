from collections import deque


if __name__ == '__main__':
    swarm = list(map(int, open('day6.txt').read().split(',')))
    swarm_ages = deque(map(len, [[f for f in swarm if f == i] for i in range(0, 9)]), maxlen=9)
    days = 256
    for day in range(1, days+1):
        respawn_fishes = swarm_ages.popleft()
        swarm_ages.append(respawn_fishes)
        swarm_ages[6] += respawn_fishes
        print(f'{day} days = {sum(swarm_ages)} fishes.')
    print(f'After {days} days there exist {sum(swarm_ages)} fishes in the swarm.')
