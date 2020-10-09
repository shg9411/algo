def solution(depar, hub, dest, roads):
    MOD = 10007

    def dtoh(s):
        if s == hub:
            dh.append(1)
            return
        if s not in road:
            return
        for nxt in road[s]:
            visited.append(nxt)
            dtoh(nxt)
            visited.pop()

    def htod(s):
        if s == dest:
            hd.append(1)
            return
        if s not in road:
            return
        for nxt in road[s]:
            visited.append(nxt)
            htod(nxt)
            visited.pop()

    road = dict()
    for s, e in roads:
        if s in road:
            road[s].append(e)
        else:
            road[s] = [e]
    dh = []
    hd = []
    visited = []
    dtoh(depar)
    htod(hub)
    return (len(dh) % MOD*len(hd) % MOD) % MOD


depar = "SEOUL"
hub = "DAEGU"
dest = "YEOSU"
roads = [["ULSAN", "BUSAN"], ["DAEJEON", "ULSAN"], ["DAEJEON", "GWANGJU"], ["SEOUL", "DAEJEON"], ["SEOUL", "ULSAN"], ["DAEJEON", "DAEGU"], [
    "GWANGJU", "BUSAN"], ["DAEGU", "GWANGJU"], ["DAEGU", "BUSAN"], ["ULSAN", "DAEGU"], ["GWANGJU", "YEOSU"], ["BUSAN", "YEOSU"], ["SEOUL", "YEOSU"]]
print(solution(depar, hub, dest, roads))
