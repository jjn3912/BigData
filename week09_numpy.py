import numpy as np
import random
def info(x):
    print(f"배열의 차원은{x.ndim}입니다")
    print(f"배열의 Shape는{x.shape}입니다")
    print(f"배열 원소의 개수는{x.size}개 입니다")

np_1d = np.arange(1,20,2)
np_1d = np_1d.reshape(1,2,5)
print(np_1d)
info(np_1d)

# any_list = [91, "university",3.91,(5, 7)]
# converted_any_list = ["1", "university","3.91","(5, 7)"]
#
# # one_type_np_list = np.array(any_list)
# one_type_np_list = np.array([2, 4, 6, 8])
# np_1d = np.array([2,4,6,8])
# np_2d = np.array([[2,4],[6,8]])
# print(np_1d.ndim, np_2d.ndim)
# print(np_1d.size,np_2d.size)
# print(np_1d.shape,np_2d.shape)
# # print(one_type_np_list)
# # for i in any_list:
# #     print(i)
# #
# # for j in one_type_np_list:
# #     print(j)