def get_scaling(toponym):
    envelope = toponym['boundedBy']['Envelope']
    lower = tuple(map(float, envelope['lowerCorner'].split()))
    upper = tuple(map(float, envelope['upperCorner'].split()))
    width = upper[0] - lower[0]
    height = upper[1] - lower[1]
    coefficient = 0.09
    return str(width / 2 * coefficient) + ',' + str(height / 2 * coefficient)
