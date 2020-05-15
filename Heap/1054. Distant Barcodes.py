"""We are the captains of our ships, and we stay 'till the end. We see our stories through.
"""

"""1054. Distant Barcodes
"""

from heapq import heapify, heappop, heappush

class Solution:

    def rearrangeBarcodes(self, barcodes):
        barcodes_freq = {}
        for barcode in barcodes:
            barcodes_freq[barcode] = barcodes_freq.get(barcode, 0) + 1
        max_heap = [(-1 * freq, barcode) for barcode, freq in barcodes_freq.items()]
        heapify(max_heap)
        new_arrangement = []
        while len(max_heap) > 1:
            more_freq, more_freq_barcode = heappop(max_heap)
            less_freq, less_freq_barcode = heappop(max_heap)
            new_arrangement += [more_freq_barcode, less_freq_barcode]
            if -1 * more_freq > 1:
                heappush(max_heap, (more_freq + 1, more_freq_barcode))
            if -1 * less_freq > 1:
                heappush(max_heap, (less_freq + 1, less_freq_barcode))
        if max_heap:
            freq, barcode = heappop(max_heap)
            new_arrangement.append(barcode)
        return new_arrangement