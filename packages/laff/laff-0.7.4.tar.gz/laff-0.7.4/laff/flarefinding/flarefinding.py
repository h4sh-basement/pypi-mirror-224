import numpy as np
import logging

logger = logging.getLogger('laff')

def possible_flares(data):
    
    
    # Find deviations, or possible flares.
    deviations = find_deviations(data)
    logger.debug(f'{len(deviations)} deviations found.')

    starts = find_minima(data, deviations) # Refine deviations by looking for local minima, or flare starts.
    logger.debug(f'{len(starts)} flare starts identified.')

    peaks = find_maxima(data, starts) # For each flare start, find the corresponding peak.
    starts, peaks = _remove_Duplicates(data, starts, peaks) # Combine any duplicate start/peaks.

    DECAYPAR = 3
    ends = _find_end(data, starts, peaks, DECAYPAR) # For each flare peak, find the corresponding flare end.

    # Combine any overlapping flares.
    starts, peaks, ends = combine_overlaps(data, starts, peaks, ends)

    return starts, peaks, ends

def find_deviations(data):

    deviations = []
    counter = 0

    for i in data.index[:-1]:

        if data.iloc[i+1].flux > data.iloc[i].flux:
            counter += 1
        else:
            counter = 0

        if counter == 2:
            check = data.iloc[i+1].flux + (data.iloc[i+1].flux_perr * 1.5) > data.iloc[i-1].flux
            if check:
                logger.debug(f'find_deviations(): dev found at {i-1} - {data.iloc[i-1].time}s')
                deviations.append(i-1)
                counter = 0
            else:
                counter = 1

    return sorted(set(deviations))

def find_minima(data, deviations):
    
    minima = []

    for deviation_index in deviations:

        if deviation_index == 0:
            startpoint = 0
            endpoint   = 1
            continue

        if deviation_index < 10:
            startpoint = 0
            endpoint = deviation_index

        else:
            startpoint = deviation_index - 10
            endpoint    = deviation_index

        points = data.iloc[startpoint:endpoint]
        minimum = data[data.flux == min(points.flux)].index.values[0]
        logger.debug(f"find_minima() - original index {deviation_index}, new index {minimum}.")
        minima.append(minimum)

    return sorted(set(minima))

def find_maxima(data, starts):

    maxima = []

    for start_index in starts:

        if abs(data.idxmax('index').time - start_index) < 30:
            startpoint = start_index
            endpoint   = data.idxmax('index').time - 1

        else:

            prev_chunk = data['flux'].iloc[start_index]
            next_chunk = np.average(data['flux'].loc[start_index:start_index+5])
            chunkcount = 1

            while next_chunk > prev_chunk:
                chunkcount += 1
                prev_chunk = next_chunk
                next_chunk = np.average(data['flux'].loc[start_index+(chunkcount*5):start_index+(chunkcount*5)+5])
                logger.critical(f'prevchunk {prev_chunk} and nextchunk {next_chunk}')

            logger.critical(f"nextchunkavg finally lower than original flux comparison at {chunkcount}")

            finalrange = (chunkcount + 1) * 5
            logger.critical(f"final range is +{finalrange}")

            startpoint = start_index
            endpoint   = start_index + finalrange

        points = data.iloc[startpoint:endpoint]
        maximum = data[data.flux == max(points.flux)].index.values[0]
        logger.debug(f"find_maxima() - for {start_index} peak found at {maximum}")
        maxima.append(maximum)

    return maxima

def _remove_Duplicates(data, startlist, peaklist):
    """
    Look for flare starts with the same peak and combine.
    
    Sometimes indices A and B are found as flare starts, and both share the same
    peak C. Hence, both A and B likely should be combined as one start, the lowest
    flux is likely to be the start. Future thought: or should it just be the
    earlier index? Which is the more general case.
    """

    unique_peaks = set()
    duplicate_peaks = []
    duplicate_index = []

    indicesToRemove = []

    for idx, peak in enumerate(peaklist):
        if peak in unique_peaks:
            duplicate_peaks.append(peak)
            duplicate_index.append(idx)
        else:
            unique_peaks.add(peak)

    unique_peaks = sorted(unique_peaks)
    duplicate_peaks = sorted(duplicate_peaks)
    duplicate_index = sorted(duplicate_index)

    for data_index, peaklist_index in zip(duplicate_peaks, duplicate_index):
        pointsToCompare = [i for i, x in enumerate(peaklist) if x == data_index]
        # points is a pair of indices in peaklist
        # each peaklist has a corresponding startlist
        # so for point a and point b, find the flux in startlist at point a and b
        # compare these two
        # whichever is the lowest flux is more likely the start
        # so we keep this index and discord the other index

        comparison = np.argmin([data.iloc[startlist[x]].flux for x in pointsToCompare])

        del pointsToCompare[comparison]

        for point in pointsToCompare:
            indicesToRemove.append(point)
    
    new_startlist = [startlist[i] for i in range(len(startlist)) if i not in indicesToRemove]
    new_peaklist = [peaklist[i] for i in range(len(peaklist)) if i not in indicesToRemove]

    return new_startlist, new_peaklist

