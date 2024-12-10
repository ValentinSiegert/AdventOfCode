def part1(data: str):
    fiter, fid, ffile, ffile_id = iter(data), -1, True, 0
    riter, rid, rfile, rfile_id = reversed(data), len(data), (True if len(data) % 2 == 1 else False), (len(data) - 1) // 2
    checksum = disk_id = fvalue = rvalue = 0
    while fid < rid:
        if ffile:
            fvalue, fid = int(next(fiter)), fid + 1
            fvalue, rvalue = (rvalue, 0) if rid == fid else (fvalue, rvalue)
            while fvalue > 0:
                checksum += disk_id * ffile_id
                disk_id, fvalue = disk_id + 1, fvalue - 1
            ffile_id, ffile = ffile_id + 1, False
        else:
            fvalue, fid = (int(next(fiter)), fid + 1) if fvalue == 0 else (fvalue, fid)
            rvalue, rid = (int(next(riter)), rid - 1) if rvalue == 0 else (rvalue, rid)
            if rfile:
                while fvalue > 0 and rvalue > 0:
                    checksum += disk_id * rfile_id
                    disk_id, fvalue, rvalue = disk_id + 1, fvalue - 1, rvalue - 1
                rfile_id, rfile = (rfile_id - 1, False) if rvalue == 0 else (rfile_id, True)
            else:
                rfile, rvalue = True, 0
            ffile = True if fvalue == 0 else False
    return checksum


def part2(data: str):
    disk, rfile_id, checksum = data, (len(data) - 1) // 2, 0
    riter, rid = (iter(data[::-1][::2]), len(data) + 1) if len(data) % 2 == 1 else (iter(data[::-1][1::2]), len(data))
    while (rvalue := int(next(riter, -1))) != -1:
        rid -= 2
        fiter, fid = iter(disk[1:rid:2]), -1
        while (fvalue := int(next(fiter, -1))) != -1:
            fid += 2
            if fvalue >= rvalue:
                diter, did, disk_id = iter(data), 0, 0
                while did < fid:
                    disk_id += int(next(diter))
                    did += 1
                if int(data[fid]) > int(disk[fid]):
                    disk_id += int(data[fid]) - int(disk[fid])
                for _ in range(rvalue):
                    checksum += disk_id * rfile_id
                    disk_id += 1
                disk = f'{disk[:fid]}{fvalue - rvalue}{disk[fid + 1:]}'
                disk = f'{disk[:rid]}0{disk[rid + 1:]}'
                break
        rfile_id -= 1
    fiter, fid, disk_id, ffile_id = iter(disk), -1, 0, 0
    while (fvalue := int(next(fiter, -1))) != -1:
        fid += 1
        if fid % 2 == 0:
            if fvalue == 0:
                disk_id += int(data[fid])
            else:
                while fvalue > 0:
                    checksum += disk_id * ffile_id
                    disk_id, fvalue = disk_id + 1, fvalue - 1
            ffile_id += 1
        else:
            disk_id += int(data[fid])
    return checksum


def solve(data: str, part: int):
    if part == 1:
        return part1(data)
    if part == 2:
        return part2(data)
    return [part1(data), part2(data)]
