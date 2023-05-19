import numpy as np

def main() -> int:
    arr = np.array([[1,2],[3,4]])           # 2x2 행렬 arr 생성
    w,v = np.linalg.eig(arr)                # 행렬 arr의 고유값(w), 고유벡터(v)를 구한다.
    d = np.linalg.det(arr)                  # 행렬 arr의 행렬식(d)를 구한다.

    print('arr = [[a1 a2] [a3 a4]] =\n', arr)
    print('eigenvalues(w) = [w1 w2] = ', w)
    print('eigenvectors(x) = [x11 x12] [x21 x22] = ', v[:,0], v[:,1])
    print('determinant(d) = {0:0.1f}'.format(d))

    print('1 * x11({0:10.8f}) + 2 * x12({1:10.8f}) => {2:10.8f}'.format(v[0][0], v[1][0], 1 * v[0][0] + 2 * v[1][0]))
    print('w1({0:10.8f}) * x11({1:10.8f}) => {2:10.8f}'.format(w[0], v[0][0], w[0] * v[0][0]))
    print('3 * x11({0:10.8f}) + 4 * x12({1:10.8f}) => {2:10.8f}'.format(v[0][0], v[1][0], 3 * v[0][0] + 4 * v[1][0]))
    print('w1({0:10.8f}) * x12({1:10.8f}) => {2:10.8f}'.format(w[0], v[1][0], w[0] * v[1][0]))

    print('1 * x21({0:10.8f}) + 2 * x22({1:10.8f}) => {2:10.8f}'.format(v[0][1], v[1][1], 1 * v[0][1] + 2 * v[1][1]))
    print('w2({0:10.8f}) * x21({1:10.8f}) => {2:10.8f}'.format(w[1], v[0][1], w[1] * v[0][1]))
    print('3 * x21({0:10.8f}) + 4 * x22({1:10.8f}) => {2:10.8f}'.format(v[0][1], v[1][1], 3 * v[0][1] + 4 * v[1][1]))
    print('w2({0:10.8f}) * x22({1:10.8f}) => {2:10.8f}'.format(w[1], v[1][1], w[1] * v[1][1]))

    print('')

    vec1 = np.array([1,2,3])
    vec2 = np.array([4,5,6])

    print('vec1 = {}'.format(vec1))
    print('vec2 = {}'.format(vec2))
    print('Cross(vec1,vec2) = {}'.format(np.cross(vec1, vec2)))

    print('')

    A = np.array([[1,2,-2],[2,1,-5],[1,-4,1]])
    b = np.array([-15,-21,18])
    print('A = ')
    print(A)
    print('b = ')
    print(b)
    print('Ax = b')
    x = np.linalg.solve(A, b)
    print('x => {}'.format(x))
    print('Ax => {}'.format(np.dot(A, x)))
    print('comparison between Ax and b = {}'.format(np.allclose(np.dot(A, x), b)))

# entry point of program
if __name__ == '__main__':
	main()
