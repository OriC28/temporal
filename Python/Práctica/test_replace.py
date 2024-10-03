import ctypes

Lista = ctypes.c_int * 5

l1 = Lista(1,2,3,4,5)

replace_lib = ctypes.CDLL("replace.dll")
replace_lib.replace.argtypes = (ctypes.POINTER(ctypes.c_int), ctypes.c_int, ctypes.c_int, ctypes.c_int)
replace_lib.replace.restype = ctypes.POINTER(ctypes.c_int)

re = replace_lib.replace(l1, 5, 1,7)