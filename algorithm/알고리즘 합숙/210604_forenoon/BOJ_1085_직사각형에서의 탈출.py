def dist_update(d):
    global min_dist
    if min_dist > d:
        min_dist = d


x, y, w, h = map(int, input().split())
min_dist = 987654321
dist_x_0 = abs(x-0)
dist_y_0 = abs(y-0)
dist_w_x = abs(x-w)
dist_h_y = abs(y-h)
dist_update(dist_x_0)
dist_update(dist_y_0)
dist_update(dist_w_x)
dist_update(dist_h_y)

print(min_dist)
