class BinarisKereses:

    def binary_search(self, arr, x):
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (high + low) // 2
            if arr[mid] < x:
                low = mid + 1
            elif arr[mid] > x:
                high = mid - 1
            else:
                return mid
        return -1
    
    def binker(self, arr, x):
        result = self.binary_search(arr, x)
        if result != -1:
            print("Az elem a következő indexen van: ", result)
        else:
            print("Az elem nincs a tömbben!")

    
kereso = BinarisKereses()
arr = [2, 3, 4, 10, 40]
x = 10
kereso.binker(arr, x)
