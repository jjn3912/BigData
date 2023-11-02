import numpy as np


a1 = np.array([1,2,3])
a2 = np.array([4,5,6])
print(a1 * a2)
a3 = np.dot(a1,a2)
print(a3)
# data = np.array([
#     [1,5,9],
#     [2,np.nan,10],
#     [np.nan,7,11],
#     [4,8,np.nan]
#     # [1, 2, np.nan, 4],
#     # [5, np.nan, 7, 8],
#     # [9, 10,11, np.nan]
#
# ])
# print(data)
#
# means = np.nanmean(data, axis=0)
# # print(means)
# for i in range(data.shape[1]):
#     # print(i)
#     mask = np.isnan(data[:, i])#True, False 값을 갖는 배열 생성
#    # print(mask)
#     data[mask, i] = means[i]
# print(data)
# df =pd.DataFrame(i.fit_transform(df), columns=df.columns)
# print(df)
# for col in df.columns:
#     df[col] = np.where(pd.isnull(df[col]),np.mean(df[col]),df[col])
#     print(df)

# print(df)
# df.fillna(df.mean(), inplace=True)
# print(df)

# def info(x):
#     print(f"배열의 차원은{x.ndim}입니다")
#     print(f"배열의 Shape는{x.shape}입니다")
#     print(f"배열 원소의 개수는{x.size}개 입니다")
#
# np_1d = np.arange(1,20,2)
# np_1d = np_1d.reshape(1,2,5)
# print(np_1d)
# info(np_1d)

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