def _find_end(data, starts, peaks, DECAYPAR):
    """
    Find the end of a flare as the decay smooths into afterglow.
    
    For each peak, start counting up through data indices. At each datapoint,
    evaluate three conditions, by calculating several gradients If we reach the next
    flare start, we end the flare here immediately.
    """
    ends = []

    for peak_index in peaks:

        cond_count = 0
        current_index = peak_index

        while cond_count < DECAYPAR:

            # Check if we reach next peak.
            if current_index == peak_index or current_index + 1 == peak_index:
                current_index += 1
                continue
            # Check if we reach end of data.
            if any([current_index + i for i in range(2)] == data.idxmax('index').time):
                break
            # Check if we reach next start.
            if current_index + 1 in starts:
                current_index += 1
                continue

            current_index += 1

            grad_NextAlong = _calc_grad(data, current_index, current_index+1)
            grad_PrevAlong = _calc_grad(data, current_index-1, current_index)
            grad_PeakToNext = _calc_grad(data, peak_index, current_index)
            grad_PeakToPrev = _calc_grad(data, peak_index, current_index-1)

            cond1 = grad_NextAlong > grad_PeakToNext
            cond2 = grad_NextAlong > grad_PrevAlong
            cond3 = grad_PeakToNext > grad_PeakToPrev

            if cond1 and cond2 and cond3:
                cond_count += 1
            elif cond1 and cond3:
                cond_count += 0.5

        ends.append(current_index)

    return sorted(ends)

def combine_overlaps(data, starts, peaks, ends):

    combined_starts = []
    combined_peaks = []
    combined_ends = []

    sorted_pairs = sorted(zip(starts, peaks, ends), key=lambda x: x[0])
    current_start, current_peak, current_end = sorted_pairs[0]

    for start, peak, end in sorted_pairs[1:]:
        if start <= current_end:
            if data['flux'].iloc[peak] > data['flux'].iloc[current_peak]:
                current_peak = peak
            current_end = max(current_end, end)
        else:
            combined_starts.append(current_start)
            combined_peaks.append(current_peak)
            combined_ends.append(current_end)
            current_start, current_peak, current_end = start, peak, end

    combined_starts.append(current_start)
    combined_peaks.append(current_peak)
    combined_ends.append(current_end)

    return combined_starts, combined_peaks, combined_ends

def _check_FluxIncrease(data, startidx, peakidx):
    """Check the flare increase is greater than x2 the start error."""
    check = data.iloc[peakidx].flux > (data.iloc[startidx].flux + (2 * data.iloc[startidx].flux_perr))
    return check

def _check_AverageNoise(data, startidx, peakidx, endidx):
    """Check if flare is greater than x1.75 the average noise across the flare."""
    average_noise = abs(np.average(data.iloc[startidx:endidx].flux_perr)) + abs(np.average(data.iloc[startidx:endidx].flux_nerr))
    flux_increase = min(data.iloc[peakidx].flux - data.iloc[startidx].flux, data.iloc[peakidx].flux - data.iloc[endidx].flux)
    check = flux_increase > average_noise * 2
    return check

def _check_PulseShape(data, startidx, peakidx, endidx):
    try:
        rise_phase = _calc_grad(data, startidx, peakidx, indexIsRange=True)
        rise_condition = sum(x > 0 for x in rise_phase) / len(rise_phase)
    except ZeroDivisionError:
        return True

    decay_phase = _calc_grad(data, peakidx, endidx, indexIsRange=True)
    decay_condition = sum(x < 0 for x in decay_phase) / len(decay_phase)
    
    logger.debug(f'check3 conditions are {rise_condition} & {decay_condition}')
    check = rise_condition >= 0.6 and decay_condition >= 0.4
    return check

def _check_AboveContinuum(data, startidx, peakidx, endidx):
    if startidx == 0:
        startidx = 1

    slope = (data['flux'].iloc[endidx+1] - data['flux'].iloc[startidx-1])/(data['time'].iloc[endidx+1]-data['time'].iloc[startidx-1])
    intercept = data['flux'].iloc[startidx-1] - slope * data['time'].iloc[startidx-1]

    points_above = 0

    for flux, time in zip(data['flux'].iloc[startidx:endidx], data['time'].iloc[startidx:endidx]):
        if flux > (slope * time + intercept):
            points_above += 1

    logger.debug(f'check4 points above are {points_above} over {len(data["flux"].iloc[startidx:endidx])}')
    check = points_above > len(data['flux'].iloc[startidx:endidx])/2
    return check

def _calc_grad(data, index1, index2, indexIsRange=False):

    if indexIsRange == False:
        deltaFlux = data.iloc[index2].flux - data.iloc[index1].flux
        deltaTime = data.iloc[index2].time - data.iloc[index1].time
        return deltaFlux/deltaTime

    if indexIsRange == True:

        indices = range(index1, index2)
        deltaFlux = []
        deltaTime = []
        for i in indices:
            deltaFlux.append(data.iloc[i+1].flux - data.iloc[i].flux)
            deltaTime.append(data.iloc[i+1].time - data.iloc[i].time)

        return [flx / tim for flx, tim in zip(deltaFlux, deltaTime)]
    
    else:
        raise ValueError("Parameter range should be boolean.")