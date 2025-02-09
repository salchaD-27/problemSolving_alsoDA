func computeArea(ax1 int, ay1 int, ax2 int, ay2 int, bx1 int, by1 int, bx2 int, by2 int) int {
	areaA := (ax2 - ax1) * (ay2 - ay1)
	areaB := (bx2 - bx1) * (by2 - by1)
	minX1, minX2 := 0, 0
	minY1, minY2 := 0, 0
	if ax1 > bx1 {
		minX1 = ax1
	} else {
		minX1 = bx1
	}
	if ax2 < bx2 {
		minX2 = ax2
	} else {
		minX2 = bx2
	}
	if ay1 > by1 {
		minY1 = ay1
	} else {
		minY1 = by1
	}
	if ay2 < by2 {
		minY2 = ay2
	} else {
		minY2 = by2
	}
	overlapWidth := minX2 - minX1
	overlapHeight := minY2 - minY1
	overlapArea := 0
	if overlapWidth > 0 && overlapHeight > 0 {
		overlapArea = overlapWidth * overlapHeight
	}
	return areaA + areaB - overlapArea
}