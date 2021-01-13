# 机器学习与数据挖掘实验

.

## 目录

- 实验内容
  - [实验一 多源数据集成 清洗 统计](#实验一-多源数据集成清洗和统计)
  - [实验二 数据统计和可视化](#实验二-数据统计和可视化)
  - [实验三 k-means聚类算法](#实验三-k-means聚类算法)
  - [实验四 逻辑回归二分类](#实验四-逻辑回归二分类)
- [仓库文件内容说明](#仓库文件内容说明)
- [小组成员](#小组成员)

## 小组成员
[返回目录](#目录)

队长：张奥翔

队员：何锦辉、王浩辉、吴振廷

## 仓库文件内容说明
[返回目录](#目录)

| 文件/目录                                                    | 说明                                      |
| ------------------------------------------------------------ | ----------------------------------------- |
| [exp1](https://github.com/hehemu/-/tree/main/exp1) | 实验一   多源数据集成、清洗和统计                           |
| [exp2](https://github.com/hehemu/-/tree/main/exp2) | 实验二   数据统计和可视化数据统计和可视化                 |
| [exp3](https://github.com/hehemu/-/tree/main/exp3) | 实验三   k-means聚类算法           |


## 实验一 多源数据集成、清洗和统计
[返回目录](#目录)

**题目 ：**

​		广州大学某班有同学100人，现要从两个数据源汇总学生数据。第一个数据源在数据库中，第二个数据源在txt文件中，两个数据源课程存在缺失
、冗余和不一致性，请用C/C++/Java程序实现对两个数据源的一致性合并以及每个学生样本的数值量化。

0、两个数据源合并后读入内存，并统计：[Answer](https://github.com/hehemu/-/blob/main/exp1/%E5%90%88%E5%B9%B6%E6%95%B0%E6%8D%AE.csv)

1、学生中家乡在Beijing的所有课程的平均成绩：[Answer](https://github.com/hehemu/-/blob/main/exp1/%E7%AC%AC%E4%B8%80%E9%97%AE.png)

2、学生家乡在广州，课程1在80分以上，且课程9在9分以上的男同学的数量：[Anwser](https://github.com/hehemu/-/blob/main/exp1/%E7%AC%AC%E4%BA%8C%E9%97%AE.png)

3、比较广州和上海两地女生的平均体能测试成绩，哪个地区的更强些？[Anwser](https://github.com/hehemu/-/blob/main/exp1/%E7%AC%AC%E4%B8%89%E9%97%AE.png)

4、学习成绩和体能测试成绩，两者的相关性是多少？（九门课的成绩分别与体能成绩计算相关性）

 (1)[Answer](https://github.com/hehemu/-/blob/main/exp1/%E7%AC%AC%E5%9B%9B%E9%97%AE%EF%BC%881%EF%BC%89.png)

 (2)[Answer](https://github.com/hehemu/-/blob/main/exp1/%E7%AC%AC%E5%9B%9B%E9%97%AE%EF%BC%882%EF%BC%89.png)
 
## 实验二 数据统计和可视化
[返回目录](#目录)

**题目 ：**
基于**实验一**中清洗后的数据练习统计和视化操作，100个同学（样本），每个同学有11门课程的成绩（11维的向量）；那么构成了一个100x11的数据矩阵。以你擅长的语言C/C++/Java/Python/Matlab，编程计算：

1、请以课程1成绩为x轴，体能成绩为y轴，画出散点图：[Answer](https://github.com/hehemu/-/blob/main/exp2/%E7%AC%AC%E4%B8%80%E9%97%AE.png)

2、以5分为间隔，画出课程1的成绩直方图：[Answer](https://github.com/hehemu/-/blob/main/exp2/%E7%AC%AC%E4%BA%8C%E9%97%AE.png)

3、对每门成绩进行z-score归一化，得到归一化的数据矩阵：[Answer](https://github.com/hehemu/-/blob/main/exp2/%E7%AC%AC%E4%B8%89%E9%97%AEcorrelation_matrix.txt)

4、计算出100x100的相关矩阵，并可视化出混淆矩阵：[Answer](https://github.com/hehemu/-/blob/main/exp2/%E7%AC%AC%E5%9B%9B%E9%97%AE.png)

5、根据相关矩阵，找到距离每个样本最近的三个样本，得到100x3的矩阵（每一行为对应三个样本的ID）输出到txt文件中，以\t,\n间隔。[Answer](https://github.com/hehemu/-/blob/main/exp2/%E7%AC%AC%E4%BA%94%E9%97%AE%E6%9C%80%E8%BF%91%E6%A0%B7%E6%9C%AC.txt)

## 实验三 k-means聚类算法
[返回目录](#目录)

**题目 ：**

用C++实现k-means聚类算法，
1.  对实验二中的z-score归一化的成绩数据进行测试，观察聚类为2类，3类，4类，5类的结果，观察得出什么结论？	（最新的代码仓库已更新此问题的解）
2.  由老师给出测试数据，进行测试，并画出可视化出散点图，类中心，类半径，并分析聚为几类合适。

样例数据(x,y)数据对：
| x    | y    |      | x    | y    |      | x    | y    |      | x    | y    |      | x    | y    |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 3.45 | 7.08 |      | 6.17 | 5.40 |      | 3.68 | 5.99 |      | 6.24 | 3.06 |      | 3.17 | 6.41 |
| 1.76 | 7.24 |      | 4.20 | 6.46 |      | 2.11 | 4.08 |      | 6.89 | 2.41 |      | 5.97 | 3.62 |
| 4.29 | 9.55 |      | 5.87 | 3.87 |      | 2.58 | 7.10 |      | 5.38 | 2.32 |      | 6.32 | 3.62 |
| 3.35 | 6.65 |      | 5.47 | 2.21 |      | 3.45 | 7.88 |      | 5.13 | 2.73 |      | 7.26 | 4.19 |

[2类及散点图](https://github.com/hehemu/-/tree/main/exp3/2cen%5D)

[3类及散点图](https://github.com/hehemu/-/tree/main/exp3/3cen%3D)

[4类及散点图](https://github.com/hehemu/-/tree/main/exp3/4cen)

[5类及散点图](https://github.com/hehemu/-/tree/main/exp3/5cen)

## 实验四 逻辑回归二分类
[返回目录](#目录)

**题目 ：**
学习sigmoid函数和逻辑回归算法。将实验三.2中的样例数据用聚类的结果打标签{0，1}，并用逻辑回归模型拟合。

1. 学习并画出sigmoid函数
2. 设计梯度下降算法，实现逻辑回归模型的学习过程。
3. 根据给定数据（实验三.2），用梯度下降算法进行数据拟合，并用学习好的模型对(2,6)分类。
